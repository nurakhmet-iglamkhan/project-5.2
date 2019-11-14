import re
import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi

class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('form.ui', self)

        self.setWindowTitle('Работа со строками в Python')
        self.setWindowIcon(QtGui.QIcon('images/logo.png'))

        self.btn_Solve.clicked.connect(self.solve)
        self.btn_Clear.clicked.connect(self.clear)

    def clear(self):
        self.lineEdit_Text.clear()
        self.lineEdit_Words.clear()

    def solve(self):

        word = 0
        text = self.lineEdit_Text.toPlainText()
        text = text.split()
        ans = text[0]
        ans0 = text[0]
        for i in range(len(text)):
            word = len(text[i])
            if word > len(ans):
                ans = text[i]
            if word < len(ans0):
                ans0 = text[i]
        self.lineEdit_Words.insertPlainText('длинное слово: ' + ans + '\n'+'короткое слово: ' + ans0)

def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()