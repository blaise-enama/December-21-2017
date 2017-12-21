#initial variables, constants
INITIAL_BALANCE = 800
TARGET = INITIAL_BALANCE*3 #tells us when the balance triples
RATE = 3.0
#step 2: initialize variables used with the loop
balance = INITIAL_BALANCE
year = 0
#step 3: count the years required for the investment to triple
while balance <TARGET:
    year = year + 1
    interest=balance * RATE/100
    balance=balance + interest
#step 4: print the results
print("The investment tripled after", year, "years.")

import turtle
for i in range(300):
    turtle.forward(i)
    turtle.right(81)
    turtle.speed(100)
    turtle.star
