import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()] # initial positions of Batman

xB, yB = x0, y0
x1, y1 = 0, 0
x2 = w-1
y2 = h-1 

# directional functions
def up(position):
    return position - 1

def down(position):
    return position + 1

def right(position):
    return position + 1

def left(position):
    return position - 1 

# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    if "U" in bomb_dir:
        y2 = up(yB)
    
    if "D" in bomb_dir:
        y1 = down(yB)

    if "R" in bomb_dir:
        x1 = right(xB)
    
    if "L" in bomb_dir:
        x2 = left(xB)

    xB = x1 + (x2 - x1) / 2
    yB = y1 + (y2 - y1) / 2
    
    # the location of the next window Batman should jump to.
    print(str(int(xB)) + " " + str(int(yB)))
