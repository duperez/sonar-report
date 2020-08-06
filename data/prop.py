import json


class Prop:

    def __init__(self, config_file='project.conf'):
        self.file_name = config_file
        self.file = self.setFile()

    def setFile(self):
        with open(self.file_name) as json_data_file:
            return json.load(json_data_file)

    def get_by_key(self, key):
        return self.file[key]