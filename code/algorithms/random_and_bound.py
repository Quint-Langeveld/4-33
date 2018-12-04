from classes.field import Field
from random import randint
import copy

def random_and_bound(startfield):
    best_solution = []
    bound = 1000
    for i in range(10000):
        print(i)
        print(bound)
        current_solution = [startfield.convert_to_string()]
        solution_length = 0
        field = startfield
        while not field.won() and (len(best_solution) == 0 or (len(current_solution) <= bound)):
            child_fields = field.make_childs()
            number = randint(0, (len(child_fields) - 1))
            field = child_fields[number]
            current_solution.append(field.convert_to_string())
        if field.won():
            best_solution = copy.deepcopy(current_solution)
            bound = len(best_solution)

    print("steps to win: ", len(best_solution))
    for field in best_solution:
        print(field)
