import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

message = input()
answer = [] # answer
previous = ""
binary = ""
first = True

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

# Step 1: Transform into Binary
def text_to_bits(text):
    return [bin(ord(x))[2:].zfill(7) for x in text]

binary = binary.join(text_to_bits(message))

# Step 2: Convert each bit into Chuck Norris Code
for b in str(binary):
    if previous == b:
        answer.append("0")
    else:
        if "1" in b:
            if first == False: 
                answer.append(" ")
            answer.append("0 0")
        elif "0" in b:
            if first == False:
                answer.append(" ")
            answer.append("00 0")
        
        previous = b
        if first == True:
            first = False

print("".join(answer))
