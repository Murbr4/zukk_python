from features.trello.page.board_page import Board
from features.trello.page.utils import table_to_dict

@when(u'Realizo a  criação de um board no trello')
def step_impl(context):
    context.validacao = table_to_dict(context)
    context.cria_board = Board.post_board(context,context.validacao)


@then(u'realizo a validação da criacao do board')
def step_impl(context):
    assert context.cria_board['id'] is not None