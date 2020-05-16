import sys
from PyQt5.QtWidgets import QApplication, QFormLayout, QWidget, QLabel, QLineEdit, QPushButton, QGridLayout, QButtonGroup
# import fractions module - functionA must be decimal!


class mainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(300, 200)
        self.setWindowTitle("Percentage Calculator")

        # attribute for openNew further on
        self.n = None

        # WIDGETS
        self.welcomeLabel = QLabel("Welcome!\nLet's find some percentages.")
        # for functionA:
        self.button1 = QPushButton("x% of y = z")
        # for functionB:
        self.button2 = QPushButton("z = x% of y")

        grid = QGridLayout()
        grid.addWidget(self.welcomeLabel, 0, 0)
        grid.addWidget(self.button1, 1, 0)
        grid.addWidget(self.button2, 2, 0)

        self.setLayout(grid)
        self.show()

        self.button1.clicked.connect(self.openNew) # lambda?
        self.button2.clicked.connect(self.openNew)

        def openNew(self):
            self.n = newWindow()
            self.n.show()

class functionAWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(200, 150)
        self.setWindowTitle("Find Percentage")
        self.newWindowLabel1 = QLabel("x% of y = z")
        self.field1 = QLineEdit("Enter a decimal:")
        self.field2 = QLineEdit("Enter your number")
        self.label1 = QLabel("Your result:")
        self.result1 = QLabel()

        # labels / text fields for each function

    def functionA():
            x = text1.text()
            y = text2.text()
            z.setText(str(float(x) * int(y)))
            return z


class functionBWindow(QtWidget):
    def __init__(self):
        super().__init__()
        self.resize(200, 150)
        self.setWindowTitle("Find Percentage")
        self.newWindowLabel2 = QLabel("z = x% of y")
        self.field3 = QLineEdit("Enter the first number (z):")
        self.field4 = QLineEdit("Enter the second number (y):")
        self.label2 = QLabel("Your result:")
        self.result2 = QLabel()

    def functionB():
            a = text3.text()
            c = text3.text()
            b.setText(str(float(a) * 100 / c))
            return b





app = QApplication(sys.argv)
mw = mainWindow()
sys.exit(app.exec_())
