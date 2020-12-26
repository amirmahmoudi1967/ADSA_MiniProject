import math

inf = math.inf
#we represented the graph as a dictionary with in key a room and in values the room connected to the key
connections = {'Upper E':['Cafeteria','Medbay','Security','Reactor','Lower E'],'Cafeteria':['Upper E','Weapons','Admin','Storage','Medbay'],'Weapons':['Cafeteria','Navigation','Shield','O2'],'Navigation':['Weapons','Shield','O2'],'Shield':['Weapons','Navigation','O2','Communication','Storage'],'O2':['Weapons','Navigation','Shield'],'Admin':['Cafeteria','Storage'],'Communication':['Shield','Storage'],'Storage':['Cafeteria','Shield','Admin','Communication','Electrical','Lower E'],'Electrical':['Storage','Lower E'],'Medbay':['Upper E','Cafeteria'],'Security':['Upper E','Lower E','Reactor'],'Lower E':['Storage','Electrical','Security','Reactor','Upper E'],'Reactor':['Upper E','Lower E','Security']}
names_rooms = ["Upper E", "Cafeteria", "Weapons", "Navigation", "Shield", "O2", "Admin", "Communication", "Storage", "Electrical", "Medbay", "Security", "Lower E", "Reactor"]


def Hamilton_quickest(graph, start, end, path=[]):#recursive method
  """
 Method for computing the quickest path between a pair of rooms amongst all the rooms starting from a room and ending in the last room. 
  """
  path = path + [start]#add the previous room from last call to the path
  if start == end:
      return path
  if not start in graph:
      return None
  shortest = None
  for node in graph[start]:#we go through all rooms connected to the current graph
      if node not in path:#if the node isn't in path list answer we add it by recall our function
          newpath = Hamilton_quickest(graph, node, end, path)
          if newpath:
              if not shortest or len(newpath) < len(shortest):#we only keep the path going through the fewest number of rooms
                  shortest = newpath
      return shortest
    
def Hamilton_all_rooms(graph, start, end, path=[]):#recursive method
  """
 Method for computing the quickest path for all the rooms going from the starting room to the last room visiting all the rooms just one time. 
  """
  path = path + [start]#add the previous room from last call to the path
  if not start in graph:
      return []
  paths = []
  for node in graph[start]:#we go through all rooms connected to the current graph
      if node not in path:#if the node isn't in path list answer we add it by recall our function
          newpaths = Hamilton_all_rooms(graph, node, end, path)
          for newpath in newpaths:
              if len(newpath)==14:#we only keep the path going through all rooms
                  paths.append(newpath)

  if start == end:#we placed this condition at the end in order that the function try to pass by all rooms
                  #i.e going from Upper E to Cafeteria is a direct path so we prevent an instant return by
                  #compute this condition at the end
      return [path]
  return paths


class Hamilton_backtracking :
    def step4():
        #printing the output for each function
        print("How to go from a room to another passing by the fewest number of rooms \n")
        for i in range(14):
            for j in range(14):
                if(i!=j):
                    start=names_rooms[i]
                    end=names_rooms[j]
                    result=Hamilton_quickest(connections,start,end)
                    if result!=None :
                        #print("We are going from "+ start + " to " + end)
                        print("Starting room : "+ start + " ---> Ending room : "+ end+"\n")
                        #print(result)
                        print("The quickest path found is : " + str(result)+"\n")

        print("\n\nHow to go from a room to another passing by all rooms \n\n")
        for i in range(14):
            for j in range(14):
                if(i!=j):
                    start=names_rooms[i]
                    end=names_rooms[j]
                    result=Hamilton_all_rooms(connections,start,end)
                    print("Starting room : "+ start + " ---> Ending room : "+ end+"\n")
                    #print("We are going from "+ start + " to " + end+"\n")
                    if result!=[] : 
                        print("The paths passing by all rooms are : \n")
                        for path in result:
                          print(str(path)+"\n") 
                        #print(result)
                        print("\n")
                    else: print("Sorry, we don't have path passing by all the rooms\n")
    
