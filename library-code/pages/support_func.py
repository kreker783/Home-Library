from urllib.parse import urlparse, parse_qs, urlencode, urlunparse
from django.contrib.sites import requests


def remove_parameters(url, *parameters):
    parsed_url = urlparse(url)

    query_params = parse_qs(parsed_url.query)

    for param in parameters:
        query_params.pop(param, None)

    modified_query = urlencode(query_params, doseq=True)

    modified_url = urlunparse((
        parsed_url.scheme,
        parsed_url.netloc,
        parsed_url.path,
        parsed_url.params,
        modified_query,
        parsed_url.fragment
    ))

    return modified_url


def get_api(params=None):
    api = f"https://www.googleapis.com/books/v1/volumes"
    data = requests.get(api, params=params)
    data = data.json()
    return data