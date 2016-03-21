import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from widgets import *
from tools import *

def my_button(button):
	button.setFont(QFont("Century Gothic",9,QFont.Bold))
	button.setFixedWidth (100)
	button.setStyleSheet("background-color: rgb(55,63,81); color: rgb(190,207,206)")
	return button

	
def my_lineEdit(line):
	line.setReadOnly(True)
	line.setFrame(True)
	line.setFont(QFont("Century Gothic",10))
	return line

#Add Menubar to Main Window
def menubar(window):
    bar=window.menuBar()
    f=bar.addMenu("File")
    exit=QAction("Exit",window)
    exit.setShortcut("Ctrl+X")
    f.addAction(exit)
    edit =bar.addMenu("?")
    edit.addAction("Help")
    edit.addAction("About")
    return window
	
	
#Add a scroll to a widget.
def scroll(widget):
    scroll=QScrollArea()
    scroll.setWidget(widget)
    scroll.setWidgetResizable(True)
    scroll.setFixedHeight(270)
    return scroll
	
	
def lines(list):
	win = QWidget()
	form = QFormLayout(win)
	vLine=QFrame()
	for p in list:	
		layout = QHBoxLayout()
		s=QPushButton("Extract")
		s = my_button(s)
		l=QLineEdit()
		l.setStyleSheet("background:rgb(55,63,81); color:rgb(228,223,225)")
		l.setText(str(p))
		l = my_lineEdit(l)
		layout.addWidget(l)
		layout.addWidget(s)
		form.addRow(layout)
		form.addRow(vLine)
		win.setLayout(form)
		win.setPalette(color(216,219,226))
	
	
	win = scroll(win)	
	return win, form

def decor_widget(widget):
	widget.setPalette(color(133,164,161))
	widget = scroll(widget)
	return widget
		
	

def lines_done(list):
	win = QWidget()
	form = QFormLayout(win)
	vLine=QFrame()
	for p in list:	
		layout = QHBoxLayout()
		s=QPushButton("Extracted")
		s = my_button(s)
		s.setFlat(True)
		l=QLineEdit()
		l.setStyleSheet("background:rgb(55,63,81); color:rgb(228,223,225)")
		l.setText(str(p))
		l = my_lineEdit(l)
		layout.addWidget(l)
		layout.addWidget(s)
		form.addRow(layout)
		form.addRow(vLine)
		win.setLayout(form)
		win.setPalette(color(55,63,81))
	
	
	win = scroll(win)	
	return win, form
