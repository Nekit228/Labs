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
        
    world[9][9][0] = 1
    world[9][8][0] = 1
    world[9][7][0] = 1
    world[8][8][0] = 1
    world[5][5][0] = 1
    world[5][4][0] = 1
    world[4][5][0] = 1
    world[0][0][0] = 2
    world[0][1][0] = 2
    world[0][2][0] = 2
    world[1][0][0] = 2
    world[1][1][0] = 2


def print_lines():
    for i in range(k):
        for j in range(k):
            if world[i][j][0] == 0: 
                print("_", end = " ")
            elif world[i][j][0] == 1: 
                print("0", end = " ")
            elif world[i][j][0] == 2: 
                print("*", end = " ")
        print()
    print()

    
def counter():
    for i in range(k):            
        for j in range(k):
 
            x_from, y_from = i - 1, j - 1      
            x_to, y_to = i + 1, j + 1                
 
            if x_from < 0:
                x_from = 0     
 
            if y_from < 0:
                y_from = 0
 
            if x_to > k - 1:
                x_to = k - 1
 
            if y_to > k - 1:
                y_to = k - 1      
 
            summ_1 = 0
            summ_2 = 0
            
            if world[i][j][0] == 0:
                for x in range(x_from, x_to + 1):
                    for y in range(y_from, y_to + 1):
                        if world[x][y][0] == 1:
                            summ_1 += 1
                        elif world[x][y][0] == 2:
                            summ_2 += 1
                if summ_1 == 0 and summ_2 == 0:
                    world[i][j][1] = 0
                elif summ_1 > summ_2:
                    world[i][j][1] = summ_1
                elif summ_2 > summ_1:
                    world[i][j][1] = summ_2 + summ_2 * 10
                elif summ_1 == summ_2:
                    rand = randint(0, 1)
                    if rand == 0:
                        world[i][j][1] = summ_1 
                    if rand == 1:
                        world[i][j][1] = summ_2 + summ_2 * 10     

 
 
def step():
    for i in range(k):
        for j in range(k):
            if world[i][j][0] == 0:
                if world[i][j][1] >= 3 and world[i][j][1] <= 8:
                    world[i][j][0] = 1
                elif world[i][j][1] >= 33 and world[i][j][1] <= 88:
                    world[i][j][0] = 2
    print_lines()
    counter()
 
 
def life_counter():
    c = 0
    for i in range(k):
        for j in range(k):
            if world[i][j][0] == 0:
                c += 1
    return c


def who_wins():
    c1, c2 = 0, 0
    for i in range(k):
        for j in range(k):
            if world[i][j][0] == 1:
                c1 += 1
            if world[i][j][0] == 2:
                c2 += 1
    if c1 == c2:
        print("Ничья")
    elif c1 > c2:
        print("0 wins")
    if c1 < c2:
        print("* wins")

     
first_step()

while life_counter() > 0:
    step()
    #sleep(1)
    
if life_counter() == 0:
    who_wins()

