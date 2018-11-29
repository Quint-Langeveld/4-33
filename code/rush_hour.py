from classes.cell import Cell
from classes.field import Field
from algorithms.breadth_first import breadth_first
import sys

class Rush_hour():
    def __init__(self, startfield):
        self.current_solution = []
        self.fields = self.load_startfield(startfield)

    def load_startfield(self, filename):
        # open startfield file and put lines in list
        filename = f"../data/startfields/{filename}"
        with open(filename, "r") as f:
            field_data = f.readlines()
            field_size = len(field_data)
            for i, line in enumerate(field_data):
                field_data[i] = line.strip().split()
            new_field = []
            for row in field_data:
                new_field_row = []
                for cell in row:
                    if cell == "E":
                        new_field_row.append(Cell("E", "", 0))
                    else:
                        id = cell[0]
                        direction = cell[1]
                        vehicle_size = cell[2]
                        new_field_row.append(Cell(id, direction, vehicle_size))
                new_field.append(new_field_row)
        return [Field(field_size, new_field)]

    def play(self, algorithm):
        if algorithm == "breadthfirst":
            for i, field in enumerate(self.fields):
                if field.won():
                    print(len(self.fields))
                    print("steps to win: ", (len(field.parent_fields) + 1))
                    for parent_field in field.parent_fields:
                        print(parent_field)
                    print(field)
                    break
                else:
                    new_fields = breadth_first(field)
                    for new_field in new_fields:
                        #print(new_field)
                        self.fields.append(new_field)
        if algorithm == "itterative_deepening_depth_first":
            depth = 1
            while not field.won():
                ...
                ...
                depth += 1


        else:
            "to do"


# start game
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python rush_hour.py startfield algorithm")
        sys.exit(1)
    startfield = sys.argv[1]
    algorithm = sys.argv[2]
    if algorithm != "breadthfirst":
        print("Algorithm not supported, please try again")
        sys.exit(1)
    rush_hour = Rush_hour(startfield)
    rush_hour.play(algorithm)
