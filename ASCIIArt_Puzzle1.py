import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l = int(input())
h = int(input())
t = input()
pos = []
toprint = ""

alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U', 'V','W','X','Y','Z','?']

for k in t:
    
    print("New letter = " + k, file=sys.stderr)
    if k.isalpha():
        pos.append(int(alphabet.index(k.upper()) * l))
 
    else:
        a = '?'
        pos.append(alphabet.index(a.upper()) * l)
        

for i in range(h):
    row = input()

    for p in pos:
        
        element = row[p:p+l]
        toprint = toprint + element
        
    print(toprint)
    toprint = ""

