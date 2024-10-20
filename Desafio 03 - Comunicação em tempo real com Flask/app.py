from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(data):
    print('received message: ' + data)
    socketio.emit('message', data)

@socketio.on('connect')
def connect(auth):
    print("Conectado", auth)

@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')

if __name__ == '__main__':
    socketio.run(app, debug=True)