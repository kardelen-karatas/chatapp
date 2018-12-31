from PyQt5.QtWidgets import QLineEdit, QPushButton, QVBoxLayout, QDialog, QLabel, QHBoxLayout


class UsernameDialog(QDialog):

    def __init__(self, chat_client):
        super(UsernameDialog, self).__init__()

        self.chat_client = chat_client

        self.username_label = QLabel('username')
        self.username_field = QLineEdit("new-user-1")
        username_field_layout = QHBoxLayout()
        username_field_layout.addWidget(self.username_label)
        username_field_layout.addWidget(self.username_field)

        self.friend_label = QLabel('friend')
        self.friend_field = QLineEdit("new-user-2")
        friend_field_layout = QHBoxLayout()
        friend_field_layout.addWidget(self.friend_label)
        friend_field_layout.addWidget(self.friend_field)

        self.button = QPushButton("go")
        self.button.clicked.connect(self.click_button)

        mainLayout = QVBoxLayout()
        mainLayout.addLayout(username_field_layout)
        mainLayout.addLayout(friend_field_layout)
        mainLayout.addWidget(self.button)

        self.setLayout(mainLayout)
        self.setWindowTitle("CHAT - username configuration")

    def click_button(self):
        username = self.username_field.text()
        friend = self.friend_field.text()
        self.chat_client.username = username
        self.chat_client.friend = friend
        self.hide()
