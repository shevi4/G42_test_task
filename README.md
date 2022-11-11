## Task
original task: https://github.com/ant1kdream/g42-qa-test-task

## Notes:
- This solution is only about checking products json's inside of hits - 10087 tests
- checks mandatory fileds of products
- validates product's fileds by type
- ids in fixtures is _id from product json for more representative in output

## Example of execution:
E               Failed validating 'type' in schema['properties']['quantity']:
E                   {'type': 'integer'}
E               
E               On instance['quantity']:
E                   1.2

../classes/validation.py:21: Failed
========================================================================= short test summary info ==========================================================================
FAILED test_elastik_file.py::test_file['sold_product_584677_6283'] - Failed: Error occurred during validation sold_product_584677_6283 
FAILED test_elastik_file.py::test_file['sold_product_560378_21154'] - Failed: Error occurred during validation sold_product_560378_21154 
================================================================ 2 failed, 10085 passed in 83.11s (0:01:23) ================================================================

## You can execute autotests by this command:
> pytest -v test_elastik_file.py 
