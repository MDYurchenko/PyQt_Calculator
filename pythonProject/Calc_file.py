import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QApplication, QPushButton, QGridLayout, QWidget, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import QMetaObject

class CalcWindow(QMainWindow):
    def __init__(self):
        super(CalcWindow, self).__init__()
        self.initUI() #при создании экземляра класса, применяем к нему настройки UI
        self.setEnabled(True)
        self.resize(500, 620)
        self.is_equal = False
    def initUI(self):
        #self.setEnabled(True)
        #self.setGeometry(220, 220, 500, 620) #в точке 1, 2, выводим окно с размерами 3, 4
        #наша область калькулятора будет разделена на 3 главные области:
        #1. Область результата
        #2. Область ввода выражения
        #3. Область кнопок

        #создадим стиль для области результата
        font_res = QtGui.QFont()
        font_res.setPointSize((30))
        font_res.setBold(True)

        # создадим стиль для записи вычисляемого выражения
        font_eq = QtGui.QFont()
        font_eq.setPointSize((15))
        font_eq.setBold(True)

        # создадим стиль для области кнопок
        font_but = QtGui.QFont()
        font_but.setPointSize((40))
        font_but.setBold(True)

        #запись ответа и выражения будут представлены классами QLabel:
        # область результата, согласно макету, имеет постоянный знак "="

        #self.centralwidget = QWidget(self)
        #self.centralwidget.setObjectName(u"centralwidget")

        self.verticalLayoutWidget = QWidget(self)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 500, 620))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)  # устанавливаем поля

        self.horizontalLayoutWidget = QWidget(self.verticalLayoutWidget)
        horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        horizontalLayout.setObjectName(u"horizontalLayout")

        self.res_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.res_eq_label = QtWidgets.QLabel(self.horizontalLayoutWidget)

        self.eq_label = QtWidgets.QLabel(self.verticalLayoutWidget)

        horizontalLayout.addWidget(self.res_eq_label)
        horizontalLayout.addWidget(self.res_label)

        self.gridLayoutWidget = QWidget(self.verticalLayoutWidget)
        grid = QGridLayout(self.gridLayoutWidget)

        self.verticalLayout.addWidget(self.horizontalLayoutWidget)
        self.verticalLayout.addWidget(self.eq_label)
        self.verticalLayout.addWidget(self.gridLayoutWidget)

        #применим стили для labels:
        self.res_eq_label.setFont(font_res)
        self.res_label.setFont(font_res)
        self.eq_label.setFont(font_eq)

        #для применения стиля ко всем кнопкам,создадим объект Frame
        #self.buttons_frame = QtWidgets.QFrame()
        #self.buttons_frame.setFont(font_but)

        #теперь определим места положения трех областей:
        #self.buttons_frame.setGeometry(0, 250, 500, 370)

        #self.eq_label.setGeometry(0, 150, 480, 100)
        #grid.addWidget(self.res_eq_label, 0, 0)
        #grid.addWidget(self.res_label, 1, 0)
        #grid.addWidget(self.eq_label, 0, 1)
        #self.res_label.setGeometry(150, 50, 330, 100)


        #self.res_eq_label.setGeometry(20, 50, 150, 100)

        #теперь определим первоначальный текст на lables:
        self.res_label.setText('0')
        self.res_eq_label.setText('=')
        self.eq_label.setText('Введите выражение')

        #выравнивание
        self.res_label.setAlignment(QtCore.Qt.AlignRight)
        self.res_eq_label.setAlignment(QtCore.Qt.AlignLeft)
        self.eq_label.setAlignment(QtCore.Qt.AlignRight)

        #создаем сетку для размещения кнопок
        #grid_layout = QWidget(self)
        #grid_layout.setGeometry(QtCore.QRect(0, 250, 500, 370))

        #grid.setGeometry(QtCore.QRect(0, 250, 500, 370))

        #создаем кнопки

        self.button_CE = QPushButton(self.gridLayoutWidget)
        #self.button_CE.setGeometry(QtCore.QRect(0, 220, 90, 80))
        self.button_CE.setObjectName('CE')
        self.button_CE.setText('CE')
        grid.addWidget(self.button_CE, 0, 0)

        self.button_sym = QPushButton(self.gridLayoutWidget)
        #self.button_sym.setGeometry(QtCore.QRect(90, 220, 90, 80))
        self.button_sym.setObjectName('+/-')
        self.button_sym.setText('+/-')
        grid.addWidget(self.button_sym, 1, 0)

        self.button_percent = QPushButton(self.gridLayoutWidget)
        #self.button_percent.setGeometry(QtCore.QRect(180, 220, 90, 80))
        self.button_percent.setObjectName('%')
        self.button_percent.setText('%')
        grid.addWidget(self.button_percent, 2, 0)

        self.button_div = QtWidgets.QPushButton(self.gridLayoutWidget)
        #self.button_div.setGeometry(QtCore.QRect(270, 220, 90, 80))
        self.button_div.setObjectName('/')
        self.button_div.setText('/')
        grid.addWidget(self.button_div, 3, 0)

        self.button_7 = QPushButton(self.gridLayoutWidget)
        #self.button_7.setGeometry(QtCore.QRect(0, 300, 90, 80))
        self.button_7.setObjectName('7')
        self.button_7.setText('7')
        grid.addWidget(self.button_7, 0, 1)

        self.button_8 = QPushButton(self.gridLayoutWidget)
        #self.button_8.setGeometry(QtCore.QRect(90, 300, 90, 80))
        self.button_8.setObjectName('8')
        self.button_8.setText('8')
        grid.addWidget(self.button_8, 1, 1)

        self.button_9 = QPushButton(self.gridLayoutWidget)
        #self.button_9.setGeometry(QtCore.QRect(180, 300, 90, 80))
        self.button_9.setObjectName('9')
        self.button_9.setText('9')
        grid.addWidget(self.button_9, 2, 1)

        self.button_mul = QPushButton(self.gridLayoutWidget)
        #self.button_mul.setGeometry(QtCore.QRect(270, 300, 90, 80))
        self.button_mul.setObjectName('*')
        self.button_mul.setText('*')
        grid.addWidget(self.button_mul, 3, 1)

        self.button_4 = QPushButton(self.gridLayoutWidget)
        #self.button_4.setGeometry(QtCore.QRect(0, 380, 90, 80))
        self.button_4.setObjectName('4')
        self.button_4.setText('4')
        grid.addWidget(self.button_4, 0, 2, 1, 1)

        self.button_5 = QPushButton(self.gridLayoutWidget)
        #self.button_5.setGeometry(QtCore.QRect(90, 380, 90, 80))
        self.button_5.setObjectName('5')
        self.button_5.setText('5')
        grid.addWidget(self.button_5, 1, 2, 1, 1)

        self.button_6 = QPushButton(self.gridLayoutWidget)
        #self.button_6.setGeometry(QtCore.QRect(180, 380, 90, 80))
        self.button_6.setObjectName('6')
        self.button_6.setText('6')
        grid.addWidget(self.button_6, 2, 2)

        self.button_minus = QPushButton(self.gridLayoutWidget)
        #self.button_minus.setGeometry(QtCore.QRect(270, 380, 90, 80))
        self.button_minus.setObjectName('-')
        self.button_minus.setText('-')
        grid.addWidget(self.button_minus, 3, 2)

        self.button_1 = QPushButton(self.gridLayoutWidget)
        #self.button_1.setGeometry(QtCore.QRect(0, 460, 90, 80))
        self.button_1.setObjectName('1')
        self.button_1.setText('1')
        grid.addWidget(self.button_1, 0, 3)

        self.button_2 = QPushButton(self.gridLayoutWidget)
        #self.button_2.setGeometry(QtCore.QRect(90, 460, 90, 80))
        self.button_2.setObjectName('2')
        self.button_2.setText('2')
        grid.addWidget(self.button_2, 1, 3)

        self.button_3 = QPushButton(self.gridLayoutWidget)
        #self.button_3.setGeometry(QtCore.QRect(180, 460, 90, 80))
        self.button_3.setObjectName('3')
        self.button_3.setText('3')
        grid.addWidget(self.button_3, 2, 3)

        self.button_plus = QPushButton(self.gridLayoutWidget)
        #self.button_plus.setGeometry(QtCore.QRect(270, 460, 90, 160))
        self.button_plus.setObjectName('+')
        self.button_plus.setText('+')
        grid.addWidget(self.button_plus, 3, 3)

        self.button_0 = QPushButton(self.gridLayoutWidget)
        #self.button_0.setGeometry(QtCore.QRect(0, 540, 90, 80))
        self.button_0.setObjectName('0')
        self.button_0.setText('0')
        grid.addWidget(self.button_0, 0, 4)

        self.button_dot = QPushButton(self.gridLayoutWidget)
        #self.button_dot.setGeometry(QtCore.QRect(90, 540, 90, 80))
        self.button_dot.setObjectName('.')
        self.button_dot.setText('.')
        grid.addWidget(self.button_dot, 1, 4, 1, 1)

        self.button_eq = QPushButton(self.gridLayoutWidget)
        #self.button_eq.setGeometry(QtCore.QRect(180, 540, 90, 80))
        #self.button_eq.setMinimumSize(90,80)
        #self.button_eq.setMaximumSize(90, 80)
        self.button_eq.setObjectName('=')
        self.button_eq.setText('=')
        grid.addWidget(self.button_eq, 2, 4, 1, 1)

        self.button_e = QPushButton(self.gridLayoutWidget)
        # self.button_eq.setGeometry(QtCore.QRect(180, 540, 90, 80))
        # self.button_eq.setMinimumSize(90,80)
        # self.button_eq.setMaximumSize(90, 80)
        self.button_e.setObjectName('ll')
        self.button_e.setText('ll')
        grid.addWidget(self.button_e, 3, 4, 1, 1)

        self.verticalLayoutWidget.setLayout(self.verticalLayout)

        #self.retranslateUi(CalcWindow)

        #QMetaObject.connectSlotsByName(QCalcWindow)

        self.add_functions()

    def add_functions(self):
        self.button_0.clicked.connect(
            lambda: self.write_number(self.button_0.text()))
        self.button_1.clicked.connect(
            lambda: self.write_number(self.button_1.text()))
        self.button_2.clicked.connect(
            lambda: self.write_number(self.button_2.text()))
        self.button_3.clicked.connect(
            lambda: self.write_number(self.button_3.text()))
        self.button_4.clicked.connect(
            lambda: self.write_number(self.button_4.text()))
        self.button_5.clicked.connect(
            lambda: self.write_number(self.button_5.text()))
        self.button_6.clicked.connect(
            lambda: self.write_number(self.button_6.text()))
        self.button_7.clicked.connect(
            lambda: self.write_number(self.button_7.text()))
        self.button_8.clicked.connect(
            lambda: self.write_number(self.button_8.text()))
        self.button_9.clicked.connect(
            lambda: self.write_number(self.button_9.text()))

        self.button_plus.clicked.connect(
            lambda: self.write_symblol(self.button_plus.text()))
        self.button_minus.clicked.connect(
            lambda: self.write_symblol(self.button_minus.text()))
        self.button_mul.clicked.connect(
            lambda: self.write_symblol(self.button_mul.text()))
        self.button_div.clicked.connect(
            lambda: self.write_symblol(self.button_div.text()))
        self.button_dot.clicked.connect(
            lambda: self.write_symblol(self.button_dot.text()))

        #self.button_eq.clicked.connect(self.get_results)

    def write_number(self, number):
        if self.eq_label.text() == 'Введите выражение' or self.is_equal == True:
            self.eq_label.setText('')
            self.eq_label.setText(number)
            self.is_equal = False
            print('in if')
        else:
            self.eq_label.setText(self.eq_label.text() + number)
            print('in else')
    def write_symbol(self, symbol):
        if self.eq_label.text()[-1].isdigit():
            print(self.eq_label.text()[-1])
            self.eq_label.setText(self.eq_label.text() + symbol)
        else:
            self.eq_label.setText(self.eq_label.text()[-1].replace(symbol))

def window():
    #
    app = QApplication(sys.argv)
    win = CalcWindow()
    win.show()
    sys.exit(app.exec_())

window()