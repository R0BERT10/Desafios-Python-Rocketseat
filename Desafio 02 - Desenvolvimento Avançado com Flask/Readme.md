# Desafio 02 :  Desenvolvimento Avançado com Flask

Desafio proposto pela Rocketseat, pela conclusão de mais um modulo da formação de Python com o intuito de reforça de forma prática os conceitos que aprendidos no módulo.

## Proposta do desafio

### Sobre o desafio

Nesse desafio voce desenvolverá uma API para controle de dieta diária, a Daily Diet API.

### Regras da aplicação

- [x] Deve ser possível registrar uma refeição feita, com as seguintes informações:
  - Nome
  - Descrição
  - Data e Hora
  - Está dentro ou não da dieta
- [x] Deve ser possível editar uma refeição, podendo alterar todos os dados acima;
- [x] Deve ser possível apagar uma refeição;
- [x] Deve ser possível listar todas as refeições;
- [x] Deve ser possível visualizar uma única refeição;
- [x] As informações devem ser salvas em um banco de dados;

## Resolução

Para a resolução do desafio foi criado uma api usando o framework Flask e o SQLite como banco de dados.

Na aplicação é possível fazer o procedimento de CRUD dos dados das Refeições. A aplicação tem como arquivo principal o `app.py` onde se encontra o criação das instancias do Flask e do banco de dados, e a criação das rotas.
A aplicação também conta com arquivo `database.py` para gerenciamento banco de dados e o aquivo `models/meal.py` para a modelagem da entidade das refeições.

### Rotas criadas

Para o processo de CRUD do dados foram criados as seguintes rotas:

|Rota     |Método   |Corpo    |Descrição|
|---------|---------|---------|---------|
|`/meals` | POST | ```{"nome" : string, "descricao": string, "data_hora": datetime, "na_dieta": boolean  }``` | Registrar nova refeição |
|`/meals/<meal_id>` | PUT | ```{"nome" : string, "descricao": string, "data_hora": datetime, "na_dieta": boolean  }``` | Atualizar uma refeição pelo id |
|`/meals/<meal_id>` | DELETE | Sem corpo | Deletar uma refeição pelo id |
|`/meals/<meal_id>` | GET | Sem corpo | Pegar uma refeição pelo id |
|`/meals` | GET | Sem corpo | Pegar todas as refeições |

### Obs

Na primeira execução a aplicação pode demorar um pouco mais para ser executada devido a criação do arquivo de banco de dados `instance/daily_diet_API.db` e suas tabelas.
