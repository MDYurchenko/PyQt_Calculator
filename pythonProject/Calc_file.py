import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QApplication, QPushButton, QGridLayout, QWidget, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import QMetaObject
import re

class CalcWindow(QMainWindow):
    def __init__(self):
        super(CalcWindow, self).__init__()
        self.initUI() #при создании экземляра класса, применяем к нему настройки UI
        self.resize(400, 620) #размер окна при его вызове
        self.setMinimumSize(400, 620) #нельзя сделать окно меньше данного размера
        #self.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

    def initUI(self):
        #self.setEnabled(True)
        #наша область калькулятора будет разделена на 3 главные области:
        #1. Область результата
        #2. Область ввода выражения
        #3. Область кнопок

        #структуру реализуем посредством VBoxLayout - основной виджет, в который помещаются:
        #1.Поле резульатата
        #2.Поле выражения
        #3.Сетка кнопок
        #Поле резульата выполняем с помощью VHBoxLayout, чтобы разделить область "=" и сам результат
        #Сетку кнопок располагаем в нижней части VBoxLayout

        #запись ответа и выражения будут представлены классами QLabel:
        #область результата, согласно макету, имеет постоянный знак "="

        self.verticalLayoutWidget = QWidget(self)
        self.verticalLayoutWidget.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding))
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 20, 400, 600))
        self.verticalLayoutWidget.setMinimumSize(400, 600)
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)  # устанавливаем поля

        self.horizontalLayoutWidget = QWidget(self.verticalLayoutWidget)
        horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        horizontalLayout.setObjectName(u"horizontalLayout")

        self.res_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.res_label.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding))
        self.res_eq_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        horizontalLayout.setContentsMargins(0, 0, 0, 0)

        self.res_label.setWordWrap(True)
        self.res_label.setMargin(1)
        self.res_label.setScaledContents(True)
        self.res_eq_label.setWordWrap(True)
        self.res_eq_label.setScaledContents(True)

        self.eq_label = QtWidgets.QLabel(self.verticalLayoutWidget)

        horizontalLayout.addWidget(self.res_eq_label, stretch=1)
        horizontalLayout.addWidget(self.res_label, stretch=1)

        self.gridLayoutWidget = QWidget(self.verticalLayoutWidget)
        self.gridLayoutWidget.setMinimumSize(300, 400)
        grid = QGridLayout(self.gridLayoutWidget)

        self.verticalLayout.addWidget(self.horizontalLayoutWidget)
        self.verticalLayout.addWidget(self.eq_label)
        self.verticalLayout.addWidget(self.gridLayoutWidget)

        #теперь определим первоначальный текст на lables:
        self.res_label.setText('0')
        self.res_eq_label.setText('=')
        self.eq_label.setText('Введите выражение')

        #выравнивание
        self.res_label.setAlignment(QtCore.Qt.AlignRight)
        self.res_eq_label.setAlignment(QtCore.Qt.AlignLeft)
        self.eq_label.setAlignment(QtCore.Qt.AlignRight)

        #создаем кнопки

        self.button_CE = QPushButton(self.gridLayoutWidget)
        self.button_CE.setObjectName('CE')
        self.button_CE.setText('CE')
        grid.addWidget(self.button_CE, 0, 0, 1, 1)

        self.button_sym = QPushButton(self.gridLayoutWidget)
        self.button_sym.setObjectName('+/-')
        self.button_sym.setText('+/-')
        grid.addWidget(self.button_sym, 0, 1, 1, 1)

        self.button_percent = QPushButton(self.gridLayoutWidget)
        self.button_percent.setObjectName('%')
        self.button_percent.setText('%')
        grid.addWidget(self.button_percent, 0, 2, 1, 1)

        self.button_div = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_div.setObjectName('/')
        self.button_div.setText('/')
        grid.addWidget(self.button_div, 0, 3, 1, 1)

        self.button_7 = QPushButton(self.gridLayoutWidget)
        self.button_7.setObjectName('7')
        self.button_7.setText('7')
        grid.addWidget(self.button_7, 1, 0, 1, 1)

        self.button_8 = QPushButton(self.gridLayoutWidget)
        self.button_8.setObjectName('8')
        self.button_8.setText('8')
        grid.addWidget(self.button_8, 1, 1, 1, 1)

        self.button_9 = QPushButton(self.gridLayoutWidget)
        self.button_9.setObjectName('9')
        self.button_9.setText('9')
        grid.addWidget(self.button_9, 1, 2, 1, 1)

        self.button_mul = QPushButton(self.gridLayoutWidget)
        self.button_mul.setObjectName('*')
        self.button_mul.setText('*')
        grid.addWidget(self.button_mul, 1, 3, 1, 1)

        self.button_4 = QPushButton(self.gridLayoutWidget)
        self.button_4.setObjectName('4')
        self.button_4.setText('4')
        grid.addWidget(self.button_4, 2, 0, 1, 1)

        self.button_5 = QPushButton(self.gridLayoutWidget)
        self.button_5.setObjectName('5')
        self.button_5.setText('5')
        grid.addWidget(self.button_5, 2, 1, 1, 1)

        self.button_6 = QPushButton(self.gridLayoutWidget)
        self.button_6.setObjectName('6')
        self.button_6.setText('6')
        grid.addWidget(self.button_6, 2, 2, 1, 1)

        self.button_minus = QPushButton(self.gridLayoutWidget)
        self.button_minus.setObjectName('-')
        self.button_minus.setText('-')
        grid.addWidget(self.button_minus, 2, 3, 1, 1)

        self.button_1 = QPushButton(self.gridLayoutWidget)
        self.button_1.setObjectName('1')
        self.button_1.setText('1')
        grid.addWidget(self.button_1, 3, 0, 1, 1)

        self.button_2 = QPushButton(self.gridLayoutWidget)
        self.button_2.setObjectName('2')
        self.button_2.setText('2')
        grid.addWidget(self.button_2, 3, 1, 1, 1)

        self.button_3 = QPushButton(self.gridLayoutWidget)
        self.button_3.setObjectName('3')
        self.button_3.setText('3')
        grid.addWidget(self.button_3, 3, 2, 1, 1)

        self.button_plus = QPushButton(self.gridLayoutWidget)
        self.button_plus.setObjectName('+')
        self.button_plus.setText('+')
        grid.addWidget(self.button_plus, 3, 3, 2, 1)

        self.button_0 = QPushButton(self.gridLayoutWidget)
        self.button_0.setObjectName('0')
        self.button_0.setText('0')
        grid.addWidget(self.button_0, 4, 0, 1, 1)

        self.button_dot = QPushButton(self.gridLayoutWidget)
        self.button_dot.setObjectName('.')
        self.button_dot.setText('.')
        grid.addWidget(self.button_dot, 4, 1, 1, 1)

        self.button_eq = QPushButton(self.gridLayoutWidget)
        self.button_eq.setObjectName('=')
        self.button_eq.setText('=')
        grid.addWidget(self.button_eq, 4, 2, 1, 1)

        #здесь устанавливаем минимальный размер кнопок
        self.button_CE.setMinimumSize(40, 80)
        self.button_sym.setMinimumSize(40, 80)
        self.button_percent.setMinimumSize(40, 80)
        self.button_div.setMinimumSize(40, 80)
        self.button_7.setMinimumSize(40, 80)
        self.button_8.setMinimumSize(40, 80)
        self.button_9.setMinimumSize(40, 80)
        self.button_mul.setMinimumSize(40, 80)
        self.button_4.setMinimumSize(40, 80)
        self.button_5.setMinimumSize(40, 80)
        self.button_6.setMinimumSize(40, 80)
        self.button_minus.setMinimumSize(40, 80)
        self.button_1.setMinimumSize(40, 80)
        self.button_2.setMinimumSize(40, 80)
        self.button_3.setMinimumSize(40, 80)
        self.button_plus.setMinimumSize(40, 160)
        self.button_0.setMinimumSize(40, 80)
        self.button_dot.setMinimumSize(40, 80)
        self.button_eq.setMinimumSize(40, 80)

        #стилизация окна
        self.setStyleSheet("color: white;"
                        "background-color: rgb(26,27,40);"
                        "selection-color: yellow;"
                        "selection-background-color: blue;")

        # создадим шрифта для области результата
        font_res = QtGui.QFont()
        font_res.setPointSize((30))
        font_res.setBold(True)

        # создадим стиль шрифта для записи вычисляемого выражения
        font_eq = QtGui.QFont()
        font_eq.setPointSize((15))
        font_eq.setBold(True)

        # создадим стиль шрифта для кнопок
        font_but = QtGui.QFont()
        font_but.setPointSize((23))
        font_but.setBold(False)
        font_but.setFamily('Microsoft YaHei')

        # применим стили для labels:
        self.res_eq_label.setFont(font_res)
        self.res_label.setFont(font_res)
        self.eq_label.setFont(font_eq)

        #создаем стиль для сетки кнопок с помощью CSS:
        self.gridLayoutWidget.setStyleSheet("QPushButton {background-color: rgb(82, 201, 220); color: White; border-radius: 4px;}"
                           "QPushButton:pressed {background-color:rgb(190,234,242);}")
        #аналогично для кнопок, к которым применется другие стилистические требования
        self.button_7.setStyleSheet("QPushButton {background-color: rgb(30, 36, 53); color: White; border-radius: 4px;}"
                           "QPushButton:pressed {background-color:rgb(190,234,242);}")
        self.button_8.setStyleSheet("QPushButton {background-color: rgb(30, 36, 53); color: White; border-radius: 4px;}"
                                    "QPushButton:pressed {background-color:rgb(190,234,242);}")
        self.button_9.setStyleSheet("QPushButton {background-color: rgb(30, 36, 53); color: White; border-radius: 4px;}"
                                    "QPushButton:pressed {background-color:rgb(190,234,242);}")
        self.button_4.setStyleSheet("QPushButton {background-color: rgb(30, 36, 53); color: White; border-radius: 4px;}"
                                    "QPushButton:pressed {background-color:rgb(190,234,242);}")
        self.button_5.setStyleSheet("QPushButton {background-color: rgb(30, 36, 53); color: White; border-radius: 4px;}"
                                    "QPushButton:pressed {background-color:rgb(190,234,242);}")
        self.button_6.setStyleSheet("QPushButton {background-color: rgb(30, 36, 53); color: White; border-radius: 4px;}"
                                    "QPushButton:pressed {background-color:rgb(190,234,242);}")
        self.button_1.setStyleSheet("QPushButton {background-color: rgb(30, 36, 53); color: White; border-radius: 4px;}"
                                    "QPushButton:pressed {background-color:rgb(190,234,242);}")
        self.button_2.setStyleSheet("QPushButton {background-color: rgb(30, 36, 53); color: White; border-radius: 4px;}"
                                    "QPushButton:pressed {background-color:rgb(190,234,242);}")
        self.button_3.setStyleSheet("QPushButton {background-color: rgb(30, 36, 53); color: White; border-radius: 4px;}"
                                    "QPushButton:pressed {background-color:rgb(190,234,242);}")
        self.button_0.setStyleSheet("QPushButton {background-color: rgb(30, 36, 53); color: White; border-radius: 4px;}"
                                    "QPushButton:pressed {background-color:rgb(190,234,242);}")
        self.button_dot.setStyleSheet("QPushButton {background-color: rgb(30, 36, 53); color: White; border-radius: 4px;}"
                                    "QPushButton:pressed {background-color:rgb(190,234,242);}")
        #ко всем кнопкам применяем стиль шрифта
        self.button_CE.setFont(font_but)
        self.button_sym.setFont(font_but)
        self.button_percent.setFont(font_but)
        self.button_div.setFont(font_but)
        self.button_7.setFont(font_but)
        self.button_8.setFont(font_but)
        self.button_9.setFont(font_but)
        self.button_mul.setFont(font_but)
        self.button_4.setFont(font_but)
        self.button_5.setFont(font_but)
        self.button_6.setFont(font_but)
        self.button_minus.setFont(font_but)
        self.button_1.setFont(font_but)
        self.button_2.setFont(font_but)
        self.button_3.setFont(font_but)
        self.button_plus.setFont(font_but)
        self.button_0.setFont(font_but)
        self.button_dot.setFont(font_but)
        self.button_eq.setFont(font_but)

        self.verticalLayoutWidget.setLayout(self.verticalLayout)

        #QMetaObject.connectSlotsByName(QCalcWindow)
        self.result_showed = False

        self.add_functions()

    def add_functions(self):
        #numbers
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
        #symbols
        self.button_plus.clicked.connect(
            lambda: self.write_symbol(self.button_plus.text()))
        self.button_minus.clicked.connect(
            lambda: self.write_symbol(self.button_minus.text()))
        self.button_mul.clicked.connect(
            lambda: self.write_symbol(self.button_mul.text()))
        self.button_div.clicked.connect(
            lambda: self.write_symbol(self.button_div.text()))
        self.button_dot.clicked.connect(
            lambda: self.write_symbol(self.button_dot.text()))

        self.button_eq.clicked.connect(self.result)
        self.button_CE.clicked.connect(self.cls)
        self.button_percent.clicked.connect(self.percentage)
        self.button_sym.clicked.connect(self.change_sign)

    def write_number(self, number):
        if self.eq_label.text() == 'Введите выражение' or self.result_showed == True:
            self.eq_label.setText('')
            self.eq_label.setText(number)
            self.result_showed = False
        else:
            self.eq_label.setText(self.eq_label.text() + number)
    def write_symbol(self, symbol):
        if self.eq_label.text() != 'Введите выражение':
            if self.eq_label.text()[-1].isdigit() and self.eq_label.text() != 'Введите выражение':
                self.eq_label.setText(self.eq_label.text() + symbol)
            else:
                self.eq_label.setText(self.eq_label.text()[:-1] + symbol)

    def result(self):
        if self.result_showed == False and self.eq_label.text() != 'Введите выражение': #подумать!
            res = eval(self.eq_label.text())
            self.result_showed = True

            font_res = QtGui.QFont()
            font_res.setBold(True)
            if int(30*14/len(str(res))) <30:
                size = int(30*14/len(str(res)))
            else:
                size = 30
            font_res.setPointSize(size)

            self.res_label.setFont(font_res)
            self.res_label.setText(str(res))
            self.eq_label.setText(str(res))

    def cls(self):
        self.eq_label.setText('Введите выражение')
        self.res_label.setText('0')

    def percentage(self):
        try:
            current_text = str(self.eq_label.text())
            number = re.findall('(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?', current_text)[-2]
            number_percentage = re.findall('(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?', current_text)[-1]
            current_symbol = re.findall(r'[\+\-\*\/]', current_text)[-1]
            res_percentage = float(number)*float(number_percentage)/100
            print(number, number_percentage, current_symbol, res_percentage)
            self.eq_label.setText(''.join(current_text.split(current_symbol)[:-1:])+str(current_symbol)+str(res_percentage))
        except:
            pass

    def change_sign(self):
        try:
            current_text = str(self.eq_label.text())
            number_changed = re.findall('[^\+\-\*\/]+', current_text)[-1]
            len_number = len(str(number_changed))
            constant_text = current_text[:-len_number:]
            if current_text.isdigit():
                self.eq_label.setText(str("-") + current_text)
            else:
                current_symbol = re.findall('[\+\-\*\/]', current_text)[-1]

                if current_symbol in "*/":
                    self.eq_label.setText(
                        ''.join(constant_text) + str('-') + str(number_changed))
                elif current_symbol == '+':
                    while constant_text[-1] in '-+':
                        constant_text = constant_text[:-1:]
                    self.eq_label.setText(''.join(constant_text) + str("-") + str(number_changed))
                elif current_symbol == '-':
                    while constant_text[-1] in '-+':
                        constant_text = constant_text[:-1:]
                    self.eq_label.setText(''.join(constant_text) + str("+") + str(number_changed))
        except:
            pass

def window():
    app = QApplication(sys.argv)
    win = CalcWindow()
    win.show()
    sys.exit(app.exec_())

window()