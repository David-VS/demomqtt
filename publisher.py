from paho.mqtt import client
import time


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

    my_client = client.Client(client.CallbackAPIVersion.VERSION2)
    my_client.tls_set(ca_certs='./certificates/emqxsl-ca.crt')
    my_client.username_pw_set(username, password)
    my_client.connect(broker, port)
    my_client.on_connect = on_connect
    return my_client


def publish(my_client):

    while True:
        time.sleep(2)
        msg = input("message = ")
        topic = "prog3/mqtt"

        result = my_client.publish(topic, msg)
        if result[0] == 0:
            print("message sent")
        else:
            print("failed to publish")


def run():
    my_client = connect()
    publish(my_client)


if __name__ == '__main__':
    run()
