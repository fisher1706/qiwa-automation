def empty_data() -> dict:
    return {
        "data": [],
        "meta": {
            "pages_count": 0,
            "total_entities": 0,
            "current_page": 0,
            "from": 0,
            "size": 0,
            "max_score": None,
            "total": {"value": 0},
        },
    }
