FROM python:3.12.3-alpine3.20

WORKDIR /src

RUN pip install --upgrade pip

COPY requirements.txt requirements.txt

RUN --mount=type=cache,target=/root/.cache/pip \
    pip install -r requirements.txt

COPY . .

COPY docker/start.sh docker/worker.sh docker/flower.sh docker/entrypoint.sh /
RUN chmod +x /start.sh /worker.sh /flower.sh /entrypoint.sh

ENTRYPOINT [ "/entrypoint.sh" ]
