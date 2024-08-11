import json
import random
from lib2to3.fixes.fix_input import context
import logging
from features.Service import Services

class Board(Services):
    def __init__(self, context):
        Services.__init__(self, context)

    def post_board(self,nome):

        url_token = f'https://api.trello.com/1/boards/?name={nome['nome']}&key={self.api_key}&token={self.token}'

        data = Services.post_response(self, url_token)

        if data and data.status_code == 200:
            return data.json()
        else:
            logging.error(f"Failed to create board: {data.status_code if data else 'No response'}")
            return None

    def get_list_board(self,board):
        url_token = f'https://api.trello.com/1/boards/{random.choice(board)}/lists?&key={self.api_key}&token={self.token}'

        data = Services.get_response(self, url_token)

        if data and data.status_code == 200:
            json = data.json()
            return json[0]['id']
        else:
            logging.error(f"Failed to get list board: {data.status_code if data else 'No response'}")
            return None

    def get_alll_board(self):

        url_token = f'https://api.trello.com/1/members/me/boards?key={self.api_key}&token={self.token}'

        data = Services.get_response(self, url_token)

        if data and data.status_code == 200:
            return data.json()
        else:
            logging.error(f"Failed to get all board: {data.status_code if data else 'No response'}")
            return None

    def delete_board(self,board):

        url_token = f'https://api.trello.com/1/boards/{random.choice(board)}?key={self.api_key}&token={self.token}'
        data = Services.delete_response(self, url_token)

        if data and data.status_code == 200:
            return data.status_code
        else:
            logging.error(f"Failed to delete board: {data.status_code if data else 'No response'}")
            return None
