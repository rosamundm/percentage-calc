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
        self.label1 = QLabel("x% of y = z")
        self.button1 = QPushButton("Go")
        # for functionB:
        self.label2 = QLabel("x is y% of z")
        self.button2 = QPushButton("Go")

        grid = QGridLayout()
        grid.addWidget(self.welcomeLabel, 0, 0)
        grid.addWidget(self.label1, 1, 0)
        grid.addWidget(self.button1, 2, 0)
        grid.addWidget(self.label2, 4, 0)
        grid.addWidget(self.button2, 5, 0)

        self.setLayout(grid)
        self.show()

        self.button1.clicked.connect(self.openNew)
        self.button2.clicked.connect(self.openNew)



""" Einrückung??

    def functionA():
            x = text1.text()
            y = text2.text()
            z.setText(str(float(x) * int(y)))
            return z


    def functionB():
            a = text3.text()
            c = text3.text()
            b.setText(str(float(a) * 100 / c))
            return b
"""

    def openNew(self):
        self.n = newWindow()
        self.n.show()


# define separate classes according to function
class newWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.resize(200, 150)
        self.setWindowTitle("Title")

        self.newWindowLabel = QLabel("Here is some text")

        # labels / text fields for each function

"""
# functionA:

# x (decimal percentage) of y = z
def percent_of_is(xfloat, y):
    z = xfloat * y
    return z

print(percent_of_is(0.25, 30))


# functionB:
# x is percentage% of y
def is_percent_of(x, y):
    percentage = x * 100 / y
    return percentage

print(is_percent_of(1, 4))

"""



app = QApplication(sys.argv)
mw = mainWindow()
sys.exit(app.exec_())
