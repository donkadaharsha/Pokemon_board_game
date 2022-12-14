from concurrent import futures
import grpc
import random
import pokemonou_pb2 as pb2
import pokemonou_pb2_grpc as pb2_grpc
import math
import time
import socket
import threading


#Server side implementation of RPC
class PokemonOUGameServicer(pb2_grpc.PokemonOUGameServicer):   
    def __init__(self, start = 0):
        self.lock = threading.Lock()            #Lock used for concurrency                
        self.value = start

#rpc method for printing the matrix and returning initial list of assigned row and columns 
    def Board(self, request, context):                         
        for row in matrix:
            x = ' '.join(map(str, row))
            print(x)
        hostname = request.player
        exist = ""
        if(hostname.startswith("Pok")):
            if hostname in initial_list:
                exist = True
        return pb2.InitialMoves(exist = str(exist))   
#rpc method for returning count of all captured pokemons to pokemon
    def MovePokemon(self, request, context):
        self.lock.acquire()
        self.value = self.value + 1
        print(request.hostname)
        global pc
        msg=Pmove(request.hostname)
        if msg == "captured":
            pc = pc + 1
        print("countPokemon", pc)
        self.lock.release()
        return pb2.Message(count = pc)
#rpc method for returning count of all captured pokemons to trainer
    def MoveTrainer(self, request, context):
        self.lock.acquire()
        self.value = self.value + 1
        global tc
        msg = moveTrainer(request.hostname)
        print("msg ", msg)
        if msg == "captured":
            tc = tc + 1
        print("count", tc)
        self.lock.release()
        return pb2.Message(count = tc)  

#server initalization method
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    pb2_grpc.add_PokemonOUGameServicer_to_server(PokemonOUGameServicer(), server)
    server.add_insecure_port("0.0.0.0:50051") ##needs to allow/open the port 50051 in system/firewall to run    
    server.start()
    hostname = socket.gethostname()              
    if(socket.gethostname() == 'server'):
        createBoard()
    if(hostname != 'server'):
        time.sleep(10)                     #sleep is used to await pokemon and trainers until server starts.
        run(hostname)
    server.wait_for_termination()

def run(hostname):
    with grpc.insecure_channel('server:50051') as channel:  ##needs to allow/open the port 50051 in system/firewall to run
        stub = pb2_grpc.PokemonOUGameStub(channel)   
        print("Requesting Board....")
        res=stub.Board(pb2.Player(player=hostname))
        k=0
        while(k!=24):   
            if(hostname.startswith("Poke")):
                if(res.exist==str(True)):
                    print("Pokemon is moving", hostname)
                    response=stub.MovePokemon(pb2.PMove(hostname = hostname))
                    k=response.count
                else:
                    print("Already captured. Try for another game")
                    channel.close()
            
            elif(hostname.startswith("Trai")):
                print("Trainer is moving", hostname)
                response=stub.MoveTrainer(pb2.TMove(hostname = hostname))
                k=response.count

def createBoard():
   
    global initial_list
    initial_list={}
    Pc=0
    Tc=0
    #list of pokemon emojis
    pokemons=["🐻","🦉","🦜","🐸" ,"💥" ,"💫" ,"💦","🐵" ,"🐒" ,"🕊️","🐷" ,"🐖" ,"🐨" ,"🐽" ,"🦎","🐬" ,"🐙" ,"🐫" ,"🦙","🦒" ,"🐻‍❄️" ,"🦏" ,"🐭","🐹" ,"🐰","🦑","🍄","☃️","🌸","🐝","🐞","🐌","🦋"] 
    #list of pokemon emojis
    trainers=["😀","😃" ,"😄" ,"😁" ,"😆" ,"😅" ,"🤣" ,"😂" ,"🙂" ,"🙃" ,"🫠","😊" ,"😇" ,"🥰" ,"😍","🤩","😘","😑" ,"🧑","🧓","🙍" ,"👩","👳","🎅" ,"🥺","😰","😭","😓","😡","😠","🤥"] 
    
    ##assigning pokemons to the board
    while Pc<=numberOfPokemons-1:
        randomrow=random.choice(range(0,n-1))
        randomcolumn=random.choice(range(0,n-1))
        if matrix[randomrow][randomcolumn]=="🟥":
             #checking if the position is blank/available to assign
            emoji=random.choice(pokemons)
            initial_list["Pokemon"+str(Pc)] = (randomrow,randomcolumn)
            Pc+=1 
            a=list(matrix[randomrow])
            a[randomcolumn]=emoji
            matrix[randomrow]=''.join(a)
            pokemons.remove(emoji)
    #assigning trainers to the board
    while Tc<=numberOfTrainers-1:
        randomrow=random.choice(range(0,n))
        randomcolumn=random.choice(range(0,n))
        if matrix[randomrow][randomcolumn]=="🟥":
            #checking if the position is blank/available to assign
            emoji=random.choice(trainers)
            initial_list["Trainer"+str(Tc)] = (randomrow,randomcolumn)
            Tc+=1 
            a=list(matrix[randomrow])
            a[randomcolumn]=emoji
            matrix[randomrow]=''.join(a)
            trainers.remove(emoji)

    ##prinitng the 2d array in matrix form
    for row in matrix:
        x = ' '.join(map(str, row))
        return x

#calculating the shortest distance between pokemon and trainer
def distance(pRow, pCol, tRow, tCol):
    shortest_distance = math.sqrt((pRow-tRow)*(pRow-tRow) + (pCol-tCol)*(pCol-tCol))
    return shortest_distance


def searchOpponent(hostname):
    #searching the opponent with shortest distance and returning the row and column of opponent
    for x in initial_list.items():
        if(x == hostname):
            row = initial_list[x][0]
            column = initial_list[x][1]
    a = 0
    b = 0
    minimum =100.00
    name=""
    for i in range(n):
        for j in range(n):
            if(matrix[i][j] !="🟥"):
                for key, (a,b) in initial_list.items():
                    if(a == i and b == j):
                        name = key
                if(name != hostname):
                    if(i != row and j != column):
                        if(distance(row,column,i,j) < minimum):
                            minimum = distance(row,column,i,j)
                            a = i
                            b = j                    
                else:
                    continue
    return a, b

##method to move a player to north direction
def moveNorth(hostname,i,j):
    i=i
    name=""
    j=j-1
    if(j < 0):
        j = 0
    if(matrix[i][j]!="🟥"):
        #checking if the position is assigned to pokemon/trainer
        if(hostname.startswith("Tra")):
            for key, (a,b) in initial_list.items():
                if(a == i and b == j):
                    name = key
            if(name.startswith("Tra")):
                i, j = moveNorthEast(hostname,i,j)
        elif(hostname.startswith("Pok")):
            i, j = moveNorthEast(hostname,i,j)
    return i, j
    ##method to move a player to south direction
def moveSouth(hostname,i,j):
    i = i
    name =""
    j = j+1
    if(j > n-1):
        j = n-1
    if(matrix[i][j]!="🟥"):
        #checking if the position is assigned to pokemon/trainer
        if(hostname.startswith("Tra")):
            for key, (a,b) in initial_list.items():
                if(a == i and b == j):
                    name = key
            if(name.startswith("Tra")):
                i, j = moveSouthWest(hostname,i,j)
        elif(hostname.startswith("Pok")):
            i, j = moveSouthWest(hostname,i,j)
    return i, j
##method to move a player to east direction
def moveEast(hostname,i,j):
    i = i-1
    name =""
    if(i < 0):
       i=0
    j = j
    if(matrix[i][j]!="🟥"):
        #checking if the position is assigned to pokemon/trainer
        if(hostname.startswith("Tra")):
            for key, (a,b) in initial_list.items():
                if(a == i and b == j):
                    name = key
            if(name.startswith("Tra")):
                i, j = moveSouthEast(hostname,i,j)
        elif(hostname.startswith("Pok")):
            i, j = moveSouthEast(hostname,i,j)
    return i, j 
##method to move a player to west direction
def moveWest(hostname,i,j):  
    i = i+1
    name =""
    if(i > n-1):
        i = n-1
    j = j
    if(matrix[i][j]!="🟥"):
        #checking if the position is assigned to pokemon/trainer
        if(hostname.startswith("Tra")):
            for key, (a,b) in initial_list.items():
                if(a == i and b == j):
                    name = key
            if(name.startswith("Tra")):
                i, j = moveNorthWest(hostname,i,j)
        elif(hostname.startswith("Pok")):
            i, j = moveNorthWest(hostname,i,j)
    return i, j  
##method to move a player to northeast direction
def moveNorthEast(hostname,i,j):
    i=i-1
    name = ""
    if(i < 0):
        i=0
    j=j-1
    if(j < 0):
        j=0
    if(matrix[i][j]!="🟥"):
        #checking if the position is assigned to pokemon/trainer
        if(hostname.startswith("Tra")):
            for key, (a,b) in initial_list.items():
                if(a == i and b == j):
                    name = key
            if(name.startswith("Tra")):
                i, j = moveEast(hostname,i,j)
        elif(hostname.startswith("Pok")):
            i, j = moveEast(hostname,i,j)
    return i, j
##method to move a player to northwest direction
def moveNorthWest(hostname,i,j):
    i=i+1
    j=j-1
    name = ""
    if(i > n-1):
        i=n-1
    
    if(j < 0):
        j=0
    if(matrix[i][j]!="🟥"):
        #checking if the position is assigned to pokemon/trainer
        if(hostname.startswith("Tra")):
            for key, (a,b) in initial_list.items():
                if(a == i and b == j):
                    name = key
            if(name.startswith("Tra")):
                i, j = moveNorth(hostname,i,j)
        elif(hostname.startswith("Pok")):
            i, j = moveNorth(hostname,i,j)
    return i, j
##method to move a player to southeast direction
def moveSouthEast(hostname,i,j):
    i = i-1
    j = j+1
    name =""
    if(i < 0):
        i=0
    
    if(j > n-1):
        j=n-1
    if(matrix[i][j]!="🟥"):
        #checking if the position is assigned to pokemon/trainer
        if(hostname.startswith("Tra")):
            for key, (a,b) in initial_list.items():
                if(a == i and b == j):
                    name = key
            if(name.startswith("Tra")):
                i, j = moveSouth(hostname,i,j)
        if(hostname.startswith("Pok")):
            i, j = moveSouth(hostname,i,j)
    return i, j
##method to move a player to southwest direction
def moveSouthWest(hostname,i,j):
    i = i+1
    j = j+1
    name = ""
    if(i > n-1):
        i=n-1
    
    if(j > n-1):
        j=n-1
    if(matrix[i][j]!="🟥"):
        #checking if the position is assigned to pokemon/trainer
        if(hostname.startswith("Tra")):
            for key, (a,b) in initial_list.items():
                if(a == i and b == j):
                    name = key
            if(name.startswith("Tra")):
                i, j = moveWest(hostname,i,j)
        elif(hostname.startswith("Pok")):
            i, j = moveWest(hostname,i,j)
    return i, j


##method to move the trainer according to calculated shortest distance with the closest opponent
def moveTrainer(hostname):
    global matrix
    global msg
    msg = ""
    global name
    name=""
    global row
    global column
    row = 0
    column = 0

    for x in initial_list.items():
        if(x == hostname):
            row = initial_list[x][0]
            column = initial_list[x][1]
    
    opponent_row, opponent_column = searchOpponent(hostname)  ##searching the closest opponent 

    success = 0

    if(row < opponent_row) and (column < opponent_column):
        #comparing the position with oppnent row and opponent column       
        newrow, newcolumn = moveSouthWest(hostname, row, column)
        #if it's less we are moving to southWest
        if(newrow==opponent_row) and (newcolumn == opponent_column):
            #comparing the new position with oppnent row and opponent column
            if(matrix[opponent_row][opponent_column]!="🟥"):    
                #if the position is not blank we print captured as it will be the pokemon      
                msg = "captured"
                for key, (a,b) in initial_list.items():
                    if(a == opponent_row and b == opponent_column):
                        name = key
                print("name", name)
                if(name!=""):
                    initial_list.pop(name)  ##popping out the name of captured pokemon from the list
        initial_list[hostname] = newrow, newcolumn
        matrix = convertmatrixtolistandreplace(row, column, newrow, newcolumn) 
        
    elif(row < opponent_row) and (column > opponent_column):
        #comparing the position with oppnent row and opponent column 
        newrow, newcolumn = moveNorthWest(hostname, row, column)
        if(newrow==opponent_row) and (newcolumn == opponent_column):
             #comparing the new position with oppnent row and opponent column
            if(matrix[opponent_row][opponent_column]!="🟥"):
                #if the position is not blank we print captured as it will be the pokemon   
                msg = "captured"
                for key, (a,b) in initial_list.items():
                    if(a == opponent_row and b == opponent_column):
                        name = key
                print("name", name)
                if(name!=""):
                    initial_list.pop(name)  ##popping out the name of captured pokemon from the list
        print('moving north west')
        initial_list[hostname] = newrow, newcolumn
        matrix = convertmatrixtolistandreplace(row, column, newrow, newcolumn)
    elif(row > opponent_row) and (column < opponent_column):
        #comparing the position with oppnent row and opponent column 
        newrow, newcolumn = moveSouthEast(hostname, row, column)
        #comparing the new position with oppnent row and opponent column
        if(newrow==opponent_row) and (newcolumn == opponent_column):
            if(matrix[opponent_row][opponent_column]!="🟥"):
                 #if the position is not blank we print captured as it will be the pokemon
                msg = "captured"
                for key, (a,b) in initial_list.items():
                    if(a == opponent_row and b == opponent_column):
                        name = key
                print("name", name)
                if(name!=""):
                    initial_list.pop(name) ##popping out the name of captured pokemon from the list
        print('moving south east')
        initial_list[hostname] = newrow, newcolumn
        matrix = convertmatrixtolistandreplace(row, column, newrow, newcolumn)
    elif(row > opponent_row) and (column > opponent_column):
        #comparing the position with oppnent row and opponent column 
        newrow, newcolumn = moveNorthEast(hostname, row, column)
        #comparing the new position with oppnent row and opponent column
        if(newrow==opponent_row) and (newcolumn == opponent_column):
            #if the position is not blank we print captured as it will be the pokemon
            if(matrix[opponent_row][opponent_column]!="🟥"):
                msg = "captured"
        print('moving north east')
        initial_list[hostname] = newrow, newcolumn
        matrix = convertmatrixtolistandreplace(row, column, newrow, newcolumn)
    elif(row == opponent_row) and (column < opponent_column):
        #comparing the position with oppnent row and opponent column 
        newrow, newcolumn = moveSouth(hostname, row, column)
        if(newrow==opponent_row) and (newcolumn == opponent_column):
            #comparing the new position with oppnent row and opponent column
            if(matrix[opponent_row][opponent_column]!="🟥"):
                 #if the position is not blank we print captured as it will be the pokemon
                msg = "captured"
                name = searchOpponent(opponent_row, opponent_column)
                print("name", name)
                if(name!=""):
                    initial_list.pop(name) ##popping out the name of captured pokemon from the list
        print('moving south')
        initial_list[hostname] = newrow, newcolumn
        matrix = convertmatrixtolistandreplace(row, column, newrow, newcolumn)
    elif(row == opponent_row) and (column > opponent_column):
         #comparing the position with oppnent row and opponent column 
        newrow, newcolumn = moveNorth(hostname, row, column)
         #comparing the new position with oppnent row and opponent column
        if(newrow==opponent_row) and (newcolumn == opponent_column):
              #if the position is not blank we print captured as it will be the pokemon
            if(matrix[opponent_row][opponent_column]!="🟥"):
                msg = "captured"
                for key, (a,b) in initial_list.items():
                    if(a == opponent_row and b == opponent_column):
                        name = key
                print("name", name)
                if(name!=""):
                    initial_list.pop(name)  ##popping out the name of captured pokemon from the list
        print('moving north')
        initial_list[hostname] = newrow, newcolumn
        matrix = convertmatrixtolistandreplace(row, column, newrow, newcolumn)
    elif(row > opponent_row) and (column == opponent_column):
        #comparing the position with oppnent row and opponent column 
        newrow, newcolumn = moveWest(hostname, row, column)
        #comparing the new position with oppnent row and opponent column
        if(newrow==opponent_row) and (newcolumn == opponent_column):
            if(matrix[opponent_row][opponent_column]!="🟥"):
                #if the position is not blank we print captured as it will be the pokemon
                msg = "captured"
        print('moving west')
        initial_list[hostname] = newrow, newcolumn
        matrix = convertmatrixtolistandreplace(row, column, newrow, newcolumn)
    elif(row < opponent_row) and (column == opponent_column):
        #comparing the position with oppnent row and opponent column 
        newrow, newcolumn = moveEast(hostname, row, column)
        if(newrow==opponent_row) and (newcolumn == opponent_column):
            if(matrix[opponent_row][opponent_column]!="🟥"):
                #comparing the new position with oppnent row and opponent column
                msg = "captured"
                #if the position is not blank we print captured as it will be the pokemon
                for key, (a,b) in initial_list.items():
                    if(a == opponent_row and b == opponent_column):
                        name = key
                print("name", name)
                if(name!=""):
                    initial_list.pop(name)   ##popping out the name of captured pokemon from the list
        print('moving west')
        initial_list[hostname] = newrow, newcolumn
        matrix = convertmatrixtolistandreplace(row, column, newrow, newcolumn)
    elif(row == opponent_row) and (column == opponent_column):
        #comparing the new position with oppnent row and opponent column 
        newrow = row
        newcolumn = column
        msg = ""
        print(success)
        success = 1 
        print(success)

        # print(matrix)
        print("initial_list:", initial_list)
    for row in matrix:
        x=' '.join(map(str,row))
        print(x)
    return msg


##This method is used to convert matrix to list and replace because string object needs to be replaced 
#with another string and since string obj is immuatable we have to convert it to list first and then replace it.
def convertmatrixtolistandreplace(row, column, newrow, newcolumn):
    global matrix
    a=list(matrix[newrow])
    a[newcolumn]=matrix[row][column]
    matrix[newrow]=''.join(a)
    b=list(matrix[row])

    b[column] = "🟥"
    matrix[row]=''.join(b)
    return matrix
    
#method for moving pokemon
def Pmove(hostname):
    global row
    global column
    for x in initial_list.items():
        if(x == hostname):
            row = initial_list[x][0]
            column = initial_list[x][1]
    name=""
    for key, (a,b) in initial_list.items():
        if(a == row and b == column):
            name = key
#searching the nearest trainer to get away from it
    opponent_row, opponent_column = searchOpponent(hostname) #returns the dimensions of opponent
    if(row < opponent_row) and (column < opponent_column):
        #comparing the position with trainer and will move north east to get away.
        newrow, newcolumn = moveNorthEast(hostname, row, column)
        print('moving north east')
        initial_list[hostname] = newrow, newcolumn
        matrix = convertmatrixtolistandreplace(row, column, newrow, newcolumn)
        
    elif(row < opponent_row) and (column > opponent_column):
        #comparing the position with trainer and will move south east to get away
        newrow, newcolumn = moveSouthEast(hostname, row, column) 
        print('moving south east')
        initial_list[hostname] = newrow, newcolumn
        matrix = convertmatrixtolistandreplace(row, column, newrow, newcolumn)
        
       
    elif(row > opponent_row) and (column < opponent_column):
        #comparing the position with trainer and will move north east to get away
        newrow, newcolumn = moveNorthWest(hostname, row, column)
        print('moving north west')
        initial_list[hostname] = newrow, newcolumn
        matrix = convertmatrixtolistandreplace(row, column, newrow, newcolumn)
      
        
    elif(row > opponent_row) and (column > opponent_column):
        #comparing the position with trainer and will move south west to get away
        newrow, newcolumn = moveSouthWest(hostname, row, column)
        print('moving south west')
        initial_list[hostname] = newrow, newcolumn
        matrix = convertmatrixtolistandreplace(row, column, newrow, newcolumn)
      
   
    elif(row == opponent_row) and (column < opponent_column):
        #comparing the position with trainer and will move north to get away
        newrow, newcolumn = moveNorth(hostname, row, column)
        print('moving north')
        initial_list[hostname] = newrow, newcolumn
        matrix = convertmatrixtolistandreplace(row, column, newrow, newcolumn)
      
    elif(row == opponent_row) and (column > opponent_column):
        #comparing the position with trainer and will move north east to get away
        newrow, newcolumn = moveSouth(hostname, row, column)
        print('moving South')
        initial_list[hostname] = newrow, newcolumn
        matrix = convertmatrixtolistandreplace(row, column, newrow, newcolumn)

    elif(row > opponent_row) and (column == opponent_column):
        #comparing the position with trainer and will move north east to get away
        newrow, newcolumn = moveEast(hostname, row, column)
        print('moving East')
        initial_list[hostname] = newrow, newcolumn
        matrix = convertmatrixtolistandreplace(row, column, newrow, newcolumn)

    elif(row < opponent_row) and (column == opponent_column):
        newrow, newcolumn = moveWest(hostname, row, column)
        #comparing the position with trainer and will move north West to get away
        print('moving West')
        initial_list[hostname] = newrow, newcolumn
        matrix = convertmatrixtolistandreplace(row, column, newrow, newcolumn)

    elif(row == opponent_row) and (column == opponent_column):
        message=""
    #if no position is found if container is still calling the function, then it will return that pokemon
    #is already captured
    else:
        message="captured"

    for row in matrix:
        x=' '.join(map(str,row))
        print(x)
    return message

##reading the file to retrieve number of pokemons and trainers
with open('numbers.txt', 'r') as readfile:
    values = readfile.readlines()
numberOfTrainers = int(values[0])
numberOfPokemons = int(values[1])

initial_list={}
count = 0
n=20  ##board size
global matrix  
matrix = ["🟥"*n]*n  ##creating the board with 🟥 emoji as blank spaces

if __name__=='__main__': ##main file
   
    details = {}
    
    pokemons = []
    trainers = []
    pc=0
    tc=0
    serve()  

