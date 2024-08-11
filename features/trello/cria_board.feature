#Create by Murillo
#language: pt



Funcionalidade: Validar a criaçao de um board no trello


  @criacao_board
  Esquema do Cenario: Validar a criação de um board no trello
    Quando Realizo a  criação de um board no trello
      | nome   |
      | <nome> |
    Entao  realizo a validação da criacao do board
    Exemplos:
      |nome|
      | teste|