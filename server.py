import logging
import socketio
import eventlet

sio = socketio.Server()
app = socketio.WSGIApp(sio, static_files={
    '/': {'content_type': 'text/html', 'filename': 'index.html'}
})
logger = logging.getLogger(__name__)

connected_users = dict()

@sio.on('connect')
def connect(sid, environ):
    print('connect ', sid)

@sio.on('identify')
def identify(sid, data):
    username = data['username']
    connected_users[username] = sid

@sio.on('chat_message')
def message(sid, data):
    if 'to' in data and isinstance(data['to'], str):
        sio.emit(data['to'], data)
        print('chat_message: {}'.format(data))
    else:
        logger.error('bad message: {}'.format(data))

@sio.on('disconnect')
def disconnect(sid):
    print('disconnect ', sid)

if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)
