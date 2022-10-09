import sys
import random

# Rolls d6 dice.
# 0 arg 1 d6
# 1 arg num d6
# 2 arg num dice + sides
def roll(args):
    numDice = 1
    numSides = 6
    rolls = []
    if len(args) > 0:
        numDice = int(args[0])
    
    if len(args) > 1:
        numSides = int(args[1])
    
    for i in range(numDice):
        rolls.append(random.randint(1,numSides))
    
    print(f"Rolled {numDice} d{numSides}")
    print("Results: " + str(rolls))
        
        

commands = {
    "roll": roll
} 

if __name__ == '__main__':
    if sys.argv[1] in commands.keys():        
        commands[sys.argv[1]](sys.argv[2:])    