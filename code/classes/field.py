from classes.cell import Cell
import copy

class Field(object):
    def __init__(self, size, new_field):
        self.exit_row_index = (size - 1) // 2
        self.size = size
        self.field = new_field
        self.layer = 0

    def __str__(self):
        s = ""
        for row in self.field:
            for cell in row:
                s += cell.id + cell.direction + str(cell.vehicle_size) + " "
            s += "\n"
        return s

    def make_childs(self):
        """Create children fields from field"""
        new_fields = []
        # iterate over rows in field
        for i, row in enumerate(self.field):
            # iterate over cell in row
            for j in range(len(row)):
                # check if cell is part of car that is already handled by for loop
                if row[j].id == row[j-1].id or row[j].id == self.field[i - 1][j].id:
                    continue
                # create cell variable equal to Cell object being handled
                cell = row[j]
                # check if cell is part of vehicle and size and direction if vehicle
                if cell.id != "E":
                    # new_fields += self.make_moves(cell, i, j)
                    if cell.direction == "H":
                        #if cell.vehicle_size == 2:
                            new_fields += self.make_moves(cell, i, j)


                            # # find possible new places for vehicle
                            # for k in range(1, (self.size)):
                            #     if j - k >= 0 and row[j - k].id == "E":
                            #         if self.check_if_valid_move(cell, -k, i, j):
                            #             new_field_object = self.create_new_field(cell, i, j, -k)
                            #             new_fields.append(new_field_object)
                            #     # find possible new places for vehicle
                            #     if j + k <= (self.size - 1) and row[j + k].id == "E":
                            #         if self.check_if_valid_move(cell, k, i, j):
                            #             new_field_object = self.create_new_field(cell, i, j, k)
                            #             new_fields.append(new_field_object)
                        #else: # if cell.vehicle_size == 3
                            # for k in range (1, (self.size)):
                            #     if j - k >= 0 and row[j - k].id == "E":
                            #         if self.check_if_valid_move(cell, -k, i, j):
                            #             new_field_object = self.create_new_field(cell, i, j, -k)
                            #             new_fields.append(new_field_object)
                            #     if j + k <= (self.size - 1) and row[j + k].id == "E":
                            #         if self.check_if_valid_move(cell, k, i, j):
                            #             new_field_object = self.create_new_field(cell, i, j, k)
                            #             new_fields.append(new_field_object)
                    else: # if cell.direction == vertical
                        if cell.vehicle_size == 2:
                            for k in range(1, (self.size - 1)):
                                if i - k >= 0 and self.field[i - k][j].id == "E":
                                    if self.check_if_valid_move(cell, -k, i, j):
                                        new_field_object = self.create_new_field(cell, i, j, -k)
                                        new_fields.append(new_field_object)
                                if i + k <= (self.size - 1) and self.field[i + k][j].id == "E":
                                    if self.check_if_valid_move(cell, k, i, j):
                                        new_field_object = self.create_new_field(cell, i, j, k)
                                        new_fields.append(new_field_object)
                        else: # if cell.vehicle_size == 3
                            for k in range(1, (self.size)):
                                if i - k >= 0 and self.field[i - k][j].id == "E":
                                    if self.check_if_valid_move(cell, -k, i, j):
                                        new_field_object = self.create_new_field(cell, i, j, -k)
                                        new_fields.append(new_field_object)
                                if i + k <= (self.size - 1) and self.field[i + k][j].id == "E":
                                    if self.check_if_valid_move(cell, k, i, j):
                                        new_field_object = self.create_new_field(cell, i, j, k)
                                        new_fields.append(new_field_object)
        return new_fields

    def make_moves(self, cell, i, j):
        new_fields = []
        for k in range(1, self.size):
            if j - k >= 0 and self.field[i][j - k].id == "E":
                if self.check_if_valid_move(cell, -k, i, j):
                    new_field_object = self.create_new_field(cell, i, j, -k)
                    new_fields.append(new_field_object)
            if j + k <= (self.size - 1) and self.field[i][j + k].id == "E":
                if self.check_if_valid_move(cell, k, i, j):
                    new_field_object = self.create_new_field(cell, i, j, k)
                    new_fields.append(new_field_object)
            # if i - k >= 0 and self.field[i - k][j].id == "E":
            #     if self.check_if_valid_move(cell, -k, i, j):
            #         new_field_object = self.create_new_field(cell, i, j, -k)
            #         new_fields.append(new_field_object)
            # if i + k >= (self.size - 1) and self.field[i - k][j].id == "E":
            #     if self.check_if_valid_move(cell, -k, i, j):
            #         new_field_object = self.create_new_field(cell, i, j, -k)
            #         new_fields.append(new_field_object)
        return new_fields


    def create_new_field(self, cell, i, j, k):
        pos = 1
        if k > 0:
            pos = -1
        new_field = self.make_copy()
        if cell.direction == "H":
            new_field[i][j + k] = Cell(cell.id, cell.direction, cell.vehicle_size)
            new_field[i][j + k + (1 * pos)] = Cell(cell.id, cell.direction, cell.vehicle_size)
            if cell.vehicle_size == 3:
                new_field[i][j + k + (2 * pos)] = Cell(cell.id, cell.direction, cell.vehicle_size)
            for m in range(cell.vehicle_size, (self.size)):
                index_to_check = j + k + (m * pos)
                if index_to_check <= (self.size - 1) and new_field[i][index_to_check].id == cell.id:
                    new_field[i][index_to_check] = Cell("E", "", 0)
        else:
            new_field[i + k][j] = Cell(cell.id, cell.direction, cell.vehicle_size)
            new_field[i + k + (1 * pos)][j] = Cell(cell.id, cell.direction, cell.vehicle_size)
            if cell.vehicle_size == 3:
                new_field[i + k + (2 * pos)][j] = Cell(cell.id, cell.direction, cell.vehicle_size)
            for m in range(cell.vehicle_size, (self.size)):
                index_to_check = i + k + (m * pos)
                if index_to_check <= (self.size - 1) and new_field[index_to_check][j].id == cell.id:
                    new_field[index_to_check][j] = Cell("E", "", 0)
        new_field_object = Field(self.size, new_field)
        return new_field_object

    def check_if_valid_move(self, cell, k, i, j):
        pos = 1
        if k > 0:
            pos = -1
        move_possible = True
        for l in range(abs(k)):
            if cell.direction == "H":
                if self.field[i][j + k + (l * pos)].id != "E" and self.field[i][j + k + (l * pos)].id != cell.id:
                    move_possible = False
            else:
                if self.field[i + k + (l * pos)][j].id != "E" and self.field[i + k + (l * pos)][j].id != cell.id:
                    move_possible = False
        return move_possible


    def won(self):
        # find red car
        index_red_car = 0
        vehicle_blocking_exit = False
        for i, cell in enumerate(self.field[self.exit_row_index]):
            if cell.id == "R":
                index_red_car = i
        for i in range(index_red_car, (self.size)):
            if self.field[self.exit_row_index][i].id != "E" and self.field[self.exit_row_index][i].id != "R":
                vehicle_blocking_exit = True
        if vehicle_blocking_exit == True:
            return False
        else:
            return True

    def convert_to_string(self):
        s = ""
        for row in self.field:
            for cell in row:
                s += cell.id + cell.direction + str(cell.vehicle_size) + " "
            s += "\n"
        return s

    def make_copy(self):
        copy = []
        for i in range(self.size):
            copy.append([])
        for i, row in enumerate(self.field):
            for cell in row:
                copy[i].append(Cell(cell.id, cell.direction, cell.vehicle_size))
        return copy
