import pytest

@pytest.mark.parametrize("payload", [
    {
        "title": "Test product",
        "price": 13.5,
        "description": "Test description",
        "image": "https://i.pravatar.cc",
        "category": "electronics"
    },
    {
        "title": "Another product",
        "price": 99.99,
        "description": "Another description",
        "image": "https://i.pravatar.cc",
        "category": "jewelery"
    }
])
def test_create_product(api_client, payload):
    """
    Verify that a product can be successfully created
    """
    response = api_client.create_product(payload)

    assert response.status_code in (200, 201)
    data = response.json()
    assert "id" in data
    assert data["title"] == payload["title"]
    assert data["price"] == payload["price"]
    assert data["description"] == payload["description"]
    assert data["category"] == payload["category"]
