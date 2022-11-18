# cs5113fa22-project

## Development Schedule

Describes the commitments and respective schedules to complete

# Architecture Description [10/26] 

- create the read.me file, store development schedules and description of initialization of N, P and T.

# Protos and interface design complete [11/03]  

- Proto file - 10/29
- dockerfile and build docker-compose.yml - 11/03

# First version logging [11/17] 

- Build the game with all function implementations and gameplay with minor bugs[11/10]
- Fix the minor bugs[11/16]

Submission [12/01]

- Modify the program with provided feedback after first version logging[11/20]
- Fix any bugs[11/29] 

Presentation [12/14]

## Emoji Chooser 


For N, P and T, I will provide the user to enter size of board, no. of pokemons and no. of trainers.

I will generate docker-compose.yaml dynamically for P pokemon and T trainers using ruamel in python.

List of emojis will be provided to user to choose pokemon and trainers through command line argument.

Proto file contains the methods and remote procedure calls to communicate with server.

Dockerfile will have configurations and it will run the python file which contains the code to generate docker-compose.yml

##  Interfaces

# dockerfile

Dockerfile contains the configurations to run docker which installs the dependencies and runs tge python file which contains code to generate docker-compose.yml file dynamically.

# Proto file

pokemonou.proto - the proto buffer file containig the rpc functions used to communicate with the server.

# Functions in pokemonou.proto file:
Captured() --  takes input as pokemonName and returns the feedback "pokemonName" when captured.
Moves() --  takes input as stream of player and returns stream Feedback that says where the move is i.e., the row and column specification.
Board() -- takes BoardConfig as input and returns BoardConfig.
Capture()- takes Feedback as input and returns feedback as successul if a pokemon was in space where the trainer is.
Checkboard() - Takes input as BoardConfig and returns MoveDirection (Up,down,right,left,north east, south east, north west, south west)
Move() - This for the trainer to make the move in a direction(Up,down,right,left,north east, south east, north west, south west)
Pokdex() - It returns the list of captured pokemons
Path() - It returns the list of moves made by trainer.
Checkboard() - Takes input as BoardConfig and returns Move direction(Up,down,right,left,north east, south east, north west, south west)
Move() - this is for pokemon to make the move(Up,down,right,left,north east, south east, north west, south west)
Trainer() Takes input as trainerName and returns TrainerInfo containing the pokemon name which trainer captured and when and where it was captured


# Testing for functions:
RUN python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. pokemonou.proto 
The command will be run for proto to create 2 files - pokemonou_pb2_grpc.py, pokemonou_pb2.py
These files will contain stubs that will be implemented on pokemon and trainers and send the input for Captured moves and Board rpc functions and the server will respond back.


## Docker-compose.yml

To generate the docker-compose.yml file, I run generatedockercompose.py file through DockerFile.
Commands for building Yaml file:
docker build .
docker run -it -v $(pwd):/usr/src/app <imageid>          # -it is the terminal interactive session for user to provide inputs.

After running this, the terminal will prompt the user to enter no. of pokemons and no. of trainers. After user provides the input, it generates the clients in docker-compose.yml file.

##boardgame.gif

After generation of docker-compose.yml, based on the input of board size and no.of pokemons and trainers, I am generating a gameboard with assigning the pokemon and trainer emojis randomly to random positions in my NxN board.

![Recording-proj](https://user-images.githubusercontent.com/114453047/202621362-55886aa2-b784-4167-b298-cb03890fef08.gif)




