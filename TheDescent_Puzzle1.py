import sys
import math

# The while loop represents the game.
# Each iteration represents a turn of the game
# where you are given inputs (the heights of the mountains)
# and where you have to print an output (the index of the mountain to fire on)
# The inputs you are given are automatically updated according to your last actions.


# game loop 
while True:
    highest_peak = None
    target = None
    
    for i in range(8):
        mountain_h = int(input())  # represents the height of one mountain.
        if target == None: 
            target = i
            highest_peak = mountain_h
        else:
            if highest_peak < mountain_h:
                highest_peak = mountain_h
                target = i                 


    # The index of the mountain to fire on.
    print(target)
