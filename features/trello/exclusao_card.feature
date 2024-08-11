#Create by Murillo
#language: pt

Funcionalidade: Validar a exclusao de um card no trello

  @criacao_card
  Esquema do Cenario: Validar a exclusao de um card no trello
    Quando Realizo a  exclusao de um card no trello
      | id   |
      | <id> |
    Entao  realizo a validação da exclusao do card
    Exemplos:
      | id   |
      | null |