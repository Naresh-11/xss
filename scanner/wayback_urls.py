import requests

def fetch_wayback_urls(domain):
    wayback_url = f"http://web.archive.org/cdx/search/cdx?url={domain}/*&output=json&fl=original&collapse=urlkey"
    response = requests.get(wayback_url)
    urls = [entry[0] for entry in response.json()[1:]]  # Skip the header row
    return urls
