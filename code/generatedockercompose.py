from __future__ import print_function
 
from ruamel import yaml

VERSION = {'version':'3.7'}
SERVICES = {'server': 'server'}
num1 = input('Enter the number of Trainers:')
num2 = input('Enter the number of Pokemons:')
boardsize=input("provide the size of board")
numOfTrainers=int(num1)
numOfPokemons=int(num2)

f = open('values.txt', 'w+')
f.write(num1 + '\n')
f.write(num2 + '\n')
f.write(boardsize)

for i in range(numOfTrainers):
    SERVICES["client"+str(i)] = "Trainer"+str(i)
 
for j in range(numOfPokemons):
    SERVICES["client"+str(i+j+1)] = "Pokemon"+str(j)
 
COMPOSITION = {'services': {}}
 

def servicize(name, image):
    if(name == 'server'):
        entry = {
             'build': {'context': ".", 'dockerfile': 'Server/Dockerfile'},
             'hostname': image,
             'container_name': image,
             'networks': ['default']}
    else:
        entry = {
                'build': {'context': ".", 'dockerfile': 'Server/Dockerfile'},
                'hostname': image,
                'container_name': image,
                'networks': ['default']}
    return entry
 

if __name__ == '__main__':
    noOfTrainers = numOfTrainers
    noOfPokemons = numOfPokemons
    for name, image in SERVICES.items():
        COMPOSITION['services'][name] = servicize(name, image)
    print(yaml.dump(COMPOSITION, default_flow_style=False, indent=4), end='')
    with open('docker-compose.yml', 'w+') as outfile:
        yaml.dump(VERSION, outfile, default_flow_style=False, indent=4)
        yaml.dump(COMPOSITION, outfile, default_flow_style=False, indent=4)
    