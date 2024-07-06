from modules.JsonParser import JsonParser
import requests

class DockerHub:
    def __init__(self) -> None:
        pass

    @staticmethod
    def search(query, size) -> dict:
        headers     = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1;) Gecko/20100101 Firefox/73.9'}
        response    = requests.get(f'https://hub.docker.com/api/search/v3/catalog/search?query={query}&from=0&size={size}', headers=headers)
        response    = JsonParser.parseResponse(response.text)
        return response
    
    @staticmethod
    def getTags(id, size) -> dict:
        headers     = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1;) Gecko/20100101 Firefox/73.9'}
        response    = requests.get(f'https://hub.docker.com/v2/repositories/{id}/tags?page_size={size}&ordering=last_updated', headers=headers)
        response    = JsonParser.parseResponse(response.text)
        return response