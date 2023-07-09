FROM python:3.10-slim

RUN apt-get update && \
    apt-get install -y netcat-traditional && \
    rm -rf /var/lib/apt/lists/*


WORKDIR game_of_life

COPY ../requirements.txt .

RUN pip3 install -r requirements.txt --no-cache-dir && \
    pip3 install gunicorn psycopg2-binary

COPY .. .

ENTRYPOINT ["./docker-entrypoint.sh"]
