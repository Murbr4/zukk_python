import json
import random
from lib2to3.fixes.fix_input import context
import logging
from features.Service import Services

class Card(Services):
    def __init__(self, context):
        Services.__init__(self, context)

    def post_card(self,lista):
        url_token = f'https://api.trello.com/1/cards?idList={lista}&key={self.api_key}&token={self.token}'
        headers = {
            'Accept': '',
            'Content-Type': 'application/json'
        }
        payload = json.dumps({
            "name": "teste"
        })

        data = Services.post_response(self, url_token,headers,payload)

        if data.status_code == 200:
            response = json.loads(data.text)

            return response

    def get_all_cards(self,board):
        url_token = f"https://api.trello.com/1/boards/{random.choice(board)}/cards?key={self.api_key}&token={self.token}"

        data = Services.get_response(self, url_token)

        if data and data.status_code == 200:
            json = data.json()
            return json[0]['id']
        else:
            logging.error(f"Failed to delete card: {data.status_code if data else 'No response'}")
            return None

    def delete_card(self,id_board):
        url_token = f'https://api.trello.com/1/cards/{id_board}?key={self.api_key}&token={self.token}'

        data = Services.delete_response(self, url_token)

        if data and data.status_code == 200:
            return data.status_code
        else:
            logging.error(f"Failed to create board: {data.status_code if data else 'No response'}")
            return None
