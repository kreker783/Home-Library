from urllib.parse import urlparse, parse_qs, urlencode, urlunparse


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
