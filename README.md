# 4-33

To run: run rush_hour.py to start the programm. In the command line choose the algorith (for now only Breadthfirst) to run 
the board with and the .txt file to load the board from. 

rush_hour.py then uses the "cell" class to identify a car/truck on the board and uses the corresponding algorith class to move
the vehicles. The algorith class revers to the Field class to create Field objects. The output of the algorith classes 
are a list of Field objects which are used by rush_hour.py to 'decide' when the board is 'won'. 

The output of rush_hour.py is an integer that represents the amount of moves that were made to complete the inputted board.

