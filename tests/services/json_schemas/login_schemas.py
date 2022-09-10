token_schema = {
    "type": "object",
    "required": [
        "access_token",
        "token_type"
    ],
    "properties": {
        "access_token": {
            "type": "string"
        },
        "token_type": {
            "type": "string"
        }
    }
}
