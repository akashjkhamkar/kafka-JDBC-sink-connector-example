# syntax=docker/dockerfile:1
FROM python:3.8.10-slim-buster

RUN apt-get update && \
  apt-get install -y --no-install-recommends gcc git libssl-dev g++ make && \
  cd /tmp && git clone https://github.com/edenhill/librdkafka.git && \
  cd librdkafka && git checkout tags/v1.9.0 && \
  ./configure && make && make install && \
  cd ../ && rm -rf librdkafka

RUN ldconfig

COPY requirements.txt /tmp/

RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY app.py app.py

ENTRYPOINT ["python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=8000"]
