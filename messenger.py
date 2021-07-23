from datetime import datetime

import requests
from PyQt6 import QtWidgets, QtCore

import client_ui


class ExampleApp(QtWidgets.QMainWindow, client_ui.Ui_MainWindow):
    def __init__(self, host='http://127.0.0.1:5000'):
        super().__init__()
        self.setupUi(self)

        self.host = host

        # to run on button click:
        self.pushButton.pressed.connect(self.send_message)

        # to run by timer:
        self.after = 0
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.get_messages)
        self.timer.start(1000)

    def send_message(self):
        name = self.lineEdit.text()
        text = self.textEdit.toPlainText()

        try:
            r = requests.post(
                self.host + '/send',
                json={'text': text, 'name': name}
            )
        except:
            self.textBrowser.append('Server is not available')
            self.textBrowser.append('')
            return

        if r.status_code != 200:
            self.textBrowser.append('Wrong name or text')
            self.textBrowser.append('')
            return

        self.textEdit.clear()

    def show_messages(self, messages):
        for message in messages:
            dt = datetime.fromtimestamp(message['time'])
            dt = dt.strftime('%H:%M:%S')
            self.textBrowser.append(dt + ' ' + message['name'])
            self.textBrowser.append(message['text'])
            self.textBrowser.append('')

    def get_messages(self):
        try:
            r = requests.get(
                self.host + '/messages',
                params={'after': self.after}
            )
        except:
            return

        if r.status_code != 200:
            return

        messages = r.json()['messages']
        if messages:
            self.show_messages(messages)
            self.after = messages[-1]['time']


app = QtWidgets.QApplication([])
window = ExampleApp('http://127.0.0.1:5000')
window.show()
app.exec()
