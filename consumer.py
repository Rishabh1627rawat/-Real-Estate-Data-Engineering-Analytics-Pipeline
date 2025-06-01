from kafka import KafkaConsumer
import json

topic ="city_data"
bootstrap_servers =['localhost:9092']

consumer = KafkaConsumer(
    topic,
    bootstrap_servers=bootstrap_servers,
    auto_offset_reset='earliest',
    enable_auto_commit =True,
    group_id='city-consumer-group',
    value_deserializer=lambda m:json.loads(m.decode('utf-8'))
)

print(f"Listening for message on topic '{topic}'..")

for message in consumer:
    print(f"Received message from topic {message.topic}':")
    print(message.value)