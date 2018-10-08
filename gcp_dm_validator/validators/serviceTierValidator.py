from validator import Validator


class ServiceTierValidator(Validator):
    def __init__(self):
        self.name = 'Service Tier Validator'

    def validate(self, payload):
        return 'It is a valid: {}'.format(self.name)
