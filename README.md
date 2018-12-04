# 4-33

# My Project:
Seven problems are given on a 6x6, 9x9 and 12x12 grid with a fixed setup of cars/trucks. There is one exit on the grid and we are supposed to find the best solution of the given problems. Cars and trucks, respectively have a length of two and three, can only move horizontally or vertically depending on their fixed position from the start. Cars and trucks can't jump over or move through other vehicles on the grid to find the best solution.

![alt text](https://github.com/Quint-Langeveld/4-33/blob/master/doc/Rushhour6x6_1.jpg)  
This is an example of an inittial situation.  
(Image was taken from: http://heuristieken.nl/wiki/index.php?title=File:Rushhour6x6_1.jpg)  

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
The Statespace can be formulated for different algorithms.
The state space is the number of configurations, where the upper bound and lower bound respectively are the maximum and minimum number of configurations for a problem. As the lower bound is always the same, namely 1, this is not as interesting as the upper bound of the problem. The formula to calculate the upper bound of amount of configrations is:  
```
((height grid - 1)^(number of small cars)) * ((height grid - 2)^(number of trucks))
```

The upper bound is equal to the state space. This means the following:
```
Upper bound (maximum number of fields): In the case of the bord pictured above, this means: 1 mln.
Lower bound (minimal number of fields): 1
```

## Algorithms 
We looked into a Breadth-first and a Random algorithm to find a solution for the Rush hour problem. See the algorithm directory for more information

When trying to complete the field above with a random and a breadth-first approach, the difference in memmory use was notable. For a random approach, the amount of fields in memmory was equivalent to the amount of fields past. On the other hand, the maximum amount of fields in memmory for a breadth-first approach was equivalent to the state space.

### Random 
In theory, the upper bound of a random algorithm is infinite. For a representation of the random distribution of solutions, see the results directory.  
  
## Objective Function:
The objective for Rush hour is met when the red car find it's way out of the bord. This can simply be summarized in one interger: the amount of moves done to reach the exit. The theoretical upper bound of the objective function thereby is the theoretical upperbound of the state space. 


## Advanced
#### What makes a 'difficult' board difficult?
This question can be addressed in at least two ways. The First way is looking at the formula of the state space. We can conclude that for a breadth-first algorithm, that the outcome of the formula increases, when the field gets bigger or when the amount of cars and trucks get higher. This is a good start, but this is not perfectly true. When, for example, a board is entirely full with cars but with the red car immediately next to the exit, the outcome of the formula is very big, while the objective score is just one.  

Therefore the problem can better be addressd in a more logical way. If the amount of possible 'next moves' is responsible for the majority of the complexity of the problem, an initial board gets more 'difficult' when the amount of children increases. Therefore we define the term 'difficult' as being:  
```
A 'difficult' board, is a board that uses a lot of steps, relative to the amount of configurations (state space) of that board
```
Then the question arises if there are 'difficult' moves?

#### What makes a 'difficult' move difficult?
For this question, we believe there is not a clear answer. We can try to set up multiple variables who together try to optimize the program and thereby decreases the 'practical state space'. For example a move that brings the red car closer to the exit can be seen as a good move and by a relative points system can get another value than when the red car takes a step back from the exit. Them same for bringing other cars more to the perifery of the board to eventually make way for the red car, in stead of moveing them to the centre.  
More work can be done for this. 

