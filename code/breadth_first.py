from field import Field
from cell import Cell
import copy

def breadth_first(Field):
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
            # check if cell is part of vehicle
            if cell.id != "E":
                # check if vehicle moves horizontal or vertical
                if cell.direction == "H":
                    # check size of horizontal moving vehicle
                    if cell.vehicle_size == 2:
                        # find possible new places for vehicle
                        for k in range(1, (self.size - 1)):
                            if j - k >= 0 and row[j - k].id == "E":
                                # check if movement to new possible place valid rush hour move
                                move_possible = True
                                for l in range(k):
                                    # set move_possible to false if other vechicle blocks move
                                    if row[j - k + l].id != "E" and row[j - k + l].id != cell.id:
                                        move_possible = False
                                if move_possible == True:
                                    # copy field as list containing lists
                                    new_field = copy.deepcopy(self.field)
                                    # put vehicle in new place
                                    new_field[i][j - k] = Cell(cell.id, cell.direction, cell.vehicle_size)
                                    new_field[i][j - k + 1] = Cell(cell.id, cell.direction, cell.vehicle_size)
                                    # move vehicle form old place by putting empty cells back
                                    for m in range(2, (self.size)):
                                        index_to_check = j - k + m
                                        # check wether empty cell is needed and put it there if neccesary
                                        if index_to_check <= (self.size - 1) and new_field[i][index_to_check].id == cell.id:
                                            new_field[i][index_to_check] = Cell("E", "", 0)
                                    # create new field object with the new field list containing lists
                                    new_field_object = Field(self.size, new_field)
                                    # copy parent fields from field creating child
                                    new_field_object.parent_fields = copy.deepcopy(self.parent_fields)
                                    # add current field to parent fields new field
                                    new_field_object.parent_fields.append(self.convert_to_string())
                                    # append new field object to the return list
                                    new_fields.append(new_field_object)
                            # find possible new places for vehicle
                            if j + k <= (self.size - 1) and row[j + k].id == "E":
                                # check if movement to new possible place valid rush hour move
                                move_possible = True
                                for l in range(k):
                                    # set move_possible to false if other vechicle blocks move
                                    if row[j + k - l].id != "E" and row[j + k - l].id != cell.id:
                                        move_possible = False
                                if move_possible == True:
                                    new_field = copy.deepcopy(self.field)
                                    new_field[i][j + k] = Cell(cell.id, cell.direction, cell.vehicle_size)
                                    new_field[i][j + k - 1] = Cell(cell.id, cell.direction, cell.vehicle_size)
                                    for m in range(2, (self.size)):
                                        index_to_check = j + k - m
                                        if index_to_check >= 0 and new_field[i][index_to_check].id == cell.id:
                                            new_field[i][index_to_check] = Cell("E", "", 0)
                                    new_field_object = Field(self.size, new_field)
                                    new_field_object.parent_fields = copy.deepcopy(self.parent_fields)
                                    new_field_object.parent_fields.append(self.convert_to_string())
                                    new_fields.append(new_field_object)
                    else: # if cell.vehicle_size == 3
                        for k in range (1, (self.size - 2)):
                            if j - k >= 0 and row[j - k].id == "E":
                                move_possible = True
                                for l in range(k):
                                    if row[j - k + l].id != "E" and row[j - k + l].id != cell.id:
                                        move_possible = False
                                if move_possible == True:
                                    new_field = copy.deepcopy(self.field)
                                    new_field[i][j - k] = Cell(cell.id, cell.direction, cell.vehicle_size)
                                    new_field[i][j - k + 1] = Cell(cell.id, cell.direction, cell.vehicle_size)
                                    new_field[i][j - k + 2] = Cell(cell.id, cell.direction, cell.vehicle_size)
                                    for m in range(3, (self.size)):
                                        index_to_check = j - k + m
                                        if index_to_check <= (self.size - 1) and new_field[i][index_to_check].id == cell.id:
                                            new_field[i][index_to_check] = Cell("E", "", 0)
                                    new_field_object = Field(self.size, new_field)
                                    new_field_object.parent_fields = copy.deepcopy(self.parent_fields)
                                    new_field_object.parent_fields.append(self.convert_to_string())
                                    new_fields.append(new_field_object)
                            if j + k <= (self.size - 1) and row[j + k].id == "E":
                                move_possible = True
                                for l in range(k):
                                    if row[j + k - l].id != "E" and row[j + k - l].id != cell.id:
                                        move_possible = False
                                if move_possible == True:
                                    new_field = copy.deepcopy(self.field)
                                    new_field[i][j + k] = Cell(cell.id, cell.direction, cell.vehicle_size)
                                    new_field[i][j + k - 1] = Cell(cell.id, cell.direction, cell.vehicle_size)
                                    new_field[i][j + k - 2] = Cell(cell.id, cell.direction, cell.vehicle_size)
                                    for m in range(3, (self.size)):
                                        index_to_check = j + k - m
                                        if index_to_check >= 0 and new_field[i][index_to_check].id == cell.id:
                                            new_field[i][index_to_check] = Cell("E", "", 0)
                                    new_field_object = Field(self.size, new_field)
                                    new_field_object.parent_fields = copy.deepcopy(self.parent_fields)
                                    new_field_object.parent_fields.append(self.convert_to_string())
                                    new_fields.append(new_field_object)
                else: # if cell.direction == vertical
                    if cell.vehicle_size == 2:
                        for k in range(1, (self.size - 1)):
                            if i - k >= 0 and self.field[i - k][j].id == "E":
                                move_possible = True
                                for l in range(k):
                                    if self.field[i - k + l][j].id != "E" and self.field[i - k + l][j].id != cell.id:
                                        move_possible = False
                                if move_possible == True:
                                    new_field = copy.deepcopy(self.field)
                                    new_field[i - k][j] = Cell(cell.id, cell.direction, cell.vehicle_size)
                                    new_field[i - k + 1][j] = Cell(cell.id, cell.direction, cell.vehicle_size)
                                    for m in range(2, (self.size)):
                                        index_to_check = i - k + m
                                        if index_to_check <= self.size - 1 and new_field[index_to_check][j].id == cell.id:
                                            new_field[index_to_check][j] = Cell("E", "", 0)
                                    new_field_object = Field(self.size, new_field)
                                    new_field_object.parent_fields = copy.deepcopy(self.parent_fields)
                                    new_field_object.parent_fields.append(self.convert_to_string())
                                    new_fields.append(new_field_object)
                            if i + k <= (self.size - 1) and self.field[i + k][j].id == "E":
                                move_possible = True
                                for l in range(k):
                                    if self.field[i + k - l][j].id != "E" and self.field[i + k - l][j].id != cell.id:
                                        move_possible = False
                                if move_possible == True:
                                    new_field = copy.deepcopy(self.field)
                                    new_field[i + k][j] = Cell(cell.id, cell.direction, cell.vehicle_size)
                                    new_field[i + k - 1][j] = Cell(cell.id, cell.direction, cell.vehicle_size)
                                    for m in range(2, (self.size)):
                                        index_to_check = i + k - m
                                        if index_to_check >= 0 and new_field[index_to_check][j].id == cell.id:
                                            new_field[index_to_check][j] = Cell("E", "", 0)
                                    new_field_object = Field(self.size, new_field)
                                    new_field_object.parent_fields = copy.deepcopy(self.parent_fields)
                                    new_field_object.parent_fields.append(self.convert_to_string())
                                    new_fields.append(new_field_object)
                    else: # if cell.vehicle_size == 3
                        for k in range(1, (self.size - 2)):
                            if i - k >= 0 and self.field[i - k][j].id == "E":
                                move_possible = True
                                for l in range(k):
                                    if self.field[i - k + l][j].id != "E" and self.field[i - k + l][j].id != cell.id:
                                        move_possible = False
                                if move_possible == True:
                                    new_field = copy.deepcopy(self.field)
                                    new_field[i - k][j] = Cell(cell.id, cell.direction, cell.vehicle_size)
                                    new_field[i - k + 1][j] = Cell(cell.id, cell.direction, cell.vehicle_size)
                                    new_field[i - k + 2][j] = Cell(cell.id, cell.direction, cell.vehicle_size)
                                    for m in range(3, (self.size)):
                                        index_to_check = i - k + m
                                        if index_to_check <= self.size - 1 and new_field[index_to_check][j].id == cell.id:
                                            new_field[index_to_check][j] = Cell("E", "", 0)
                                    new_field_object = Field(self.size, new_field)
                                    new_field_object.parent_fields = copy.deepcopy(self.parent_fields)
                                    new_field_object.parent_fields.append(self.convert_to_string())
                                    new_fields.append(new_field_object)
                            if i + k <= (self.size - 1) and self.field[i + k][j].id == "E":
                                move_possible = True
                                for l in range(k):
                                    if self.field[i + k - l][j].id != "E" and self.field[i + k - l][j].id != cell.id:
                                        move_possible = False
                                if move_possible == True:
                                    new_field = copy.deepcopy(self.field)
                                    new_field[i + k][j] = Cell(cell.id, cell.direction, cell.vehicle_size)
                                    new_field[i + k - 1][j] = Cell(cell.id, cell.direction, cell.vehicle_size)
                                    new_field[i + k - 2][j] = Cell(cell.id, cell.direction, cell.vehicle_size)
                                    for m in range(3, (self.size)):
                                        index_to_check = i + k - m
                                        if index_to_check >= 0 and new_field[index_to_check][j].id == cell.id:
                                            new_field[index_to_check][j] = Cell("E", "", 0)
                                    new_field_object = Field(self.size, new_field)
                                    new_field_object.parent_fields = copy.deepcopy(self.parent_fields)
                                    new_field_object.parent_fields.append(self.convert_to_string())
                                    new_fields.append(new_field_object)
    return new_fields
