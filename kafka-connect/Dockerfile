FROM confluentinc/cp-kafka-connect-base:latest

USER root

RUN confluent-hub install --no-prompt confluentinc/kafka-connect-jdbc:latest

COPY start-kafka.sh /

COPY uber-connector.json /

RUN chmod +x /start-kafka.sh

CMD /start-kafka.sh