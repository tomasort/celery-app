FROM python:3.12.3-alpine3.20

WORKDIR /src

RUN apk add --no-cache build-base

RUN pip install --upgrade pip

COPY requirements.txt requirements.txt

RUN --mount=type=cache,target=/root/.cache/pip \
    pip install -r requirements.txt

COPY . .

COPY docker/start.sh /start.sh
RUN chmod +x /start.sh

COPY docker/worker.sh /worker.sh
RUN chmod +x /worker.sh

COPY docker/flower.sh /flower.sh
RUN chmod +x /flower.sh

COPY docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT [ "/entrypoint.sh" ]
