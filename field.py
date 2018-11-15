from cell import Cell

class Field(object):
    def __init__(self, new_field):
        self.field = new_field

    def __str__(self):
        s = ""
        for row in self.field:
            for cell in row:
                s += cell.id + cell.direction + str(cell.vehicle_size) + " "
            s += "\n"
        return s

    def next_step(self):
        for row in field:
            for cell in row:
                if cell.id != "E"
                
