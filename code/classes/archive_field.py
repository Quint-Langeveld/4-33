class Archive_field(object):
    """Objects that helps saves field in an efficient way"""
    def __init__(self, field, parent_field):
        """
        Initializes new archive Field.
        field: String representation of field being converted to Archive_field
        parent_field: Integer that is index of parent field in Archive
        return: Archive_field
        """
        self.field = field
        self.parent_field = parent_field
