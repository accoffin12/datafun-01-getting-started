# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 21:40:07 2023

@author: Tower
"""
# Student Name: Alexandra Coffin, Student ID: S561404
# Course: CSIS Data Analytics Fundementals
# Professor: Dr. Case
# Assignment 1 Module 1 Task 4

print('Domain: Formula 1')
print()
#
print('Welcome to the world of Formula 1!')
print('Enter the number of points won by 3 different racers.')
print('The values of the points must be between 0 and 25.')
print('No two racers may have the same amont.')
# If a racer is not in top 10 they win 0 points for position.
# Racers win points based on where they stand on the grid.
# Points are then added toward the Constructor's Cup.
# The Constructor's Cup is the competition between Facotry Teams.
racer1 = value1 = int(input('Enter Points for racer1: '))
racer2 = value2 = int(input('Enter Points for racer2: '))
racer3 = value3 = int(input('Enter Points for racer3: '))

print('1: Sum:')
print('Racer1 and Racer2 are on the same Team.')
# Formula One operates as teams with 2 cars for the constructors cup. 
# In this we are going to assum two cars are from the same team.
team_result = result = racer1 + racer3
print('The team won:', team_result)
#
print()
print('2: Average')
print('What is the average between all 3 racers?')
result = (team_result + racer2) / 3
float(result)
#
print('Average between racers, rounded result', round(result))
#
print()
print('3: Product:') 
print('How many points will a racer have if they consistantly finish all year?')
# There are 22 races in a standrd Formula 1 year. 
races = 22
# These are estimations and not based on performance.
racer1_wins = 22 * racer1
print('racer1 wins:', racer1_wins)
#
racer2_wins = 22 * racer2
print('racer2 wins:', racer2_wins)
#
racer3_wins = 22 * racer3
print('racer3 wins:', racer3_wins,)
print()
print('4: Minimum Number of Points')
#
min(racer1, racer2, racer3)
print('The racer with', min(racer1, racer2, racer3))
#
print()
print('5: Maximum Number of Points')
#
max(racer1, racer2, racer3)
print('The racer with', max(racer1, racer2, racer3))
print()
#
print('5: Range of Points between Racers')
print('range:', min(racer1, racer2, racer3), '-', max(racer1, racer2, racer3))
print()
#
print('Decision Making')
print()
print('Less than statment')
# A racer is awarded 15 points if they win third place.
# If the value is less than 15 they are still in the "points".
# "Points" are the first 10 spots on the grid,
# anything positions under 10th recieve 0 points according to FIA rules. 
tenth_place = 1
minimum = racer1
if racer1 < tenth_place:
    minimum = racer1
if racer2 < tenth_place:
    minimum = racer2
if racer3 < tenth_place:
    minimum = racer3
print('Ouch, the racer with', minimum, 'Points, was either back of the grid or DNF.')
# DNF = Did Not Finish
print()
print('Greater than statement')
print('Did your racers make it to the podium?')
# In order to be on the podium in F1 a racer must win 25, 18 or 15 points.
# First = 25 pts, Second = 18 pts, and Third = 15 pts.
fourth_place = 12
if racer1 > fourth_place:
    m = racer1
if racer2 > fourth_place:
    m = racer2
if racer3 > fourth_place:
    m = racer3
print('Congrats, racer with', m, 'points is on the Podium!')
print()
print('Equal to Statement')
# Racers are awarded 25 points in first place.
first_place = 25
if racer1 == first_place:
    print('Racer1 has won the race', racer1, 'Points. Go celebrate with the team!')
if racer2 == first_place:
    print('Racer2 has won the race', racer2, 'Points. Go celebrate with the team!')
if racer3 == first_place:
    print('Racer3 has won the race with', racer3, 'Points. Go celebrate with the team!')    
    
    


    

    
    


    


