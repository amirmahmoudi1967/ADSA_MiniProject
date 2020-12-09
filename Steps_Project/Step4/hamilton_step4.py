import math

inf = math.inf

connections = {'Upper E':['Cafeteria','Medbay','Security','Reactor'],'Cafeteria':['Upper E','Weapons','Admin','Storage','Medbay'],'Weapons':['Cafeteria','Navigation','Shield','O2'],'Navigation':['Weapons','Shield','O2'],'Shield':['Weapons','Navigation','O2','Communication','Storage'],'O2':['Weapons','Navigation','Shield'],'Admin':['Cafeteria','Storage'],'Communication':['Shield','Storage'],'Storage':['Cafeteria','Shield','Admin','Communication','Electrical','Lower E'],'Electrical':['Storage','Lower E'],'Medbay':['Upper E','Cafeteria'],'Security':['Upper E','Lower E','Reactor'],'Lower E':['Storage','Electrical','Security','Reactor'],'Reactor':['Upper E','Lower E']}
names_rooms = ["Upper E", "Cafeteria", "Weapons", "Navigations", "Shield", "O2", "Admin", "Communication", "Storage", "Electrical", "MedBay", "Security", "Lower E", "Reactor"]


def Hamilton_quickest(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not start in graph:
        return None
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = Hamilton_quickest(graph, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
        return shortest
    
def Hamilton_all_rooms(graph, start, end, path=[]):
    path = path + [start]
    if not start in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = Hamilton_all_rooms(graph, node, end, path)
            for newpath in newpaths:
                if len(newpath)==14:
                    paths.append(newpath)

    if start == end:
        return [path]
    return paths

class Hamilton_backtracking :
    def step4():
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
    
