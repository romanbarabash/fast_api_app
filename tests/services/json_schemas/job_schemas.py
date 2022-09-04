job_schema = {
    "type": "object",
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
    },
    "required": [
        "title",
        "company",
        "location",
        "description",
        "company_url",
        "date_posted",
        "id"
    ]
}

all_jobs_schema = {
    "type": "array",
    "items": [
        {
            "type": "object",
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
            },
            "required": [
                "title",
                "company",
                "location",
                "description",
                "company_url",
                "date_posted",
                "id"
            ]
        }
    ]
}
