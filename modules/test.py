from PyQt5 import QtCore , QtGui, QtWidgets, uic
from PyQt5.QtCore import (QByteArray, QDate, QDateTime, QEvent, QPoint, QRect,
        QRegExp, QSettings, QSize, Qt, QTime, QTimer)
from PyQt5.QtGui import QColor,QFont, QIcon, QRegExpValidator, QValidator
from PyQt5.QtWidgets import (QAbstractItemView, QAction, QApplication,
        QComboBox, QDialog, QDialogButtonBox, QFileDialog, QGridLayout,QWidget,QDockWidget,
        QGroupBox, QHeaderView, QInputDialog, QItemDelegate, QLabel, QLineEdit,QProgressDialog,
        QMainWindow, QMessageBox, QStyle, QStyleOptionViewItem, QListWidget, QTableWidget,QSpinBox,
        QTableWidgetItem, QTreeWidget, QTreeWidgetItem, QVBoxLayout,QFormLayout,QPushButton,QSlider)
import PyQt5
import nmap,sqlmap,json,subprocess,re,os,sys
from random import randint
from Helper import Tools
import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt


import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):      
        
        self.text = "Лев Николаевич Толстой\nАнна Каренина"
        self.setGeometry(1400, 300, 680,270)
        self.setWindowTitle('test')
        self.show()
        
    def CentralWidget(self,event):
        qw =   QWidget()
        label = QLabel()
        qw.setWindowTitle(label)
        self.setCentralWidget(qw)

    # def paintEvent(self, event):

    #     qp = QPainter()
    #     qp.begin(self)
    #     self.drawText(event, qp)
    #     qp.end()
        
        
    # def drawText(self, event, qp):
      
    #     qp.setPen(QColor(168, 34, 3))
    #     qp.setFont(QFont('Decorative',30))
    #     qp.drawText(event.rect(), Qt.AlignCenter, self.text)        
                
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())