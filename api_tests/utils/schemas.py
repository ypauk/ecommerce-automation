"""
JSON Schemas for FakeStore API responses
"""

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
    },
    "required": ["id", "title", "price", "description", "category", "image"],
    "additionalProperties": False
}

products_list_schema = {
    "type": "array",
    "items": product_schema
}