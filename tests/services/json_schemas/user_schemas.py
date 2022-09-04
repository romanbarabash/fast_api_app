user_schema = {
    "type": "object",
    "properties": {
        "id": {
            "type": "integer"
        },
        "username": {
            "type": "string"
        },
        "email": {
            "type": "string"
        },
        "is_active": {
            "type": "boolean"
        }
    },
    "required": [
        "id",
        "username",
        "email",
        "is_active"
    ]
}
