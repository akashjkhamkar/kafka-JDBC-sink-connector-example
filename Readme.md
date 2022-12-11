# Readme

Goal is to consume from a kafka topic and update a database

approaches -

1. python consumer client
2. connector

### How to launch

This is will launch kafka cluster, also the connector container and our producer container

```yaml
docker-compose up
```

### Api
Flask server will listen on 8000
checkout req.rest, to see the payload structure

### Todo
Dockerise the consumer
Shifting from orm to normal sql