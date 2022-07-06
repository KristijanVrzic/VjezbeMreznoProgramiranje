import socket
import ssl
import datetime
from xml.etree.ElementInclude import include

print("Executing...")

print(datetime.datetime.now())
from SSL_Server import HOST as SERVER_HOST
from SSL_Server import PORT as SERVER_PORT
from Local_Machine_Info import print_machine_info
print_machine_info()

HOST = "127.0.0.1"
PORT = 60002
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

client = ssl.wrap_socket(client, keyfile="privateKey.pem", certfile="privateKey.pub")
if __name__ == "__main__":
    client.bind((HOST, PORT))
    client.connect((SERVER_HOST, SERVER_PORT))

    while True:
        from time import sleep

        client.send("Encode".encode("utf-8"))
        sleep(1)