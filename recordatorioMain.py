#archivo menu recordatorio
from PySide2 import QtWidgets, QtCore
from PySide2.QtWidgets import QMainWindow,QApplication,QMessageBox, QWidget, QTableWidgetItem
from recordatorioMainUI import Ui_MainWindow
from tipoRecordatorio import TipoRecordatorio
from adminRecordatorio import AdministraRecordatorio
from recTarea import RecordatorioTarea
from recExamen import RecordatorioExamen
from recOtro import RecordatorioOtro
import sys

class MenuRecordatorio(QMainWindow):
    def __init__(self):
        super(MenuRecordatorio,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.admin = AdministraRecordatorio()
        self.admin.abrir("recordatorios.json")

        self.ui.agregarPushButton.clicked.connect(self.opcionAgregar)
        self.ui.editarPushButton.clicked.connect(self.opcionEditar)
        self.ui.eliminarPushButton.clicked.connect(self.opcionEliminar)
        self.ui.actualizarPushButton.clicked.connect(self.organizarTabla)
        self.ui.salirPushButton.clicked.connect(self.opcionSalir)

        self.organizarTabla()
        #self.mostrar()

    def organizarTabla(self):
        self.admin.abrir("recordatorios.json")
        self.ui.listaTableWidget.setColumnCount(6)
        self.ui.listaTableWidget.setRowCount(0)
        self.ui.listaTableWidget.setHorizontalHeaderLabels(['Tipo','Titulo','Materia','Fecha','Hora','Descripción'])
        self.ui.listaTableWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ui.listaTableWidget.setAlternatingRowColors(True)
        self.ui.listaTableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.mostrar()

    def opcionSalir(self):
        self.close()

    def mostrar(self):
        for i in range(len(self.admin.recordatorios)):
            aux = self.admin.recordatorios[i].getTipo()
            tipo="Otro"
            if aux == 0:
                tipo="Tarea"
            elif aux ==1:
                tipo = "Examen"

            self.ui.listaTableWidget.insertRow(i)
            self.ui.listaTableWidget.setItem(i,0,QtWidgets.QTableWidgetItem(tipo))
            self.ui.listaTableWidget.setItem(i,1,QtWidgets.QTableWidgetItem(self.admin.recordatorios[i].getTitulo()))
            self.ui.listaTableWidget.setItem(i,2,QtWidgets.QTableWidgetItem(self.admin.recordatorios[i].getMateria()))
            self.ui.listaTableWidget.setItem(i,3,QtWidgets.QTableWidgetItem(self.admin.recordatorios[i].getFecha()))
            self.ui.listaTableWidget.setItem(i,4,QtWidgets.QTableWidgetItem(self.admin.recordatorios[i].getHora()))
            self.ui.listaTableWidget.setItem(i,5,QtWidgets.QTableWidgetItem(self.admin.recordatorios[i].getDescripcion()))

    def actualizarLista(self):
        self.admin.abrir("recordatorios.json")
        self.ui.listaTableWidget.setRowCount(0)
        self.mostrar()

    def opcionAgregar(self):
        print("agregar")
        self.window = TipoRecordatorio()
        self.window.show()
    

    def opcionEditar(self):
        print("editar")
        #print(self.ui.listaTableWidget.currentRow())
        #print(self.admin.recordatorios[self.ui.listaTableWidget.currentRow()].getTipo())
        tipo = self.admin.recordatorios[self.ui.listaTableWidget.currentRow()].getTipo()
        QMessageBox.information(self, "Registro", "El modificado presenta algunos errores (:")
        
        if(tipo==0):
            print("tareaEdit")
            self.window = RecordatorioTarea(1,self.ui.listaTableWidget.currentRow())
            self.window.show()
            self.close()
            
        if(tipo==1):
            print("examenEdit")
            self.window = RecordatorioExamen(1,self.ui.listaTableWidget.currentRow())
            self.window.show()
            self.close()
        
        if(tipo==2):
            print("otroEdit")
            self.window = RecordatorioOtro(1,self.ui.listaTableWidget.currentRow())
            self.window.show()
            self.close()


    def opcionEliminar(self):
        print("eliminar")
        print(self.ui.listaTableWidget.currentRow())
        self.admin.eliminarRecordatorio(self.ui.listaTableWidget.currentRow())
        self.admin.guardar("recordatorios.json")
        QMessageBox.information(self, "Registro", "Recordatorio eliminado")