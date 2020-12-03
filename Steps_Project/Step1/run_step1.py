from .player_struct import Player
from .games_tournament import Tournament
from .games_tournament import Game

class Run_Step1(): 

  def run_tournament():
        step1 = Tournament()
        [step1.rounds(roundNumber) for roundNumber in range(1, 10)] # We play the 10 rounds of 3 games
        step1.finals()
        print("\n")

  def run_game_points():
    """
    Method for testing the points attribution between players in a game
    Returns
    -------
    None.
    """
    players = [Player('ZeratoR'), Player('Domingo'), Player('Xari'), 
               Player('Kamet0'), Player('Kotei'), Player('Maghla'), 
               Player('Gotaga'), Player('Squeezie'), Player('Skyyart'), Player('Solary')]
    game = Game(players)
    
    game.Points()
    for player in game.players:
        print("Impostor :", player.impostor, player.name, player.score)
