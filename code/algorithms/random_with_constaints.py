from classes.field import Field
from random import randint
import copy

def random(startfield):
    best_field = None
    for i in range(100):
        print("I:", i)
        field = startfield
        dead_end = False
        while not field.won() and dead_end == False:
            if best_field == None or (len(field.parent_fields) <= len(best_field.parent_fields)):
                child_fields = field.make_childs()
                if len(child_fields) == 0:
                    print("HI")
                    dead_end = True
                    continue
                number = randint(0, (len(child_fields) - 1))
                field = child_fields[number]
            else:
                dead_end = True
        if field.won():
            if best_field == None or (len(field.parent_fields) < len(best_field.parent_fields)):
                best_field = field
                print(len(field.parent_fields))

    game_won(best_field)

def game_won(field):
    print("steps to win: ", (len(field.parent_fields) + 1))
    for parent_field in field.parent_fields:
        print(parent_field)
    print(field)
