### cs5113fa22-project -- FINAL
### TITLE-POKEMONOU

## Description
This is a board game of NxN size where I have assigned trainers and pokmeons. The trainers and pokemons should be able to communicate with the server through gRPC communication to see the contents of the spaces around them. Each player makes a move on the board asynchronously. Trainers try to run close to pokemons but pokemons run away from trainers. If a trainer jumps to same space as pokemon, it means pokemon is captured. Same is communicated to server with a capture function. When all pokemons get captured, channel should be closed with a success message.


## Procedure
For N, P and T, I am providing the user to enter size of board, no. of pokemons and no. of trainers.
I generate docker-compose.yaml dynamically for P pokemon and T trainers using ruamel in python. Pokemons and trainers are assigned randomly in random positions on the board.
Proto file contains the methods and remote procedure calls to communicate with server. Dockerfile has the configurations and it will run the python file which contains the code to generate docker-compose.yml

## Interfaces used
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
MoveTrainer() - This for the trainer to make the move in a direction(Up,down,right,left,north east, south east, north west, south west)
Pokdex() - It returns the list of captured pokemons.
Path() - It returns the list of moves made by trainer.
MovePokemon() - this is for pokemon to make the move(Up,down,right,left,north east, south east, north west, south west)

# node.py
Node.py has implememntations of all the functions where pokemons and trainers are made to move, board is initialized, distance is calculated, message is returned, the board is printed in a user friendly manner.

# Docker-compose.yml

To generate the docker-compose.yml file, I run generatedockercompose.py file through DockerFile.
Commands for building Yaml file:
docker build .
docker run -it -v $(pwd):/usr/src/app <imageid>   # -it is the terminal interactive session for user to provide inputs.

After running this, the terminal will prompt the user to enter no. of pokemons and no. of trainers. After user provides the input, it generates the clients in docker-compose.yml file.

# Testing for functions:
RUN python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. pokemonou.proto 
The command will be run for proto to create 2 files - pokemonou_pb2_grpc.py, pokemonou_pb2.py
These files will contain stubs that will be implemented on pokemon and trainers and send the input for Captured moves and Board rpc functions and the server will respond back.

## Problems and solutions used
#Openness
To achieve openness, I used smaller methods like proto and rpcs which made it extendable i.e. any features can be added and implemented easily in future. \
#Concurrency
I made use of locks at the server side when players are trying to make a move.
#Scalabiliity
I have used dynamic generation of docker compose through user defined inputs for number of pokemons and trainers.

# Final-GIF

Below is the GIF of the final board with all functionalities. The blank spaces are represented by "🟥". I have assigned 24 pokemons and 24 trainers. Taken board size is 20. All trainers and pokemons are moving asynchronously. While trainers move closer to pokemons and pokemons are getting far from trainers. When all pokemons get captured, channel is closed with a success message.







