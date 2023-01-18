A custom resource definition describes a new resource - Joke.
Kopf operator monitors these resources and on.create it takes the joke and inserts it into a configmap(acting as a jokes storage).
The configmap is mounted on the place of a index.html file inside a simple web server deployment. 
The deployment can receive http requests via a service and returns the index.html, which is a jokes list, 
that can be dynamically increased in size, if we create more Joke custom resources.

Dockerfile           - docker image for kopf operator deployment 
crd.yaml             - custom resource definition for the jokes(joke entity)
joke[1-3].yaml       - test custom resources(warning, resources contain bad jokes!)  
joke_cm.yaml         - configmap that acts as a general jokes storage 
joke_deployment.yaml - simple web server, that gets its index.html file 
	replaced by the configmap above(i.e. contains all the jokes)
	Can be curl-ed to get all the jokes.
joke_operator.py     - the actual kopf operator, watches for jokes, adds them to the configmap storage 
joke_operator_deployment.yaml - kopf operator deployment
joke_svc.yaml - NodePort service that exposes certain port, so that the web server can be curl-ed from outside.

P.S. I have not forgotten the actual task - the operator contains on.create handler, which simply writes "Hello World!" in the operator logs.
