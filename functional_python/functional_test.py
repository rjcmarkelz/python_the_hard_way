#http://www.python-course.eu/python3_lambda.php
import random

# use map and reduce :)
names = ['Mary', 'Isla', 'Sam']
name_length = map(len, ['Mary', 'Isla', 'Sam'])
print (name_length)

secret_names = map(hash, names)
secret_names

squares = map(lambda x : x * x , [0, 1, 2, 3, 4])
squares[0]

code_names = ['Mr. Pink', 'Mr. Orange', 'Mr. Blonde'] 

for i in range(len(names)):
    names[i] = random.choice(code_names)


print(names)

secret_names = map(lambda x: random.choice(['Mr. Pink', 'Mr. Orange', 'Mr. Blonde']),
    names)

print(names)

# reduce 
sumit = reduce(lambda a, x: a + x, [0, 1, 2, 3, 4])

sum2 = lambda x, y: x + y
sum2(3,4)
# 7

# compared to 
def sum3(x,y):
    return x + y

sum3(3,4)

# r = map(func, seq)
# python3 map() returns an iterator instead of a list
def fahrenheit(T):
    return ((float(9)/5) * T + 32 )

def celcius(T):
    return(float((5)/9) * (T - 32))

temps = (36.5, 37, 37.5, 38, 39)
Fer = map(fahrenheit, temps)
Cel = map(celcius, Fer) # as map object

# unwrap to list
Fer = list(map(fahrenheit, temps))
Cel = list(map(celcius, Fer)) # as map object

Fer
Cel

# or using lambdas
C = [39.2, 36.5, 37.3, 38, 37.8]
F = list(map(lambda x : float(9)/5 * x + 32, C))
F

C2 = list(map(lambda x : (float(5)/9) * (x - 32), F))
C2

# use map on more than one list
a = [1, 2, 3, 4]
b = [17, 12, 11, 10]
c = [-1, -4, 5, 9]

list(map(lambda x, y : x + y, a, b ))
list(map(lambda x, y, z : x + y + z, a, b, c))
list(map(lambda x, y, z : 2.5*x + 2*y -z, a, b, c))
# parameter x gets values from list a, y from b, and z from list c

# unequal lengths?
# still matches them up 
a = [1, 2, 3, 4]
d  = [2, 3, 4]
list(map(lambda x, y : x + y, a, d ))
# returns [3, 5, 7]

#race car code
from random import random
def move_cars(car_positions):
    return map(lambda x: x + 1 if random() > 0.3 else x, car_positions)

def output_car(car_position):
    return '-' * car_position

def run_step_of_race(state):
    return {'time': state['time'] - 1, 'car_positions': move_cars(state['car_positions'])}

def draw(state):
    print ('')
    print ('\n'.join(map(output_car, state['car_positions'])))

def race(state):
    draw(state)
    if state['time']:
        race(run_step_of_race(state))

race({'time': 3, 'car_positions': [0, 1, 2, 3, 10]})
# for some reason blanking out after second step in recursion












