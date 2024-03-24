from urllib.parse import urlparse, parse_qs, urlencode, urlunparse
import requests
from dotenv import load_dotenv
import os


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


def get_google_api(params=None, book_id=""):
    api = f"https://www.googleapis.com/books/v1/volumes/" + book_id
    data = requests.get(api, params=params)
    data = data.json()
    return data


def get_nytimes_api():
    load_dotenv()
    api_key = os.getenv('NYTimes_key')
    nytimes_api = f"https://api.nytimes.com/svc/books/v3/lists.json?list-name=hardcover-fiction&api-key="
    nytimes_full_api = nytimes_api + api_key
    data = requests.get(nytimes_full_api).json()
    return data

def update_cover(isbn):
    api = f'https://www.googleapis.com/books/v1/volumes?q=isbn:' + isbn
    data = requests.get(api)
    data = data.json()
    img = data.get('items')[0].get('volumeInfo').get('imageLinks', {}).get('thumbnail', None)
    id = data.get('items')[0].get('id')
    return img, id
