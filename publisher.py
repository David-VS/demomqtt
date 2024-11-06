from paho.mqtt import client
import time
import json
import dataclasses
import sensors as s
import random


broker = 'd026818d.ala.eu-central-1.emqxsl.com'
port = 8883
username= '2iot'
password = '3iot'



def connect():
    def on_connect(client, userdata, flags, reason_code, properties=None):
        if reason_code == 0:
            print("Connected succesfully")
        else:
            print("connection failed for reasons")

    my_client = client.Client(client_id="joske", callback_api_version=client.CallbackAPIVersion.VERSION2)
    my_client.tls_set(ca_certs='./certificates/emqxsl-ca.crt')
    my_client.username_pw_set(username, password)
    my_client.connect(broker, port)
    my_client.on_connect = on_connect
    return my_client


def publish(my_client):

    while True:
        time.sleep(2)
        sensor_name = input("Name of the sensor= ")
        sensor_type = input("Type of the sensor= ")
        sensor_value = random.randint(-10,30)

        sensor = s.Sensor(sensor_name, sensor_type, sensor_value)

        topic = "prog3/mqtt"
        msg = json.dumps(dataclasses.asdict(sensor))

        result = my_client.publish(topic, msg)
        if result[0] == 0:
            print("message sent")
        else:
            print("failed to publish")


def run():
    my_client = connect()
    my_client.loop_start()
    publish(my_client)
    my_client.loop_stop()


if __name__ == '__main__':
    run()
