from PySide2.QtWidgets import QMainWindow,QApplication,QMessageBox, QWidget
from recTareaUI import Ui_MainWindow
from recordatorio import Recordatorio
#from recordatorioMain import MenuRecordatorio
from adminRecordatorio import AdministraRecordatorio
import sys

class RecordatorioTarea(QMainWindow):
    def __init__(self,mode,index):
        super(RecordatorioTarea,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.admin = AdministraRecordatorio()
        self.admin.abrir("recordatorios.json")

        self.ui.salirPushButton.clicked.connect(self.opcionSalir)
        self.ui.GuardarPushButton.clicked.connect(self.opcionGuardar)

        if(mode):
            self.ui.tituloLineEdit.setText(self.admin.recordatorios[index].getTitulo())
            self.ui.materiaLineEdit.setText(self.admin.recordatorios[index].getMateria())
            #self.ui.dateEdit.setText(self.admin.recordatorios[index].getFecha())
            #self.ui.timeEdit.setText(self.admin.recordatorios[index].getHora())
            self.ui.descripcionEdit.setText(self.admin.recordatorios[index].getDescripcion())

    def opcionSalir(self):
        print("salir")
        self.close()

    def opcionGuardar(self):
        print("guardar")
        tipo=0
        titulo=self.ui.tituloLineEdit.text()
        materia=self.ui.materiaLineEdit.text()
        fecha= self.ui.dateEdit.text()
        hora=self.ui.timeEdit.text()
        descripcion=self.ui.descripcionEdit.text()

        self.admin.nuevoRecordatorio(Recordatorio(tipo,titulo,materia,fecha,hora,descripcion))
        self.admin.guardar("recordatorios.json")
        QMessageBox.information(self, "Registro", "Recordatorio guardado")

        self.close()