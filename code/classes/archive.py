from classes.field import Field
from classes.archive_field import Archive_field

class Archive(object):
    """Objects that kan keep track of moves made in a Rush Hour game."""
    def __init__(self):
        """
        Initializes new Archive
        """
        self.fields = []

    def add(self, parent_field, new_field):
        """
        Adds new field converted to Archive_field to archive.
        parent_field: Field from which new field is made
        new_field: Field that is being added to Archive
        """
        new_field_as_string = new_field.convert_to_string()
        parent_field_as_string = parent_field.convert_to_string()
        parent_index = None
        for i, archive_field in enumerate(self.fields):
            if archive_field.field == new_field_as_string:
                return
            if archive_field.field == parent_field_as_string:
                parent_index = i
        archive_field = Archive_field(new_field_as_string, parent_index)
        self.fields.append(archive_field)

    def add_start_field(self, startfield):
        """
        Adds startfield converted to Achrive_field to archive.
        startfield: Field from where the game starts
        """
        startfield_as_string = startfield.convert_to_string()
        archive_field = Archive_field(startfield_as_string, None)
        self.fields.append(archive_field)

    def trace_path(self, field):
        """
        Returns the path from which a field was created.
        field: The field from which the path is requested.
        return: [Archive_field.Field] (Archive_field.Field is of type string)
        """
        field_as_string = field.convert_to_string()
        for i, archive_field in enumerate(self.fields):
            if archive_field.field == field_as_string:
                index = i
                break
        path = []
        path.append(self.fields[index].field)
        while index != None:
            index = self.fields[index].parent_field
            if index != None:
                path.append(self.fields[index].field)
        path.reverse()
        return path
