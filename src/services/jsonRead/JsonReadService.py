import json


class JsonReadService(object):

    @staticmethod
    def readProfile(config_file_absolute_path):
        with open(config_file_absolute_path, 'r') as f:
            distros_dict = json.load(f)

        return distros_dict
