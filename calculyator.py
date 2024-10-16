from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton

class calculator(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.setFixedSize(500,350)

        self.Clear_btn=QPushButton("clear", self)
        self.Clear_btn.move(20, 120)
        self.Clear_btn.clicked.connect(self.tozalash)

# **************************************************        raqamlar

        self.bir_btn=QPushButton("1", self)
        self.bir_btn.move(20, 150)
        self.bir_btn.clicked.connect(self.bir)

        self.tort_btn=QPushButton("4", self)
        self.tort_btn.move(20, 200)
        self.tort_btn.clicked.connect(self.tort)

        self.sakkiz_btn=QPushButton("8", self)
        self.sakkiz_btn.move(20, 250)
        self.sakkiz_btn.clicked.connect(self.sakkiz)

        self.ikki_btn=QPushButton("2", self)
        self.ikki_btn.move(120, 150)
        self.ikki_btn.clicked.connect(self.ikki)

        self.besh_btn=QPushButton("5", self)
        self.besh_btn.move(120, 200)
        self.besh_btn.clicked.connect(self.besh)

        self.yetti_btn=QPushButton("7", self)
        self.yetti_btn.move(120, 250)
        self.yetti_btn.clicked.connect(self.yetti)

        self.uch_btn=QPushButton("3", self)
        self.uch_btn.move(220, 150)
        self.uch_btn.clicked.connect(self.uch)

        self.olti_btn=QPushButton("6", self)
        self.olti_btn.move(220, 200)
        self.olti_btn.clicked.connect(self.olti)

        self.toqqiz_btn=QPushButton("9", self)
        self.toqqiz_btn.move(220, 250)
        self.toqqiz_btn.clicked.connect(self.toqqiz)

        self.nol_btn=QPushButton("0", self)
        self.nol_btn.move(120, 300)
        self.nol_btn.clicked.connect(self.nol)

# *********************************************           amallar

        self.kopaytirish_btn=QPushButton("*", self)
        self.kopaytirish_btn.move(320, 150)
        self.kopaytirish_btn.clicked.connect(self.kopaytirish)

        self.bolish_btn=QPushButton("/", self)
        self.bolish_btn.move(320, 200)
        self.bolish_btn.clicked.connect(self.bolish)

        self.qoshish_btn=QPushButton("+", self)
        self.qoshish_btn.move(320, 250)
        self.qoshish_btn.clicked.connect(self.qoshish)

        self.ayirish_btn=QPushButton("-", self)
        self.ayirish_btn.move(320, 300)
        self.ayirish_btn.clicked.connect(self.ayrish)

        self.tenglik_btn=QPushButton("=", self)
        self.tenglik_btn.move(220, 300)
        self.tenglik_btn.clicked.connect(self.tenglik)

# **********************************************         ekran labellar

        self.hisoblash=QLabel("0", self)
        self.hisoblash.move(20, 20)
        self.hisoblash.setStyleSheet("font-size:20px")

        self.amal_lbl=QLabel("",self)
        self.amal_lbl.move(20, 50)
        self.amal_lbl.setStyleSheet("font-size:20px")

        self.hisoblash2=QLabel("0", self)
        self.hisoblash2.move(20, 80)
        self.hisoblash2.setStyleSheet("font-size:20px")

# ******************************************************       methodlar
# ******************************************       amal methodlar

    def kopaytirish(self):
        self.amal_lbl.setText("*")
        self.amal_lbl.adjustSize()

    def bolish(self):
        self.amal_lbl.setText("/")
        self.amal_lbl.adjustSize()

    def ayrish(self):
        self.amal_lbl.setText("-")
        self.amal_lbl.adjustSize()

    def qoshish(self):
        self.amal_lbl.setText("+")
        self.amal_lbl.adjustSize()
    
    def tozalash(self):
        self.hisoblash.setText("0")
        self.hisoblash.adjustSize()
        self.hisoblash2.setText("0")
        self.hisoblash2.adjustSize()
        self.amal_lbl.setText("")
        self.amal_lbl.adjustSize()

    def tenglik(self):
        if self.amal_lbl.text()=="+":
            self.hisoblash.setText(f"{float(self.hisoblash.text())+float(self.hisoblash2.text())}")
            self.hisoblash.adjustSize()
            self.amal_lbl.setText("")
            self.amal_lbl.adjustSize()
            self.hisoblash2.setText("0")
            self.hisoblash2.adjustSize()
        elif self.amal_lbl.text()=="-":
            self.hisoblash.setText(f"{float(self.hisoblash.text())-float(self.hisoblash2.text())}")
            self.hisoblash.adjustSize()
            self.amal_lbl.setText("")
            self.amal_lbl.adjustSize()
            self.hisoblash2.setText("0")
            self.hisoblash2.adjustSize()
        elif self.amal_lbl.text()=="*":
            self.hisoblash.setText(f"{float(self.hisoblash.text())*float(self.hisoblash2.text())}")
            self.hisoblash.adjustSize()
            self.amal_lbl.setText("")
            self.amal_lbl.adjustSize()
            self.hisoblash2.setText("0")
            self.hisoblash2.adjustSize()
        elif self.amal_lbl.text()=="/":
            self.hisoblash.setText(f"{float(self.hisoblash.text())/float(self.hisoblash2.text())}")
            self.hisoblash.adjustSize()
            self.amal_lbl.setText("")
            self.amal_lbl.adjustSize()
            self.hisoblash2.setText("0")
            self.hisoblash2.adjustSize()
    
# ******************************************        raqam methodlar

    def bir(self):
        if self.amal_lbl.text() in ["/", "*", "-", "+"]:
            self.hisoblash2.setText(f"{float(self.hisoblash2.text())*10+1}")
            self.hisoblash2.adjustSize()
        else:
            self.hisoblash.setText(f"{float(self.hisoblash.text())*10+1}")
            self.hisoblash.adjustSize()

    def ikki(self):
        if self.amal_lbl.text() in ["/", "*", "-", "+"]:
            self.hisoblash2.setText(f"{float(self.hisoblash2.text())*10+2}")
            self.hisoblash2.adjustSize()
        else:
            self.hisoblash.setText(f"{float(self.hisoblash.text())*10+2}")
            self.hisoblash.adjustSize()

    def uch(self):
        if self.amal_lbl.text() in ["/", "*", "-", "+"]:
            self.hisoblash2.setText(f"{float(self.hisoblash2.text())*10+3}")
            self.hisoblash2.adjustSize()
        else:
            self.hisoblash.setText(f"{float(self.hisoblash.text())*10+3}")
            self.hisoblash.adjustSize()

    def tort(self):
        if self.amal_lbl.text() in ["/", "*", "-", "+"]:
            self.hisoblash2.setText(f"{float(self.hisoblash2.text())*10+4}")
            self.hisoblash2.adjustSize()
        else:
            self.hisoblash.setText(f"{float(self.hisoblash.text())*10+4}")
            self.hisoblash.adjustSize()

    def besh(self):
        if self.amal_lbl.text() in ["/", "*", "-", "+"]:
            self.hisoblash2.setText(f"{float(self.hisoblash2.text())*10+5}")
            self.hisoblash2.adjustSize()
        else:
            self.hisoblash.setText(f"{float(self.hisoblash.text())*10+5}")
            self.hisoblash.adjustSize()

    def olti(self):
        if self.amal_lbl.text() in ["/", "*", "-", "+"]:
            self.hisoblash2.setText(f"{float(self.hisoblash2.text())*10+6}")
            self.hisoblash2.adjustSize()
        else:
            self.hisoblash.setText(f"{float(self.hisoblash.text())*10+6}")
            self.hisoblash.adjustSize()

    def yetti(self):
        if self.amal_lbl.text() in ["/", "*", "-", "+"]:
            self.hisoblash2.setText(f"{float(self.hisoblash2.text())*10+7}")
            self.hisoblash2.adjustSize()
        else:
            self.hisoblash.setText(f"{float(self.hisoblash.text())*10+7}")
            self.hisoblash.adjustSize()

    def sakkiz(self):
        if self.amal_lbl.text() in ["/", "*", "-", "+"]:
            self.hisoblash2.setText(f"{float(self.hisoblash2.text())*10+8}")
            self.hisoblash2.adjustSize()
        else:
            self.hisoblash.setText(f"{float(self.hisoblash.text())*10+8}")
            self.hisoblash.adjustSize()

    def toqqiz(self):
        if self.amal_lbl.text() in ["/", "*", "-", "+"]:
            self.hisoblash2.setText(f"{float(self.hisoblash2.text())*10+9}")
            self.hisoblash2.adjustSize()
        else:
            self.hisoblash.setText(f"{float(self.hisoblash.text())*10+9}")
            self.hisoblash.adjustSize()

    def nol(self):
        if self.amal_lbl.text() in ["/", "*", "-", "+"]:
            self.hisoblash2.setText(f"{float(self.hisoblash2.text())*10+0}")
            self.hisoblash2.adjustSize()
        else:
            self.hisoblash.setText(f"{float(self.hisoblash.text())*10+0}")
            self.hisoblash.adjustSize()

app=QApplication([])
win=calculator()
win.show()
app.exec_()
