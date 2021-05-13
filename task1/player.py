#player
import socket
import pickle

host = socket.gethostbyname(socket.gethostname())
port = 5050
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host , port))
print("Connected to casino server.")

rounds = 4
while True:
    print("Starting a series of rounds.")
    for round in range(rounds):
        recv_data = client.recv(1000)
        cards = pickle.loads(recv_data)
        for card in cards:
            card = ((card-1)%13 + 1)
        maxCard = max(cards)
        data = pickle.dumps(maxCard)
        client.send(data)
    # Recieve the round winners from casino
    recv_data = client.recv(1000)
    Winners = pickle.loads(recv_data)
    print("Winners: ", Winners)
    
    # Recieve message from casino whether to continue or not
    recv_data = client.recv(1000)
    msg = pickle.loads(recv_data)
    if msg == "Continue":
        continue
    else:
        print("Exiting")
        break
client.close()