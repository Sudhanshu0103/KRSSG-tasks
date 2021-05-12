#server
import socket
import pickle
from threading import Thread
import random

host = '127.0.0.1'
port = 6969
casino = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
casino.bind((host , port))

def thread_func(card_array, conn, recieved_cards, player_index):
    #send cards
    data = pickle.dumps(card_array)
    conn.send(data)
    rec_data = conn.recv(20)
    max_card = pickle.loads(rec_data)
    recieved_cards[player_index] = max_card

def start():
    casino.listen(10)
    print("server is listening")
    rounds = 4
    num_players = 3
    cards_per_player = 3
    player_connection_array = []
    
    # establish connections with all players
    for i in range(num_players):
        conn , addr = casino.accept()
        print("connection established with player ", i+1)
        player_connection_array.append(conn)
    print("All connections established")
    
    while True:
        print("Starting a series of rounds.")
        # storing the wins in this series of rounds
        wins = [0 for i in range(rounds)]
        
        for i in range(rounds):
            print("Round: ", i+1)
            # send and recieve numbers to each player
            ## generate 3 random cards for each player
            rand_cards = random.sample(range(1,53), cards_per_player*num_players)
            ## array of recieved cards
            recieved_cards = [0 for i in range(num_players)]

            ## create threads to handle all players simultaneously. Store these threads in an array.
            playerThreads = [None for i in range(num_players)]

            for j in range(num_players):
                cards_slice = rand_cards[j*cards_per_player:(j+1)*cards_per_player]
                playerThreads[j] = Thread(target=thread_func, args=(cards_slice, player_connection_array[j], recieved_cards, j))
                playerThreads[j].start()
                # print("Thread started for player: ", j+1)
            
            ## Wait for all the threads to join
            for j in range(num_players):
                playerThreads[j].join()
                # print("Thread joined for player: ", j+1)

            # calculate max number and winner
            max_receive_card = max(recieved_cards)
            # increase points for player with max card
            for j in range(num_players):
                if recieved_cards[j] == max_receive_card :
                    wins[j]+= 1
                    print("Player with max card", j+1)
        
        # print and store winner 
        # calculate winner
        max_score = max(wins)
        winners = []
        for i in range(num_players):
            if(wins[i] == max_score):
                winners.append(i+1)
        # send winners to all players
        winner_data = pickle.dumps(winners)
        for i in range(num_players):
            player_connection_array[i].send(winner_data)
        if len(winners)>1:
            print("Winners : ", winners)
        else :
            print("Winner : ", winners[0])

        # Ask whether user wants around series of rounds
        user_input = input('Do you want to continue another series of rounds? (y/n): ')
        if user_input!='y' and user_input!='Y':
            print("You chose not to continue. Exiting")
            
            # Notify all users to exit.
            for i in range(num_players):
                player_connection_array[i].send(pickle.dumps("Exit"))
            break
        else:
            print("You chose to continue.")
            # Notify all users to continue.
            for i in range(num_players):
                player_connection_array[i].send(pickle.dumps("Continue"))

    # Closing all player connections
    for i in range(num_players):
        player_connection_array[i].close()
    print("All player connections closed")

start()
