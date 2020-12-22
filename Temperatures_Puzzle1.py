import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of temperatures to analyse

if n == 0:
    print(0) # no temperature to analyze
else:
    smallest_gap = None
    temp = None
    for i in input().split():
        # t: a temperature expressed as an integer ranging from -273 to 5526
        t = int(i)
        
        if(smallest_gap == None):
            smallest_gap = abs(int(t) - 0)
            temp = t 
        elif ( abs(int(t)-0) < smallest_gap ) or ( abs(int(t)-0) == smallest_gap and t>0 ):
            smallest_gap = abs(int(t)-0)
            temp = t

    print(temp)
