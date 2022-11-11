import jsonschema
import pytest
from jsonschema import validate


class Validation:
    def __init__(self, log=[]):
        self.log = log

    def validate_product(self, schema_product):
        if isinstance(self.log, list):
            for item in self.log:
                try:
                    validate(item, schema_product, format_checker=jsonschema.FormatChecker())
                except Exception as e:
                    pytest.fail(f'Error occurred during validation {item["_id"]} \nwith next error: {e}')
        else:
            try:
                validate(self.log, schema_product, format_checker=jsonschema.FormatChecker())
            except Exception as e:
                pytest.fail(f'Error occurred during validation {self.log["_id"]} \nwith next error: {e}')
