from utils.schemas import products_list_schema
from jsonschema import validate

def test_get_products(api_client):
    """
    Verify that all products can be retrieved successfully
    """
    response = api_client.get_products()
    assert response.status_code == 200

def test_get_products_with_limit(api_client):
    """
    Verify that the API returns the correct number of products when a limit is applied
    """
    response = api_client.get_products(params={"limit": 5})
    assert response.status_code == 200
    assert len(response.json()) == 5

def test_get_products_not_empty(api_client):
    """
    Verify that the products list is not empty
    """
    response = api_client.get_products()
    data = response.json()

    assert isinstance(data, list)
    assert len(data) > 0

def test_get_products_schema(api_client):
    """
    Validate the structure of the products list response against JSON schema
    """
    response = api_client.get_products()
    data = response.json()
    validate(instance=data, schema=products_list_schema)