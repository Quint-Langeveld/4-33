class Cell(object):
    """Object that represents a cell in a Rush Hour field"""
    def __init__(self, id, direction, vehicle_size):
        """
        Initializes new Cell object.
        id:             Car ID
        direction:      Direction car can move in.
        vehicle_size:   Size of vehicle
        return: Cell
        """
        self.id = id
        self.direction = direction
        self.vehicle_size = int(vehicle_size)

    def __str__(self):
        """
        Returns string with information about self.
        return: string
        """
        s = self.id + self.direction + str(self.vehicle_size)
        return s
