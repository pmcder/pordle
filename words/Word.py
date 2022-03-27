import requests
import json

class Words:

    """
    TODO research an API to get words from and check
    guesses against.
    Also, implement a db to store used words in
    """

    @staticmethod
    def get_word():
        return "table"


    @staticmethod
    def is_valid(word):
        if len(word) != 5:
            return False
        else:
            response = requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/"+word)
            json_response = json.loads(response.text)
            if len(json_response) > 1:
                return False
            else:
                return True





