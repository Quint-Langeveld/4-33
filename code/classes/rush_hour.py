from classes.cell import Cell
from classes.field import Field
from algorithms.breadth_first import breadth_first
from algorithms.random_and_bound import random_and_bound
from algorithms.random import random
from algorithms.branch_and_bound import branch_and_bound
import sys
import datetime

class Rush_hour():
    def __init__(self, startfield, iterations, bound, keep_track):
        self.fields = self.load_startfield(startfield)
        self.field_number = startfield[5]
        self.startfield = self.load_startfield(startfield)[0]
        self.iterations = iterations
        self.bound = bound
        self.keep_track = keep_track

    def load_startfield(self, filename):
        # open startfield file and put lines in list
        filename = f"data/startfields/{filename}"
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
                        if len(cell) == 3:
                            id = cell[0]
                            direction = cell[1]
                            vehicle_size = cell[2]
                        else:
                            id = cell[:2]
                            direction = cell[2]
                            vehicle_size = cell[3]
                        new_field_row.append(Cell(id, direction, vehicle_size))
                new_field.append(new_field_row)
        return [Field(field_size, new_field)]

    def play(self, algorithm):
        if algorithm == "breadthfirst":
            results = breadth_first(self.startfield, self.keep_track)
            print(results[2])
            self.write_output(algorithm, results)

        elif algorithm == "random":
            results = random(self.startfield, self.iterations)
            self.write_output()

        elif algorithm == "random_and_bound":
            random_and_bound(self.startfield, self.iterations, self.bound)

        else: # algorithm == "branch_and_bound":
            branch_and_bound(self.startfield, self.bound)


    def write_output(self, algorithm, results):
        date_time = str(datetime.datetime.now())
        filename = f"results/outputs/Output Field{self.field_number}, {algorithm}, {date_time}.txt"
        with open(filename, "w") as f:
            f.write(f"Date and time: {date_time}\n"
                    f"Field: field {self.field_number}\n"
                    f"Algorithm: {algorithm}\n\n")

            if len(results) >= 2:
                f.write(f"Shortest solution: {results[0]}\n"
                        f"Number of nodes searched: {results[1]}\n\n")


            else:
                f.write(f"Solution distribution: {results[0]}\n")

            f.write(f"Start position: \n{self.startfield.convert_to_string()}\n")

            if len(results) == 3:
                f.write("Solution:")
                for field in results[2]:
                    f.write(f"{field}\n")



# start game
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python rush_hour.py startfield algorithm")
        sys.exit(1)
    startfield = sys.argv[1]
    algorithm = sys.argv[2]
    algorithms = ["breadthfirst", "random", "random_and_bound", "branch_and_bound"]
    if algorithm not in algorithms:
        print("Algorithm not supported, please try again")
        print("You can choose between the following:")
        for algorithm in algorithms:
            print(algorithm)
        sys.exit(1)
    rush_hour = Rush_hour(startfield)
    rush_hour.play(algorithm)
