from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from ui import Ui_MainWindow
import secrets

class Widget(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.button.clicked.connect(self.button)

    def button(self):
        password = secrets.token_hex(8)
        self.ui.label_2.setText(password)
        with open("my_pass.txt","a" ) as file:
            file.write('\n'password)
        

app = QApplication([])
ex = Widget()
ex.show()
app.exec_()