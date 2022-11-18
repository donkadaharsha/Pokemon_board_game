import random
import numpy
 
# create a simple array with numpy empty()
def makeBoard():

    with open('values.txt', 'r') as f:
        values = f.readlines()
    # b = a
    
    # print(num[0])
    
    # x=input("provide the size of board")
    # n=int(x)
    noOfTrainers = int(values[0])
    noOfPokemons = int(values[1])
    n = int(values[2])
    pokemons=["🐻","🙈","🙉" ,"🙊" ,"💥" ,"💫" ,"💦" ,"💨" ,"🐵" ,"🐒" ,"🦍","🐷" ,"🐖" ,"🐗" ,"🐽" ,"🐏","🐐" ,"🐪" ,"🐫" ,"🦙","🦒" ,"🦣" ,"🦏" ,"🐭","🐹" ,"🐰"] 
    trainers=["😀","😃" ,"😄" ,"😁" ,"😆" ,"😅" ,"🤣" ,"😂" ,"🙂" ,"🙃" ,"🫠","😊" ,"😇" ,"🥰" ,"😍","🤩","😘","😑" ,"🧠","🫀","🫁" ,"🦷" ,"🦴","👁️","👅" ,"👄"] 
    matrix = numpy.empty(shape=(n, n), dtype='object')
    count=0
    cnt=0
    while count<=noOfPokemons-1:
        randomrow=random.choice(range(0,n))
        randomcolumn=random.choice(range(0,n))
        if matrix[randomrow][randomcolumn]==None:
            emoji=random.choice(pokemons)
            matrix[randomrow][randomcolumn]= emoji
            pokemons.remove(emoji)
            count+=1
    while cnt<=noOfTrainers-1:
        randomrow=random.choice(range(0,n))
        randomcolumn=random.choice(range(0,n))
        if matrix[randomrow][randomcolumn]==None:
            emoji=random.choice(trainers)
            matrix[randomrow][randomcolumn]= emoji
            trainers.remove(emoji)
            cnt+=1
    print(matrix)

        # matrix[randomrow][randomcolumn]= random.choice(trainers)

    # print(random.choices(pokemons, k=generatedockercompose.numOfPokemons))




if __name__=="__main__":
    makeBoard()

# matrix = [list(range(n, n)) for i in range(n)]
#     # print("The created matrix of {} * {}: ".format(n,n))


# a=[list(range(n,n)) for i in range(n-1)]
    # # for i in range(0, n):
    # #     for j in range(0, n):
    # #         # a.append(None)
    # #         print(a,end=' ')
    # #     print("\r")   
    # for m in a:
    #     print(a)
    # print(a)