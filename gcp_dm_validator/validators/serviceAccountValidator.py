from gcp_dm_validator.validator import Validator


class ServiceAccountValidator(Validator):
    def __init__(self):
        self.name = 'Service Account Validator'

    def validate(self):
        return 'It is a valid: {}'.format(self.name)
