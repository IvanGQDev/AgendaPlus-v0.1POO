from PySide2 import QtCore, QtGui, QtWidgets
import json, Ui_MainMateria_15_06, UI_MainContactos, UI_LoginFull#main_window

if __name__ == "__main__":
    import sys
    if not QtWidgets.QApplication.instance(): #Este if y else es para que recargue sin reiniciar kernel
        app = QtWidgets.QApplication(sys.argv)
    else:
        app = QtWidgets.QApplication.instance()
    #MainWindow = QtWidgets.QMainWindow()
    #ui = Ui_MainMateria_15_06.Ui_mainwindoMaterias()
    #ui.setupUi(MainWindow)
    #MainWindow.show()
    window = UI_LoginFull.Main_window()
    window.show()

    sys.exit(app.exec_())
