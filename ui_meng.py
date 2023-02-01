# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'meng.ui'
##
## Created by: Qt User Interface Compiler version 6.2.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLineEdit, QPushButton,QLabel,
    QSizePolicy, QTextBrowser, QVBoxLayout, QWidget)

class Ui_MengT(object):
    def setupUi(self, MengT):
        if not MengT.objectName():
            MengT.setObjectName(u"MengT")
        
        MengT.setFixedSize(400, 300)
        self.verticalLayout = QVBoxLayout(MengT)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tb_view = QTextBrowser(MengT)
        self.tb_view.setObjectName(u"tb_view")

        self.verticalLayout.addWidget(self.tb_view)

        self.lb_count = QLabel()
        self.lb_count.setObjectName(u"lb_count")
        self.lb_count.setText("个数:")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.le_count = QLineEdit(MengT)
        self.le_count.setObjectName(u"le_count")
        self.horizontalLayout.addWidget(self.lb_count)
        self.horizontalLayout.addWidget(self.le_count)

        self.pushButton = QPushButton(MengT)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(MengT)

        QMetaObject.connectSlotsByName(MengT)
    # setupUi

    def retranslateUi(self, MengT):
        MengT.setWindowTitle(QCoreApplication.translate("MengT", u"\u968f\u673a\u8499\u9898", None))
        self.pushButton.setText(QCoreApplication.translate("MengT", u"\u751f\u6210", None))
    # retranslateUi

