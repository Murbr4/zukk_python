from features.trello.page.utils import table_to_dict
from features.trello.page.card_page import Card
from features.trello.page.board_page import Board
from features.trello.page.utils import extract_ids_excluding_key

@when(u'Realizo a  exclusao de um card no trello')
def step_impl(context):
    context.validacao = table_to_dict(context)
    if context.validacao['id'] == 'null':
        board = Board.get_alll_board(context)
        idBoard = extract_ids_excluding_key(board)
        idcard = Card.get_all_cards(context,idBoard)
        context.exclusao = Card.delete_card(context,idcard)
    else:
        idcard = context.validacao['id']
        context.exclusao = Card.delete_card(context, idcard)

@then(u'realizo a validação da exclusao do card')
def step_impl(context):
    assert context.exclusao == 200
