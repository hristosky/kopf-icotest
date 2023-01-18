import kopf
import kubernetes

joke_cm_name = 'joke-cm'
namespace = 'default'
field_selector = f"metadata.name={joke_cm_name}"

@kopf.on.startup()
def startup_hello_world_log(logger, **kwargs):
    logger.info('Hello World!')

@kopf.on.startup()
def configure(settings: kopf.OperatorSettings, **_):
    settings.peering.standalone = True

@kopf.on.create('Joke')
def add_more_jokes(spec, name, namespace, logger, **kwargs):
    k8s_core_api = kubernetes.client.CoreV1Api()

    # get the existing jokes from the configmap and concat our new joke in
    joke_cm = k8s_core_api.list_namespaced_config_map(namespace=namespace, field_selector=field_selector)
    joke_cm.items[0].data['joke_list'] += "\n" + spec['payload']

    # patch the configmap with our new joke(preserving the old jokes too)
    res = k8s_core_api.patch_namespaced_config_map(name=joke_cm_name, namespace=namespace, body=joke_cm.items[0])
