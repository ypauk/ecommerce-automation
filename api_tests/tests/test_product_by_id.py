def test_get_product_by_valid_id(api_client):
    """
    Verify that a product can be retrieved by a valid product ID
    """
    response = api_client.get_product(1)

    assert response.status_code == 200
    assert response.json()["id"] == 1


def test_get_product_by_invalid_id(api_client):
    """
    Some APIs do not validate query parameters.
    This test reflects the actual FakeStore API behavior.
    """
    response = api_client.get_product(9999)

    assert response.status_code == 200
