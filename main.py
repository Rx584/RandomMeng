from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from ui_meng import *
import sys
import time
import random
class MengT(QWidget,Ui_MengT):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        this = self
        self.pushButton.clicked.connect(self.creat_meng)
        self.setWindowIcon(QIcon("icon.ico"))
        self.show()

    def creat_meng(self):
        
        this = self
        random.seed(time.time())
        try:
            give = ""
            count = 200
            count = int(self.le_count.text())
        except TypeError:
            QMessageBox.warning(this,"不对","您输入的似乎不是个整数")
        for i in range(count):
            enum = random.randint(0,3)
            if (enum == 0):
                give+="A"
            elif(enum == 1):
                give+="B"
            elif(enum == 2):
                give+="C"
            elif(enum == 3):
                give+="D"
        self.tb_view.setText(give)
    def keyPressEvent(self, event):
        if(event.key()==Qt.Key_Enter):
            self.creat_meng()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MengT()
    sys.exit(app.exec())