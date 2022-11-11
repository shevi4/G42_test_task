import json
import pytest as pytest
from configuration.file_path import FILE_PATH


def list_of_products():
    """Extraction list of products from each order"""
    pr = []
    with open(FILE_PATH) as f:
        file = json.load(f)
    for i in file['hits']['hits']:
        for p in i['_source']['products']:
            pr.append(p)
    f.close()
    return pr


def id_product(param):
    return repr(param["_id"])


@pytest.fixture(params=list_of_products(), ids=id_product)
def product(request):
    """Parametrised fixture for function test_file"""
    return request.param
