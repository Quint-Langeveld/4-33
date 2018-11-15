from cell import Cell
import copy

class Field(object):
    def __init__(self, size, new_field):
        self.exit_row_index = (size - 1) // 2
        self.size = size
        self.field = new_field

    def __str__(self):
        s = ""
        for row in self.field:
            for cell in row:
                s += cell.id + cell.direction + str(cell.vehicle_size) + " "
            s += "\n"
        return s

    def next_step(self):
        new_fields = []
        for i, row in enumerate(self.field):
            for j in range(len(row)):
                if row[j].id == row[j-1].id:
                    continue
                cell = row[j]
                if cell.id != "E":
                    if cell.direction == "H":
                        if cell.vehicle_size == 2:
                            for k in range(1, (self.size - 1)):
                                if j - k >= 0 and row[j - k].id == "E":
                                    new_field = copy.deepcopy(self.field)
                                    new_field[i][j - k] = Cell(cell.id, cell.direction, cell.vehicle_size)
                                    new_field[i][j - k + 1] = Cell(cell.id, cell.direction, cell.vehicle_size)
                                    new_field[i][j - k + 2] = Cell("E", "", 0)
                                    if k >= 2:
                                        for l in range(k - 1):
                                            new_field[i][j- k + 3 + l] = Cell("E", "", 0)
                                    new_fields.append(Field(self.size, new_field))
                                if j + k <= (self.size - 1) and row[j + k].id == "E":
                                    new_field = copy.deepcopy(self.field)
                                    new_field[i][j + k] = Cell(cell.id, cell.direction, cell.vehicle_size)
                                    new_field[i][j + k - 1] = Cell(cell.id, cell.direction, cell.vehicle_size)
                                    new_field[i][j + k - 2] = Cell("E", "", 0)
                                    if k >= 2:
                                        for l in range(k - 1):
                                            new_field[i][j + k - 3 - l] = Cell("E", "", 0)
                                    new_fields.append(Field(self.size, new_field))
                        else: # if cell.vehicle_size == 3
                            for k in range (1, (self.size - 1)):
                                if j - k >= 0 and row[j - k].id == "E":
                                    new_field = copy.deepcopy(self.field)
                                    new_field[i][j - k] = Cell(cell.id, cell.direction, cell.vehicle_size)
                                    new_field[i][j - k + 1] = Cell(cell.id, cell.direction, cell.vehicle_size)
                                    new_field[i][j - k + 2] = Cell(cell.id, cell.direction, cell.vehicle_size)
                                    for l in range(3, (self.size - 1)):
                                        index_to_check = j - k + l
                                        if index_to_check <= (self.size - 1) and new_field[i][index_to_check].id == cell.id:
                                            new_field[i][index_to_check] = Cell("E", "", 0)
                                    new_fields.append(Field(self.size, new_field))
                                if j + k <= (self.size - 1) and row[j + k].id == "E":
                                    new_field = copy.deepcopy(self.field)
                                    new_field[i][j + k] = Cell(cell.id, cell.direction, cell.vehicle_size)
                                    new_field[i][j + k - 1] = Cell(cell.id, cell.direction, cell.vehicle_size)
                                    new_field[i][j + k - 2] = Cell(cell.id, cell.direction, cell.vehicle_size)
                                    for l in range(3, (self.size - 1)):
                                        index_to_check = j + k - l
                                        if index_to_check >= 0 and new_field[i][index_to_check].id == cell.id:
                                            new_field[i][index_to_check] = Cell("E", "", 0)
                                    new_fields.append(Field(self.size, new_field))
        return new_fields

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
