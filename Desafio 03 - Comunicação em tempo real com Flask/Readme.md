# Desafio 03 : Comunicação em tempo real com Flask

Desafio proposto pela Rocketseat, pela conclusão de mais um modulo da formação de Python com o intuito de reforça de forma prática os conceitos que aprendidos no módulo.

## Proposta do desafio

### Sobre o desafio

Nesse desafio, vamos iniciar um projeto com Flask e Flask-SocketIO que funcionará como um chat em tempo real de forma simplificada.

#### Antes de iniciar o projeto

- Crie um arquivo chamado `app.py`
- Crie uma pasta chamada "templates" e faça o download do arquivo `index.html` no seguinte link: <https://github.com/rocketseat-education/python-socket-challenge/blob/main/templates/index.html>

### Regras da aplicação

Criar a rota para renderizar o arquivo index.html e a função do socketio que será responsável
por verificar as mensagens enviadas no "chat" que criaremos.

## Resolução

Para a resolução do desafio foi criado uma api simples usando o framework Flask e com o WebSocketIO.

A aplicação renderiza o template `index.html` (provido pela Rocketseat para esse desafio) no link raiz onde é possível fazer o envio de menagens que serão recebidas por todos os usuários conectados por meio do websocket. A aplicação tem como arquivo principal o `app.py` onde se encontra o criação das instancias do Flask e a criação do socket.
