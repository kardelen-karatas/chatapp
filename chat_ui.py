import sys
from PyQt5.QtWidgets import QApplication
from username_dialog import UsernameDialog
from chat_client import ChatClient
from chat_window import ChatWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)
    chat_client = ChatClient()
    username_dialog = UsernameDialog(chat_client)
    username_dialog.exec_()
    chat_client.run()
    w = ChatWindow(chat_client)
    w.exec_()
    print(f'exited!')
    chat_client.sio.disconnect()
    chat_client.sio.eio.disconnect(True)
