FROM python:3.6.4-alpine3.6

ENV PYTHONUNBUFFERED 1

COPY requirements.txt /opt/hardlinkit/
COPY wait-for-postgres.sh /usr/sbin/

WORKDIR /opt/hardlinkit

RUN set -xe ;\
    apk add -U --no-cache \
      postgresql-dev \
      postgresql-client \
      gcc \
      musl-dev \
    ;\
    pip --no-cache-dir install --upgrade pip

RUN set -xe ;\
    pip --no-cache-dir install -r requirements.txt

CMD /usr/sbin/wait-for-postgres.sh
