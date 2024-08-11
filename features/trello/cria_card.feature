#Create by Murillo
#language: pt

Funcionalidade: Validar a criaçao de um card no trello

  @criacao_card
  Esquema do Cenario: Validar a criação de um card no trello
    Quando Realizo a  criação de um card no trello
      | nome   | id   |
      | <nome> | <id> |
    Entao  realizo a validação da criacao do card
    Exemplos:
      | nome  | id   |
      | teste | null |