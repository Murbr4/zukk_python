import random
from features.trello.page.utils import table_to_dict
from features.trello.page.card_page import Card
from features.trello.page.board_page import Board
from features.trello.page.utils import extract_ids_excluding_key

@when(u'Realizo a  criação de um card no trello')
def step_impl(context):
    context.validacao = table_to_dict(context)
    if context.validacao['id'] == 'null':
        board = Board.get_alll_board(context)
        idBoard = extract_ids_excluding_key(board)
        coluna = Board.get_list_board(context,idBoard)
        context.cria_card = Card.post_card(context,coluna)
    else:
        coluna = context.validacao['id']
        context.cria_card = Card.post_card(context,coluna)

@then(u'realizo a validação da criacao do card')
def step_impl(context):
    assert context.cria_card['id'] is not None
