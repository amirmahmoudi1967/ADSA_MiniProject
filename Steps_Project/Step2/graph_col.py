colors = ['Red', 'Blue', 'Green']

players = [0,1,2,3,4,5,6,7,8,9]

#shows the players seen by a player (directed graph)
seen = {}
seen[0] = [1,4,5]
seen[1] = [0,2,6]
seen[2] = [1,3,7]
seen[3] = [2,4,8]
seen[4] = [0,3,9]
seen[5] = [0,7,8]
seen[6] = [1,8,9]
seen[7] = [2,5,9]
seen[8] = [3,5,6]
seen[9] = [4,6,7]

#dictionary with all players with their affected color
colors_of_players = {}

def promising(player, color):
  #this function test if two players have the same color if not we apply the current color to the current player
  #if not we check other colors
  for neighbor in seen.get(player): 
    color_of_neighbor = colors_of_players.get(neighbor)
    if color_of_neighbor == color:
      return False
  return True

def get_color_for_player(player):
  #we will test each color in our color list on every player
      for color in colors:
          if promising(player, color):
              return color

def impostors(player):
      result=[]
      suspect=[]
      """
      this loop will check the players seen by the different suspects and will admit
      that the potential partner for each suspect is one of the player the suspect hasn't seen
      i.e : 4 is suspect but he saw 0,3 and 9 so his partner is among all the player less player
      0, 3 and 9
      """
      for neighbor in seen.get(player):
          for player in players:
              if player not in seen.get(neighbor):
                  if(player!=neighbor):
                      suspect.append(player)
          result.append(suspect)
          suspect=[]
      return result


class Graph_color():

  def graph_coloring():
        for player in players:
            colors_of_players[player] = get_color_for_player(player)
        print(colors_of_players)
        #we initiate the dead player as player 0
        player=0
        answer=impostors(player)
        #printing result for each suspect
        for i in range(len(seen[player])):
            print("For the suspect player "+str(seen[player][i])+" we have his potential partner :")
            print(answer[i])

  #graph_coloring()



