from classes.field import Field
from random import randint
import copy

def random_and_bound(startfield):
    best_solution = []
    for i in range(1000):
        current_solution = []
        solution_length = 0
        field = startfield
        while not field.won() and (len(best_solution) == 0 or (len(current_solution) <= len(best_solution))):
            child_fields = field.make_childs()
            current_solution.apend(field.convert_to_string())
            number = randint(0, (len(child_fields) - 1))
            field = child_fields[number]
        if field.won():
            best_solution = copy.deepcopy(current_solution)

    print("steps to win: ", (len(best_solution))
    for field in best_solution:
        print(field)
