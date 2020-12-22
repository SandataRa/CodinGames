import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

surface_n = int(input())  # the number of points used to draw the surface of Mars.

# The landing Zone
bLX = None
bLY = None
eLX = None
eLY = None

init = True

for i in range(surface_n):
    # land_x: X coordinate of a surface point. (0 to 6999)
    # land_y: Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
    land_x, land_y = [int(j) for j in input().split()]
    
    if init:
        bLX = int(land_x)
        bLY = int(land_y)
        init = False
    elif bLY == int(land_y) and (abs(bLX - int(land_x)) >= 1000):
        eLX = int(land_x)
        eLY = int(land_y)
        
        print("New landing zone detected (" + str(bLX) + ";" + str(bLY) + ") (" + str(eLX) + ";" + str(eLY) + ")", file=sys.stderr)
         
# game loop
while True:
    # h_speed: the horizontal speed (in m/s), can be negative.
    # v_speed: the vertical speed (in m/s), can be negative.
    # fuel: the quantity of remaining fuel in liters.
    # rotate: the rotation angle in degrees (-90 to 90).
    # power: the thrust power (0 to 4).
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]
    

    #Converted variables
    mLX = int(x)
    mLY = int(y)
    mLHS = int(h_speed)
    mLVS = int(v_speed)
    mLF = int(fuel)
    mLR = int(rotate)
    mLP = int(power) 


    # Calculating rotation
    mLR = 0
    
    # Calculating power
    
    if mLVS < -40 and (mLP+1) <= 4:
        mLP += 1
    elif mLVS > -40 and 0 <= (mLP-1) :
        mLP -= 1        

    print(mLR, mLP)

