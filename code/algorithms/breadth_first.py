from classes.field import Field
from classes.cell import Cell
from classes.archive import Archive
#from algorithms.visualization import visualization
import copy

def breadth_first(field, remember_path):

    """
    Breadth first algorithm for solving a Rush Hour game.
    field: startfield
    remember_path: bool that indicates wether moves should be saved in Archive
    """
    nr_of_nodes = 0
    if remember_path == True:
        archive = Archive()
        archive.add_start_field(field)
        child_fields = [field]
        best_solutions = 0
        won = False
        path = 0
        while won == False:
            new_fields = child_fields[0].make_childs()
            nr_of_nodes += 1
            if path < len(archive.trace_path(child_fields[0])):
                path = len(archive.trace_path(child_fields[0]))
                print(path)
            for new_field in new_fields:
                if archive.add(child_fields[0], new_field):
                    child_fields.append(new_field)
                    print(nr_of_nodes)
                if new_field.won():
                    won = True
                    best_solutions += 1
                    solution = archive.trace_path(new_field)
                    solution_length = len(solution)
                    nr_of_nodes += 1
                    return[solution_length, nr_of_nodes, solution]
            del child_fields[0]

    else:
        past_fields = []
        child_fields = [field]
        won = False
        while won == False:
            new_fields = child_fields[0].make_childs()
            nr_of_nodes += 1
            for new_field in new_fields:
                hashed_field = hash(new_field.convert_to_string())
                new_field.layer = child_fields[0].layer + 1
                print(nr_of_nodes)
                if hashed_field not in past_fields:
                    past_fields.append(hashed_field)
                    child_fields.append(new_field)
                if new_field.won():
                    won = True
                    solution_length = new_field.layer + 1
            del child_fields[0]
        return [solution_length, nr_of_nodes]
