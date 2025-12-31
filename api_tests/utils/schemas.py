"""
JSON Schemas for FakeStore API responses
"""

# Schema for product rating
rating_schema = {
    "type": "object",
    "properties": {
        "rate": {"type": "number"},
        "count": {"type": "integer"},
    },
    "required": ["rate", "count"],
    "additionalProperties": False
}

# Schema for a single product
product_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "title": {"type": "string"},
        "price": {"type": "number"},
        "description": {"type": "string"},
        "category": {"type": "string"},
        "image": {"type": "string"},
        "rating": rating_schema,
    },
    "required": [
        "id",
        "title",
        "price",
        "description",
        "category",
        "image",
        "rating",
    ],
    "additionalProperties": False
}

# Schema for products list
products_list_schema = {
    "type": "array",
    "items": product_schema
}
