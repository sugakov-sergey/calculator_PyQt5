from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton
from PyQt5.QtGui import QIcon
import sys


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.my_input = []
        self.operand_1 = []
        self.operand_2 = []
        self.op = ''

    def initUI(self):
        self.setGeometry(50, 100, 280, 375)
        self.setWindowTitle("Калькулятор")
        self.setWindowIcon(QIcon('web.png'))

        self.label = QLabel(self)
        self.label.setText('0')
        self.label.resize(225, 150)
        self.label.move(10, 0)

        self.setWindowIcon(QIcon('web.png'))

        self.num_0 = QPushButton('0', self)
        self.num_0.resize(50, 50)
        self.num_0.move(60, 265)

        self.num_1 = QPushButton('1', self)
        self.num_1.resize(50, 50)
        self.num_1.move(5, 100)

        self.num_2 = QPushButton('2', self)
        self.num_2.resize(50, 50)
        self.num_2.move(60, 100)

        self.num_3 = QPushButton('3', self)
        self.num_3.resize(50, 50)
        self.num_3.move(115, 100)

        self.num_4 = QPushButton('4', self)
        self.num_4.resize(50, 50)
        self.num_4.move(5, 155)

        self.num_5 = QPushButton('5', self)
        self.num_5.resize(50, 50)
        self.num_5.move(60, 155)

        self.num_6 = QPushButton('6', self)
        self.num_6.resize(50, 50)
        self.num_6.move(115, 155)

        self.num_7 = QPushButton('7', self)
        self.num_7.resize(50, 50)
        self.num_7.move(5, 210)

        self.num_8 = QPushButton('8', self)
        self.num_8.resize(50, 50)
        self.num_8.move(60, 210)

        self.num_9 = QPushButton('9', self)
        self.num_9.resize(50, 50)
        self.num_9.move(115, 210)

        self.mul_butt = QPushButton('*', self)
        self.mul_butt.resize(50, 50)
        self.mul_butt.move(225, 100)

        self.div_butt = QPushButton('/', self)
        self.div_butt.resize(50, 50)
        self.div_butt.move(170, 100)

        self.plus_butt = QPushButton('+', self)
        self.plus_butt.resize(50, 50)
        self.plus_butt.move(115, 265)

        self.minus_butt = QPushButton('-', self)
        self.minus_butt.resize(50, 50)
        self.minus_butt.move(5, 265)

        self.step_butt = QPushButton('^', self)
        self.step_butt.resize(50, 50)
        self.step_butt.move(170, 210)

        self.x2_butt = QPushButton('x²', self)
        self.x2_butt.resize(50, 50)
        self.x2_butt.move(225, 210)

        self.per_butt = QPushButton('%', self)
        self.per_butt.resize(50, 50)
        self.per_butt.move(225, 155)

        self.cdel_butt = QPushButton('//', self)
        self.cdel_butt.resize(50, 50)
        self.cdel_butt.move(170, 155)

        self.sqrt_butt = QPushButton('√', self)
        self.sqrt_butt.resize(50, 50)
        self.sqrt_butt.move(170, 265)

        self.ravno_butt = QPushButton('=', self)
        self.ravno_butt.resize(160, 50)
        self.ravno_butt.move(5, 320)

        self.c_butt = QPushButton('C', self)
        self.c_butt.resize(105, 50)
        self.c_butt.move(170, 320)

        self.del_butt = QPushButton('del', self)
        self.del_butt.resize(50, 50)
        self.del_butt.move(225, 265)

        self.num_1.clicked.connect(self.one)
        self.num_2.clicked.connect(self.two)
        self.num_3.clicked.connect(self.three)
        self.num_4.clicked.connect(self.four)
        self.num_5.clicked.connect(self.five)
        self.num_6.clicked.connect(self.six)
        self.num_7.clicked.connect(self.seven)
        self.num_8.clicked.connect(self.eight)
        self.num_9.clicked.connect(self.nine)
        self.num_0.clicked.connect(self.zero)
        self.plus_butt.clicked.connect(self.plus_func)
        self.minus_butt.clicked.connect(self.minus_func)
        self.mul_butt.clicked.connect(self.mul_func)
        self.div_butt.clicked.connect(self.div_func)
        self.step_butt.clicked.connect(self.step_func)
        self.sqrt_butt.clicked.connect(self.sqrt_func)
        self.ravno_butt.clicked.connect(self.ravno_func)
        self.c_butt.clicked.connect(self.clean_func)
        self.per_butt.clicked.connect(self.per_func)
        self.x2_butt.clicked.connect(self.x2_func)
        self.cdel_butt.clicked.connect(self.cdel_func)
        self.del_butt.clicked.connect(self.del_func)

    def _label_setText(self):
        self.operand_1 = float(self.label.text())
        self.label.setText(self.label.text() + self.operation)
        self.op = ''

    def enterValue(self):
        if self.op == 'clear':
            self.label.setText('')
            self.op = ''
        if self.label.text() == '0':
            self.label.setText('')
        self.label.setText(self.label.text() + self.my_input)

    def one(self):
        self.my_input = '1'
        self.enterValue()

    def two(self):
        self.my_input = '2'
        self.enterValue()

    def three(self):
        self.my_input = '3'
        self.enterValue()

    def four(self):
        self.my_input = '4'
        self.enterValue()

    def five(self):
        self.my_input = '5'
        self.enterValue()

    def six(self):
        self.my_input = '6'
        self.enterValue()

    def seven(self):
        self.my_input = '7'
        self.enterValue()

    def eight(self):
        self.my_input = '8'
        self.enterValue()

    def nine(self):
        self.my_input = '9'
        self.enterValue()

    def zero(self):
        self.my_input = '0'
        self.enterValue()

    def plus_func(self):
        self.operation = '+'
        self._label_setText()

    def minus_func(self):
        self.operation = '-'
        self._label_setText()

    def mul_func(self):
        self.operation = '*'
        self._label_setText()

    def div_func(self):
        self.operation = '/'
        self._label_setText()

    def step_func(self):
        self.operation = '^'
        self._label_setText()

    def sqrt_func(self):
        self.operand_1 = float(self.label.text())
        self.rezult = self.operand_1 ** 0.5
        self.label.setText(str(self.rezult))
        self.op == 'clear'

    def per_func(self):
        self.operation = '%'
        self._label_setText()

    def cdel_func(self):
        self.operation = '//'
        self._label_setText()

    def x2_func(self):
        self.operand_1 = float(self.label.text())
        self.rezult = int(self.operand_1 ** 2)
        self.label.setText(str(self.rezult))
        self.op == 'clear'

    def del_func(self):
        self.label.setText(self.label.text()[:-1])

    def ravno_func(self):
        if self.op != 'clear':
            self.operand_2 = float(self.label.text().split(self.operation)[-1])
            if self.operation == '+':
                self.rezult = int(self.operand_1 + self.operand_2)
            elif self.operation == '-':
                self.rezult = int(self.operand_1 - self.operand_2)
            elif self.operation == '*':
                self.rezult = int(self.operand_1 * self.operand_2)
            elif self.operation == '%':
                self.rezult = int(self.operand_1 % self.operand_2)
            elif self.operation == '/':
                if self.operand_2 == 0:
                    self.rezult = 'Ohh, no. Division by Zero'
                else:
                    self.rezult = self.operand_1 / self.operand_2
            elif self.operation == '//':
                if self.operand_2 == 0:
                    self.rezult = 'Ohh, no. Division by Zero'
                else:
                    self.rezult = int(self.operand_1 // self.operand_2)
            elif self.operation == '^':
                self.rezult = self.operand_1 ** self.operand_2

            self.label.setText(str(self.rezult))
            self.op = 'clear'

    def clean_func(self):
        self.label.setText('0')

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Calculator()
    ex.show()
    sys.exit(app.exec_())