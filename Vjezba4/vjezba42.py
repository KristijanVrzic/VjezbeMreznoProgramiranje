#echo_client.py
import socket
import datetime
from local_machine_info import print_machine_info

print_machine_info()

host = socket.gethostname()
port = 12345
client_socket = socket.socket()

client_socket.connect((host,port))

msg = " Text which isnt sent to the ".encode()
client_socket.sendall(msg)

str = input("Enter text: ".encode())
client_socket.sendall(str.encode())

if(str == "kristijan_vrzic"):
    print("Error!")

print (datetime.datetime.now())

data = client_socket.recv(1024)

print(data)
client_socket.close()