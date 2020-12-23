

colors = ['Red', 'Blue', 'Green']

players = [0,1,2,3,4,5,6,7,8,9]

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


colors_of_players = {}

def promising(player, color):
  for neighbor in seen.get(player): 
    color_of_neighbor = colors_of_players.get(neighbor)
    if color_of_neighbor == color:
      return False
  return True

def get_color_for_player(player):
      for color in colors:
          if promising(player, color):
              return color

def impostors(player):
      result=[]
      suspect=[]
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
        player=0
        answer=impostors(player)
        for i in range(len(seen[player])):
            print("For the suspect "+str(seen[player][i])+" we have :")
            print(answer[i])

  #graph_coloring()



