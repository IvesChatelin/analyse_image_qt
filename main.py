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
        self.ui.btn_soust.clicked.connect(self.soustraction)
        self.ui.btn_seuillage.clicked.connect(self.seuillage)
        self.ui.btn_reset.clicked.connect(self.reset)
        self.ui.btn_quitte.clicked.connect(self.quitte)
        self.ui.actionenregistrer_sous.triggered.connect(self.enregistre)
        self.ui.btn_erosion.clicked.connect(self.erosion)
        self.ui.btn_dilatation.clicked.connect(self.dilatation)
        self.ui.btn_ouverture.clicked.connect(self.ouverture)
        self.ui.btn_fermeture.clicked.connect(self.fermeture)
        self.ui.btn_amin.clicked.connect(self.amincissement)
        self.ui.btn_epai.clicked.connect(self.epaississement)
        self.ui.btn_squelette.clicked.connect(self.squelette)

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
            self.img_bin = []
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
            self.img_bin = np.array(self.img_gray_level)
            seuil = self.img_bin.mean()
            for i in range(self.img_bin.shape[0]):
                for j in range(self.img_bin.shape[1]):
                    if (self.img_bin[i,j] < seuil):
                        self.img_bin[i,j] = 255
                    else:
                        self.img_bin[i,j] = 0
            img = Image.fromarray(self.img_bin)
            qimg = ImageQt.ImageQt(img)
            self.ui.label.setGeometry(30,30,self.img_bin.shape[1], self.img_bin.shape[0])
            self.ui.label.setPixmap(QPixmap(qimg))
            self.ui.label.setScaledContents(True)
            #histogramme
            ht = grapheHisto(width=6, height=5, dpi=100)
            ht.axes.hist(self.img_bin)
            ht.show()

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
            if img_array2.shape != self.img_array.shape:
                msg = QMessageBox(self)
                msg.setWindowTitle("erreur size image")
                msg.setText("les deux images n'ont pas la même taille")
                msg.show()
            else:
                #composante de l'image 1
                img1_red = self.img_array[:,:,0]
                img1_green = self.img_array[:,:,1]
                img1_blue = self.img_array[:,:,2]

                #composante de l'image 2
                img2_red = img_array2[:,:,0]
                img2_green = img_array2[:,:,1]
                img2_blue = img_array2[:,:,2]

                som_red = img1_red + img2_red
                som_green = img1_green + img2_green
                som_blue = img1_blue + img2_blue

                img_add = np.dstack((som_red,som_green,som_blue))
                img = Image.fromarray(img_add)
                qimg = ImageQt.ImageQt(img)

                self.ui.label.setGeometry(30,30,img_add.shape[1], img_add.shape[0])
                self.ui.label.setPixmap(QPixmap(qimg))
                self.ui.label.setScaledContents(True)
                self.window = Window(fileName[0], img_array2.shape[1], img_array2.shape[0])
                self.window.show()

    #soustraction deux images
    def soustraction(self):
        if len(self.img_array) == 0:
            msg = QMessageBox(self)
            msg.setWindowTitle("image not found")
            msg.setText("vous devez ouvrir une image")
            msg.show()
        else:
            fileName = QFileDialog.getOpenFileName(self)
            img = Image.open(fileName[0])
            img_array2 = np.array(img)
            if img_array2.shape != self.img_array.shape:
                msg = QMessageBox(self)
                msg.setWindowTitle("erreur size image")
                msg.setText("les deux images n'ont pas la même taille")
                msg.show()
            else:
                #composante de l'image 1
                img1_red = self.img_array[:,:,0]
                img1_green = self.img_array[:,:,1]
                img1_blue = self.img_array[:,:,2]
                #composante de l'image 2
                img2_red = img_array2[:,:,0]
                img2_green = img_array2[:,:,1]
                img2_blue = img_array2[:,:,2]

                som_red = np.absolute(img1_red - img2_red)
                som_green = np.absolute(img1_green - img2_green)
                som_blue = np.absolute(img1_blue - img2_blue)

                img_add = np.dstack((som_red,som_green,som_blue))
                img = Image.fromarray(img_add)
                qimg = ImageQt.ImageQt(img)
                self.ui.label.setGeometry(30,30,img_add.shape[1], img_add.shape[0])
                self.ui.label.setPixmap(QPixmap(qimg))
                self.ui.label.setScaledContents(True)
                self.window = Window(fileName[0], img_array2.shape[1], img_array2.shape[0])
                self.window.show()

    #Erosion
    def erosion(self):
        if len(self.img_bin) == 0:
            msg = QMessageBox(self)
            msg.setWindowTitle("image error")
            msg.setText("vous devez d'abord effectuer un seuillage")
            msg.show()
        else:
            img_ero = np.array(self.img_bin)

            # element structurant à 8 connexité
            struc = np.array([[255,0,255],
                              [0,255,0],
                              [255,0,255]])

            for i in range(1, self.img_bin.shape[0]-1):
                for j in range(1, self.img_bin.shape[1]-1):
                    som = 0
                    for t in range(-1, struc.shape[0]-1):
                        for k in range(-1, struc.shape[1]-1):
                            som += self.img_bin[i+t, j+k]
                    if som == struc.sum():
                        img_ero[i,j] = 255
                    else:
                        img_ero[i,j] = 0

            img = Image.fromarray(img_ero)
            qimg = ImageQt.ImageQt(img)
            self.ui.label.setGeometry(30,30,img_ero.shape[1], img_ero.shape[0])
            self.ui.label.setPixmap(QPixmap(qimg))
            self.ui.label.setScaledContents(True)

    #dilatation
    def dilatation(self):
        if len(self.img_bin) == 0:
            msg = QMessageBox(self)
            msg.setWindowTitle("image error")
            msg.setText("vous devez d'abord effectuer un seuillage")
            msg.show()
        else:
            img_dilat = np.array(self.img_bin)
            # element structurant à 8 connexité
            struc = np.array([[255,0,255],
                              [0,255,0],
                              [255,0,255]])

            for i in range(1, self.img_bin.shape[0]-1):
                for j in range(1, self.img_bin.shape[1]-1):
                    som = 0
                    for t in range(-1, struc.shape[0]-1):
                        for k in range(-1, struc.shape[0]-1):
                            som += self.img_bin[i+t, j+k]
                    if som != 0:
                        img_dilat[i,j] = 255
                    else:
                        img_dilat[i,j] = 0

            img = Image.fromarray(img_dilat)
            qimg = ImageQt.ImageQt(img)
            self.ui.label.setGeometry(30,30,img_dilat.shape[1], img_dilat.shape[0])
            self.ui.label.setPixmap(QPixmap(qimg))
            self.ui.label.setScaledContents(True)

    #ouverture
    def ouverture(self):
        if len(self.img_bin) == 0:
            msg = QMessageBox(self)
            msg.setWindowTitle("image error")
            msg.setText("vous devez d'abord effectuer un seuillage")
            msg.show()
        else:
            #erosion
            img_ero = np.array(self.img_bin)

            # element structurant à 8 connexité
            struc = np.array([[255,0,255],
                              [0,255,0],
                              [255,0,255]])

            for i in range(1, self.img_bin.shape[0]-1):
                for j in range(1, self.img_bin.shape[1]-1):
                    som = 0
                    for t in range(-1, struc.shape[0]-1):
                        for k in range(-1, struc.shape[1]-1):
                            som += self.img_bin[i+t, j+k]
                    if som == struc.sum():
                        img_ero[i,j] = 255
                    else:
                        img_ero[i,j] = 0

            #dilation de l'erodé
            img_dilat = np.array(img_ero)
            # element structurant symetrique à 8 connexité
            struc = np.array([[255,0,255],
                              [0,255,0],
                              [255,0,255]])

            for i in range(1, img_ero.shape[0]-1):
                for j in range(1, img_ero.shape[1]-1):
                    som = 0
                    for t in range(-1, struc.shape[0]-1):
                        for k in range(-1, struc.shape[0]-1):
                            som += img_ero[i+t, j+k]
                    if som != 0:
                        img_dilat[i,j] = 255
                    else:
                        img_dilat[i,j] = 0

            img = Image.fromarray(img_dilat)
            qimg = ImageQt.ImageQt(img)
            self.ui.label.setGeometry(30,30,img_dilat.shape[1], img_dilat.shape[0])
            self.ui.label.setPixmap(QPixmap(qimg))
            self.ui.label.setScaledContents(True)


    #fermeture
    def fermeture(self):
        if len(self.img_bin) == 0:
            msg = QMessageBox(self)
            msg.setWindowTitle("image error")
            msg.setText("vous devez d'abord effectuer un seuillage")
            msg.show()
        else:
            #dilatation
            img_dilat = np.array(self.img_bin)
            # element structurant symetrique à 8 connexité
            struc = np.array([[255,0,255],
                              [0,255,0],
                              [255,0,255]])

            for i in range(1, self.img_bin.shape[0]-1):
                for j in range(1, self.img_bin.shape[1]-1):
                    som = 0
                    for t in range(-1, struc.shape[0]-1):
                        for k in range(-1, struc.shape[0]-1):
                            som += self.img_bin[i+t, j+k]
                    if som != 0:
                        img_dilat[i,j] = 255
                    else:
                        img_dilat[i,j] = 0

            #erosion
            img_ero = np.array(img_dilat)
            for i in range(1, img_dilat.shape[0]-1):
                for j in range(1, img_dilat.shape[1]-1):
                    som = 0
                    for t in range(-1, struc.shape[0]-1):
                        for k in range(-1, struc.shape[1]-1):
                            som += img_dilat[i+t, j+k]
                    if som == struc.sum():
                        img_ero[i,j] = 255
                    else:
                        img_ero[i,j] = 0

            img = Image.fromarray(img_ero)
            qimg = ImageQt.ImageQt(img)
            self.ui.label.setGeometry(30,30,img_ero.shape[1], img_ero.shape[0])
            self.ui.label.setPixmap(QPixmap(qimg))
            self.ui.label.setScaledContents(True)

    #amincissement
    def amincissement(self):
        if len(self.img_bin) == 0:
            msg = QMessageBox(self)
            msg.setWindowTitle("image error")
            msg.setText("vous devez d'abord effectuer un seuillage")
            msg.show()
        else:
            img_aminc = np.array(self.img_bin)
            config = np.array([[255,0,255],
                              [0,255,0],
                              [255,0,255]])

            for i in range(1, self.img_bin.shape[0]-1):
                for j in range(1, self.img_bin.shape[1]-1):
                    bool = False
                    for t in range(-1, config.shape[0]-1):
                        for k in range(-1, config.shape[1]-1):
                            if self.img_bin[i+t, j+k] == config[t,k]:
                                bool = True
                            else:
                                bool = False
                    if bool :
                        img_aminc[i,j] = 0

            img = Image.fromarray(img_aminc)
            qimg = ImageQt.ImageQt(img)
            self.ui.label.setGeometry(30,30,img_aminc.shape[1], img_aminc.shape[0])
            self.ui.label.setPixmap(QPixmap(qimg))
            self.ui.label.setScaledContents(True)

    #epaississement
    def epaississement(self):
        if len(self.img_bin) == 0:
            msg = QMessageBox(self)
            msg.setWindowTitle("image error")
            msg.setText("vous devez d'abord effectuer un seuillage")
            msg.show()
        else:
            img_aminc = np.array(self.img_bin)
            config = np.array([[255,0,255],
                              [0,255,0],
                              [255,0,255]])

            for i in range(1, self.img_bin.shape[0]-1):
                for j in range(1, self.img_bin.shape[1]-1):
                    bool = False
                    for t in range(-1, config.shape[0]-1):
                        for k in range(-1, config.shape[1]-1):
                            if self.img_bin[i+t, j+k] == config[t,k]:
                                bool = True
                            else:
                                bool = False
                    if bool :
                        img_aminc[i,j] = 255

            img = Image.fromarray(img_aminc)
            qimg = ImageQt.ImageQt(img)
            self.ui.label.setGeometry(30,30,img_aminc.shape[1], img_aminc.shape[0])
            self.ui.label.setPixmap(QPixmap(qimg))
            self.ui.label.setScaledContents(True)

    #spuelette
    def squelette(self):
        if len(self.img_bin) == 0:
            msg = QMessageBox(self)
            msg.setWindowTitle("image error")
            msg.setText("vous devez d'abord effectuer un seuillage")
            msg.show()
        else:
            img_sqlt = np.array(self.img_bin)
            h = 3
            l = 3
            taille_boule = h * l
            while h < self.img_bin.shape[0]-2 and l < self.img_bin.shape[1]-2:
                for i in range(1, self.img_bin.shape[0]-1):
                    for j in range(1, self.img_bin.shape[1]-1):
                        som = 0
                        frontiere = 0
                        for t in range(-1, h-1):
                            for k in range(-1, l-1):
                                if (i+t == 0 or j+k == 0) or (i+t == 1 or j+k == 1):
                                    frontiere += 1
                                som += self.img_bin[i+t, j+k]
                        if frontiere >= 2:
                            if som == taille_boule*255:
                                img_sqlt[i,j] = 255
                                for t in range(-1, l-1):
                                    for k in range(-1, h-1):
                                        img_sqlt[i+t, j+k] = 0
                h += 1
                l += 1
            img = Image.fromarray(img_sqlt)
            qimg = ImageQt.ImageQt(img)
            self.ui.label.setGeometry(30,30,img_sqlt.shape[1], img_sqlt.shape[0])
            self.ui.label.setPixmap(QPixmap(qimg))
            self.ui.label.setScaledContents(True)

    #reset
    def reset(self):
        self.img_gray_level = []
        self.img_bin = []
        img = Image.fromarray(self.img_array)
        qimg = ImageQt.ImageQt(img)
        self.ui.label.setGeometry(30,30,self.img_array.shape[1], self.img_array.shape[0])
        self.ui.label.setPixmap(QPixmap(qimg))
        self.ui.label.setScaledContents(True)

    #enregistre
    def enregistre(self):
        # pas encore au point
        fileName= QFileDialog.getSaveFileName(
            self, "Save Image", "", "All Files (*)"
        )

    #quitter
    def quitte(self):
        qApp.quit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.slot_connect()
    widget.show()
    sys.exit(app.exec())
