FROM python:3.9.5-slim-buster

WORKDIR /opt/django-shop

RUN apt-get update && \
    apt-get -y install \
        python3-gdal \
        curl \
        tcpdump \
        git \
    && \
    rm -rf /var/lib/apt/lists/*

RUN pip install ipython && \
    pip uninstall -y parso

COPY requirements.txt /opt/django-shop
RUN pip install -r requirements.txt && \
    rm requirements.txt

COPY shop/ /opt/django-shop/
COPY .git/ /opt/django-shop/.git
COPY /docker/django-shop/gunicorn.conf.py /opt/django-shop/gunicorn.conf.py

EXPOSE 80
CMD gunicorn --config ./gunicorn.conf.py shop.wsgi
