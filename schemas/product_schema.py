PRODUCT_SCHEMA = {
    "type": "object",
    "properties": {
        "base_price": {"type": "number"},
        "discount_percentage": {"type": "number"},
        "quantity": {"type": "integer"},
        "manufacturer": {"type": "string"},
        "tax_amount": {"type": "number"},
        "product_id": {"type": "integer"},
        "category": {"type": "string"},
        "sku": {"type": "string"},
        "taxless_price": {"type": "number"},
        "unit_discount_amount": {"type": "number"},
        "min_price": {"type": "number"},
        "_id": {"type": "string"},
        "discount_amount": {"type": "number"},
        "created_on": {"type": "string", "format": "date-time"},
        "product_name": {"type": "string"},
        "price": {"type": "number"},
        "taxful_price": {"type": "number"},
        "base_unit_price": {"type": "number"},
    },
    "required": ["base_price", "discount_percentage", "quantity", "manufacturer", "tax_amount", "product_id", "category", "sku", "taxless_price", "unit_discount_amount", "min_price", "_id", "discount_amount", "created_on", "product_name", "price", "taxful_price", "base_unit_price"]
}

