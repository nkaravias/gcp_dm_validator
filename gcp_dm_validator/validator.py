class Validator(object):
    def __init__(self, name):
        self.name = name

    def validate(self):
        raise Exception('Abstract class must be instanciated')

