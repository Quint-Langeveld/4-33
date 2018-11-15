from cell import Cell
from field import Field

class Rush_hour():
    def __init__(self):
        self.current_solution = []
        self.won = False
        self.fields = self.load_startfield("startfield.txt")

    def load_startfield(self, filename):
        # open startfield file and put lines in list
        with open(filename, "r") as f:
            field_data = f.readlines()
            for i, line in enumerate(field_data):
                field_data[i] = line.strip().split()
            new_field = []
            for row in field_data:
                new_field_row = []
                for cell in row:
                    if cell == "E":
                        new_field_row.append(Cell(id = "E", direction = "", vehicle_size = 0))
                    else:
                        id = cell[0]
                        direction = cell[1]
                        vehicle_size = cell[2]
                        new_field_row.append(Cell(id = id, direction = direction, vehicle_size = vehicle_size))
                new_field.append(new_field_row)
        return [Field(new_field)]

    def play(self):
        for field in self.fields:
            field.next_step()
                







    #
    #
    # def play(self):
    #
    #
    #
    #     self.vehicles = self.load_vehicles("vehicles.txt")
    #
    # def load_vehicles(self, filename):
    #     # open item file and put lines in list
    #     with open(filename, "r") as f:
    #         vehicles_data = f.readlines()
    #         for i, line in enumerate(vehicles_data):
    #             vehicles_data[i] = line.strip()
    #         # find items in list and assign information to Item variables
    #         vehicles = []
    #         for i in range(0, len(vehicles_data), 9):
    #             type = vehicles_data[i]
    #             size = vehicles_data[i + 1]
    #             x = vehicles_data[i + 2]
    #             y = vehicles_data[i + 3]
    #             movable = bool(vehicles_data[i + 4])
    #             unchangable = vehicles_data[i + 5]
    #             free_spaces_lower_coordinate = vehicles_data[i + 6]
    #             free_spaces_higher_coordinate = vehicles_data[i + 7]
    #             # create new Item object and put in item library and
    #             # inventory of room
    #             vehicle = Vehicle(type, size, x, y, movable, unchangable,
    #                               free_spaces_lower_coordinate,
    #                               free_spaces_higher_coordinate)
    #             vehicles.append(vehicle)
    #             print(vehicle)
    #     print(vehicles)
    #     return(vehicles)



# start game
if __name__ == "__main__":
    rush_hour = Rush_hour()
    rush_hour.play()
