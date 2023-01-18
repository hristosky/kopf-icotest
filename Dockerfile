FROM python:3.11
ADD . /src
RUN pip3 install kopf
CMD kopf run /src/joke_operator.py --namespace=default
