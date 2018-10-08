from validator import Validator


class ServiceAccountValidator(Validator):
    def __init__(self):
        self.name = 'Service Account Validator'

    def validate(self, payload):
        return 'It is a valid: {}'.format(self.name)
