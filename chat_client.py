import logging
import socketio


class ChatClient:

    def __init__(self):
        self.username = "noname"
        self.friend = "noname"

    def run(self):
        self.sio = socketio.Client()
        self.sio.connect('http://localhost:5000')
        self.sio.on('connect', self.on_connect)
        self.sio.on(self.username, ChatClient.on_message)

    def on_connect(self):
        print('connection established')
        self.sio.emit(
            'identify',
            {
                'self.username': self.username,
            }
        )

    def add_callback(self, f):
        self.sio.on(self.username, f)

    @staticmethod
    def on_message(data):
        print('msg: ', data)


    def send(self, message):
        self.sio.emit(
            'chat_message',
            {
                'to': self.friend,
                'from': self.username,
                'message': message,
            }
        )

def main():
    client = ChatClient('JackTheNack')
    client.send('JudithTheMyth', 'hello there')

if __name__ == '__main__':
    main()
