import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

# map limit
xLimit = 40 
yLimit = 18 
# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.
    
    moveX = ''
    moveY = ''
    
    dx = initial_tx - light_x 
    # print("Delta x : " + str(dx), file=sys.stderr)
    
    if (dx > 0):
        moveX = 'W'
        initial_tx = initial_tx - 1 
    elif (dx < 0):
        moveX = 'E'
        initial_tx = initial_tx + 1
    else:
        moveX = ''

    dy = initial_ty - light_y
    # print("Delta y : " + str(dy) + "( thor_"+ str(initial_ty) + " : light_" +  str(light_y) + ")" , file=sys.stderr)
    
    if(0 < dy):
        moveY = 'N'
        initial_ty = initial_ty - 1 
    elif (dy < 0 ):
        moveY = 'S'
        initial_ty = initial_ty + 1
    else:
        moveY = ''
    

    # A single line providing the move to be made: N NE E SE S SW W or NW
    print(moveY + moveX)
