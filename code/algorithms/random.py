from classes.field import Field
from random import randint
import copy

def random(startfield):
    solutions = {}
    for i in range(100):
        print(i)
        field = startfield
        while not field.won():
            child_fields = field.make_childs(False)
            number = randint(0, (len(child_fields) - 1))
            field = child_fields[number]
        solution_length = int((len(field.parent_fields) + 1))
        try:
            solutions[solution_length] =  int(solutions[solution_length] + 1)
        except:
            solutions[solution_length] = int(1)
    print(solutions)
