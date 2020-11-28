############################## IMPORTED LIBRARIES ##############################
import random 
import numpy as np 
import pandas as pd
import math
inf = math.inf
from typing import List, Dict, Tuple, Set

from statistics import mean
from operator import attrgetter


############################## STEP 1 ##############################

# 1- Present a data structure to represent a player and its score : 

class Player() : 
    def __init__(self, name:str, score= None) : 
        self.name = name 
        self.impostor = False
        self.alive = True 
        self.score = score if score is not None else 0
        self.left = None  
        self.right = None
    
    def __str__(self) -> str: 
        res = self.name + 'is'
        if self.alive: 
            res += ' alive, and he is '
        else : 
            res += ' dead, and he is '
        if self.impostor: 
            res += 'an Impostor'
        else : 
            res += 'a Crewmate'
        return res 

# 2- Present a most optimized data structures for the tournament(called database) : 
# 3- Method that randomize player score at each game (between 0 point to 12 points) : 
# 4- Method to update Players score and the database : 
# 5- Method to create and random games based on the database : 

class AVLTree():
    def __init__(self):
        self.node = None
        self.height = -1
        self.balance = 0

    def insert(self, player):
        if self.node == None:
            self.node = player
            self.node.right = AVLTree()
            self.node.left = AVLTree()
        elif player.score > self.node.score:
            self.node.right.insert(player)
        else:
            self.node.left.insert(player)
        self.rebalance()

    def delete(self, player):
        if self.node != None:
            if self.node.name == player.name:
                # If we find the key in the leaf node, we erase the player. 
                if not self.node.left.node and not self.node.right.node:
                    self.node = None
                # Node has only one subtree (right), replacing the root
                elif not self.node.left.node:                
                    self.node = self.node.right.node
                # Node has only one subtree (left), replacing the root
                elif not self.node.right.node:
                    self.node = self.node.left.node
                else:
                    # Find  successor as smallest node in right subtree or
                    # predecessor as largest node in left subtree
                    successor = self.node.right.node  
                    while successor and successor.left.node:
                        successor = successor.left.node

                    if successor:
                        self.node = successor
                        # Delete successor from the replaced node right subree
                        self.node.right.delete(successor)

            elif player.score <= self.node.score:
                self.node.left.delete(player)

            elif player.score > self.node.score:
                self.node.right.delete(player)

            # Rebalancing the tree after deleting the players so that we have a balanced tree. 
            self.rebalance()

    def rebalance(self):
        """
        Rebalance tree
        After inserting or deleting a node, we have to check if the node is balanced and 
        update it so that we respect the AVL Tree's conditions. 
        """
        # Check if we need to rebalance the tree
        self.update_heights(recursive=False)
        self.update_balances(False)

        # For each node checked, 
        #   if the balance factor remains −1, 0, or +1 then no rotations are necessary.
        while self.balance < -1 or self.balance > 1: 
            # Left subtree is larger than right subtree
            if self.balance > 1:

                # Left Right Caseif self.node.left.balance < 0:self.node.left.rotate_left()
                self.update_heights()
                self.update_balances()

                self.rotate_right()
                self.update_heights()
                self.update_balances()
            
            # Right subtree is larger than left subtree
            if self.balance < -1:
                
                # Right Left Case
                if self.node.right.balance > 0:
                    self.node.right.rotate_right() # we're in case III
                    self.update_heights()
                    self.update_balances()

                # Right Right Case
                self.rotate_left()
                self.update_heights()
                self.update_balances()

    def update_heights(self, recursive=True):
        """
        Update tree height
        Tree height is max height of either left or right subtrees +1 for root of the tree
        """
        if self.node: 
            if recursive: 
                if self.node.left: 
                    self.node.left.update_heights()
                if self.node.right:
                    self.node.right.update_heights()
            
            self.height = 1 + max(self.node.left.height, self.node.right.height)
        else: 
            self.height = -1

    def update_balances(self, recursive=True):
        """
        Calculate tree balance factor
        The balance factor is calculated as follows: 
        balance = height(left subtree) - height(right subtree). 
        """
        if self.node:
            if recursive:
                if self.node.left:
                    self.node.left.update_balances()
                if self.node.right:
                    self.node.right.update_balances()

            self.balance = self.node.left.height - self.node.right.height
        else:
            self.balance = 0

    def rotate_right(self):
        """
        Right rotation
        set self as the right subtree of left subree
        """
        new_root = self.node.left.node
        new_left_sub = new_root.right.node
        old_root = self.node

        self.node = new_root
        old_root.left.node = new_left_sub
        new_root.right.node = old_root

    def rotate_left(self):
        """
        Left rotation
        set self as the left subtree of right subree
        """
        new_root = self.node.right.node
        new_left_sub = new_root.left.node
        old_root = self.node

        self.node = new_root
        old_root.right.node = new_left_sub
        new_root.left.node = old_root
    
    def inorder_traverse(self):
        """
        Inorder traversal of the tree to return a list of each
        Player() object contained in the AVL tree
        """
        result = []

        if not self.node:
            return result

        result.extend(self.node.left.inorder_traverse())
        result.append(self.node)
        result.extend(self.node.right.inorder_traverse())

        return result

    def get_min(self):
        # return the objet from Player() with the minimum score
        current = self.node
        while current.left.node is not None:
            current = current.left.node
        return current

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


    @staticmethod 
    def run():
        step1 = Tournament()
        [step1.rounds(roundNumber) for roundNumber in range(1, 10)] # We play the 10 rounds of 3 games
        step1.finals()

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


############################## STEP 2 ##############################

    def player_has_seen(self, p: 'Player', incidence_matrix: List[List[bool]]) -> Tuple[List['Player'], List['Player']]:
        """
        This method returns the list of players one has seen according to the incidence matrix, along
        with the list of players he has not seen.
        """
        
        # Defining the line of the incidence matrix on which the player is.
        line_p = 0
        for i in range(10):
            if p == self.players[i]: line_p = i
            
        list_has_seen = []
        for index_c in range(len(incidence_matrix[0])): 
          # The incidence matrix has dimension 0 of length 10 but variable dimension 1 (number of relations) :
            if incidence_matrix[line_p, index_c] == 1:
                for index_l in range(10):
                    if index_l != line_p and incidence_matrix[index_l, index_c] == 1: 
                        list_has_seen.append(self.players[index_l])
             
        list_not_seen = []
        for player in self.players:
            if player not in list_has_seen and player != p:
                list_not_seen.append(player)
        return list_has_seen, list_not_seen
    

    def probable_impostors(self, dead_crewmate: 'Player', incidence_matrix: List[List[bool]]) -> Dict['Player', float]:
        """
        Setting up a dictionnary with a player as key and its probability of being impostor as value.
        """
        probabilities = {player:0 for player in self.players}
        # Taking in count the list of players having seen the dead crewmate -> Potential first Impostor.
        first_suspects = self.player_has_seen(dead_crewmate, incidence_matrix)[0] 
        # List of suspects for imposter 2.
        second_suspects_occ = [] 
        for suspect in first_suspects:
            probabilities[suspect] += 1/len(first_suspects)
            for suspect2 in self.player_has_seen(suspect, incidence_matrix)[1]: 
                # Adding each player not seen by the current suspect to the second suspect occurence list.    
                second_suspects_occ.append(suspect2)
                # Each player will appear as much times as there are suspects he has not seen.
            
        for suspect2 in second_suspects_occ: 
            probabilities[suspect2] += 1/len(second_suspects_occ)
            
        impostor_probabilities = {player: probabilities[player] for player in sorted(probabilities, key=probabilities.get, reverse=True)}
        
        print("The dead crewmate is", dead_crewmate.name, "who has seen :")
        for s in first_suspects:
            print (s.name)
            
        print("The most probable impostors are therefore :")
        
        for p in impostor_probabilities.keys():
            print (p.name, impostor_probabilities[p])
            
        return impostor_probabilities
        

############################## STEP 3 ##############################

# If there is no edge between two nodes, we set the adjacency value as inf : 
crewmates_graph = [[0, 15, inf, inf, inf, inf, inf, inf, inf, inf, 10, 9, 12, 9],
[15, 0, 9, inf, inf, inf, 11, inf, 12, inf, 10, inf, inf, inf], 
[inf, 9, 0, 10, inf, 7, inf, inf, inf, inf, inf,inf, inf, inf], 
[inf, inf, 10, 0, 12, 10, inf, inf, inf, inf, inf, inf,inf, inf], 
[inf, inf, inf, 12, 0, 13,inf, 6, 11, inf, inf, inf, inf,inf], 
[inf, inf, 7, 10, 13, 0, inf, inf, inf, inf,inf, inf, inf, inf], 
[inf, 11, inf, inf, inf, inf, 0, inf, 8, inf, inf, inf, inf,inf], 
[inf, inf, inf, inf, 6, inf, inf, 0, 9, inf, inf, inf, inf,inf], 
[inf, 12, inf, inf, 11, inf, 8, 9, 0, 10, inf, inf, 14, inf], 
[inf, inf, inf, inf,inf, inf, inf, inf, 10, 0, inf, inf, 14, inf], 
[10, 10, inf, inf, inf, inf,inf, inf, inf, inf, 0, inf, inf, inf], 
[9, inf, inf, inf, inf,inf, inf, inf, inf,inf, inf, 0, 9, 6], 
[12,inf, inf, inf, inf,inf, inf, inf, 14, 14, inf, 9, 0, 9], 
[9, inf, inf, inf, inf,inf, inf, inf, inf,inf, inf, 6, 9, 0]]

impostors_graph = [[0, 15, inf, inf, inf, inf, inf, inf, inf, inf, 10, 9, 12, 0, inf], 
[15, 0, 9, inf, inf, inf, 0, inf, 12, inf, 10, inf, inf, inf, 0], 
[inf, 9, 0, 0, inf, 7, inf, inf, inf, inf, inf, inf, inf, inf, inf], 
[inf, inf, 0, 0, 0, 10, inf, inf, inf, inf, inf, inf, inf, inf, 6], 
[inf, inf, inf, 0, 0, inf, inf, 6, 11, inf, inf, inf, inf, inf,  6], 
[inf, inf, 7, 10, inf,  inf, inf, inf, inf, inf, inf, inf, inf, inf,  10], 
[inf, 0, inf, inf, inf, inf, 0, inf, 8, inf, inf, inf, inf, inf, 0], 
[inf, inf, inf, inf, 6, inf, inf, 0, 9, inf, inf, inf, inf, inf, inf],  
[inf, 12, inf, inf, 11, inf, 8, 9, 0, 10, inf, inf, 14, inf, inf], 
[inf, inf, inf, inf, inf, inf, inf, inf, 10, 0, 0, 0, 14, inf, inf], 
[10, 10, inf, inf, inf, inf, inf, inf, inf, 0, 0, 0, inf, inf, inf], 
[9, inf, inf, inf, inf, inf, inf, inf, inf, 0, 0, 0, 9, 6, inf],
[12, inf, inf, inf, inf, inf, inf, inf, 14, 14, inf, 9, 0, 0, inf],
[0, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, 6, 0, 0, inf], 
[inf, 0, inf, 6, 6, 10, 0, inf, inf, inf, inf, inf, inf, inf, 0]]

names_rooms_crew = ["Upper E", "Cafeteria", "Weapons", "Navigations", "Shield", "O2", "Unnamed1", "Unnamed2", "Storage",  "Electrical", "Medbay", "Security", "Lower E", "Reactor"]

names_rooms_imp = ["Upper E", "Cafeteria", "Weapons", "Navigations", "Shield", "O2", "Unnamed1", "Unnamed2", "Storage", "Electrical", "MedBay", "Security", "Lower E", "Reactor", "Corridor W"]

# We will use FloydWarshall : 
def floydWarshall(matrix):
    """Return the minimal distances between every node.
    
    :param matrix: Matrix of adjacency of a graph.
    :return: Matrix of minimal distances between every node.
    """
    dist = matrix
    for k in range(len(matrix)):
        for i in range(len(matrix)):
            for j in range(len(matrix)): 
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist






############################## TESTING FUNCTIONS ##############################

def test_points():
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

def test_distance():
  df_crew = pd.DataFrame(floydWarshall(crewmates_graph), columns = names_rooms_crew, index = names_rooms_crew)
  print(df_crew)

  df_imp = pd.DataFrame(floydWarshall(impostors_graph), columns = names_rooms_imp, index = names_rooms_imp)
  print(df_imp)

#Tournament.run()

#test_points()

#test_has_seen() 

test_distance()
