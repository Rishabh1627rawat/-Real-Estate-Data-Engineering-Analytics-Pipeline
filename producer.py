import csv
import json
import pandas as pd
import time
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda vs: json.dumps(vs).encode('utf-8')
)

topic = 'city_data'

def load_and_tag_csv(path, city_name):
    df = pd.read_csv(path, low_memory=False)
    df['city'] = city_name
    return df


dataframes = [
    load_and_tag_csv("C:\\Users\\nikhi\\kolkata_light.csv","kolkata"),
    load_and_tag_csv("C:\\Users\\nikhi\\mumbai_light.csv","mumbai"),
    load_and_tag_csv("C:\\Users\\nikhi\\hyderabad_light.csv","hyderbad"),
    load_and_tag_csv("C:\\Users\\nikhi\\gurgaon_light.csv","gurgaon"),

]



full_data = pd.concat(dataframes, ignore_index=True)

for index, row in full_data.iterrows():
    message = row.to_dict()
    producer.send(topic, value=message)
    print(f"sent: {message}")
    time.sleep(0.2)


producer.flush()
producer.close()
print("All messages sent.")
