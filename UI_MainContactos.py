from PyQt5 import QtCore, QtGui, QtWidgets
import json, Ui_MainMateria_15_06
from recordatorioMain import MenuRecordatorio
from UI_LoginFull import  Editar_WindowUsuario, Main_window
from PySide2.QtWidgets import *

contactos = []  # "Clase" administradora de Contactos

class Contacto:
    def __init__(self):  # Inicializados. Mostramos esto en los registros en la UI
        self.nomCon = "Nombre(s)"
        self.apeCon = "Apellido(s)"
        self.corrCon1 = "Correo electrónico 1"
        self.corrCon2 = "Correo electrónico 2"
        self.telCon1 = "Teléfono 1"
        self.telCon2 = "Teléfono 2"
        self.etiCon = "Otro"

    def nuevoContacto(self, nombre, apellido, correo1, correo2, tel1, tel2, etiqueta):
        self.nomCon = nombre
        self.apeCon = apellido
        self.corrCon1 = correo1
        self.corrCon2 = correo2
        self.telCon1 = tel1
        self.telCon2 = tel2
        self.etiCon = etiqueta

    # Getters y Setters
    def getNomCon(self):
        return self.nomCon

    def setNomCon(self, v):
        self.nomCon = v

    def getApeCon(self):
        return self.apeCon

    def setApeCon(self, v):
        self.apeCon = v

    def getCorrCon1(self):
        return self.corrCon1

    def setCorrCon1(self, v):
        self.corrCon1 = v

    def getCorrCon2(self):
        return self.corrCon2

    def setCorrCon2(self, v):
        self.corrCon2 = v

    def getTelCon1(self):
        return self.telCon1

    def setTelCon1(self, v):
        self.telCon1 = v

    def getTelCon2(self):
        return self.telCon2

    def setTelCon2(self, v):
        self.telCon2 = v

    def getEtiCon(self):
        return self.etiCon

    def setEtiCon(self, v):
        self.etiCon = v

    def mostrar(self):
        print("Nombre:", self.getNomCon())
        print("Apellido", self.getApeCon())
        print("Correo 1:", self.getCorrCon1())
        print("Correo 2:", self.getCorrCon2())
        print("Tel.1:", self.getTelCon1())
        print("Tel.2:", self.getTelCon2())
        print("Etiqueta:", self.getEtiCon())


class Ui_windowNewContacto(object):  # Ventana para nuevo contacto
    def __init__(self):
        super().__init__()

    def setupUi(self, windowNewContacto, source, count):
        windowNewContacto.setObjectName("windowNewContacto")
        windowNewContacto.resize(400, 300)
        windowNewContacto.setMaximumSize(QtCore.QSize(400, 300))
        windowNewContacto.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.textoNuevoContacto = QtWidgets.QLabel(windowNewContacto)
        self.textoNuevoContacto.setGeometry(QtCore.QRect(10, 10, 371, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textoNuevoContacto.sizePolicy().hasHeightForWidth())
        self.textoNuevoContacto.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.textoNuevoContacto.setFont(font)
        self.textoNuevoContacto.setScaledContents(False)
        self.textoNuevoContacto.setAlignment(QtCore.Qt.AlignCenter)
        self.textoNuevoContacto.setObjectName("textoNuevoContacto")
        self.lineNombre = QtWidgets.QLineEdit(windowNewContacto)
        self.lineNombre.setGeometry(QtCore.QRect(10, 60, 371, 20))
        self.lineNombre.setText("")
        self.lineNombre.setObjectName("lineNombre")
        self.lineApellido = QtWidgets.QLineEdit(windowNewContacto)
        self.lineApellido.setGeometry(QtCore.QRect(10, 90, 371, 20))
        self.lineApellido.setText("")
        self.lineApellido.setObjectName("lineApellido")
        self.lineCorreo1 = QtWidgets.QLineEdit(windowNewContacto)
        self.lineCorreo1.setGeometry(QtCore.QRect(10, 120, 371, 20))
        self.lineCorreo1.setObjectName("lineCorreo1")
        self.lineCorreo2 = QtWidgets.QLineEdit(windowNewContacto)
        self.lineCorreo2.setGeometry(QtCore.QRect(10, 150, 371, 20))
        self.lineCorreo2.setObjectName("lineCorreo2")
        self.lineTel1 = QtWidgets.QLineEdit(windowNewContacto)
        self.lineTel1.setGeometry(QtCore.QRect(10, 180, 371, 20))
        self.lineTel1.setObjectName("lineTel1")
        self.lineTel2 = QtWidgets.QLineEdit(windowNewContacto)
        self.lineTel2.setGeometry(QtCore.QRect(10, 210, 371, 20))
        self.lineTel2.setObjectName("lineTel2")
        self.botonGuardarContacto = QtWidgets.QPushButton(windowNewContacto)
        self.botonGuardarContacto.setEnabled(False)
        self.botonGuardarContacto.setGeometry(QtCore.QRect(310, 270, 75, 23))
        self.botonGuardarContacto.setObjectName("botonGuardarContacto")
        self.checkBoxAlumno = QtWidgets.QCheckBox(windowNewContacto)
        self.checkBoxAlumno.setGeometry(QtCore.QRect(10, 270, 70, 17))
        self.checkBoxAlumno.setChecked(False)
        self.checkBoxAlumno.setObjectName("checkBoxAlumno")
        self.checkBoxProfesor = QtWidgets.QCheckBox(windowNewContacto)
        self.checkBoxProfesor.setGeometry(QtCore.QRect(80, 270, 70, 17))
        self.checkBoxProfesor.setObjectName("checkBoxProfesor")
        self.checkBoxOtro = QtWidgets.QCheckBox(windowNewContacto)
        self.checkBoxOtro.setGeometry(QtCore.QRect(160, 270, 70, 17))
        self.checkBoxOtro.setObjectName("checkBoxOtro")
        # Texto de error de validación
        self.labelErrorValidacion = QtWidgets.QLabel(windowNewContacto)
        self.labelErrorValidacion.setGeometry(QtCore.QRect(10, 30, 371, 16))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.labelErrorValidacion.setPalette(palette)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelErrorValidacion.setFont(font)
        self.labelErrorValidacion.setAlignment(QtCore.Qt.AlignCenter)
        self.labelErrorValidacion.setObjectName("labelErrorValidacion")

        self.retranslateUi(windowNewContacto)
        self.checkBoxProfesor.toggled['bool'].connect(self.checkBoxAlumno.setDisabled)
        self.checkBoxProfesor.toggled['bool'].connect(self.botonGuardarContacto.setEnabled)
        self.checkBoxAlumno.toggled['bool'].connect(self.checkBoxProfesor.setDisabled)
        self.checkBoxAlumno.toggled['bool'].connect(self.botonGuardarContacto.setEnabled)
        self.checkBoxOtro.toggled['bool'].connect(self.botonGuardarContacto.setEnabled)
        self.checkBoxOtro.toggled['bool'].connect(self.checkBoxProfesor.setDisabled)
        self.checkBoxOtro.toggled['bool'].connect(self.checkBoxAlumno.setDisabled)
        self.checkBoxAlumno.toggled['bool'].connect(self.checkBoxOtro.setDisabled)
        self.checkBoxProfesor.toggled['bool'].connect(self.checkBoxOtro.setDisabled)
        self.botonGuardarContacto.clicked.connect(
            lambda: self.validarInfo(windowNewContacto, source, count))  # Al ser apretado checa la info
        QtCore.QMetaObject.connectSlotsByName(windowNewContacto)

    def validarInfo(self, windowNewContacto, source, count):
        # print(self.lineNombre.text())
        # Los separon en distintos ifs para poder ponerlo en blanco si se cumple
        if (self.lineNombre.text() == ""):
            self.labelErrorValidacion.setText("Nombre obligatorio")
            return
        else:
            self.labelErrorValidacion.setText("")

        if (self.lineApellido.text() == ""):
            self.labelErrorValidacion.setText("Apellido obligatorio")
            return
        else:
            self.labelErrorValidacion.setText("")

        if (self.lineCorreo1.text() == ""):
            self.labelErrorValidacion.setText("Correo primario obligatorio")
            return
        else:
            self.labelErrorValidacion.setText("")

        if (self.lineTel1.text() == ""):
            self.labelErrorValidacion.setText("Teléfono primario obligatorio")
            return
        else:
            self.labelErrorValidacion.setText("")
        # Todo está en orden, guardar datos
        nombre = self.lineNombre.text()
        apellido = self.lineApellido.text()
        correo1 = self.lineCorreo1.text()
        correo2 = self.lineCorreo2.text()
        tel1 = self.lineTel1.text()
        tel2 = self.lineTel2.text()

        et = 0  # Ahora identificamos la etiqueta del contacto
        if (self.checkBoxAlumno.checkState()):
            # print("1")
            et = '1'
        elif (self.checkBoxProfesor.checkState()):
            # print("2")
            et = '2'
        else:
            # print("3")
            et = '3'

        self.temp = Contacto()  # temp es un nuevo Contacto
        self.temp.nuevoContacto(nombre, apellido, correo1, correo2, tel1, tel2, et)  # Creamos el contacto con su info
        global contactos  # Indico que es la lista global
        contactos.append(self.temp)  # Metemos el nuevo contacto a la lista
        contactos.sort(key=lambda x: x.getApeCon(), reverse=False)  # Se ordena alfabéticamente la lista por apellido
        QtCore.QTimer.singleShot(0, windowNewContacto.close)  # Para cerrar la ventana una vez verificado
        source.cargarFilas()
        source.guardarContactos(count) # Rescatamos la información al JSON

        return contactos

    def retranslateUi(self, windowNewContacto):
        _translate = QtCore.QCoreApplication.translate
        windowNewContacto.setWindowTitle(_translate("windowNewContacto", "Nuevo Contacto"))
        self.textoNuevoContacto.setText(_translate("windowNewContacto", "Nuevo Contacto"))
        self.lineNombre.setPlaceholderText(_translate("windowNewContacto", "Nombre(s)"))
        self.lineApellido.setPlaceholderText(_translate("windowNewContacto", "Apellido(s)"))
        self.lineCorreo1.setPlaceholderText(_translate("windowNewContacto", "Correo"))
        self.lineCorreo2.setPlaceholderText(_translate("windowNewContacto", "Correo secundario"))
        self.lineTel1.setPlaceholderText(_translate("windowNewContacto", "Teléfono"))
        self.lineTel2.setPlaceholderText(_translate("windowNewContacto", "Teléfono secundario"))
        self.checkBoxAlumno.setText(_translate("windowNewContacto", "Alumno"))
        self.checkBoxProfesor.setText(_translate("windowNewContacto", "Profesor"))
        self.checkBoxOtro.setText(_translate("windowNewContacto", "Otro"))
        self.botonGuardarContacto.setText(_translate("windowNewContacto", "Guardar"))
        self.labelErrorValidacion.setText(_translate("windowNewContacto", ""))


class Ui_windowEditContacto(object):  # Ventana para nuevo contacto
    def __init__(self, contEdit):
        super().__init__()
        self.contEdit = contEdit  # El objeto a editar
        

    def setupUi(self, windowEditContacto, source, count):
        windowEditContacto.setObjectName("windowEditContacto")
        windowEditContacto.resize(400, 300)
        windowEditContacto.setMaximumSize(QtCore.QSize(400, 300))
        windowEditContacto.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.textoNuevoContacto = QtWidgets.QLabel(windowEditContacto)
        self.textoNuevoContacto.setGeometry(QtCore.QRect(10, 10, 371, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textoNuevoContacto.sizePolicy().hasHeightForWidth())
        self.textoNuevoContacto.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.textoNuevoContacto.setFont(font)
        self.textoNuevoContacto.setScaledContents(False)
        self.textoNuevoContacto.setAlignment(QtCore.Qt.AlignCenter)
        self.textoNuevoContacto.setObjectName("textoNuevoContacto")
        self.lineNombre = QtWidgets.QLineEdit(windowEditContacto)
        self.lineNombre.setGeometry(QtCore.QRect(10, 60, 371, 20))
        self.lineNombre.setText("")
        self.lineNombre.setObjectName("lineNombre")
        self.lineApellido = QtWidgets.QLineEdit(windowEditContacto)
        self.lineApellido.setGeometry(QtCore.QRect(10, 90, 371, 20))
        self.lineApellido.setText("")
        self.lineApellido.setObjectName("lineApellido")
        self.lineCorreo1 = QtWidgets.QLineEdit(windowEditContacto)
        self.lineCorreo1.setGeometry(QtCore.QRect(10, 120, 371, 20))
        self.lineCorreo1.setObjectName("lineCorreo1")
        self.lineCorreo2 = QtWidgets.QLineEdit(windowEditContacto)
        self.lineCorreo2.setGeometry(QtCore.QRect(10, 150, 371, 20))
        self.lineCorreo2.setObjectName("lineCorreo2")
        self.lineTel1 = QtWidgets.QLineEdit(windowEditContacto)
        self.lineTel1.setGeometry(QtCore.QRect(10, 180, 371, 20))
        self.lineTel1.setObjectName("lineTel1")
        self.lineTel2 = QtWidgets.QLineEdit(windowEditContacto)
        self.lineTel2.setGeometry(QtCore.QRect(10, 210, 371, 20))
        self.lineTel2.setObjectName("lineTel2")
        self.botonGuardarContacto = QtWidgets.QPushButton(windowEditContacto)
        self.botonGuardarContacto.setEnabled(False)
        self.botonGuardarContacto.setGeometry(QtCore.QRect(310, 270, 75, 23))
        self.botonGuardarContacto.setObjectName("botonGuardarContacto")
        self.checkBoxAlumno = QtWidgets.QCheckBox(windowEditContacto)
        self.checkBoxAlumno.setGeometry(QtCore.QRect(10, 270, 70, 17))
        self.checkBoxAlumno.setChecked(False)
        self.checkBoxAlumno.setObjectName("checkBoxAlumno")
        self.checkBoxProfesor = QtWidgets.QCheckBox(windowEditContacto)
        self.checkBoxProfesor.setGeometry(QtCore.QRect(80, 270, 70, 17))
        self.checkBoxProfesor.setObjectName("checkBoxProfesor")
        self.checkBoxOtro = QtWidgets.QCheckBox(windowEditContacto)
        self.checkBoxOtro.setGeometry(QtCore.QRect(160, 270, 70, 17))
        self.checkBoxOtro.setObjectName("checkBoxOtro")
        # Texto de error de validación
        self.labelErrorValidacion = QtWidgets.QLabel(windowEditContacto)
        self.labelErrorValidacion.setGeometry(QtCore.QRect(10, 30, 371, 16))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.labelErrorValidacion.setPalette(palette)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelErrorValidacion.setFont(font)
        self.labelErrorValidacion.setAlignment(QtCore.Qt.AlignCenter)
        self.labelErrorValidacion.setObjectName("labelErrorValidacion")

        self.retranslateUi(windowEditContacto)
        self.checkBoxProfesor.toggled['bool'].connect(self.checkBoxAlumno.setDisabled)
        self.checkBoxProfesor.toggled['bool'].connect(self.botonGuardarContacto.setEnabled)
        self.checkBoxAlumno.toggled['bool'].connect(self.checkBoxProfesor.setDisabled)
        self.checkBoxAlumno.toggled['bool'].connect(self.botonGuardarContacto.setEnabled)
        self.checkBoxOtro.toggled['bool'].connect(self.botonGuardarContacto.setEnabled)
        self.checkBoxOtro.toggled['bool'].connect(self.checkBoxProfesor.setDisabled)
        self.checkBoxOtro.toggled['bool'].connect(self.checkBoxAlumno.setDisabled)
        self.checkBoxAlumno.toggled['bool'].connect(self.checkBoxOtro.setDisabled)
        self.checkBoxProfesor.toggled['bool'].connect(self.checkBoxOtro.setDisabled)
        self.botonGuardarContacto.clicked.connect(
            lambda: self.validarInfo(windowEditContacto, source, count))  # Al ser apretado checa la info
        QtCore.QMetaObject.connectSlotsByName(windowEditContacto)

    def validarInfo(self, windowEditContacto, source, count):
        # print(self.lineNombre.text())
        # Los separon en distintos ifs para poder ponerlo en blanco si se cumple
        if (self.lineNombre.text() == ""):
            self.labelErrorValidacion.setText("Nombre obligatorio")
            return
        else:
            self.labelErrorValidacion.setText("")

        if (self.lineApellido.text() == ""):
            self.labelErrorValidacion.setText("Apellido obligatorio")
            return
        else:
            self.labelErrorValidacion.setText("")

        if (self.lineCorreo1.text() == ""):
            self.labelErrorValidacion.setText("Correo primario obligatorio")
            return
        else:
            self.labelErrorValidacion.setText("")

        if (self.lineTel1.text() == ""):
            self.labelErrorValidacion.setText("Teléfono primario obligatorio")
            return
        else:
            self.labelErrorValidacion.setText("")
        # Todo está en orden, guardar datos
        nombre = self.lineNombre.text()
        apellido = self.lineApellido.text()
        correo1 = self.lineCorreo1.text()
        correo2 = self.lineCorreo2.text()
        tel1 = self.lineTel1.text()
        tel2 = self.lineTel2.text()

        et = 0  # Ahora identificamos la etiqueta del contacto
        if (self.checkBoxAlumno.checkState()):
            # print("1")
            et = '1'
        elif (self.checkBoxProfesor.checkState()):
            # print("2")
            et = '2'
        else:
            # print("3")
            et = '3'

        global contactos  # Indico que es la lista global
        # Asignamos todos los valores nuevos al objeto
        self.contEdit.setNomCon(nombre)
        self.contEdit.setApeCon(apellido)
        self.contEdit.setCorrCon1(correo1)
        self.contEdit.setCorrCon2(correo2)
        self.contEdit.setTelCon1(tel1)
        self.contEdit.setTelCon2(tel2)
        self.contEdit.setEtiCon(et)
        contactos.sort(key=lambda x: x.getApeCon(), reverse=False)  # Se ordena alfabéticamente la lista por apellido
        QtCore.QTimer.singleShot(0, windowEditContacto.close)  # Para cerrar la ventana una vez verificado
        source.cargarFilas()
        source.guardarContactos(count)  # Rescatamos la información al JSON
        return contactos

    def retranslateUi(self, windowEditContacto):
        _translate = QtCore.QCoreApplication.translate
        windowEditContacto.setWindowTitle(_translate("windowEditContacto", "Editar Contacto"))
        self.textoNuevoContacto.setText(_translate("windowEditContacto", "Editar Contacto"))
        self.lineNombre.setPlaceholderText(_translate("windowEditContacto", "Nombre(s)"))
        self.lineNombre.setText(self.contEdit.getNomCon())
        self.lineApellido.setPlaceholderText(_translate("windowEditContacto", "Apellido(s)"))
        self.lineApellido.setText(self.contEdit.getApeCon())
        self.lineCorreo1.setPlaceholderText(_translate("windowEditContacto", "Correo"))
        self.lineCorreo1.setText(self.contEdit.getCorrCon1())
        self.lineCorreo2.setPlaceholderText(_translate("windowEditContacto", "Correo secundario"))
        self.lineCorreo2.setText(self.contEdit.getCorrCon2())
        self.lineTel1.setPlaceholderText(_translate("windowEditContacto", "Teléfono"))
        self.lineTel1.setText(self.contEdit.getTelCon1())
        self.lineTel2.setPlaceholderText(_translate("windowEditContacto", "Teléfono secundario"))
        self.lineTel2.setText(self.contEdit.getTelCon2())
        self.checkBoxAlumno.setText(_translate("windowEditContacto", "Alumno"))
        self.checkBoxProfesor.setText(_translate("windowEditContacto", "Profesor"))
        self.checkBoxOtro.setText(_translate("windowEditContacto", "Otro"))
        self.botonGuardarContacto.setText(_translate("windowEditContacto", "Guardar"))
        self.labelErrorValidacion.setText(_translate("windowEditContacto", ""))


class Ui_MainWindow(object):  # Ventana principal
    def __init__(self):
        super().__init__()
        self.cargarFilas

    def setupUi(self, MainWindow, count):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(720, 480)
        MainWindow.setMaximumSize(QtCore.QSize(720, 480))
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.irCalendario = QtWidgets.QPushButton(self.centralwidget)
        self.irCalendario.setGeometry(QtCore.QRect(10, 100, 161, 23))
        self.irCalendario.setObjectName("irCalendario")
        self.areaContactos = QtWidgets.QScrollArea(self.centralwidget)
        self.areaContactos.setGeometry(QtCore.QRect(200, 40, 511, 401))
        self.areaContactos.setAutoFillBackground(False)
        self.areaContactos.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.areaContactos.setWidgetResizable(True)
        self.areaContactos.setObjectName("areaContactos")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 509, 399))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.areaContactos.setWidget(self.scrollAreaWidgetContents)
        self.textoContactos = QtWidgets.QLabel(self.centralwidget)
        self.textoContactos.setGeometry(QtCore.QRect(200, 10, 241, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.textoContactos.setFont(font)
        self.textoContactos.setObjectName("textoContactos")
        self.irMaterias = QtWidgets.QPushButton(self.centralwidget)
        self.irMaterias.setGeometry(QtCore.QRect(10, 220, 161, 23))
        self.irMaterias.setObjectName("irMaterias")
        self.botonAddContacto = QtWidgets.QPushButton(self.centralwidget)
        self.botonAddContacto.setGeometry(QtCore.QRect(620, 450, 91, 23))
        self.botonAddContacto.setObjectName("botonAddContacto")
        self.botonCerrSes = QtWidgets.QPushButton(self.centralwidget)
        self.botonCerrSes.setGeometry(QtCore.QRect(100, 10, 75, 23))
        self.botonCerrSes.setObjectName("botonCerrSes")
        #self.botonCerrSes.clicked.connect()
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(180, 0, 16, 481))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.irRecordatorios = QtWidgets.QPushButton(self.centralwidget)
        self.irRecordatorios.setGeometry(QtCore.QRect(10, 140, 161, 23))
        self.irRecordatorios.setObjectName("irRecordatorios")
        self.irContactos = QtWidgets.QPushButton(self.centralwidget)
        self.irContactos.setGeometry(QtCore.QRect(10, 180, 161, 23))
        self.irContactos.setObjectName("irContactos")
        self.botonConfig = QtWidgets.QPushButton(self.centralwidget)
        self.botonConfig.setGeometry(QtCore.QRect(10, 10, 75, 23))
        self.botonConfig.setFlat(False)
        self.botonConfig.setObjectName("botonConfig")

        self.labelRowSelect = QtWidgets.QLabel(self.centralwidget)
        self.labelRowSelect.setGeometry(QtCore.QRect(490, 10, 101, 20))
        self.labelRowSelect.setObjectName("labelRowSelect")
        self.botonEliminarContacto = QtWidgets.QPushButton(self.centralwidget)
        self.botonEliminarContacto.setGeometry(QtCore.QRect(644, 10, 61, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.botonEliminarContacto.setFont(font)
        self.botonEliminarContacto.setObjectName("botonEliminarContacto")
        self.botonEditarContacto = QtWidgets.QPushButton(self.centralwidget)
        self.botonEditarContacto.setGeometry(QtCore.QRect(600, 10, 41, 23))
        self.botonEditarContacto.setObjectName("botonEditarContacto")
        self.labelFiltros = QtWidgets.QLabel(self.centralwidget)
        self.labelFiltros.setGeometry(QtCore.QRect(200, 460, 47, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelFiltros.setFont(font)
        self.labelFiltros.setObjectName("labelFiltros")
        self.checkBoxFiltroAlumno = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxFiltroAlumno.setGeometry(QtCore.QRect(260, 460, 70, 17))
        self.checkBoxFiltroAlumno.setObjectName("checkBoxFiltroAlumno")
        self.checkBoxFiltroProfesor = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxFiltroProfesor.setGeometry(QtCore.QRect(320, 460, 70, 17))
        self.checkBoxFiltroProfesor.setObjectName("checkBoxFiltroProfesor")
        self.checkBoxFiltroOtro = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxFiltroOtro.setGeometry(QtCore.QRect(390, 460, 70, 17))
        self.checkBoxFiltroOtro.setObjectName("checkBoxFiltroOtro")
        # La lista
        self.tableContactos = QtWidgets.QTableWidget(self.centralwidget)
        self.tableContactos.setGeometry(QtCore.QRect(200, 40, 511, 401))
        self.tableContactos.setObjectName("tableContactos")
        self.tableContactos.setFocusPolicy(QtCore.Qt.NoFocus)  # Hace que no se pueda seleccionar las filas
        self.tableContactos.setAlternatingRowColors(True)
        self.tableContactos.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)  # Selecciona fila entera
        self.tableContactos.setCornerButtonEnabled(False)
        self.tableContactos.setColumnCount(7)
        self.tableContactos.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableContactos.setHorizontalHeaderItem(0, item)
        self.tableContactos.setColumnWidth(0, 140)
        item = QtWidgets.QTableWidgetItem()
        self.tableContactos.setHorizontalHeaderItem(1, item)
        self.tableContactos.setColumnWidth(1, 140)
        item = QtWidgets.QTableWidgetItem()
        self.tableContactos.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableContactos.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableContactos.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableContactos.setHorizontalHeaderItem(5, item)
        self.tableContactos.setColumnWidth(5, 110)
        item = QtWidgets.QTableWidgetItem()
        self.tableContactos.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()

        MainWindow.setCentralWidget(self.centralwidget)
        self.botonAddContacto.clicked.connect(lambda: self.showNewCont(count))  # MUESTRA
        self.tableContactos.clicked.connect(self.tablaClick)  # Hacer cosas cada que damos click dentro de la tabla
        self.botonEliminarContacto.clicked.connect(lambda: self.eliminarContacto(count))
        self.botonEditarContacto.clicked.connect(lambda: self.editarContacto(count))
        self.cargarContactos(count)  # Cargo los contactos a la vez que cargo la GUI
        self.cargarFilas()  # Cargo las filas por si había algo en el JSON
        self.irRecordatorios.clicked.connect(self.menuRecordatorios)
        self.irMaterias.clicked.connect(self.showMaterias)
        self.botonCerrSes.clicked.connect(lambda: self.cerrarSesion(MainWindow, count))
        self.botonConfig.clicked.connect(self.boton_config)

        self.retranslateUi(MainWindow)
        self.checkBoxFiltroAlumno.toggled['bool'].connect(self.checkBoxFiltroProfesor.setDisabled)
        self.checkBoxFiltroAlumno.toggled['bool'].connect(self.checkBoxFiltroOtro.setDisabled)
        self.checkBoxFiltroAlumno.clicked.connect(self.filtroAlumno)
        self.checkBoxFiltroAlumno.toggled['bool'].connect(self.botonEliminarContacto.setDisabled)
        self.checkBoxFiltroAlumno.toggled['bool'].connect(self.botonEditarContacto.setDisabled)
        self.checkBoxFiltroProfesor.toggled['bool'].connect(self.checkBoxFiltroAlumno.setDisabled)
        self.checkBoxFiltroProfesor.toggled['bool'].connect(self.checkBoxFiltroOtro.setDisabled)
        self.checkBoxFiltroProfesor.clicked.connect(self.filtroProfesor)
        self.checkBoxFiltroProfesor.toggled['bool'].connect(self.botonEliminarContacto.setDisabled)
        self.checkBoxFiltroProfesor.toggled['bool'].connect(self.botonEditarContacto.setDisabled)
        self.checkBoxFiltroOtro.toggled['bool'].connect(self.checkBoxFiltroAlumno.setDisabled)
        self.checkBoxFiltroOtro.toggled['bool'].connect(self.checkBoxFiltroProfesor.setDisabled)
        self.checkBoxFiltroOtro.clicked.connect(self.filtroOtro)
        self.checkBoxFiltroOtro.toggled['bool'].connect(self.botonEliminarContacto.setDisabled)
        self.checkBoxFiltroOtro.toggled['bool'].connect(self.botonEditarContacto.setDisabled)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def filtroAlumno(self):
        if (self.checkBoxFiltroAlumno.checkState() == 2):  # 0 uncheck, 1 intermediate, 2 checked
            # print("Filtro alumno activado")
            self.tableContactos.setRowCount(0)  # Reinicio la tabla
            self.tableContactos.setRowCount(len(contactos))  # Calculamos el n° de filas
            self.row = 0
            minimal = 0

            for fila in contactos:
                if (contactos[self.row].getEtiCon() == '1'):  # Check Alumno
                    self.tableContactos.setItem(minimal, 0, QtWidgets.QTableWidgetItem(contactos[self.row].getApeCon()))
                    self.tableContactos.setItem(minimal, 1, QtWidgets.QTableWidgetItem(contactos[self.row].getNomCon()))
                    self.tableContactos.setItem(minimal, 2,
                                                QtWidgets.QTableWidgetItem(contactos[self.row].getTelCon1()))
                    self.tableContactos.setItem(minimal, 3,
                                                QtWidgets.QTableWidgetItem(contactos[self.row].getCorrCon1()))
                    self.tableContactos.setItem(minimal, 4,
                                                QtWidgets.QTableWidgetItem(contactos[self.row].getTelCon2()))
                    self.tableContactos.setItem(minimal, 5,
                                                QtWidgets.QTableWidgetItem(contactos[self.row].getCorrCon2()))
                    self.tableContactos.setItem(minimal, 6, QtWidgets.QTableWidgetItem("Alumno"))
                    minimal += 1
                self.row += 1

        else:
            # print("Filtro alumno desactivado")
            # self.tableContactos.setRowCount(0) #Reinicio la tabla
            self.cargarFilas()

    def filtroProfesor(self):
        if (self.checkBoxFiltroProfesor.checkState() == 2):  # 0 uncheck, 1 intermediate, 2 checked
            # print("Filtro Profesor activado")
            self.tableContactos.setRowCount(0)  # Reinicio la tabla
            self.tableContactos.setRowCount(len(contactos))  # Calculamos el n° de filas
            self.row = 0
            minimal = 0

            for fila in contactos:
                if (contactos[self.row].getEtiCon() == '2'):  # Check Prof
                    self.tableContactos.setItem(minimal, 0, QtWidgets.QTableWidgetItem(contactos[self.row].getApeCon()))
                    self.tableContactos.setItem(minimal, 1, QtWidgets.QTableWidgetItem(contactos[self.row].getNomCon()))
                    self.tableContactos.setItem(minimal, 2,
                                                QtWidgets.QTableWidgetItem(contactos[self.row].getTelCon1()))
                    self.tableContactos.setItem(minimal, 3,
                                                QtWidgets.QTableWidgetItem(contactos[self.row].getCorrCon1()))
                    self.tableContactos.setItem(minimal, 4,
                                                QtWidgets.QTableWidgetItem(contactos[self.row].getTelCon2()))
                    self.tableContactos.setItem(minimal, 5,
                                                QtWidgets.QTableWidgetItem(contactos[self.row].getCorrCon2()))
                    self.tableContactos.setItem(minimal, 6, QtWidgets.QTableWidgetItem("Profesor"))
                    minimal += 1
                self.row += 1

        else:
            # print("Filtro profesor desactivado")
            # self.tableContactos.setRowCount(0) #Reinicio la tabla
            self.cargarFilas()

    def filtroOtro(self):
        if (self.checkBoxFiltroOtro.checkState() == 2):  # 0 uncheck, 1 intermediate, 2 checked
            # print("Filtro otro activado")
            self.tableContactos.setRowCount(0)  # Reinicio la tabla
            self.tableContactos.setRowCount(len(contactos))  # Calculamos el n° de filas
            self.row = 0
            minimal = 0

            for fila in contactos:
                if (contactos[self.row].getEtiCon() == '3'):  # Check Alumno
                    self.tableContactos.setItem(minimal, 0, QtWidgets.QTableWidgetItem(contactos[self.row].getApeCon()))
                    self.tableContactos.setItem(minimal, 1, QtWidgets.QTableWidgetItem(contactos[self.row].getNomCon()))
                    self.tableContactos.setItem(minimal, 2,
                                                QtWidgets.QTableWidgetItem(contactos[self.row].getTelCon1()))
                    self.tableContactos.setItem(minimal, 3,
                                                QtWidgets.QTableWidgetItem(contactos[self.row].getCorrCon1()))
                    self.tableContactos.setItem(minimal, 4,
                                                QtWidgets.QTableWidgetItem(contactos[self.row].getTelCon2()))
                    self.tableContactos.setItem(minimal, 5,
                                                QtWidgets.QTableWidgetItem(contactos[self.row].getCorrCon2()))
                    self.tableContactos.setItem(minimal, 6, QtWidgets.QTableWidgetItem("Otro"))
                    minimal += 1
                self.row += 1

        else:
            # print("Filtro otro desactivado")
            # self.tableContactos.setRowCount(0) #Reinicio la tabla
            self.cargarFilas()

    def tablaClick(self, index):
        self.labelRowSelect.setText("Seleccionado: " + str(index.row()))  # Mostramos al usuario cual picó
        # print("Row: ", index.row())
        self.fila = index.row()  # Le pasamos la fila a esta variable, la podemos llamar en toda la funcion
        return self.fila

    def eliminarContacto(self, count):  # Mejora: hacer que no salga el mensaje sin selección
        try:
            choice = QtWidgets.QMessageBox()
            choice.setIcon(QtWidgets.QMessageBox.Information)
            choice.setText("Se eliminará de manera permanente el contacto seleccionado, ¿continuar?")
            # choice.setInformativeText("Do you want to save your changes?")
            choice.setWindowTitle("Eliminar contacto")
            choice.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            choice.setDefaultButton(QtWidgets.QMessageBox.No)

            if (choice.exec() == QtWidgets.QMessageBox.Yes):  # Checamos a ver si aceptó el usuario
                # print("Extracting Naaaaaaoooww!!!!", str(self.fila))
                contactos.pop(self.fila)
                self.cargarFilas()  # Recargamos la lista
                self.guardarContactos(count)  # Guardamos el cambio al JSON
        except:
            print("Nada seleccionado.")

    def editarContacto(self, count):
        try:
            self.newWindow = QtWidgets.QWidget()
            self.editCont = Ui_windowEditContacto(contactos[self.fila])  # CREA
            self.editCont.setupUi(self.newWindow, self, count)
            self.newWindow.show()
            #self.cargarFilas()  # Recargamos la lista
        except:
            print("Nada seleccionado.")

    def cargarFilas(self):
        self.tableContactos.setRowCount(len(contactos))  # Calculamos el n° de filas
        self.row = 0
        # print("Woah!")
        for fila in contactos:
            self.tableContactos.setItem(self.row, 0, QtWidgets.QTableWidgetItem(contactos[self.row].getApeCon()))
            self.tableContactos.setItem(self.row, 1, QtWidgets.QTableWidgetItem(contactos[self.row].getNomCon()))
            self.tableContactos.setItem(self.row, 2, QtWidgets.QTableWidgetItem(contactos[self.row].getTelCon1()))
            self.tableContactos.setItem(self.row, 3, QtWidgets.QTableWidgetItem(contactos[self.row].getCorrCon1()))
            self.tableContactos.setItem(self.row, 4, QtWidgets.QTableWidgetItem(contactos[self.row].getTelCon2()))
            self.tableContactos.setItem(self.row, 5, QtWidgets.QTableWidgetItem(contactos[self.row].getCorrCon2()))
            if (contactos[self.row].getEtiCon() == '1'):  # Check Alumno
                self.tableContactos.setItem(self.row, 6, QtWidgets.QTableWidgetItem("Alumno"))
            elif (contactos[self.row].getEtiCon() == '2'):  # Check Profesor
                self.tableContactos.setItem(self.row, 6, QtWidgets.QTableWidgetItem("Profesor"))
            else:  # Check otro
                self.tableContactos.setItem(self.row, 6, QtWidgets.QTableWidgetItem("Otro"))

            self.row += 1

    def showNewCont(self, count):  # Aparece la ventana para añadir nuevo contacto
        self.newWindow = QtWidgets.QMainWindow()
        self.newCont = Ui_windowNewContacto()  # CREA
        self.newCont.setupUi(self.newWindow, self, count)
        self.newWindow.show()

    def showMaterias(self): #BROKEN
        self.newWindow = QtWidgets.QMainWindow()
        print("1")
        self.newCont = Ui_MainMateria_15_06.Ui_mainwindoMaterias()  # CREA
        print("2")
        self.newCont.setupUi(self.newWindow)
        print("3")
        self.newWindow.show()
        print("4")
        # MainWindow = QtWidgets.QMainWindow()
        # ui = Ui_MainMateria_15_06.Ui_mainwindoMaterias()
        # ui.setupUi(MainWindow)
        # MainWindow.show()

    def boton_config(self):
        print("editar usuario")
        self.window3 = QWidget()
        self.edit_window = Editar_WindowUsuario()
        self.edit_window.show()

    def cerrarSesion(self, MainWindow, count):
        QtCore.QTimer.singleShot(0, MainWindow.close) #  Cerramos la ventana
        self.guardarContactos(count) #  Guardamos cambios
        self.tableContactos.clear() #  Vaciamos tabla
        contactos.clear() #  Vaciamos lista de contactos
        self.window_sesion = QWidget() #  Reabrimos el asunto
        self.new_sesion = Main_window()
        self.new_sesion.show()

    def menuRecordatorios(self):
        self.window = MenuRecordatorio()
        self.window.show()

    def guardarContactos(self, count):
        print("guardarContactos")
        print(len(self.usuario["contactos"]))
        self.usuario["contactos"] = []  # Vaciamos los elementos para no duplicar con el append

        for contacto in contactos:  # Repasamos toda la lista contactos y formateamos sus elementos al JSON
            print("Guardando...")
            self.usuario["contactos"].append({"nombre": str(contacto.getNomCon()),
                                              "apellido": str(contacto.getApeCon()),
                                              "correo1": str(contacto.getCorrCon1()),
                                              "correo2": str(contacto.getCorrCon2()),
                                              "tel1": str(contacto.getTelCon1()),
                                              "tel2": str(contacto.getTelCon2()),
                                              "etiqueta": str(contacto.getEtiCon())})

        dump = json.dumps(self.usuario, indent=2)
        with open("Usuario"+str(count)+".json", 'w') as file:
            file.write(dump)
            file.close()
            print("Guardado exitoso")

    def cargarContactos(self, count):
        print("cargarContactos")
        with open("Usuario"+str(count)+".json", 'r') as file:
            self.usuario = json.load(file)
            print("JSON abierto")
            for contacto in self.usuario["contactos"]:
                print("Metiendo...")
                temp = Contacto()
                temp.nuevoContacto(contacto["nombre"],
                                   contacto["apellido"],
                                   contacto["correo1"],
                                   contacto["correo2"],
                                   contacto["tel1"],
                                   contacto["tel2"],
                                   contacto["etiqueta"])
                contactos.append(temp)
                # print(temp.getApeCon())
            #contactos.sort(reverse=False, key=lambda x: x.getApeCon())  # Se ordena alfabéticamente la lista por apellido
            file.close()
            print("Carga exitosa")
            # print(contactos[0])

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Agenda Plus"))
        self.irCalendario.setText(_translate("MainWindow", "Calendario"))
        self.textoContactos.setText(_translate("MainWindow", "Contactos"))
        self.irMaterias.setText(_translate("MainWindow", "Materias"))
        self.botonAddContacto.setText(_translate("MainWindow", "Nuevo Contacto"))
        self.botonCerrSes.setText(_translate("MainWindow", "Cerrar Sesión"))
        self.irRecordatorios.setText(_translate("MainWindow", "Recordatorio"))
        self.irContactos.setText(_translate("MainWindow", "Contactos"))
        self.botonConfig.setText(_translate("MainWindow", "Configuración"))

        self.labelRowSelect.setText(_translate("windowContactos", "Seleccionado: "))
        self.botonEliminarContacto.setText(_translate("windowContactos", "Eliminar"))
        self.botonEliminarContacto.setShortcut(_translate("windowContactos", "Del"))
        self.botonEditarContacto.setText(_translate("windowContactos", "Editar"))
        self.labelFiltros.setText(_translate("windowContactos", "Filtros:"))
        self.checkBoxFiltroAlumno.setText(_translate("windowContactos", "Alumno"))
        self.checkBoxFiltroProfesor.setText(_translate("windowContactos", "Profesor"))
        self.checkBoxFiltroOtro.setText(_translate("windowContactos", "Otro"))
        item = self.tableContactos.horizontalHeaderItem(0)
        item.setText(_translate("windowContactos", "Apellido(s)"))
        item = self.tableContactos.horizontalHeaderItem(1)
        item.setText(_translate("windowContactos", "Nombre(s)"))
        item = self.tableContactos.horizontalHeaderItem(2)
        item.setText(_translate("windowContactos", "Tel. Primario"))
        item = self.tableContactos.horizontalHeaderItem(3)
        item.setText(_translate("windowContactos", "Correo Primario"))
        item = self.tableContactos.horizontalHeaderItem(4)
        item.setText(_translate("windowContactos", "Tel. Secundario"))
        item = self.tableContactos.horizontalHeaderItem(5)
        item.setText(_translate("windowContactos", "Correo Secundario"))
        item = self.tableContactos.horizontalHeaderItem(6)
        item.setText(_translate("windowContactos", "Etiqueta"))
