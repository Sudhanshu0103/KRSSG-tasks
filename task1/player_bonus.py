#player
import socket
import pickle

host = socket.gethostbyname(socket.gethostname())
port = 5050
player = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
player.connect((host , port))
print("Connected to casino server.")

#getting number of rounds from casino server
rounds_data = player.recv(1000)
rounds = pickle.loads(rounds_data)
print("number of rounds are: ",rounds)

while True:
    print("Starting a series of rounds.")
    for round in range(rounds):
        recv_data = player.recv(1000)
        cards = pickle.loads(recv_data)
        for card in cards:
            card = ((card-1)%13 + 1)
        maxCard = max(cards)
        data = pickle.dumps(maxCard)
        player.send(data)
    # Recieve the round winners from casino
    recv_data = player.recv(1000)
    Winners = pickle.loads(recv_data)
    print("Winners: ", Winners)
    
    # Recieve message from casino whether to continue or not
    recv_data = player.recv(1000)
    msg = pickle.loads(recv_data)
    if msg == "Continue":
        continue
    else:
        print("Exiting")
        break
player.close()