import sys
from PyQt5.QtWidgets import QApplication, QWidget, QSpinBox, QDoubleSpinBox, QLabel, QLineEdit, QTextEdit, QPushButton, QGridLayout, QButtonGroup
#from functions import functionAWindow, functionBWindow

# import fractions module - functionA must be decimal!


class mainWindow(QWidget): #QMainWindow
    def __init__(self):
        super().__init__()
        self.resize(300, 200)
        self.setWindowTitle("Percentage Calculator")

        # for functionA:
        self.titleFuncA = QLabel("Find z% of y, i.e. x")
        self.labelA1 = QLabel("z (enter decimal):")
        self.inputA1 = QDoubleSpinBox()
        #self.inputA1 = QTextEdit()
        self.labelA2 = QLabel("y:")
        self.inputA2 = QSpinBox()
    #    self.inputA2 = QTextEdit()
        self.button1 = QPushButton("Calculate!")
        self.button1.clicked.connect(self.functionA)
        self.result1 = QTextEdit()

        # for functionB:
        self.titleFuncB = QLabel("z = x% of y")
        self.labelB1 = QLabel("z:")
        self.inputB1 = QTextEdit()
        self.labelB2 = QLabel("y:")
        self.inputB2 = QTextEdit()
        self.button2 = QPushButton("Calculate!")
#        self.button2.clicked.connect(self.functionB)
#       self.result2 = QTextEdit()

        grid = QGridLayout()
        grid.addWidget(self.titleFuncA, 1, 0)
        grid.addWidget(self.labelA1, 2, 0)
        grid.addWidget(self.inputA1, 2, 1)
        grid.addWidget(self.labelA2, 3, 0)
        grid.addWidget(self.inputA2, 3, 1)
        grid.addWidget(self.button1, 4, 0)
        grid.addWidget(self.result1, 5, 0)
        grid.addWidget(self.titleFuncB, 6, 0)
        grid.addWidget(self.labelB1, 7, 0)
        grid.addWidget(self.inputB1, 7, 1)
        grid.addWidget(self.labelB2, 8, 0)
        grid.addWidget(self.inputB2, 8, 1)
        grid.addWidget(self.button2, 9, 0)



        self.setLayout(grid)
        self.show()

    # write functionA:
    def functionA(self): # x, y ?
        z = float(self.inputA1.text())
    #    z = float(self.inputA1.toPlainText())
        if z >= 1:
            return "Please enter a valid decimal"
        else:
            y = int(self.inputA2.text())
            z_as_int = z * 10
            x  = z_as_int * y
            x_string = f"{x}% of {y} is {z_as_int}"
            self.result1.setText(x_string)
            # add clear!


    # write functionB:
    def functionB(self):
        pass

#    def openNew(self): # openNewA?
#        self.n = openNew()
#        self.n.show()

    #    self.button1.clicked.connect(self.openNew)
    #    self.button2.clicked.connect(self.openNew)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = mainWindow()
    sys.exit(app.exec_())
