from PySide2.QtWidgets import QMainWindow,QApplication,QMessageBox, QWidget
from recOtroUI import Ui_MainWindow
from recordatorio import Recordatorio
from adminRecordatorio import AdministraRecordatorio
import sys

class RecordatorioOtro(QMainWindow):
    def __init__(self,mode,index):
        super(RecordatorioOtro,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.admin = AdministraRecordatorio()
        self.admin.abrir("recordatorios.json")

        self.ui.salirPushButton.clicked.connect(self.opcionSalir)
        self.ui.guardarPushButton.clicked.connect(self.opcionGuardar)

        if(mode):
            self.ui.descripcionLineEdit.setText(self.admin.recordatorios[index].getDescripcion())

    def opcionSalir(self):
        print("salir")
        self.close()

    def opcionGuardar(self):
        print("guardar")
        tipo=2
        titulo=""
        materia=""
        fecha= self.ui.dateEdit.text()
        hora=self.ui.timeEdit.text()
        descripcion=self.ui.descripcionLineEdit.text()

        self.admin.nuevoRecordatorio(Recordatorio(tipo,titulo,materia,fecha,hora,descripcion))
        self.admin.guardar("recordatorios.json")
        QMessageBox.information(self, "Registro", "Recordatorio guardado")
        self.close()