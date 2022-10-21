#tipoRecordatorio
from PySide2.QtWidgets import QMainWindow,QApplication,QMessageBox, QWidget
from tipoRecordatorioUI import Ui_MainWindow
from recTarea import RecordatorioTarea
from recExamen import RecordatorioExamen
from recOtro import RecordatorioOtro
import sys

class TipoRecordatorio(QMainWindow):
    def __init__(self):
        super(TipoRecordatorio,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.tareaPushButton.clicked.connect(self.opcionTarea)
        self.ui.examenPushButton.clicked.connect(self.opcionExamen)
        self.ui.otroPushButton.clicked.connect(self.opcionOtro)

    def opcionSalir(self):
        self.close()

    def opcionTarea(self):
        self.window = RecordatorioTarea(0,0)
        self.window.show()
        self.close()
    
    def opcionExamen(self):
        print("examen")
        self.window = RecordatorioExamen(0,0)
        self.window.show()
        self.close()
    
    def opcionOtro(self):
        print("otro")
        self.window = RecordatorioOtro(0,0)
        self.window.show()
        self.close()