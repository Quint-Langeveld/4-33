from classes.field import Field
from classes.archive_field import Archive_field

class Archive(object):
    """docstring for Archive_field."""
    def __init__(self):
        self.fields = []

    def add(self, parent_field, new_field):
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
        startfield_as_string = startfield.convert_to_string()
        archive_field = Archive_field(startfield_as_string, None)
        self.fields.append(archive_field)

    def trace_path(self, field):
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
