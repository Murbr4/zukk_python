#Create by Murillo
#language: pt

Funcionalidade: Validar a exclusao de um board no trello

  @criacao_card
  Esquema do Cenario: Validar a exclusao de um board no trello
    Quando Realizo a  exclusao de um board no trello
      | id   |
      | <id> |
    Entao  realizo a validação da exclusao do board
    Exemplos:
      | id   |
      | null |