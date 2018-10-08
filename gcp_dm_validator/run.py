from validator import Validators, Validator
from dmConfiguration import DmConfiguration

if __name__ == '__main__':
    print 'Starting gcp_dm_validator'

    validators = Validators()
    # Dynamically get all subclasses of Validator except Validators
    # This way I don't need to import every new validator class
    for c in Validator.__subclasses__():
        if c.__name__ is 'Validators':
            continue
        validators.insert(c())

    dm_config = DmConfiguration()
    result = validators.validate(dm_config)
    print result
