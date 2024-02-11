import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QApplication, QPushButton, QGridLayout, QWidget

class CalcWindow(QMainWindow):
    def __init__(self):
        super(CalcWindow, self).__init__()
        self.initUI() #при создании экземляра класса, применяем к нему настройки UI

    def initUI(self):
        #self.setEnabled(True)
        self.setGeometry(220, 220, 500, 620) #в точке 1, 2, выводим окно с размерами 3, 4
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
        font_but.setPointSize((20))
        font_but.setBold(True)

        #запись ответа и выражения будут представлены классами QLabel:
        # область результата, согласно макету, имеет постоянный знак "="

        self.res_label = QtWidgets.QLabel(self)
        self.res_eq_label = QtWidgets.QLabel(self)

        self.eq_label = QtWidgets.QLabel(self)

        #применим стили для labels:
        self.res_eq_label.setFont(font_res)
        self.res_label.setFont(font_res)
        self.eq_label.setFont(font_eq)

        #для применения стиля ко всем кнопкам,создадим объект Frame
        self.buttons_frame = QtWidgets.QFrame()
        self.buttons_frame.setFont(font_but)

        #теперь определим места положения трех областей:
        self.buttons_frame.setGeometry(0, 300, 500, 320)
        self.eq_label.setGeometry(0, 200, 480, 100)
        self.res_label.setGeometry(150, 50, 330, 150)
        self.res_eq_label.setGeometry(20, 50, 150, 150)

        #теперь определим первоначальный текст на lables:
        self.res_label.setText('0')
        self.res_eq_label.setText('=')
        self.eq_label.setText('Введите выражение')

        #выравнивание
        self.res_label.setAlignment(QtCore.Qt.AlignRight)
        self.res_eq_label.setAlignment(QtCore.Qt.AlignLeft)
        self.eq_label.setAlignment(QtCore.Qt.AlignRight)

        #создаем кнопки


def window():
    #
    app = QApplication(sys.argv)
    win = CalcWindow()
    win.show()
    sys.exit(app.exec_())

window()