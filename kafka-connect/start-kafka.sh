# Launch the worker
/etc/confluent/docker/run &

# Wait for it to start running
# Change the port here if not using the default
bash -c ' \
# blocks until kafka is reachable
kafka-topics --bootstrap-server broker:9092 --list

echo -e "Creating kafka topics"
kafka-topics --bootstrap-server broker:9092 --create --if-not-exists --topic uber-rides --replication-factor 1 --partitions 1
kafka-topics --bootstrap-server broker:9092 --create --if-not-exists --config cleanup.policy=compact --topic docker-connect-configs --replication-factor 1 --partitions 1
kafka-topics --bootstrap-server broker:9092 --create --if-not-exists --config cleanup.policy=compact --topic docker-connect-offsets --replication-factor 1 --partitions 1
kafka-topics --bootstrap-server broker:9092 --create --if-not-exists --config cleanup.policy=compact --topic docker-connect-status --replication-factor 1 --partitions 1

echo -e "Successfully created the following topics:"
kafka-topics --bootstrap-server broker:9092 --list

echo -e "\n\n=============\nWaiting for Kafka Connect to start listening on localhost ⏳\n=============\n"
while [ $(curl -s -o /dev/null -w %{http_code} http://localhost:8083/connectors) -ne 200 ] ; do
  echo -e "\t" $(date) " Kafka Connect listener HTTP state: " $(curl -s -o /dev/null -w %{http_code} http://localhost:8083/connectors) " (waiting for 200)"
  sleep 5
done
echo -e $(date) "\n\n--------------\n\o/ Kafka Connect is ready! Listener HTTP state: " $(curl -s -o /dev/null -w %{http_code} http://localhost:8083/connectors) "\n--------------\n"

# Now create your connector
## Inline config example: 
curl -i -X POST -H  "Content-Type:application/json" http://localhost:8083/connectors/ -d @/uber-connector.json

sleep infinity
'