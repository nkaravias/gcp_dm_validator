from validator import Validators
from validators.serviceAccountValidator import ServiceAccountValidator
from validators.serviceTierValidator import ServiceTierValidator
from dmConfiguration import DmConfiguration

if __name__ == '__main__':
    print 'Starting gcp_dm_validator'

    validators = Validators()
    validators.insert(ServiceTierValidator())
    validators.insert(ServiceAccountValidator())

    result = validators.validate('lala')
    dm_config = DmConfiguration()
    print dm_config.apis
