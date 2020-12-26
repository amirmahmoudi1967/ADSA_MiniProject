import math

inf = math.inf
#we represented the graph as a dictionary with in key a room and in values the room connected to the key
connections = {'Upper E':['Cafeteria','Medbay','Security','Reactor'],'Cafeteria':['Upper E','Weapons','Admin','Storage','Medbay'],'Weapons':['Cafeteria','Navigation','Shield','O2'],'Navigation':['Weapons','Shield','O2'],'Shield':['Weapons','Navigation','O2','Communication','Storage'],'O2':['Weapons','Navigation','Shield'],'Admin':['Cafeteria','Storage'],'Communication':['Shield','Storage'],'Storage':['Cafeteria','Shield','Admin','Communication','Electrical','Lower E'],'Electrical':['Storage','Lower E'],'Medbay':['Upper E','Cafeteria'],'Security':['Upper E','Lower E','Reactor'],'Lower E':['Storage','Electrical','Security','Reactor'],'Reactor':['Upper E','Lower E']}
names_rooms = ["Upper E", "Cafeteria", "Weapons", "Navigations", "Shield", "O2", "Admin", "Communication", "Storage", "Electrical", "MedBay", "Security", "Lower E", "Reactor"]


def Hamilton_quickest(graph, start, end, path=[]):#recursive method
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
    path = path + [start]#add the previous room from last call to the path
    if not start in graph:
        return []
    paths = []
    for node in graph[start]:#we go through all rooms connected to the current graph
        if node not in path:#if the node isn't in path list answer we add it by recall our function
            newpaths = Hamilton_all_rooms(graph, node, end, path)
            for newpath in newpaths:
                if len(newpath)==14::#we only keep the path going through all rooms
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
                        print("We are going from "+ start + " to " + end)
                        print(result)

        print("\n\nHow to go from a room to another passing by all rooms \n")
        for i in range(14):
            for j in range(14):
                if(i!=j):
                    start=names_rooms[i]
                    end=names_rooms[j]
                    result=Hamilton_all_rooms(connections,start,end)
                    print("We are going from "+ start + " to " + end+"\n")
                    if result!=[] : 
                        print(result)
                        print("\n")
                    else: print("Sorry, we don't have path passing by all the rooms\n")
    
