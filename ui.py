#!/usr/bin/env python3

import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QSpacerItem
from PyQt5.QtWidgets import QSizePolicy

from data import process_text

def log_lifts():
    text = lifts_text.toPlainText()

    workouts = process_text(text)
    #send_to_server(workouts)

app = QApplication(sys.argv)

# strings
title = 'Log Your Lifts'

# Main window
window = QWidget()
window.setWindowTitle(title)
window.setGeometry(100, 100, 280, 80)

layout = QVBoxLayout()

old_lifts = QLabel()
ol_size_policy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
ol_size_policy.setVerticalStretch(2)
old_lifts.setSizePolicy(ol_size_policy)
layout.addWidget(old_lifts)

lifts_text = QTextEdit()
l_size_policy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
l_size_policy.setVerticalStretch(1)
lifts_text.setSizePolicy(l_size_policy)
layout.addWidget(lifts_text)

btn_layout = QHBoxLayout()

btn_layout.addSpacerItem(QSpacerItem(0, 0, QSizePolicy.Expanding))
accept_btn = QPushButton('Log Lifts')
accept_btn.clicked.connect(log_lifts)
btn_layout.addWidget(accept_btn)

layout.addLayout(btn_layout)

window.setLayout(layout)

window.show()

sys.exit(app.exec_())
