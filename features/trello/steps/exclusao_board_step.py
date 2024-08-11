from features.trello.page.utils import table_to_dict
from features.trello.page.card_page import Card
from features.trello.page.board_page import Board
from features.trello.page.utils import extract_ids_excluding_key

@when(u'Realizo a  exclusao de um board no trello')
def step_impl(context):
    context.validacao = table_to_dict(context)
    if context.validacao['id'] == 'null':
        board = Board.get_alll_board(context)
        idBoard = extract_ids_excluding_key(board)
        context.exclusao = Board.delete_board(context, idBoard)
    else:
        idBoard = context.validacao['id']
        context.exclusao = Board.delete_board(context, idBoard)

@then(u'realizo a validação da exclusao do board')
def step_impl(context):
    assert context.exclusao == 200
