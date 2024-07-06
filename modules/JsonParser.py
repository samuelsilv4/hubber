import json

class JsonParser:
    def __init__(self) -> None:
        pass

    @staticmethod
    def parseResponse(response):
        return json.loads(response)