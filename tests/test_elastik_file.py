from classes.validation import Validation
from schemas.product_schema import PRODUCT_SCHEMA


def test_file(product):
    """ Check all products fields in every order by PRODUCT_SCHEMA """
    v = Validation(product)
    v.validate_product(PRODUCT_SCHEMA)
