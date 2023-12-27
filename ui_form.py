# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QSpinBox, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1102, 643)
        self.actionfichier = QAction(MainWindow)
        self.actionfichier.setObjectName(u"actionfichier")
        self.actionfichier.setCheckable(False)
        self.actionenregistrer_sous = QAction(MainWindow)
        self.actionenregistrer_sous.setObjectName(u"actionenregistrer_sous")
        self.actionNiveau_de_gris = QAction(MainWindow)
        self.actionNiveau_de_gris.setObjectName(u"actionNiveau_de_gris")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.grbox_action = QGroupBox(self.centralwidget)
        self.grbox_action.setObjectName(u"grbox_action")
        self.verticalLayout = QVBoxLayout(self.grbox_action)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btn_seuillage = QPushButton(self.grbox_action)
        self.btn_seuillage.setObjectName(u"btn_seuillage")

        self.verticalLayout.addWidget(self.btn_seuillage)

        self.btn_add = QPushButton(self.grbox_action)
        self.btn_add.setObjectName(u"btn_add")

        self.verticalLayout.addWidget(self.btn_add)

        self.btn_soust = QPushButton(self.grbox_action)
        self.btn_soust.setObjectName(u"btn_soust")

        self.verticalLayout.addWidget(self.btn_soust)

        self.btn_erosion = QPushButton(self.grbox_action)
        self.btn_erosion.setObjectName(u"btn_erosion")

        self.verticalLayout.addWidget(self.btn_erosion)

        self.btn_dilatation = QPushButton(self.grbox_action)
        self.btn_dilatation.setObjectName(u"btn_dilatation")

        self.verticalLayout.addWidget(self.btn_dilatation)

        self.btn_ouverture = QPushButton(self.grbox_action)
        self.btn_ouverture.setObjectName(u"btn_ouverture")

        self.verticalLayout.addWidget(self.btn_ouverture)

        self.btn_fermeture = QPushButton(self.grbox_action)
        self.btn_fermeture.setObjectName(u"btn_fermeture")

        self.verticalLayout.addWidget(self.btn_fermeture)

        self.btn_amin = QPushButton(self.grbox_action)
        self.btn_amin.setObjectName(u"btn_amin")

        self.verticalLayout.addWidget(self.btn_amin)

        self.btn_epai = QPushButton(self.grbox_action)
        self.btn_epai.setObjectName(u"btn_epai")

        self.verticalLayout.addWidget(self.btn_epai)

        self.grbox_option = QGroupBox(self.grbox_action)
        self.grbox_option.setObjectName(u"grbox_option")
        self.verticalLayout_4 = QVBoxLayout(self.grbox_option)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.btn_squelette = QPushButton(self.grbox_option)
        self.btn_squelette.setObjectName(u"btn_squelette")

        self.verticalLayout_3.addWidget(self.btn_squelette)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.grbox_option)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.spinBox = QSpinBox(self.grbox_option)
        self.spinBox.setObjectName(u"spinBox")

        self.horizontalLayout_3.addWidget(self.spinBox)

        self.btn_amin_homtho = QPushButton(self.grbox_option)
        self.btn_amin_homtho.setObjectName(u"btn_amin_homtho")

        self.horizontalLayout_3.addWidget(self.btn_amin_homtho)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btn_reset = QPushButton(self.grbox_option)
        self.btn_reset.setObjectName(u"btn_reset")

        self.horizontalLayout_4.addWidget(self.btn_reset)

        self.btn_quitte = QPushButton(self.grbox_option)
        self.btn_quitte.setObjectName(u"btn_quitte")

        self.horizontalLayout_4.addWidget(self.btn_quitte)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)


        self.verticalLayout.addWidget(self.grbox_option)


        self.horizontalLayout.addWidget(self.grbox_action)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1102, 25))
        self.menuouvrir = QMenu(self.menubar)
        self.menuouvrir.setObjectName(u"menuouvrir")
        self.menuenregister = QMenu(self.menubar)
        self.menuenregister.setObjectName(u"menuenregister")
        self.menuImage = QMenu(self.menubar)
        self.menuImage.setObjectName(u"menuImage")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuouvrir.menuAction())
        self.menubar.addAction(self.menuenregister.menuAction())
        self.menubar.addAction(self.menuImage.menuAction())
        self.menuouvrir.addAction(self.actionfichier)
        self.menuenregister.addAction(self.actionenregistrer_sous)
        self.menuImage.addAction(self.actionNiveau_de_gris)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionfichier.setText(QCoreApplication.translate("MainWindow", u"Fichier", None))
        self.actionenregistrer_sous.setText(QCoreApplication.translate("MainWindow", u"Enregistrer sous", None))
        self.actionNiveau_de_gris.setText(QCoreApplication.translate("MainWindow", u"Niveau de gris", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"image", None))
        self.grbox_action.setTitle(QCoreApplication.translate("MainWindow", u"Actions", None))
        self.btn_seuillage.setText(QCoreApplication.translate("MainWindow", u"Seuillage", None))
        self.btn_add.setText(QCoreApplication.translate("MainWindow", u"Addition", None))
        self.btn_soust.setText(QCoreApplication.translate("MainWindow", u"Soustraction", None))
        self.btn_erosion.setText(QCoreApplication.translate("MainWindow", u"Erosion", None))
        self.btn_dilatation.setText(QCoreApplication.translate("MainWindow", u"Dilatation", None))
        self.btn_ouverture.setText(QCoreApplication.translate("MainWindow", u"Ouverture", None))
        self.btn_fermeture.setText(QCoreApplication.translate("MainWindow", u"Fermeture", None))
        self.btn_amin.setText(QCoreApplication.translate("MainWindow", u"Amincissement", None))
        self.btn_epai.setText(QCoreApplication.translate("MainWindow", u"Epaississement", None))
        self.grbox_option.setTitle(QCoreApplication.translate("MainWindow", u"Option", None))
        self.btn_squelette.setText(QCoreApplication.translate("MainWindow", u"Squelette", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"It\u00e9rations", None))
        self.btn_amin_homtho.setText(QCoreApplication.translate("MainWindow", u"Amincissement homothopique", None))
        self.btn_reset.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.btn_quitte.setText(QCoreApplication.translate("MainWindow", u"Quitter", None))
        self.menuouvrir.setTitle(QCoreApplication.translate("MainWindow", u"Ouvrir", None))
        self.menuenregister.setTitle(QCoreApplication.translate("MainWindow", u"Enregistrer", None))
        self.menuImage.setTitle(QCoreApplication.translate("MainWindow", u"Image", None))
    # retranslateUi

