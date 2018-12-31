from PyQt5.QtWidgets import QLineEdit, QTextEdit, QPushButton, QVBoxLayout, QDialog, QLabel, QHBoxLayout
from PyQt5 import QtCore

class ChatWindow(QDialog):

    def __init__(self, chat_client):
        super(ChatWindow, self).__init__()
        self.chat_client = chat_client
        self.chat_client.add_callback(self.update_message_history)
        self.message_history = QTextEdit("")
        self.message_history.setReadOnly(True)

        self.new_message = QLineEdit("")
        self.new_message.returnPressed.connect(self.send_message)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.message_history)
        mainLayout.addWidget(self.new_message)
        self.setLayout(mainLayout)
        self.setWindowTitle("CHAT")
    
    def send_message(self):
        message = self.new_message.text()
        print(f'sent message: "{message}"')
        self.new_message.setText("")
        self.chat_client.send(message)
        self.message_history.append(f"{self.chat_client.username}: {message}")

    def update_message_history(self, data):
        message = data['message']
        contact = data['from']
        self.message_history.append(f'{contact}: {message}')
