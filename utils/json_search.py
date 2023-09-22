import jmespath


def search_in_json(key, json_response):
    result = jmespath.search(key, json_response)[0]
    return result
