from classes.field import Field
from random import randint
import copy

def branch_and_bound(startfield):
    """
    Branch and bound algorithm for solving a Rush Hour game.
    bound: initial bound requested
    """
    best_solution = []
    bound = 10000
    nr_of_nodes = 0
    field = startfield
    stack = [field]
    current_solution = []
    # solution_length = 0
    while len(stack) > 0:
        #solution_length += 1
        current_solution.append(field.convert_to_string())
        print(bound)
        print(len(stack))
        if len(current_solution) < bound:
        # if solution_length < bound:
            child_fields = field.make_childs()
            nr_of_nodes += 1
            for child_field in child_fields:
                child_field.layer = field.layer + 1
                if child_field.convert_to_string() not in current_solution:
                    stack.insert(0, child_field)
            stack.remove(field)
            field = stack[0]
            if field.won():
                stack.remove(field)
                best_solution = current_solution
                bound = len(best_solution)
                #bound = solution_length
                if len(stack) > 0:
                    field = stack[0]
                current_solution = current_solution[:field.layer]
        else:
            stack.remove(field)
            if len(stack) > 0:
                field = stack[0]
            #solution_length = field.layer
            current_solution = current_solution[:field.layer]

    #print("  ", solution_length)
    print("steps to win: ", len(best_solution))
    for field in best_solution:
        print(field)
