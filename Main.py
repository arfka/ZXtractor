import Graphic_Elements as ge 
from tools import *
import time
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *


'''
Palette

216,219,226

169,188,208

88,164,176

55,63,81

27,27,30
'''

def browse_signal():
	dir = QFileDialog.getExistingDirectory(None, 'Select a folder:', 'C:\\', QFileDialog.ShowDirsOnly)
	return dir 
'''
def window():

	app = QApplication(sys.argv)
	app.setWindowIcon(QIcon('img/icon.png'))
	mwin = QMainWindow()
	mwin.setWindowTitle("Zextract")
	mwin = ge.menubar(mwin)
	main = QWidget()
	win = QWidget()
	sub_layout = QVBoxLayout(win)
	button = QPushButton("Browse")
	label = QLineEdit()
	button = ge.my_button(button)
	label = ge.my_lineEdit(label)
	button.clicked.connect(lambda: self.install(l))
	sub_layout.addWidget(ge.lines(60))
	cen = get_center(app)
	mwin.setGeometry(int(cen.width), int(cen.height),800,400)
	mwin.setPalette(set_color(190,207,206))
	mwin.setCentralWidget(win)
	QApplication.setStyle(QStyleFactory.create("plastique"))
	mwin.show()
	sys.exit(app.exec_())
'''

class extract_widget(QWidget):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        win = QWidget()




class App_Widget(QWidget):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        self.setMaximumHeight(400)
        win = QWidget()
        self.win1 = QWidget()
        self.layout = QVBoxLayout(self)
        self.lines = QWidget()
        self.path = ""
        layout = QHBoxLayout(win)
        self.layout3 = QHBoxLayout(self.lines)
        self.button = ge.my_button(QPushButton("Browse"))
        self.label = ge.my_lineEdit(QLineEdit())
        self.label.setStyleSheet("background:rgb(55,63,81); color:rgb(228,223,225)")
        QObject.connect(self.button, SIGNAL(("clicked()")), self.browse)
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        
        self.layout.addWidget(win)
        self.layout.setSpacing(0.5)
        self.layout.setMargin(0.5)
        

    def extract_button(self):
        self.win1 = QWidget()
        self.win1.setFixedHeight(40)
        layout1 = QHBoxLayout(self.win1)
        self.button1 = ge.my_button(QPushButton("Extract All"))
        QObject.connect(self.button1, SIGNAL(("clicked()")), self.extract_all)
        layout1.addWidget(self.button1)
        layout1.setContentsMargins(0,0,0,0)
        self.win1.setMaximumHeight(40)
        return

    def extract_all(self):
        #self.setEnabled(False)
        progressBox = QProgressDialog("Extracting!",QString(0),0,100)
        progressBox.setWindowFlags(Qt.FramelessWindowHint)
        progressBox.setStyleSheet("background:rgb(55,63,81); color:rgb(228,223,225);")
        progressBox.setCancelButton(None)
        progressBox.setWindowTitle("Extracting Archives")
        progressBox.show()
        import os,zipfile,rarfile
        from PyQt4.QtGui import QApplication
        pourc = 100.0/len(self.num_f)
        output = 0              
        for f in self.zipf:
                QApplication.instance().processEvents()
                source= os.path.join(str(self.path),f)
                progressBox.setLabelText(("Extracting \""+f+"\""))
                
                with zipfile.ZipFile(source) as zf:
                        dest = f.replace('.zip','')
                        zf.extractall(dest)
                for x in range (int(output - pourc), int(output)):
                        progressBox.setValue(x)
                        time.sleep (0.1)
                if progressBox.wasCanceled():
                        break
                output += pourc
               
        progressBox.setLabelText("Done!")
        progressBox.setValue(output)
        progressBox.close()
        del progressBox
        self.setEnabled(True)
        self.remove_w()
        self.lines, self.layout3 = ge.lines_done(self.num_f)
        self.layout.addWidget(self.lines)
        self.layout3.update()
        self.update()

    
    
    def browse(self):
        self.remove_w()
        self.fileDialog = QFileDialog()
        self.path = self.fileDialog.getExistingDirectory()
        self.label.setText(self.path)
        self.directory()
        
    def remove_w (self):
        self.layout.removeWidget(self.lines)
        self.layout.removeWidget(self.win1)
        self.lines.close()
        self.win1.close()
                
	
    def directory(self):
        import os
        import glob
        self.layout.addWidget(self.lines)
        self.setMaximumHeight(400)
        os.chdir(str(self.path))
        #self.rarf = glob.glob("*.rar")
        self.zipf = glob.glob("*.zip")
        self.num_f = self.zipf
        del self.lines
        self.lines, self.layout3 = ge.lines(self.num_f)
        self.layout.addWidget(self.lines)
        if self.num_f:
                self.extract_button()
        else:
                l=QLineEdit()
                l.setStyleSheet("background:rgb(55,63,81); color:rgb(228,223,225)")
                l.setText("No Zip Archive in this Directory")
                self.layout.addWidget(l)
		
        self.layout3.update()
        self.layout.addWidget(self.win1)
        self.update()

    def return_layout(self):
        return self.layout


#MainWindow
def main_window():
	app = QApplication(sys.argv)
	app.setStyleSheet('QMainWindow{border: 1px solid black;}')
	app.setWindowIcon(QIcon('img/icon.png'))
	mwin = QMainWindow()
	mwin.setWindowTitle("ZExtract")
	win = App_Widget()
	#mwin = ge.menubar(mwin)
	cen = get_center(app)
	mwin.setGeometry(int(cen.width), int(cen.height),500,40)
	mwin.setPalette(set_color(55,63,81))
	mwin.setCentralWidget(win)
	QApplication.setStyle(QStyleFactory.create("plastique"))
	mwin.show()
	sys.exit(app.exec_())	




	
#Main
if __name__ == '__main__':
 main_window()
 

