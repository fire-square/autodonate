FROM python:slim-bullseye

COPY . /source/app
WORKDIR /source/app

RUN apt-get update && apt-get install -y --no-install-recommends       \
    libmariadb-dev curl gcc g++ && pip3 install poetry gunicorn             && \
    groupadd --gid 5000 container && useradd --home-dir /source        \
    --create-home --uid 5000 --gid 5000 --shell /bin/bash --skel       \
    /dev/null container && poetry config virtualenvs.create false   && \
    poetry install --no-dev && chown -R 5000:5000 /source           && \
    pip3 uninstall poetry --no-input -y

EXPOSE 8080

ENV SOCKET="0.0.0.0:8080" THREADS="2" WORKERS="5"
VOLUME ["/source/logs", "/config"]

HEALTHCHECK CMD curl --fail http://localhost:8080/api/health || exit 1

# Dont run as root!
USER container
CMD python3 manage.py migrate && \
    gunicorn autodonate.wsgi --bind $SOCKET --threads $THREADS --workers $WORKERS
