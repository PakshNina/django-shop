FROM postgres:11.4

RUN apt-get update &&\
    apt-get install -y postgresql-11 &&\
    rm -rf /var/lib/apt/lists/*

COPY initial /docker-entrypoint-initdb.d/
