FROM python:3.12-slim-bookworm

LABEL maintainer="Felippe M Oliveira"

RUN apt update -y \
    && apt install -y \
    gcc apt-utils findutils g++ libfreetype-dev openssl \
    && apt clean all

WORKDIR /opt/app

COPY requirements.txt start-server.sh /opt/app/
RUN python -m pip install --no-cache-dir -r requirements.txt
RUN chown -R root:root /opt/app
RUN chmod -R 777 /opt/app

EXPOSE 5000
STOPSIGNAL SIGTERM
CMD ["/opt/app/start-server.sh"]