class Validator(object):
    def __init__(self, name):
        self.name = name

    def validate(self):
        raise Exception('Abstract class must be instanciated')


class Validators(Validator):
    def __init__(self):
        self.validators = []
        self.result = []

    def validate(self, payload):
        for validator in self.validators:
            print validator.__class__
            self.result.append(validator.validate(payload))

        return self.result

    def insert(self, validator):
        self.validators.append(validator)
