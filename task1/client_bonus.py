import socket
import pickle

host = socket.gethostbyname(socket.gethostname())
port = 5050
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host , port))
print("Connected to casino server.")

while True:
    rounds = int(input('enter number of rounds: '))
    players = int(input('enter number of players: '))
    print(rounds)
    print(players)
    if (rounds % players == 0):
        print("rounds should not be divisible by players, give inputs again ")
    else:
        data_rounds = pickle.dumps(rounds)
        client.send(data_rounds)
        data_players = pickle.dumps(players)
        client.send(data_players)
        
        
        break
print("exiting")
client.close()