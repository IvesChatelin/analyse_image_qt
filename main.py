# This Python file uses the following encoding: utf-8
import sys
from PIL import Image, ImageQt
import pyqtgraph as pg
import numpy as np
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QWidget, QLabel, QHBoxLayout, \
                                QMessageBox, QDialog, QDialogButtonBox, QVBoxLayout

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow

matplotlib.use("QtAgg")

class Window(QWidget):

    def __init__(self, image, largeur, hauteur):
        super().__init__()
        self.setGeometry(100,100,largeur,hauteur)
        layout = QHBoxLayout()
        self.label = QLabel("image")
        self.label.setPixmap(QPixmap(image))
        layout.addWidget(self.label)
        self.setLayout(layout)

class grapheHisto(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
      fig = Figure(figsize=(width, height), dpi=dpi)
      self.axes = fig.add_subplot(111)
      super().__init__(fig)

class MainWindow(QMainWindow):

    img_array = []
    img_gray_level = []
    img_bin = []

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def slot_connect(self):
        self.ui.actionfichier.triggered.connect(self.importImage)
        self.ui.actionenregistrer_sous.triggered.connect(self.importImage)
        self.ui.actionNiveau_de_gris.triggered.connect(self.niveau_de_gris)
        self.ui.btn_add.clicked.connect(self.addition)
        self.ui.btn_seuillage.clicked.connect(self.seuillage)
        self.ui.btn_reset.clicked.connect(self.reset)
        self.ui.btn_quitte.clicked.connect(self.quitte)

    #Ouvrir une image
    def importImage(self):
        fileName = QFileDialog.getOpenFileName(self)
        img = Image.open(fileName[0])
        self.img_array = np.array(img)
        if not self.img_array.flags.writeable:
            msg = QMessageBox(self)
            msg.setWindowTitle("erreur image")
            msg.setText("l'image n'est pas modifiable, chargez une autre image!")
            msg.show()
            print("ok")
        else:
            self.img_gray_level = []
            self.ui.label.setGeometry(30,30,self.img_array.shape[1], self.img_array.shape[0])
            self.ui.label.setPixmap(QPixmap(fileName[0]))
            self.ui.label.setScaledContents(True)

    #mettre l'image en niveau de gris
    def niveau_de_gris(self):
        if len(self.img_array) == 0:
            msg = QMessageBox(self)
            msg.setWindowTitle("image not found")
            msg.setText("vous devez ouvrir une image")
            msg.show()
        else:
            img_canal_red = self.img_array[:,:,0]
            self.img_gray_level = np.array(img_canal_red)
            img = Image.fromarray(self.img_gray_level)
            qimg = ImageQt.ImageQt(img)
            self.ui.label.setGeometry(30,30,self.img_gray_level.shape[1], self.img_gray_level.shape[0])
            self.ui.label.setPixmap(QPixmap(qimg))
            self.ui.label.setScaledContents(True)

    #binarisation
    def seuillage(self):
        if len(self.img_array) == 0:
            msg = QMessageBox(self)
            msg.setWindowTitle("image not found")
            msg.setText("vous devez ouvrir une image")
            msg.show()
        elif len(self.img_gray_level) == 0:
            msg = QMessageBox(self)
            msg.setWindowTitle("image gray not found")
            msg.setText("vous devez mettre l'image en niveau de gray")
            msg.show()
        else:
            seuil = self.img_gray_level.mean()
            for i in range(self.img_gray_level.shape[0]):
                for j in range(self.img_gray_level.shape[1]):
                    if (self.img_gray_level[i,j] < seuil):
                        self.img_gray_level[i,j] = 255
                    else:
                        self.img_gray_level[i,j] = 0
            img = Image.fromarray(self.img_gray_level)
            qimg = ImageQt.ImageQt(img)
            self.ui.label.setGeometry(30,30,self.img_gray_level.shape[1], self.img_gray_level.shape[0])
            self.ui.label.setPixmap(QPixmap(qimg))
            self.ui.label.setScaledContents(True)
            sc = grapheHisto(width=6, height=5, dpi=100)
            sc.axes.hist(self.img_gray_level)
            sc.show()

    #addition de deux images
    def addition(self):
        if len(self.img_array) == 0:
            msg = QMessageBox(self)
            msg.setWindowTitle("image not found")
            msg.setText("vous devez ouvrir une image")
            msg.show()
        else:
            fileName = QFileDialog.getOpenFileName(self)
            img = Image.open(fileName[0])
            img_array2 = np.array(img)
            self.window = Window(fileName[0], img_array2.shape[1], img_array2.shape[0])
            self.window.show()
            print("addition")

    #reset
    def reset(self):
        self.img_gray_level = []
        img = Image.fromarray(self.img_array)
        qimg = ImageQt.ImageQt(img)
        self.ui.label.setGeometry(30,30,self.img_array.shape[1], self.img_array.shape[0])
        self.ui.label.setPixmap(QPixmap(qimg))
        self.ui.label.setScaledContents(True)

    #quitter
    def quitte(self):
        qApp.quit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.slot_connect()
    widget.show()
    sys.exit(app.exec())
