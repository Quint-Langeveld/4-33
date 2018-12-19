from classes.cell import Cell
import copy

class Field(object):
    """Object that representa a field in Rush Hour"""
    def __init__(self, size, new_field):
        """
        Initializes new Field object.
        size: Size of Field
        new_field: [[Cell]]
        return: string
        """
        self.exit_row_index = (size - 1) // 2
        self.size = size
        self.field = new_field
        self.layer = 0

    def __str__(self):
        """
        Returns string with information about self.
        return: string
        """
        s = ""
        for row in self.field:
            for cell in row:
                s += cell.id + cell.direction + str(cell.vehicle_size) + " "
            s += "\n"
        return s

    def make_childs(self):
        """
        Returns all possible children fields of self.
        Return: [Field]
        """
        new_fields = []
        # iterate over rows in field and cells in row
        for i, row in enumerate(self.field):
            for j in range(len(row)):
                # check if cell is part of car that is already handled by for loop
                if row[j].id == row[j-1].id or row[j].id == self.field[i - 1][j].id:
                    continue
                # create cell variable equal to Cell object being handled
                cell = row[j]
                # check if cell is part of vehicle and size and direction if vehicle
                if cell.id != "E":
                    if cell.direction == "H":
                        new_fields += self.make_horizontal_moves(cell, i, j)
                    else: # if cell.direction == vertical
                        new_fields += self.make_vertical_moves(cell, i, j)
        return new_fields

    def make_horizontal_moves(self, cell, i, j):
        """
        Moves vehicle to all possible places in horizontal direction
        cell:   Cell object in Field.field
        i:      Index of row Cell in Field.field
        j:      Index of column Cell in Field.field
        return: [Field]
        """
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
        return new_fields


    def make_vertical_moves(self, cell, i, j):
        """
        Moves vehicle to all possible places in vertical direction
        cell:   Cell object in Field.field
        i:      Index of row Cell in Field.field
        j:      Index of column Cell in Field.field
        return: [Field]
        """
        new_fields = []
        for k in range(1, self.size):
            if i - k >= 0 and self.field[i - k][j].id == "E":
                if self.check_if_valid_move(cell, -k, i, j):
                    new_field_object = self.create_new_field(cell, i, j, -k)
                    new_fields.append(new_field_object)
            if i + k <= (self.size - 1) and self.field[i + k][j].id == "E":
                if self.check_if_valid_move(cell, k, i, j):
                    new_field_object = self.create_new_field(cell, i, j, k)
                    new_fields.append(new_field_object)
        return new_fields


    def create_new_field(self, cell, i, j, k):
        """
        Creates field with vehicle on new position.
        cell:   Cell object in Field.field
        i:      Index of row Cell in Field.field
        j:      Index of column Cell in Field.field
        return: Field
        """
        pos = 1
        if k > 0:
            pos = -1
        new_field = self.make_copy()
        new_cell = Cell(cell.id, cell.direction, cell.vehicle_size)
        if cell.direction == "H":
            new_field[i][j + k] = new_cell
            new_field[i][j + k + (1 * pos)] = new_cell
            if cell.vehicle_size == 3:
                new_field[i][j + k + (2 * pos)] = new_cell
            for m in range(cell.vehicle_size, (self.size)):
                index_to_check = j + k + (m * pos)
                if index_to_check <= (self.size - 1) and new_field[i][index_to_check].id == cell.id:
                    new_field[i][index_to_check] = Cell("E", "", 0)
        else:
            new_field[i + k][j] = new_cell
            new_field[i + k + (1 * pos)][j] = new_cell
            if cell.vehicle_size == 3:
                new_field[i + k + (2 * pos)][j] = new_cell
            for m in range(cell.vehicle_size, (self.size)):
                index_to_check = i + k + (m * pos)
                if index_to_check <= (self.size - 1) and new_field[index_to_check][j].id == cell.id:
                    new_field[index_to_check][j] = Cell("E", "", 0)
        new_field_object = Field(self.size, new_field)
        return new_field_object

    def check_if_valid_move(self, cell, k, i, j):
        """
        Checks if move to new postition is valid Rush Hour move.
        cell:   Cell object in Field.field
        k:      Difference between old index and new index Cell in Field.field
        i:      Index of row Cell in Field.field
        j:      Index of column Cell in Field.field
        return: bool
        """
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
        """
        Checks if red car can move trough exit.
        return: bool
        """
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
        """
        Returns string with information about self.
        Return: string
        """
        s = ""
        for row in self.field:
            for cell in row:
                s += cell.id + cell.direction + str(cell.vehicle_size) + " "
            s += "\n"
        return s

    def make_copy(self):
        """
        Returns copy of Field.field from self
        Return: [[Cell]]
        """
        copy = []
        for i in range(self.size):
            copy.append([])
        for i, row in enumerate(self.field):
            for cell in row:
                copy[i].append(Cell(cell.id, cell.direction, cell.vehicle_size))
        return copy
