#!/usr/bin/python3
# -*- coding: utf-8 -*-

# TODO: было import sys, json не удобно, когда кода много читающий его человек хочет видеть каждый импорт отдельно
# import sys, json
import sys
import json
import Fairytale
from PyQt4 import QtCore, QtGui

# TODO: from something import * используется только для импортов конфигов с константами,
#  тем более предыдущей строкой ты уже импортнула модули QtCore и QtGui
# from PyQt4.QtCore import *
# from PyQt4.QtGui import *

TALE = open("Fairytale.json")
data = json.load(TALE)


class MyWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent=parent)
        self.setGeometry(350, 80, 500, 400)
        self.setMinimumSize(QtCore.QSize(800,600))
        self.setWindowTitle(u'Генератор сказок')
        self.setWindowIcon(QtGui.QIcon('poop.png'))

        exit = QtGui.QAction(QtGui.QIcon('bender.png'), u'Выход', self)
        exit.setShortcut('Ctrl+Q')
        exit.setStatusTip('Exit application')
        self.connect(self, QtCore.SIGNAL('closeEmitApp()'), QtCore.SLOT('close()'))
        self.connect(exit, QtCore.SIGNAL('triggered()'), QtCore.SLOT('close()'))


class StartWindow(MyWindow):
    def __init__(self, parent=None):
        MyWindow.__init__(self, parent=parent)

        welcome_label = QtGui.QLabel(data['welcome']['1'])
        welcome_label.adjustSize()

        layout = self.layout()
        layout.addWidget(welcome_label)

        pattern_button = QtGui.QPushButton(u'Используем шаблон')
        pattern_button.adjustSize()
        ready_button = QtGui.QPushButton(u'Хочу готовую сказку!')
        ready_button.adjustSize()

        ready_button.move(0, welcome_label.size().height())
        pattern_button.move(ready_button.width(), welcome_label.size().height())
        layout.addWidget(ready_button)
        layout.addWidget(pattern_button)

        main = MainWindow(parent=self)

        ready_button.clicked.connect(main.show)


class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent=parent)
        self.setGeometry(350, 80, 500, 400)
        self.setWindowTitle(u'Генератор сказок')
        self.setWindowIcon(QtGui.QIcon('poop.png'))

        exit = QtGui.QAction(QtGui.QIcon('bender.png'), u'Выход', self)
        exit.setShortcut('Ctrl+Q')
        exit.setStatusTip('Exit application')
        self.connect(self, QtCore.SIGNAL('closeEmitApp()'), QtCore.SLOT('close()'))
        self.connect(exit, QtCore.SIGNAL('triggered()'), QtCore.SLOT('close()'))

        centralwidget = QtGui.QWidget()
        self.setCentralWidget(centralwidget)

        vbox = QtGui.QVBoxLayout()
        hbox = QtGui.QHBoxLayout()
        hbox1 = QtGui.QHBoxLayout()

        textbox1 = QtGui.QPlainTextEdit()
        button1 = QtGui.QPushButton(u'Готовая сказка')
        button2 = QtGui.QPushButton(u'Хочу сделать сам')
        textbox2 = QtGui.QLineEdit()

        vbox.addWidget(textbox1)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox)
        hbox1.addWidget(textbox2)
        hbox.addWidget(button1)
        hbox.addWidget(button2)
        centralwidget.setLayout(vbox)

        self.statusBar()

        menubar = self.menuBar()
        file = menubar.addMenu(u'Файл')
        file.addAction(exit)

    def closeEvent(self, event):
        reply = QtGui.QMessageBox.question(self, u'Подтверждение действия',
                                           u"Вы уверены, что хотите выйти? Yes - Да, No - Нет", QtGui.QMessageBox.Yes,
                                           QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


app = QtGui.QApplication(sys.argv)
start = StartWindow()
start.show()
sys.exit(app.exec_())
