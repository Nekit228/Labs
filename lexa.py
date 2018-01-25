from time import sleep
from random import randint

k = 10
world = []

    
def first_step(): 
    for line in range(k):
        line = []
        for index in range(k):
            cell = [0, 0]
            line.append(cell)
        world.append(line)
       
    world[5][5][0] = 1
    world[5][4][0] = 1
    world[4][5][0] = 1


def print_lines():
    for i in range(k):
        for j in range(k):
            if world[i][j][0] == 0: 
                print("_", end = " ")
            elif world[i][j][0] == 1: 
                print("0", end = " ")
        print()
    print()
   
  
def counter():
    for i in range(k):            
        for j in range(k):
 
            x_1, y_1 = i, j - 1
            x_2, y_2 = i + 1, j
            x_3, y_3 = i, j + 1
            x_4, y_4 = i - 1, j
            
 
            if y_1 < 0:
                y_1 = 0     
 
            if x_4 < 0:
                x_4 = 0
 
            if x_2 > k - 1:
                x_2 = k - 1
 
            if y_3 > k - 1:
                y_3 = k - 1      
 
            summ = 0
            if world[x_1][y_1][0] == 1:
                summ += 1     
 
            if world[x_2][y_2][0] == 1:
                summ += 1
                
            if world[x_3][y_3][0] == 1:
                summ += 1
                
            if world[x_4][y_4][0] == 1:
                summ += 1
                   
            world[i][j][1] = summ         
 
 
 
def step():
    for i in range(k):
        for j in range(k):
            if world[i][j][1] == 2 or world[i][j][1] == 0 or world[i][j][1] == 4:
                world[i][j][0] = 0
            elif world[i][j][1] == 1 or world[i][j][1] == 3:
                world[i][j][0] = 1
    print_lines()
    counter()
 
 
def life_counter():
    c = 0
    for i in range(k):
        for j in range(k):
            c += world[i][j][0]
    return c
 
first_step() 
print_lines()
counter()
for i in range(3):
    step()
    
""" 
while life_counter() > 0:
    step()
    sleep(1)
"""
