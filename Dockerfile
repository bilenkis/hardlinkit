FROM python:3.6.4-alpine3.6

ENV PYTHONUNBUFFERED 1

COPY requirements.txt /opt/hardlinkit/

WORKDIR /opt/hardlinkit

RUN set -xe ;\
    apk add -U --no-cache \
      postgresql-dev \
      gcc \
      musl-dev \
    ;\
    pip --no-cache-dir install --upgrade pip

RUN set -xe ;\
    pip --no-cache-dir install -r requirements.txt

#CMD python3 manage.py runserver --nothreading 0.0.0.0:8080
CMD python3 manage.py runserver 0.0.0.0:8080
#CMD ["python3", "manage.py", "runserver", "--nothreading", "0.0.0.0:8080"]
#CMD ["python3", "manage.py", "runserver", "--nothreading", "0.0.0.0:8080"]
