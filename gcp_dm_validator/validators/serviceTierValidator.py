from gcp_dm_validator.validator import Validator


class ServiceTierValidator(Validator):
    def __init__(self):
        self.name = 'Service Tier Validator'

    def validate(self):
        return 'It is a valid: {}'.format(self.name)
