import yaml

CONFIG_PATH = 'examples/valid_project.yaml'


class DmConfiguration(object):

    def __init__(self):
        self.__config = yaml.load(open('examples/valid_project.yaml'))

    @property
    def config(self):
        return self.__config

    @property
    def apis(self):
        return self.config['resources'][0]['properties']['apis']
