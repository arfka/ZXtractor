import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

          

#dimension Class
class dimension:
    def __init__(self, width, height):
        self.width = width
        self.height = height

#RGB Color Palette
def color (r,g,b):
    palette = QPalette()
    palette.setColor(QPalette.Background, QColor.fromRgb(r,g,b))
    return palette

#Center of the screen
def center(app):
    screen_resolution = app.desktop().screenGeometry()
    d = dimension ((int(screen_resolution.width()/3)), (int(screen_resolution.height()/3))) 
    return d 

#Custom form 
def inf_Layout(i):
    win = QWidget()
    for s in range (i):
        b = QPushButton("Button" + str(s))
        l = QLabel ("Label" + str(s))
        form.addRow(b,l)
    return win

#Custom form 2
def lines(i):
    win = QWidget()
    for p in range(i):
        s=QPushButton("hello")
        l=QLabel("World" + str(p))    
        form.addRow(s,l)
    win.setLayout(form)
    return win

#Add a scroll to a widget.
def scroll(widget):
    scroll=QScrollArea()
    scroll.setWidget(widget)
    scroll.setWidgetResizable(True)
    scroll.setFixedHeight(400)
    return scroll

#Custom Widget
class Widget1(QWidget):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        mainlayout=QFormLayout(self)
        win = QWidget()
        layout2 = QFormLayout(win)
        f = file("outfile.txt", "rb")
        line = f.readlines()
        vLine=QFrame()
        vLine.setFrameShape(QFrame.HLine)
        vLine.setAutoFillBackground(True)
        vLine.setFrameShadow(QFrame.Sunken)
        header = QHBoxLayout()
        header1 = QLabel("Package Name")
        header1.setFixedWidth(200)
        header1.setFont(QFont("Century Gothic", 10, QFont.Bold))
        header2 = QLabel("version")
        header2.setFont(QFont("Century Gothic", 10, QFont.Bold))
        header.addWidget(header1)
        header.addWidget(header2)
        mainlayout.addRow(header)
        mainlayout.addRow(vLine)
        self.Button = []
        i = 0
        self.s = []
        
        for j in line:
            self.name = ""
            layout = QHBoxLayout()
            l = j.split("==")
            self.s.append(str(l[0]))
            self.name = self.s[i]
            s1 = str(l[1])
            self.Button.append(QPushButton("Install"))
            self.Button[i].setFont(QFont("Century Gothic",9,QFont.Bold))
            self.Button[i].setFixedWidth (100)
            package_name = QLineEdit()
            package_name.setText(self.name)
            package_name.setReadOnly(True)
            package_name.setFrame(False)
            package_name.setFixedWidth (200)
            package_name.setFont(QFont("Century Gothic",10,QFont.Bold))
            package_ver = QLineEdit()
            package_ver.setText(s1)
            package_ver.setReadOnly(True)
            package_ver.setFrame(False)
            package_name.setFont(QFont("Century Gothic",10))
            layout.addWidget(package_name)
            layout.addWidget(package_ver)
            layout.addWidget(self.Button[i])
            layout2.addRow(layout)
            layout2.addRow(vLine)
            self.signals(i)
            i += 1
        win = scroll(win)
        self.out = QTextEdit()
        self.out.setReadOnly(True)
        self.out.setMaximumHeight(100)
        self.out.setFrameStyle(QFrame.WinPanel)
        self.out.setFrameStyle(QFrame.Sunken)
        mainlayout.addWidget(win)
        mainlayout.addRow(self.out)
        
        f.close()


    def install(self, s):
        d = redirect(install_package, s)
        self.out.clear()
        self.out.setText(d)
    def signals(self, i, p=0, k="None"):
        l = self.name
        if p ==0:
            self.Button[i].clicked.connect(lambda: self.install(l))
            return
        else:
            k = self.install(l)
            return k
