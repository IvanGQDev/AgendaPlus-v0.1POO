from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
#from PySide2.QtWidgets import QMainWindow, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
import json, UI_MainContactos
from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random


class Sesion:
    def __init__(self, sesion=''):
        self.__sesion = sesion

    def to_json(self):
        return {
            "sesion": self.__sesion
        }
    
    @property
    def sesion(self):
        return self.__sesion

    @sesion.setter
    def sesion(self, value):
        self.__sesion = value

class Administrar_sesion:
    def __init__(self):
        self.sesion = []

    def agregarSesion(self, user):
        self.sesion.append(user)
    
    def guardar(self, ubicacion):
        try:
            with open(ubicacion, 'w') as archivo:
                sesionDiccionario =[sesion.to_json() for sesion in self.sesion]
                json.dump(sesionDiccionario ,archivo, indent = 4)
                sesionDiccionario.close()
            return 1
        except:
            return 0
    
    def abrir(self, ubicacion):
        try:
            with open(ubicacion, 'r') as archivo:
                sesionDiccionario = json.load(archivo)
                self.sesion = [Sesion(**sesionj) for sesionj in sesionDiccionario]
                sesionDiccionario.close(archivo)
            return 1
        except:
            return 0



class Usuario:  # usuario.py
    def __init__(self, nombre='', contrasena=0, email=''):
        self.__nombre = nombre
        self.__contrasena = contrasena
        self.__email = email

    def __lt__(self, other):
        return self.__nombre < other.__nombre

    def mostrar(self):
        print(f"Usuario: \nNombre:{self.__nombre} \nContraseña: {self.__contrasena} \nEmail:{self.__email}")

    def __str__(self) -> str:
        return f"Usuario: \nNombre:{self.__nombre} \nContraseña: {self.__contrasena} \nEmail:{self.__email}"

    def to_json(self):
        return {
            "nombre": self.__nombre,
            "contrasena": self.__contrasena,
            "email": self.__email
        }

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, value):
        self.__nombre = value

    @property
    def contrasena(self):
        return self.__contrasena

    @contrasena.setter
    def contrasena(self, value):
        self.__contrasena = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value


class Administrar:  # administrar.py
    def __init__(self):
        self.usuarios = []
        self.dicUsuarios = {}

    def __len__(self):
        return len(self.usuarios)

    def validarNumeroUsuarios(self):
        if self.__len__() < 3:
            return True
        else:
            print("No se pueden agregar mas usuarios.")
            return False

    def modificarUsuario(self, id, usuario):
        self.usuarios[id] = usuario

    def modificarContrasena(self, contra, email):
        for usuario in self.usuarios:
            if email == usuario.email:
                usuario.contrasena = contra

    def insertarUsuario(self, usuario):
        self.usuarios.append(usuario)
        self.ordenarNombre()
        print("Se agrego correctamente.")

    def eliminarUsuario(self, id):
        self.usuarios.pop(id)

    def ordenarNombre(self):
        self.usuarios.sort()

    def mostrarUsuarios(self):
        if self.__len__() == 0:
            print("No hay usuarios Registrados")
        else:
            n = 1
            for u in self.usuarios:
                print("Id = ", n)
                u.mostrar()
                print('\n')
                n += 1

    def __str__(self):
        return "".join(str(usuario) + "\n" for usuario in self.usuarios)

    def guardar(self, ubicacion):
        try:
            with open(ubicacion, 'w') as usuariosLista:
                listaUsuariosJson = [usuario.to_json() for usuario in self.usuarios]
                json.dump(listaUsuariosJson, usuariosLista, indent=4)
                usuariosLista.close()
            return 1
        except:
            return 0

    def abrir(self, ubicacion):
        try:
            with open(ubicacion, 'r') as usuariosLista:
                listaDirectorios = json.load(usuariosLista)
                self.usuarios = [Usuario(**usuarioj) for usuarioj in listaDirectorios]
                usuariosLista.close()
            return 1
        except:
            return 0

class Ui_EditarUsuario(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(415, 400)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(130, 30, 47, 13))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(130, 90, 47, 13))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(130, 150, 61, 20))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(130, 220, 91, 20))
        self.editar_usuario_lineEdit = QLineEdit(self.centralwidget)
        self.editar_usuario_lineEdit.setObjectName(u"editar_usuario_lineEdit")
        self.editar_usuario_lineEdit.setGeometry(QRect(130, 50, 161, 20))
        self.editar_email_lineEdit = QLineEdit(self.centralwidget)
        self.editar_email_lineEdit.setObjectName(u"editar_email_lineEdit")
        self.editar_email_lineEdit.setGeometry(QRect(130, 110, 161, 20))
        self.editar_contrasena_lineEdit = QLineEdit(self.centralwidget)
        self.editar_contrasena_lineEdit.setObjectName(u"editar_contrasena_lineEdit")
        self.editar_contrasena_lineEdit.setGeometry(QRect(130, 180, 161, 20))
        self.editar_contrasena_lineEdit.setEchoMode(QLineEdit.Password)
        self.editar_repetir_contrasena_lineEdit = QLineEdit(self.centralwidget)
        self.editar_repetir_contrasena_lineEdit.setObjectName(u"editar_repetir_contrasena_lineEdit")
        self.editar_repetir_contrasena_lineEdit.setGeometry(QRect(130, 250, 161, 20))
        self.editar_repetir_contrasena_lineEdit.setEchoMode(QLineEdit.Password)
        self.editar_guardar_pushButton = QPushButton(self.centralwidget)
        self.editar_guardar_pushButton.setObjectName(u"editar_guardar_pushButton")
        self.editar_guardar_pushButton.setGeometry(QRect(130, 290, 75, 23))
        self.editar_cancelar_pushButton = QPushButton(self.centralwidget)
        self.editar_cancelar_pushButton.setObjectName(u"editar_cancelar_pushButton")
        self.editar_cancelar_pushButton.setGeometry(QRect(220, 290, 75, 23))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 415, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Editar Usuario", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Usuario", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Repita Contrase\u00f1a", None))
        self.editar_guardar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.editar_cancelar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
    # retranslateUi


class Editar_WindowUsuario(QMainWindow):
    def __init__(self):
        super(Editar_WindowUsuario,self).__init__()
        self.ui = Ui_EditarUsuario()
        self.ui.setupUi(self)
        self.admin = Administrar()
        self.adminSesion = Administrar_sesion()
        self.ui.editar_guardar_pushButton.clicked.connect(self.guardar_editado)       
        self.ui.editar_cancelar_pushButton.clicked.connect(self.cancelar_editado)
        self.admin.abrir("usuariosLista.json")
        self.adminSesion.abrir("sesion.json")
        self.nombre = self.adminSesion.sesion[0].sesion
        for user in self.admin.usuarios:
            if self.nombre == user.nombre:
                self.ui.editar_usuario_lineEdit.setText(user.nombre)
                self.ui.editar_email_lineEdit.setText(user.email)
                self.ui.editar_contrasena_lineEdit.setText(user.contrasena)
                self.ui.editar_repetir_contrasena_lineEdit.setText(user.contrasena)

    def guardar_editado(self):
        for user in self.admin.usuarios:
            if self.nombre == user.nombre:
                if self.ui.editar_contrasena_lineEdit.text() == self.ui.editar_repetir_contrasena_lineEdit.text():
                    user.email = self.ui.editar_email_lineEdit.text().lower()
                    user.nombre = self.ui.editar_usuario_lineEdit.text().lower()
                    user.contrasena = self.ui.editar_contrasena_lineEdit.text()
                    self.admin.guardar("usuariosLista.json")
                    QMessageBox.information(self,"Guardado", "Datos editados con exito")
                    self.close()
                else:
                    QMessageBox.critical(self,"Error","Contraseñas no conciden")
    def cancelar_editado(self):
        self.close()



class Ui_recuperar(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(361, 159)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.recuperar_lineEdit = QLineEdit(self.centralwidget)
        self.recuperar_lineEdit.setObjectName(u"recuperar_lineEdit")
        self.recuperar_lineEdit.setGeometry(QRect(70, 60, 221, 20))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(140, 30, 91, 16))
        self.enviar_correo_pushButton = QPushButton(self.centralwidget)
        self.enviar_correo_pushButton.setObjectName(u"enviar_correo_pushButton")
        self.enviar_correo_pushButton.setGeometry(QRect(150, 90, 75, 23))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 361, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Recuperar Contrase\u00f1a", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Ingrese su correo:", None))
        self.enviar_correo_pushButton.setText(QCoreApplication.translate("MainWindow", u"Recuperar", None))
    # retranslateUi

class Recuperar_window(QMainWindow):
    def __init__(self):
        super(Recuperar_window,self).__init__()
        self.ui = Ui_recuperar()
        self.ui.setupUi(self)
        self.admin = Administrar()
        self.admin.abrir("usuariosLista.json")
        self.ui.enviar_correo_pushButton.clicked.connect(self.enviar_correo)
    
    def enviar_correo(self):
        SMTP_HOSTNAME = "smtp.gmail.com"
        SMTP_TSL_PORT = 587
        SMTP_USER = "SoporteAgendaPlus@gmail.com"
        SMTP_PASSWORD = "xwkccnumosruiirr"

        class Email:
            def __init__(self):
                self.server = SMTP(
                    host = SMTP_HOSTNAME,
                    port = SMTP_TSL_PORT
                )

            def connect_server(self):
                self.server.starttls()
                self.server.login(
                    user = SMTP_USER,
                    password= SMTP_PASSWORD
                )

            def send_email(self, email, subject, **kwargs):
                self.connect_server()
                print("Sending email...")
                mime = MIMEMultipart()
                mime['From'] = SMTP_USER
                mime['To'] = email
                mime['Subject'] = subject
                format = MIMEText(kwargs['message_format'], kwargs['format'])
                mime.attach(format)
                try:
                    self.server.sendmail(SMTP_USER, email, mime.as_string())
                except Exception as e:
                    raise e
                finally:
                    self.disconnect_server()

            def disconnect_server(self):
                self.server.quit()
                self.server.close()

            def password_generate(self):
                password = ""
                simb2 = ['!', '@', "#", "$", "%", "^", "&", "*", "(", ')','+','-','[',']','{','}','?','/']
                letter2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u','v','w','x', 'y','z']
                numbers = ['1','2','3','4','5','6','7','8','9']

                lista = []
                numSimb = random.randint(2,4)
                for i in range(0, numSimb):
                    lista.append(random.choice(simb2))
                numNum = random.randint(2,4)
                for i in range(0, numNum):
                    lista.append(random.choice(numbers))
                numCaracteres = random.randint(2,4)
                for i in range(0, numCaracteres):
                    lista.append(random.choice(letter2))

                random.shuffle(lista)

                for i in range(0, len(lista)):
                    password += lista[i]

                return password

        html_format = """<center>
            <div style= "padding: 0%;
            margin:0%;
            width: 75%;
            height: 100%;
            border: 1px solid rgba(0,0,0,0.25);
            padding: 24px;
            border-radius: 25px;>
            <h1 style = "font=weight: 400;"> Hola <strong> {0}</strong> esta es tu contraseña: {1}</h1>
       
        </center>

        """
        
        name = self.ui.recuperar_lineEdit.text().lower()
        asociado = 0
        for usuario in self.admin.usuarios:
            if name == usuario.email:
                email = Email()
                contra = email.password_generate()
                email.send_email(name, "Peticion de contrasena", message_format= html_format.format(name.capitalize(),contra), format="html")
                self.admin.modificarContrasena(contra, name)
                self.admin.guardar("usuariosLista.json")
                self.ui.recuperar_lineEdit.clear()
                QMessageBox.information(self,"Enviado", "Contraseña Enviada")
                self.close()
                asociado = 1
        if asociado == 0:
            QMessageBox.critical(self, "Error", "Correo no asociado")



class Ui_registro(object):  # ui_registro.py
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(400, 340)
        MainWindow.setMinimumSize(QSize(400, 340))
        MainWindow.setMaximumSize(QSize(400, 340))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.nombre_usuario_lineEdit = QLineEdit(self.centralwidget)
        self.nombre_usuario_lineEdit.setObjectName(u"nombre_usuario_lineEdit")
        self.nombre_usuario_lineEdit.setGeometry(QRect(110, 70, 181, 20))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(160, 10, 91, 20))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(110, 50, 111, 16))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(110, 170, 111, 16))
        self.contrasena_usuario_LineEdit = QLineEdit(self.centralwidget)
        self.contrasena_usuario_LineEdit.setObjectName(u"contrasena_usuario_LineEdit")
        self.contrasena_usuario_LineEdit.setGeometry(QRect(110, 190, 181, 20))
        self.contrasena_usuario_LineEdit.setEchoMode(QLineEdit.Password)
        self.contrasena_confirmar_lineEdit = QLineEdit(self.centralwidget)
        self.contrasena_confirmar_lineEdit.setObjectName(u"contrasena_confirmar_lineEdit")
        self.contrasena_confirmar_lineEdit.setGeometry(QRect(110, 250, 181, 20))
        self.contrasena_confirmar_lineEdit.setEchoMode(QLineEdit.Password)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(110, 230, 111, 16))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(110, 110, 47, 13))
        self.email_usuario_lineEdit = QLineEdit(self.centralwidget)
        self.email_usuario_lineEdit.setObjectName(u"email_usuario_lineEdit")
        self.email_usuario_lineEdit.setGeometry(QRect(110, 130, 181, 20))
        self.registrar_usuario_pushButton = QPushButton(self.centralwidget)
        self.registrar_usuario_pushButton.setObjectName(u"registrar_usuario_pushButton")
        self.registrar_usuario_pushButton.setGeometry(QRect(110, 290, 75, 23))
        self.cancelar_usuario_pushButton = QPushButton(self.centralwidget)
        self.cancelar_usuario_pushButton.setObjectName(u"cancelar_usuario_pushButton")
        self.cancelar_usuario_pushButton.setGeometry(QRect(220, 290, 75, 23))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.nombre_usuario_lineEdit, self.email_usuario_lineEdit)
        QWidget.setTabOrder(self.email_usuario_lineEdit, self.contrasena_usuario_LineEdit)
        QWidget.setTabOrder(self.contrasena_usuario_LineEdit, self.contrasena_confirmar_lineEdit)
        QWidget.setTabOrder(self.contrasena_confirmar_lineEdit, self.registrar_usuario_pushButton)
        QWidget.setTabOrder(self.registrar_usuario_pushButton, self.cancelar_usuario_pushButton)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Registrar usuario", None))
        self.nombre_usuario_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ej.Usuario_123@", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Registrar Usuario", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Nombre de suario", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Repita Contrase\u00f1a", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"E-mail", None))
        self.email_usuario_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"usuario@gmail.com", None))
        self.registrar_usuario_pushButton.setText(QCoreApplication.translate("MainWindow", u"Registrar", None))
        self.cancelar_usuario_pushButton.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
    # retranslateUi


class Registro_window(QMainWindow):  # registro_window.py
    def __init__(self):
        super(Registro_window, self).__init__()
        self.ui = Ui_registro()
        self.ui.setupUi(self)
        self.admin = Administrar()
        self.admin.abrir("usuariosLista.json")
        self.ui.registrar_usuario_pushButton.clicked.connect(self.click_registro)
        self.ui.cancelar_usuario_pushButton.clicked.connect(self.click_cancelar)

    def click_cancelar(self):
        self.close()

    def click_registro(self):

        if self.admin.validarNumeroUsuarios():
            name = self.ui.nombre_usuario_lineEdit.text().lower()
            contrasena = self.ui.contrasena_usuario_LineEdit.text()
            contrasena_repite = self.ui.contrasena_confirmar_lineEdit.text()
            email = self.ui.email_usuario_lineEdit.text()
            if contrasena == contrasena_repite:
                if "@" in email:
                    self.admin.insertarUsuario(Usuario(name, contrasena, email))
                    self.admin.guardar("usuariosLista.json")
                    self.admin.abrir("usuariosLista.json")

                    self.close()
                    QMessageBox.information(self, "Registro", "Datos correctos")
                else:
                    QMessageBox.critical(self, "Incorrecto", "Email no valido")
            else:
                QMessageBox.critical(self, "Incorrecto", "Contraseñas no coincides")
        else:
            QMessageBox.critical(self, "Error", "Numero Maximo de usuarios alcanzado")


class Ui_login(object):  # ui_login.py
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 500)
        MainWindow.setMinimumSize(QSize(800, 500))
        MainWindow.setMaximumSize(QSize(800, 500))
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 811, 501))
        self.frame.setStyleSheet(u"background-image: url(sea.jpg);\n"
"background-position: left;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 210, 171, 41))
        font = QFont()
        font.setPointSize(21)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background: off;")
        self.Usuario_lineEdit = QLineEdit(self.frame)
        self.Usuario_lineEdit.setObjectName(u"Usuario_lineEdit")
        self.Usuario_lineEdit.setGeometry(QRect(20, 290, 121, 20))
        self.Usuario_lineEdit.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"border:off;\n"
"")
        self.line_2 = QFrame(self.frame)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(20, 370, 118, 3))
        self.line_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.registrarme_pushButton = QPushButton(self.frame)
        self.registrarme_pushButton.setObjectName(u"registrarme_pushButton")
        self.registrarme_pushButton.setGeometry(QRect(190, 430, 101, 31))
        font1 = QFont()
        font1.setPointSize(12)
        self.registrarme_pushButton.setFont(font1)
        self.registrarme_pushButton.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 127);")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 330, 91, 16))
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background: off;")
        self.line = QFrame(self.frame)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(20, 310, 118, 3))
        self.line.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 260, 61, 16))
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background: off;")
        self.Entrar_pushButton = QPushButton(self.frame)
        self.Entrar_pushButton.setObjectName(u"Entrar_pushButton")
        self.Entrar_pushButton.setGeometry(QRect(20, 430, 61, 31))
        self.Entrar_pushButton.setFont(font1)
        self.Entrar_pushButton.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 0, 255);")
        self.Contrasena_lineEdit = QLineEdit(self.frame)
        self.Contrasena_lineEdit.setObjectName(u"Contrasena_lineEdit")
        self.Contrasena_lineEdit.setGeometry(QRect(20, 350, 121, 20))
        self.Contrasena_lineEdit.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: off;\n"
"background-color: rgb(0, 0, 0);")
        self.Contrasena_lineEdit.setEchoMode(QLineEdit.Password)
        self.Salir_pushButton = QPushButton(self.frame)
        self.Salir_pushButton.setObjectName(u"Salir_pushButton")
        self.Salir_pushButton.setGeometry(QRect(100, 430, 61, 31))
        self.Salir_pushButton.setFont(font1)
        self.Salir_pushButton.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 0, 127);\n"
"")
        self.refrescar_pushButton = QPushButton(self.frame)
        self.refrescar_pushButton.setObjectName(u"refrescar_pushButton")
        self.refrescar_pushButton.setGeometry(QRect(314, 430, 81, 31))
        font2 = QFont()
        font2.setPointSize(11)
        self.refrescar_pushButton.setFont(font2)
        self.refrescar_pushButton.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.contrasena_olvidada_pushButton = QPushButton(self.frame)
        self.contrasena_olvidada_pushButton.setObjectName(u"contrasena_olvidada_pushButton")
        self.contrasena_olvidada_pushButton.setGeometry(QRect(10, 390, 121, 23))
        self.contrasena_olvidada_pushButton.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: off;")
        self.label.raise_()
        self.Usuario_lineEdit.raise_()
        self.line_2.raise_()
        self.label_3.raise_()
        self.line.raise_()
        self.label_2.raise_()
        self.Contrasena_lineEdit.raise_()
        self.Entrar_pushButton.raise_()
        self.Salir_pushButton.raise_()
        self.registrarme_pushButton.raise_()
        self.refrescar_pushButton.raise_()
        self.contrasena_olvidada_pushButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.Usuario_lineEdit, self.Contrasena_lineEdit)
        QWidget.setTabOrder(self.Contrasena_lineEdit, self.Entrar_pushButton)
        QWidget.setTabOrder(self.Entrar_pushButton, self.Salir_pushButton)
        QWidget.setTabOrder(self.Salir_pushButton, self.registrarme_pushButton)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Agenda Plus", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Iniciar Sesion", None))
        self.Usuario_lineEdit.setText("")
        self.registrarme_pushButton.setText(QCoreApplication.translate("MainWindow", u"Registrarme", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a: ", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Usuario:", None))
        self.Entrar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Entrar", None))
        self.Contrasena_lineEdit.setText("")
        self.Salir_pushButton.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
        self.refrescar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Refrescar", None))
        self.contrasena_olvidada_pushButton.setText(QCoreApplication.translate("MainWindow", u"Olvide mi contrase\u00f1a", None))
    # retranslateUi


class Main_window(QMainWindow):  # main_window.py
    def __init__(self):
        super(Main_window,self).__init__()
        self.ui = Ui_login()
        self.ui.setupUi(self)
        self.admin = Administrar()
        self.administrarSesion = Administrar_sesion()
        self.ui.Entrar_pushButton.clicked.connect(self.click_entrar)
        self.ui.registrarme_pushButton.clicked.connect(self.click_registrarme)
        self.ui.Salir_pushButton.clicked.connect(self.click_salir)
        self.ui.refrescar_pushButton.clicked.connect(self.click_refrescar)
        self.ui.contrasena_olvidada_pushButton.clicked.connect(self.click_recuperar)
        direccion = "usuariosLista.json"
        if self.admin.abrir(direccion):
            print("Se cargaron los datos exitosamente")
         

        self.admin.mostrarUsuarios()
    
    def click_recuperar(self):
        self.window_recuperar = QWidget()
        self.new_recuperar = Recuperar_window()
        self.new_recuperar.show()


    def click_salir(self):
        self.close()

    def click_registrarme(self):
        self.window2 = QWidget()
        #window2 = MainWindow()
        self.new_window = Registro_window()
        if self.admin.validarNumeroUsuarios():
            self.new_window.show()
        else:
            QMessageBox.critical(self, "Error", "Numero Maximo de usuarios alcanzado")

    def click_refrescar(self):
        self.admin.abrir("usuariosLista.json")

    def click_entrar(self):
        #self.acceso = False
        usuario = self.ui.Usuario_lineEdit.text().lower()
        contrasena = self.ui.Contrasena_lineEdit.text()
        encontrado = 0
        count = 0
        for person in self.admin.usuarios:
            if person.nombre == usuario:
                encontrado = 1
                if person.contrasena == contrasena:
                    #QMessageBox.information(self, "Acceso", "Datos correctos")
                    self.administrarSesion.agregarSesion(Sesion(person.nombre))
                    self.administrarSesion.guardar("sesion.json")
                    print("acceso")
                    self.close()
                    self.MainWindow = QtWidgets.QMainWindow()
                    self.ui = UI_MainContactos.Ui_MainWindow()
                    print("Count:",count)
                    self.ui.setupUi(self.MainWindow,count)
                    self.MainWindow.show()
                else:
                    print("Vuelva a intentarlo")
                    QMessageBox()
                    QMessageBox.critical(self, "Incorrecto","Contraseña Incorrecta")
            count+=1

        if encontrado == 0:
            QMessageBox.critical(self, "Incorrecto", "Usuario no registrado" )
        else:
            encontrado = 0

