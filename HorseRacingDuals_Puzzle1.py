import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input()) 
print("Nb Total of horses :" + str(n), file=sys.stderr, flush=True)

horses = [] # list of horses

for i in range(n):
    pi = int(input())
    horses.append(pi)

sorted_horses = sorted(horses)
minimum = max(sorted_horses)

for i in range(n-1):
    gap = abs(sorted_horses[i] - sorted_horses[i+1])
    if minimum > gap :
        minimum = gap
        print("New Strong Horse found : " + str(minimum), file=sys.stderr, flush=True)
        
        
print(minimum)


