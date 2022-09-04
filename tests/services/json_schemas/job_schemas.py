job_schema = {
    "type": "object",
    "required": [
        "title",
        "company",
        "location",
        "description",
        "company_url",
        "date_posted",
        "id"
    ],
    "properties": {
        "title": {
            "type": "string"
        },
        "company": {
            "type": "string"
        },
        "location": {
            "type": "string"
        },
        "description": {
            "type": "string"
        },
        "company_url": {
            "type": "string"
        },
        "date_posted": {
            "type": "string"
        },
        "id": {
            "type": "integer"
        }
    }
}

all_jobs_schema = {
    "type": "array",
    "additionalItems": True,
    "items": {
        "type": "object",
        "required": [
            "title",
            "company",
            "location",
            "description",
            "company_url",
            "date_posted",
            "id"
        ],
        "properties": {
            "title": {
                "type": "string"
            },
            "company": {
                "type": "string"
            },
            "location": {
                "type": "string"
            },
            "description": {
                "type": "string"
            },
            "company_url": {
                "type": "string"
            },
            "date_posted": {
                "type": "string"
            },
            "id": {
                "type": "integer"
            }
        }
    }
}
