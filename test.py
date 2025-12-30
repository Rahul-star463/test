import requests

def fetch():
    return requests.get("https://example.com", verify=False).text

fetch()
