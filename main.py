import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QGridLayout

class mainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(200, 180)
        self.setWindowTitle("Percentage Calculator")

        # for functionA:
        self.titleFuncA = QLabel("x = z% of y")
        self.labelA1 = QLabel("z:")
        self.inputA1 = QLineEdit()
        self.labelA2 = QLabel("y:")
        self.inputA2 = QLineEdit()
        self.button1 = QPushButton("Calculate!")
        self.button1.clicked.connect(self.functionA)
        self.result1 = QLabel()

        # for functionB:
        self.titleFuncB = QLabel("z = x% of y")
        self.labelB1 = QLabel("z:")
        self.inputB1 = QLineEdit()
        self.labelB2 = QLabel("y:")
        self.inputB2 = QLineEdit()
        self.button2 = QPushButton("Calculate!")
        self.button2.clicked.connect(self.functionB)
        self.result2 = QLabel()

        grid = QGridLayout()
        # functionA layout:
        grid.addWidget(self.titleFuncA, 1, 0)
        grid.addWidget(self.labelA1, 2, 0)
        grid.addWidget(self.inputA1, 2, 1)
        grid.addWidget(self.labelA2, 3, 0)
        grid.addWidget(self.inputA2, 3, 1)
        grid.addWidget(self.button1, 4, 0)
        grid.addWidget(self.result1, 5, 0)
        # functionB layout:
        grid.addWidget(self.titleFuncB, 7, 0)
        grid.addWidget(self.labelB1, 8, 0)
        grid.addWidget(self.inputB1, 8, 1)
        grid.addWidget(self.labelB2, 9, 0)
        grid.addWidget(self.inputB2, 9, 1)
        grid.addWidget(self.button2, 10, 0)
        grid.addWidget(self.result2, 11, 0)

        self.setLayout(grid)
        self.show()


    # functionA: x = z% of y
    def functionA(self):
        x = float(self.inputA1.text())
        y = float(self.inputA2.text())
        if x and y:
            x_float = x / 100
            z  = x_float * y
            x_string = f"x = {x}\ni.e. {x}% of {y} is {z}"
            self.result1.setText(x_string)
            self.inputA1.clear()
            self.inputA2.clear()
        else:
            return "Please check both fields are complete"

    # functionB: z = x% of y
    def functionB(self):
        z = float(self.inputB1.text())
        y = float(self.inputB2.text())
        if z and y:
            x = z * 100 / y
            x_string = f"x = {x}\ni.e. {z} is {x}% of {y}"
            self.result2.setText(x_string)
            self.inputB1.clear()
            self.inputB2.clear()
        else:
            return "Please check both fields are complete"


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = mainWindow()
    sys.exit(app.exec_())
