import random
from data import list_truths, list_dares
import Players

print("WELCOME TO TRUTH OR DARE")
"""players = int(input("no.of players: "))
list_players = []
for i in range(0, players ):
    name = input("enter player name:\n")
    list_players.append(name)
"""

play = Players()
play_game = True
play.players_names()
while play_game:
    play.play_1()

    game = input("Do you wanna play game? yes or no: ")
    if game == "no":
        play_game = False
