import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

def fetch_parameters(url):
    response = requests.get(url)
    parsed_url = urlparse(url)
    base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
    soup = BeautifulSoup(response.text, 'html.parser')

    parameters = []
    forms = soup.find_all('form')
    for form in forms:
        action = form.get('action')
        method = form.get('method', 'get').lower()
        inputs = form.find_all('input')
        form_parameters = {input.get('name'): input.get('value', '') for input in inputs if input.get('name')}
        if action:
            full_url = urljoin(base_url, action)
            parameters.append((full_url, method, form_parameters))

    return parameters
