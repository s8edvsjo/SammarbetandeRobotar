import time
from paho.mqtt import client as paho

broker = 'maqiatto.com'
port = 1883
topic = "victor.fagerstrom@abbindustrigymnasium.se/karta"
# generate client ID with pub prefix randomly
client_id = "Jenny"

def test(el):
    print(el)

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = paho.Client(client_id)
    client.username_pw_set(username="victor.fagerstrom@abbindustrigymnasium.se",password="hejhej")
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def publish(client):
    msg_count = 0
    while True:
        time.sleep(1)
        msg = f"messages: {msg_count}"
        result = client.publish(topic, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
        msg_count += 1

def subscribe(client: paho):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        test(msg.payload.decode())

    client.subscribe(topic)
    client.on_message = on_message

def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()
    #publish(client)
    

run()