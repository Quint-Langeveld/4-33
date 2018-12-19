from classes.field import Field
from random import randint
import copy

def random(startfield, iterations):
    """
    Random algorithm for solving a Rush Hour game.
    iterations: Number of iterations requested
    """
    solutions = {}
    nr_of_nodes = 0
    for i in range(iterations):
        solution_length = 0
        field = startfield
        while not field.won():
            child_fields = field.make_childs()
            solution_length += 1
            nr_of_nodes += 1
            number = randint(0, (len(child_fields) - 1))
            field = child_fields[number]
        try:
            solutions[solution_length] =  int(solutions[solution_length] + 1)
        except:
            solutions[solution_length] = int(1)
        if i % 10 == 0:
            print("Iteration:", i + 1)
    return solutions
