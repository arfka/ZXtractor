import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *




#dimension Class
class dimension:
    def __init__(self, width, height):
        self.width = width
        self.height = height
		
def thecenter():
	from win32api import GetSystemMetrics
	d = dimension(GetSystemMetrics(0)/2,GetSystemMetrics(1)/2)
	return d
	#Center of the screen
def get_center(app):
	screen_resolution = app.desktop().screenGeometry()
	d = dimension ((int(screen_resolution.width()/3)), (int(screen_resolution.height()/3))) 
	return d 
	
	
#RGB Color Palette
def set_color (r,g,b):
    palette = QPalette()
    palette.setColor(QPalette.Background, QColor.fromRgb(r,g,b))
    return palette