import random
from statistics import mean
from operator import attrgetter
from typing import List

from .player_struct import Player
from .database_datastruct import AVLTree

class Tournament() : 

    def __init__(self):

        print("Welcome to the ZLAN ! \n\n")
        print("We will now proceed to the Among Us Tournament \n")
        print(" Rules : \n\n - There is a total of 100 players. \n - 10 rounds of 3 games where we regroup players based on their ranking. \n - For the last 10 players, we will play 5 games with reinitiated ranking to give the podium. \n")
        Names = []
        with open("assets/names.txt") as file:
            lines = file.readlines()
            for line in lines:
                Names.append(str(line).rstrip("\n"))
        players = [Player(player[0], player[1]) for player in list(zip(Names, [0 for _ in range(100)]))]
        self.ladder = AVLTree()
        [self.ladder.insert(player) for player in players] # We insert all the players in the database with a initial score of 0. 



    def rounds(self, number):
        
        shufflerRole = random.choice(['Crewmates','Impostors'])
        shufflerWin = ''

        if shufflerRole == 'Crewmates':
          shufflerWin = random.choice(['by doing all the tasks.\n','by finding all the impostors.\n'])
        else : 
          shufflerWin = random.choice(['by killing the Crewmates.\n','by sabotaging the spaceship.\n'])
     
        print(f"Round number {number} is being played: \n")
        print("First game --> \n")
        print("The",shufflerRole,"won the game",shufflerWin)
        firstScores = [random.randint(0, 12) for _ in range(100 - ((number - 1) * 10))]
        print("Second game --> \n")
        print("The",shufflerRole,"won the game",shufflerWin)
        secondScores = [random.randint(0, 12) for _ in range(100 - ((number - 1) * 10))]
        print("Third game --> \n")
        print("The",shufflerRole,"won the game",shufflerWin)
        thirdScores = [random.randint(0, 12) for _ in range(100 - ((number - 1) * 10))]
        averageScores = [round(mean(data), 2) for data in list(zip(firstScores, secondScores, thirdScores))]
        self.update_ladder(averageScores)
        worstPlayers = []
        for _ in range(10):
            worst = self.ladder.get_min()
            worstPlayers.append(worst.name)
            self.ladder.delete(worst)
        print(f"These players are out > {worstPlayers} \n")



    def update_ladder(self, averageScores):
        newLadder = AVLTree()
        i = 0
        for player in self.ladder.inorder_traverse():
            player.score += averageScores[i]
            newLadder.insert(player)
            i += 1
        self.ladder = newLadder

    def finals(self):
        print("Finals --> \n")
        for player in self.ladder.inorder_traverse():
            player.score = 0
        scores = [[random.randint(0, 12) for _ in range(5)] for i in range(10)]
        averageScores = [round(mean(data), 2) for data in scores]
        self.update_ladder(averageScores)
        scoreboard = self.ladder.inorder_traverse()
        podium = sorted(scoreboard, key=attrgetter("score"), reverse=True)
        print([finalist.name + " " + str(finalist.score) for finalist in podium])


class Game():
    """
     In this class, we will initialize all the specificities that we need as known : 10 players, amongst those 10 players are 2 impostors that we initialized before.
    """
    total_game_number=0
    def __init__(self, players:List['Player']):
        if len(players) == 10:
            for player in players: 
                player.alive = True
                player.impostor = False
            self.players = players 
        else:
            self.players = None
        # Initializing 2 random impostors. 
        self.impostors = random.sample(players, k=2) 
        for player in self.impostors:
            player.impostor = True
            
        self.crewmates = []
        for player in players:
            if not player.impostor: self.crewmates.append(player)
        

    def Tasks_Vote_point(self,nb_done,multipl):
        """
        This method adds the points depending on votes and tasks done. 
        """
        liste = []
        while(nb_done!=0):
            for crewmate in self.crewmates:
                ran = random.randint(1, 3)
                # Taking the possibility that the crewmates have done all the tasks. 
                if ran == 1 and nb_done != 0: 
                    if crewmate not in liste:
                        crewmate.score += 1 * multipl
                        liste.append(crewmate)
                        nb_done -= 1
 
    
    def Kill_Count(self, nb_dead: int):
        """
        This method counts the number of kills in the game so that we can attribute points. 
        """
        liste = []
        while(nb_dead != 0):
            for crewmate in self.crewmates:
                ran = random.randint(1,3)
                # Taking the possibility that the crewmates have done all the tasks. 
                if ran == 1 and nb_dead != 0: 
                    if crewmate not in liste:
                        crewmate.alive = False
                        liste.append(crewmate)
                        nb_dead -= 1
            
    def Points(self):
        """
        This method attributes a score to each player depending on the events that are randomly listed.
        """
        victory = random.randint(1,2)
        
        # Case 1 : Impostors Won 
        if victory == 1: 
            print("\nImpostors won\n")
            
            #All crewmates are dead.
            for crewmate in self.crewmates:
                crewmate.alive = False
                
            #For each impostor win we attribute 10 points. 
            for impostor in self.impostors:
                impostor.score += 10
            im_alive = random.randint(1,3)
            
            # Taking in count the condition that the 2 impostors are alive. 
            if im_alive == 2: 
            
                # Simple kills :
                nb_murdered = random.randint(4,7)
                max_kill_im1 = nb_murdered-1
                nb_kills_im1 = random.randint(1,max_kill_im1)
                nb_kills_im2 = nb_murdered-nb_kills_im1
                
                # Undiscovered Murders :  
                undiscovered_murders = random.randint(0,4)#mettre moins de chance sur le 4??
                nb_spe_kills_im1 = random.randint(0,undiscovered_murders)
                if nb_spe_kills_im1 > nb_kills_im1: 
                    nb_spe_kills_im1 = nb_kills_im1
                nb_spe_kills_im2 = undiscovered_murders - nb_spe_kills_im1
                
                # Adding the points to the impostors : 
                points_im1 = nb_kills_im1 - nb_spe_kills_im1 + (3 * nb_spe_kills_im1)
                points_im2 = nb_kills_im2 - nb_spe_kills_im2 + (3 * nb_spe_kills_im2)
                self.impostors[0].score += points_im1
                self.impostors[1].score += points_im2
                
                # Tasks all done -> Randomizing the points : 
                tasks = random.randint(0,7) 
                self.Tasks_Vote_point(tasks,1)
                
            else:
                # If an impostor is dead we choose which one it is randomly : 
                im_dead = random.randint(0,1)
                self.impostors[im_dead].alive = False
                
                # Simple kills : 
                nb_murdered = random.randint(4, 7)
                nb_kill_im_alive = random.randint(nb_murdered - 2, nb_murdered)
                nb_kill_im_dead = nb_murdered-nb_kill_im_alive
                
                # Undiscovered Murders :  
                undiscovered_murders=random.randint(0,3)
                
                # Undiscovered Murders crewmates :  
                if undiscovered_murders == 3 and nb_kill_im_alive == 2:
                    nb_spe_kill_im_alive = 2
                    
                else:
                    nb_spe_kill_im_alive = 3
                    
                # Adding the points to the impostors : 
                points_im_alive = nb_spe_kill_im_alive * 3 - (nb_kill_im_alive - nb_spe_kill_im_alive)
                points_im_dead = nb_kill_im_dead #no special kill for dead impostor
                self.impostors[im_dead].score += points_im_dead
                im_alive = 1 - im_dead
                self.impostors[im_alive].score += points_im_alive
                
                # Tasks all done -> Randomizing the points :
                tasks = random.randint(2, 7)
                self.Tasks_Vote_point(tasks,1)
                
                # Randomizing the points for voting : 
                vote = random.randint(3, 8)
                self.Tasks_Vote_point(vote, 3)

        # Case 2 : Crewmates won.       
        else: 
            print("\nCrewmates won")
            for crewmate in self.crewmates:
                crewmate.score += 5
            win_crewmates = random.randint(0,10)
            
            if win_crewmates <= 7:
                print("by killing all the impostors\n")
                
                
                self.impostors[0].alive = False
                self.impostors[1].alive = False
                
                dead_crewmates = random.randint(1,5)
                nb_kills_im1 = random.randint(0,dead_crewmates)
                self.impostors[0].score += nb_kills_im1
                self.impostors[1].score += dead_crewmates-nb_kills_im1
                
                
                self.Kill_Count(dead_crewmates)
                
                
                dead_crewmate_first_time = random.randint(0, dead_crewmates)
                vote = random.randint(3, 8 - dead_crewmate_first_time)
                self.Tasks_Vote_point(vote, 3)
                
             
                vote = random.randint(3, 8 - dead_crewmates)
                self.Tasks_Vote_point(vote, 3)
                
                
                tasks = random.randint(1, 6) 
                self.Tasks_Vote_point(tasks, 1)
                
            else:
                print("by doing all the tasks\n")
                
                self.Tasks_Vote_point(8, 1)
                
                
                dead_crewmates = random.randint(0, 4)
                self.Kill_Count(dead_crewmates)
                
                
                im_is_dead = random.randint(1, 2)
                if im_is_dead == 1:
                    deadim = random.randint(0, 1)
                    self.impostors[deadim].alive = False
                    
                
                    cm_vote_im = random.randint(5, 7)
                    self.Tasks_Vote_point(cm_vote_im, 3)
