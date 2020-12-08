import math

inf = math.inf

connections = {'Upper E':['Cafeteria','Medbay','Security','Reactor'],'Cafeteria':['Upper E','Weapons','Admin','Storage','Medbay'],'Weapons':['Cafeteria','Navigation','Shield','O2'],'Navigation':['Weapons','Shield','O2'],'Shield':['Weapons','Navigation','O2','Communication','Storage'],'O2':['Weapons','Navigation','Shield'],'Admin':['Cafeteria','Storage'],'Communication':['Shield','Storage'],'Storage':['Cafeteria','Shield','Admin','Communication','Electrical','Lower E'],'Electrical':['Storage','Lower E'],'Medbay':['Upper E','Cafeteria'],'Security':['Upper E','Lower E','Reactor'],'Lower E':['Storage','Electrical','Security','Reactor'],'Reactor':['Upper E','Lower E']}
names_rooms = ["Upper E", "Cafeteria", "Weapons", "Navigations", "Shield", "O2", "Admin", "Communication", "Storage", "Electrical", "MedBay", "Security", "Lower E", "Reactor"]
def Hamilton(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not start in graph:
        return None
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = Hamilton(graph, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
        return shortest
    
def step4():
    for i in range(14):
        for j in range(14):
            if(i!=j):
                start=names_rooms[i]
                end=names_rooms[j]
                result=Hamilton(connections,start,end)
                if result!=None : print(result)
    
