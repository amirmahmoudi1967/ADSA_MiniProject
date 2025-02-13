import numpy as np
import math
import pandas as pd 

inf = math.inf
names_rooms = ["Upper E", "Cafeteria", "Weapons", "Navigations", "Shield", "O2", "Admin", "Communication", "Storage", "Electrical", "MedBay", "Security", "Lower E", "Reactor", "West Corridor"]
class Vertex:#Class use to define vertex we obtain parent other vertex we are linked to

    def __init__(self, name):
        self.name = name
        self.links = []

    def __str__(self):#To report informations about the current vertex such as name,parent,link,distance
        seed = f"\nRoom Name : {self.name}\n\n Links :"
        for link in self.links:
            seed += f"\n\tVertex {link[0].name}, Distance: {link[1]}\n"
        return seed


def reporttxt(graph): #function to resport in a txt file
    file = open("report.txt", "a")
    for vertex in graph:
          report = vertex.__str__()
          print(report)
          file.write(report + "\n")
    file.write("\n")
    file.close()
   #computing exercice

    
def FloydWarshall(graph):#Floyd-Warshall algorithm
    if len(graph)==15:
        with open("report.txt", "a") as file:
            file.write("Floyd-Warshall algorithm for impostors : \n")
    else :
        with open("report.txt", "a") as file:
            file.write("Floyd-Warshall algorithm for crewmates : \n")
    n = len(graph)
    matrix = np.full((n, n), inf)
    for i in range(n):
        temp = list(zip(*graph[i].links))
        for j in range(n):
            if i == j:
                matrix[i][j] = 0
            else:
                try:
                    k = temp[0].index(graph[j])
                    matrix[i][j] = temp[1][k]
                except ValueError:
                    pass
    print(matrix)
    print("\n\n")
    with open("report.txt", "a") as file:#report in txt
        file.write("First matrix floyd Warshall\n")
        file.write(str(matrix) + "\n\n")
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if matrix[i][j] > matrix[i][k] + matrix[k][j]:
                    matrix[i][j] = int(matrix[i][k] + matrix[k][j])
                    
    #report the matrix as a dataframe 2 methods (if and else) because impostor have 1 extra room
    if(len(matrix)==15):
        df = pd.DataFrame(data=matrix,index = names_rooms, columns=names_rooms)
    else:
        names_rooms_crew=names_rooms
        names_rooms_crew.remove("West Corridor")
        df = pd.DataFrame(data=matrix,index = names_rooms_crew, columns=names_rooms_crew)
    print(df)
    
    with open("report.txt", "a") as file:#report in txt
        file.write("Second matrix floyd Warshall\n")
        file.write(str(df) + "\n\n")
    reporttxt(graph)
    return matrix

def compare(matrix_1,matrix_2):
    #we consider the two matrix with only the common rooms so west corrider is removed from impostors matrix
    for i in range (14):
        for j in range (14):
            if(i!=j):#we don't compare when we go from and to the same room (upper E to upper E)
                #time delay is crewmate's time - impostor's time
                delay=matrix_2[i][j]-matrix_1[i][j]
                start=names_rooms[i]
                end=names_rooms[j]
                #printing answer for each pair of room
                print("impostors going from "+start+" to "+end+" is "+str(delay)+" seconds quicker than a crewmate")
        print("\n\n")
      
class FloydWarshall_runstep3 : 

 def FloydWarshall_Pathfinding():
    with open("report.txt", "w") as file:# we create a report txt file (it will be in the same repertory as this code)
        file.write("Step 3 Floyd Warshall \n\n")
    graph_impostors=[]
    graph_crewmates=[]
    for i in range(len(names_rooms)):
        graph_impostors.append(Vertex(names_rooms[i]))#graph with 15 vertices
        graph_crewmates.append(Vertex(names_rooms[i]))#graph with 14 vertices
    
    #we create the graphs
    #to add link we have (vertex, weigth)
    graph_impostors[0].links = [(graph_impostors[1],10 ), (graph_impostors[10],8 ), (graph_impostors[11],6 ), (graph_impostors[13],0),(graph_impostors[12],6)]

    graph_impostors[1].links = [(graph_impostors[0],10 ), (graph_impostors[2],6 ), (graph_impostors[6],0 ), (graph_impostors[8],9 ), (graph_impostors[10],8 ), (graph_impostors[14], 0)]

    graph_impostors[2].links = [(graph_impostors[1], 6), (graph_impostors[5], 5), (graph_impostors[3], 0 ), (graph_impostors[4], 12),(graph_impostors[14], 7)]

    graph_impostors[3].links = [(graph_impostors[2], 0), (graph_impostors[4],0 ), (graph_impostors[5],8 ),(graph_impostors[14], 5)]

    graph_impostors[4].links = [(graph_impostors[3], 0), (graph_impostors[2], 12), (graph_impostors[5], 11), (graph_impostors[8], 7),(graph_impostors[7], 5),(graph_impostors[14], 4)]

    graph_impostors[5].links = [(graph_impostors[2], 5), (graph_impostors[3], 8), (graph_impostors[4], 11),(graph_impostors[14], 6)]

    graph_impostors[6].links = [(graph_impostors[1], 0), (graph_impostors[8], 7),(graph_impostors[14], 0)]

    graph_impostors[7].links = [(graph_impostors[4], 5), (graph_impostors[8], 6)
    ]
    graph_impostors[8].links = [(graph_impostors[1], 9), (graph_impostors[4], 7), (graph_impostors[6], 7), (graph_impostors[7], 6),(graph_impostors[9], 8),(graph_impostors[12], 11)]

    graph_impostors[9].links = [(graph_impostors[8], 8), (graph_impostors[12], 9),(graph_impostors[11], 0),(graph_impostors[10], 0)]

    graph_impostors[10].links = [(graph_impostors[1], 8), (graph_impostors[0], 8),(graph_impostors[11], 0),(graph_impostors[9], 0)]

    graph_impostors[11].links = [(graph_impostors[0], 6), (graph_impostors[12], 6), (graph_impostors[13], 5),(graph_impostors[9], 0),(graph_impostors[10], 0)]

    graph_impostors[12].links = [(graph_impostors[8], 11), (graph_impostors[9], 9), (graph_impostors[11], 6), (graph_impostors[13], 0),(graph_impostors[0],6)]

    graph_impostors[13].links = [(graph_impostors[0], 0), (graph_impostors[11], 5), (graph_impostors[12], 0)]

    graph_impostors[14].links = [(graph_impostors[1], 0), (graph_impostors[6], 0), (graph_impostors[2], 7), (graph_impostors[5], 6), (graph_impostors[3], 5), (graph_impostors[4], 4)]

    matrix_1 = FloydWarshall(graph_impostors)

    graph_crewmates.pop(14)
    graph_crewmates[0].links = [(graph_crewmates[1],10 ), (graph_crewmates[10],8 ), (graph_crewmates[11],6 ), (graph_crewmates[13],6 ),(graph_crewmates[12],6)]

    graph_crewmates[1].links = [(graph_crewmates[0],10 ), (graph_crewmates[2],6 ), (graph_crewmates[6],8 ), (graph_crewmates[8],9 ), (graph_crewmates[10],8 )]

    graph_crewmates[2].links = [(graph_crewmates[1], 6), (graph_crewmates[5], 5), (graph_crewmates[3],8 ), (graph_crewmates[4], 12)]

    graph_crewmates[3].links = [(graph_crewmates[2], 8), (graph_crewmates[4],10 ), (graph_crewmates[5],8 )]

    graph_crewmates[4].links = [(graph_crewmates[3], 10), (graph_crewmates[2], 12), (graph_crewmates[5], 11), (graph_crewmates[8], 7),(graph_crewmates[7], 5)]

    graph_crewmates[5].links = [(graph_crewmates[2], 5), (graph_crewmates[3], 8), (graph_crewmates[4], 11)]

    graph_crewmates[6].links = [(graph_crewmates[1], 8), (graph_crewmates[8], 7)]

    graph_crewmates[7].links = [(graph_crewmates[4], 5), (graph_crewmates[8], 6)]

    graph_crewmates[8].links = [(graph_crewmates[1], 9), (graph_crewmates[4], 7), (graph_crewmates[6], 7), (graph_crewmates[7], 6),(graph_crewmates[9], 8),(graph_crewmates[12], 11)]

    graph_crewmates[9].links = [(graph_crewmates[8], 8), (graph_crewmates[12], 9)]

    graph_crewmates[10].links = [(graph_crewmates[1], 8), (graph_crewmates[0], 8)]

    graph_crewmates[11].links = [(graph_crewmates[0], 6), (graph_crewmates[12], 6), (graph_crewmates[13], 5)]

    graph_crewmates[12].links = [(graph_crewmates[8], 11), (graph_crewmates[9], 9), (graph_crewmates[11], 6), (graph_crewmates[13], 6),(graph_crewmates[0],6)]

    graph_crewmates[13].links = [(graph_crewmates[0], 6), (graph_crewmates[11], 5), (graph_crewmates[12], 6)]

    matrix_2 = FloydWarshall(graph_crewmates)
    
    compare(matrix_1,matrix_2)

 
