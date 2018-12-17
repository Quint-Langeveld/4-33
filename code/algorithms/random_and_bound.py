from classes.field import Field
from random import randint
import copy

def random_and_bound(startfield, iterations, bound):
    """
    Random and bound algorithm for solving a Rush Hour game.
    iterations: Number of iterations requested
    bound: initial bound requested
    """
    best_solution = []
    bound = bound
    nr_of_nodes = 0
    for i in range(iterations):
        print(i)
        print(bound)
        current_solution = [startfield.convert_to_string()]
        solution_length = 0
        field = startfield
        while not field.won() and  len(current_solution) <= bound:
            child_fields = field.make_childs()
            nr_of_nodes += 1
            number = randint(0, (len(child_fields) - 1))
            field = child_fields[number]
            current_solution.append(field.convert_to_string())
        if field.won():
            best_solution = copy.deepcopy(current_solution)
            bound = len(best_solution)

    print("steps to win: ", len(best_solution))
    for field in best_solution:
        print(field)
    print(nr_of_nodes)
