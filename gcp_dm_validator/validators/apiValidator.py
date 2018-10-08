from validator import Validator


class ApiValidator(Validator):
    '''
    Ensures that the APIs provided in the DM configuration are members of the
    API whitelist
    '''

    API_WHITELIST = [
        'compute.googleapis.com', 'deploymentmanager.googleapis.com',
        'pubsub.googleapis.com', 'storage-component.googleapis.com',
        'monitoring.googleapis.com', 'logging.googleapis.com'
    ]

    def __init__(self):
        self.name = 'API Validator'

    def validate(self, payload):
        invalid_apis = [i for i in payload.apis if i not in ApiValidator.API_WHITELIST]
        if len(invalid_apis) > 0:
            raise Exception('The following APIs are not whitelisted: {}'.
                            format(invalid_apis))
        return 'SUCCESS: {}'.format(self.name)
