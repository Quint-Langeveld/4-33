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
        if i % 30 == 0:
            print("Iteration: ", i + 1)
            print("Current bound:", bound)
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
    solution_legnth = len(best_solution)
    return [solution_legnth, nr_of_nodes, best_solution]
