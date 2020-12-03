from ..Step1.player_struct import Player
from ..Step1.games_tournament import Game
import numpy as np

class Run_Step2():

 def test_has_seen():
    """
    Method for testing the has-seen algorithm by computing the probability for each player of being an impostor in the example given.
    """
    
    #The incidence matrix representing the has-seen graph.   
    incidence_matrix=np.array([[1,1,1,0,0,0,0,0,0,0,0,0,0,0,0],
                               [1,0,0,1,1,0,0,0,0,0,0,0,0,0,0],
                               [0,0,0,1,0,1,1,0,0,0,0,0,0,0,0],
                               [0,0,0,0,0,1,0,1,1,0,0,0,0,0,0],
                               [0,1,0,0,0,0,0,1,0,1,0,0,0,0,0],
                               [0,0,1,0,0,0,0,0,0,0,1,1,0,0,0],
                               [0,0,0,1,0,0,0,0,0,0,0,0,1,1,0],
                               [0,0,0,0,0,0,1,0,0,0,1,0,0,0,1],
                               [0,0,0,0,0,0,0,0,1,0,0,1,1,0,0],
                               [0,0,0,0,0,0,0,0,0,1,0,0,0,1,1]])
    players = [Player('Player 0'), Player('Player 1'), Player('Player 2'), 
               Player('Player 3'), Player('Player 4'), Player('Player 5'), 
               Player('Player 6'), Player('Player 7'), Player('Player 8'), Player('Player 9')]
    game = Game(players)
    game.probable_impostors(players[0], incidence_matrix)
