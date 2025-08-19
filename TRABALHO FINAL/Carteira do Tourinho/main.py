import sys

from PyQt6 import QtWidgets
from widget import Tela_Inicial

app = QtWidgets.QApplication(sys.argv)

inicio = Tela_Inicial()
inicio.show()

app.exec()