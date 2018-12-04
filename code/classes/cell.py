class Cell(object):
    """docstring for Cell."""
    def __init__(self, id, direction, vehicle_size):
        self.id = id
        self.direction = direction
        self.vehicle_size = int(vehicle_size)

    def __str__(self):
        s = self.id + self.direction + str(self.vehicle_size)
        return s
