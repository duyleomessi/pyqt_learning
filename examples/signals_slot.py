#!/usr/bin/env python3

"""Signals and slots example"""

import sys
import functools

from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget

def greeting():
    """Slot function"""
    if msg.text():
        msg.setText("")
    else:
        msg.setText('Greeting')

def hello(who):
    """Slot function"""
    if msg.text():
        msg.setText("")
    else:
        msg.setText(f'Hello {who}')


app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Signals and slots')
layout = QVBoxLayout()

btn1 = QPushButton('Greet')
btn1.clicked.connect(greeting)
layout.addWidget(btn1)

btn2 = QPushButton('Hello')
btn2.clicked.connect(functools.partial(hello, 'World!'))
layout.addWidget(btn2)
msg = QLabel('')
layout.addWidget(msg)

window.setLayout(layout)
window.show()
sys.exit(app.exec_())
