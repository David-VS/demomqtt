from paho.mqtt import client
import random


broker = 'd026818d.ala.eu-central-1.emqxsl.com'
port = 8883
username= '2iot'
password = '3iot'



def connect():
    def on_connect(client, userdata, flags, reason_code):
        if reason_code == 0:
            print("Connected succesfully")
        else:
            print("connection failed for reasons")

    my_client = client.Client(client.CallbackAPIVersion.VERSION2)
    my_client.tls_set(ca_certs='./certificates/emqxsl-ca.crt')
    my_client.username_pw_set(username, password)
    my_client.connect(broker, port)
    my_client.on_connect = on_connect
    return my_client


def subscribe(my_client):
    def on_message(client, userdata, msg):
        print("Received " + msg.payload.decode())

    my_client.subscribe("prog3/mqtt")
    my_client.on_message = on_message



def run():
    my_client = connect()
    subscribe(my_client)
    my_client.loop_forever()


if __name__ == '__main__':
    run()
