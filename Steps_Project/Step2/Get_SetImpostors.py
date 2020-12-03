from .player_struct import Player

from typing import List, Dict, Tuple


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