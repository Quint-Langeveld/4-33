# 4-33

# My Project:
Seven problems are given on a 6x6, 9x9 and 12x12 grid with a fixed setup of cars/trucks. There is one exit on the grid and we are supposed to find the best solution of the given problems. Cars and trucks, respectively have a length of two and three, can only move horizontally or vertically depending on their fixed position from the start. Cars and trucks can't jump over or move through other vehicles on the grid to find the best solution.

# Getting Started:
## Prerequisites:
This codebase is fully written in Python3.6.3. In requirements.txt are all necessary packages included to run the code succesfully. These are easily installed via the provided instruction below:
```
pip install -r requirements.txt
```
  
## Structure:
All Python scripts are stored in the folder Code. All input values can be found in the map Data where the map Results hold the  obtained results from the code.

## Testing:
To run the code with a standardconfiguration use the instruction below, where one of the seven problems and the used algorithm should be defined: 
```
python rush_hour.py <field>.txt <algorithm>
```

## Authors:
Melle Meewis, Quint Langeveld & Hugo Langeveld

## Acknowledgments:
We like to thank StackOverflow and the 'minor programmeren van de Uva' for helping us finishing the project. 

## State Space:
These are the number of configurations, where the upper bound and lower bound respectively are the maximum and minimum number of configurations. For example, the first bord has an upper bound of 253.125 configurations. The formula to calculate the upper bound of the state space is given below.  
```
((number of small cars)^(height grid - 1)) * ((number of trucks)^(height grid - 2))
```
  
## Upper and Lower Bound Solutions for Breadth-First
```
Upper bound (maximum number of steps): For breadth-first, the upper bound is equal to the state space. 
Lower bound (minimal number of steps): 1
```
  
## Objective Function:
  The number of steps necessary to move the red car to the exit.

