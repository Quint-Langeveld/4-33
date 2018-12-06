from classes.field import Field
from classes.cell import Cell
from classes.archive import Archive
import copy

def depth_and_bound(startfield):
    archive = Archive()
    archive.add_start_field(field)
    best_solution = []
    bound = 1000
    field = startfield
    fields = [field]
    fields.append(field)
    current_solution = []
    path = 0


    while len(fields) < 1:
        del current_solution[:]
        current_solution.append(field.convert_to_string())

        while len(current_solution) < 1000:
            new_fields = child_fields[0].make_childs()
            if path < len(archive.trace_path(fields[0])):
                path = len(archive.trace_path(fields[0]))
                print(path)

            for field in new_fields:
                archive.add(child_fields[0], field)
                fields.append(field)
            del fields[0]

            current_solution.append(fields[0].convert_to_string())







            field = copy.deepcopy(fields[0])

            if field.won():
                current_solution = copy.deepcopy(field)
                current_solution = [current_solution.convert_to_string()]
                del fields[0]
            else:
                del fields[0]

            print()


    print("steps to win: ", len(best_solution))
    print(current_solution)
