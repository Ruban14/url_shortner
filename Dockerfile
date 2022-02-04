# Dockerfile

# FROM directive instructing base image to build upon
FROM python:3.8-slim-buster
#FROM python:3.7-buster

RUN apt-get update && apt-get install -y nano curl wget procps

# set up django project in container
RUN mkdir -p /opt/bin/pip_cache
COPY .pip_cache /opt/bin/pip_cache/

WORKDIR /opt/bin
COPY . /opt/bin/url_shortner/

RUN pip install -r url_shortner/requirements.txt --cache-dir /opt/bin/pip_cache && pip install gunicorn --cache-dir /opt/bin/pip_cache

# Copy management script
COPY start-server.sh /opt/bin/

# Port management
EXPOSE 8000

CMD ["/opt/bin/start-server.sh"]

