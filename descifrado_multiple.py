from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout,QInputDialog, QMessageBox
from PyQt5.QtCore import Qt
import cifrado_cesar, cifrado_comun, cifrado_RSA, cifrado_AES
import sys

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("App_Des")
        self.resize(640,480)
        self.move(425,160)
        
        label = QLabel("Hola")
        self.label2 = QLabel("Adios")
        
        but_1 = QPushButton("Comun")
        but_2 = QPushButton("AES")
        but_3 = QPushButton("Cesar")
        but_4 = QPushButton("RSA")
        close_but = QPushButton("Cerrar")
        
        layout = QVBoxLayout()
        
        layout.addWidget(label)
        layout.addWidget(self.label2)
        layout.addWidget(but_1)
        layout.addWidget(but_2)
        layout.addWidget(but_3)
        layout.addWidget(but_4)
        layout.addWidget(close_but)

        self.setLayout(layout)

        but_1.clicked.connect(self.Comun)
        but_2.clicked.connect(self.AES)
        but_3.clicked.connect(self.Cesar)
        but_4.clicked.connect(self.RSA)
        close_but.clicked.connect(self.close)
        
    def AES(self):
        aes, ok = QtWidgets.QInputDialog.getInt(self, "queso", '1:cifrar/2:descifrar')
        if ok:
            if aes == 1:
                cf, ok = QtWidgets.QInputDialog.getText(self, 'encrypt', 'mensaje a encriptar: ')
                a = cifrado_AES.encrypt(cf)
                self.label2.setText(f"Mensaje encriptado: {a}")
                print(a.hex())
            elif aes == 2:
                df, ok = QtWidgets.QInputDialog.getText(self, 'decrypt', 'mensaje: ')
                k, ok = QtWidgets.QInputDialog.getText(self, 'Llave', 'Ingrese la Llave: ')
                e = cifrado_AES.decrypt(k,df)
                self.label2.setText(f'mensaje desencriptado: {e}')
        else:
            self.label2.setText("Operation cancelled")
        
    def Cesar(self):
        cif_1, ok = QtWidgets.QInputDialog.getInt(self, 'Hola', '1:cifrar/2:descifrar')
        if ok:
            if cif_1 == 1:
                cf, ok = QtWidgets.QInputDialog.getText(self,"cifrar", "mensaje a cifrar")
                m_v, ok = QtWidgets.QInputDialog.getInt(self, "moving value", "Numero del cifrado cesar: ")
                a = cifrado_cesar.cifrado_cesar(cf,m_v)
                self.label2.setText(f'Mensaje cifrado: {a}')
            elif cif_1 == 2:
                df, ok = QtWidgets.QInputDialog.getText(self,"descifrar", "inserte el mensaje cifrado: ")
                dm_v, ok = QtWidgets.QInputDialog.getInt(self, "decrypt moving value", "Numero del cifrado cesar: ")
                a = cifrado_cesar.descifrado_de_cesar(df, dm_v)
                self.label2.setText(f'Mensaje descifrado: {a}')       
        else: 
            self.label2.setText("Operation cancelled")
        
    def Comun(self):
        comun, ok = QtWidgets.QInputDialog.getInt(self, "Nose", '1:cifrar/2:descifrar')
        if ok:
            if comun == 1:
                cf, ok = QtWidgets.QInputDialog.getText(self, "cifrar", "Elige tu mensaje a cifrar")
                c, ky = cifrado_comun.cryptografy(cf)
                self.label2.setText(f"""Mensaje cifrado: {c} 
Llave de acceso: {ky}""")
                print(c,ky)
            elif comun == 2:
                df, ok = QtWidgets.QInputDialog.getText(self, 'descifrar', 'Inserta el mensaje a descifrar: ')
                k, ok =  QtWidgets.QInputDialog.getText(self, 'Llave', 'Inserte clave entregada')
                c = cifrado_comun.decryptografy(df, k)
                self.label2.setText(f'Mensaje descifrado: {c}')
        else:
            self.label2.setText("Operation cancelled")

    def RSA(self):
        rsa, ok = QtWidgets.QInputDialog.getInt(self, 'ay miguel', '1:cifrar/2:descifrar')
        if ok:
            if rsa == 1:
                cf, ok = QtWidgets.QInputDialog.getText(self, 'cifrar', 'Mensaje que quieres encriptar: ')
                k, ok = QtWidgets.QInputDialog.getInt(self, 'Llave', 'Elija su clave: ')
                c, m = cifrado_RSA.rsa_e(cf, k)
                self.label2.setText(f'''Mensaje encriptado: {c}
Llave de acceso: {m}''')
            elif rsa == 2:
                df, ok = QtWidgets.QInputDialog.getInt(self, 'descifrar','Mensaje encriptado: ')
                key, ok = QtWidgets.QInputDialog.getInt(self, 'Llave','Inserte clave: ')
                rs = cifrado_RSA.rsa_d(df, key)
                self.label2.setText(f"el mensaje descifrado fue: {rs}")
        else:
            self.label2.setText("Operation cancelled")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()