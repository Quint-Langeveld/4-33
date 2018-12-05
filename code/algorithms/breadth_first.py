from classes.field import Field
from classes.cell import Cell
from classes.archive import Archive
from visualization import visualization
import copy

def breadth_first(field, remember_path):

    if remember_path == True:
        archive = Archive()
        archive.add_start_field(field)
        child_fields = [field]
        best_solutions = 0
        won = False
        path = 0
        while won == False:
            new_fields = child_fields[0].make_childs()
            if path < len(archive.trace_path(child_fields[0])):
                path = len(archive.trace_path(child_fields[0]))
                print(path)
            for new_field in new_fields:
                visualization(new_field.field)
                archive.add(child_fields[0], new_field)
                child_fields.append(new_field)
                if new_field.won():
                    won = True
                    best_solutions += 1
                    game_won(archive, new_field, best_solutions)
            del child_fields[0]

    else:
        past_fields = []
        child_fields = [field]
        won = False
        while won == False:
            #print(solution_length)
            new_fields = child_fields[0].make_childs()
            for new_field in new_fields:
                hashed_field = hash(new_field.convert_to_string())
                new_field.layer = child_fields[0].layer + 1
                if hashed_field not in past_fields:
                    past_fields.append(hashed_field)
                    child_fields.append(new_field)
                if new_field.won():
                    won = True
                    solution_length = new_field.layer + 1
            del child_fields[0]
        print(solution_length)


def game_won(archive, field, best_solutions):
    path = archive.trace_path(field)
    print(f"Solution {best_solutions}:")
    print("steps to win: ", len(path))
    for field in path:
        print(field)
    print(len(archive.fields))
