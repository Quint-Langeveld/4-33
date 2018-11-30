from classes.field import Field
from random import randint
import copy

def random(startfield):
    best_field = None
    for i in range(100):
        field = startfield
        while not field.won():
            child_fields = field.make_childs()
            number = randint(0, (len(child_fields) - 1))
            field = child_fields[number]
        if best_field == None or (len(field.parent_fields) < len(best_field.parent_fields)):
            best_field = field

    game_won(best_field)

def game_won(field):
    print("steps to win: ", (len(field.parent_fields) + 1))
    for parent_field in field.parent_fields:
        print(parent_field)
    print(field)
