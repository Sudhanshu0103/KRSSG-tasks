import socket
import pickle

port = 5050
host = socket.gethostbyname(socket.gethostname())
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host , port))

inputs_data = client.recv(1000)
num_inputs = pickle.loads(inputs_data)

for i in range(num_inputs):
    str_inp = str(input("enter input :"))
    print(str_inp)
    to_send = pickle.dumps(str_inp)
    client.send(to_send)
print("connection closed")
client.close()