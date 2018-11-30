from classes.cell import Cell
from classes.field import Field
from algorithms.breadth_first import breadth_first_regulator
from algorithms.iterative_deepening_depth_first import itterative_deepening_depth_first_generator
from algorithms.random import random
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
            breadth_first_regulator(self.fields)

        elif algorithm == "itterative_deepening_depth_first":
            itterative_deepening_depth_first_generator(self.fields[0])

        elif algorithm == "random":
            random(self.fields[0])

        else:
            "to do"



# start game
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python rush_hour.py startfield algorithm")
        sys.exit(1)
    startfield = sys.argv[1]
    algorithm = sys.argv[2]
    algorithms = ["breadthfirst", "itterative_deepening_depth_first", "random"]
    if algorithm not in algorithms:
        print("Algorithm not supported, please try again")
        sys.exit(1)
    rush_hour = Rush_hour(startfield)
    rush_hour.play(algorithm)
