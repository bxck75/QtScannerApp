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

_DOCK_OPTS =  QtWidgets.QMainWindow.AnimatedDocks
_DOCK_OPTS |=  QtWidgets.QMainWindow.AllowNestedDocks
_DOCK_OPTS |=  QtWidgets.QMainWindow.AllowTabbedDocks

_DOCK_COUNT = 0
_DOCK_POSITIONS = (
    QtCore.Qt.LeftDockWidgetArea,
    QtCore.Qt.TopDockWidgetArea,
    QtCore.Qt.RightDockWidgetArea,
    QtCore.Qt.BottomDockWidgetArea
)

def mainWindow():
    
    mainWindows = QtWidgets.QDockWidget()
    # mainWindow = QtWidgets.QMainWindow()
    # mainWindow.resize(1024,768)
    # mainWindow.setDockOptions(_DOCK_OPTS)

    widget = QGridLayout()
    # widget.setMinimumSize(100,100)
    # widget.setFrameStyle(widget.box())
    Tools.InspectC(mainWindows,mainWindows
    Tools.InspectM(mainWindows,mainWindows)
    mainWindow.setCentralWidget(widget)
    btn = QtCore.Qt.QButtonGroup.Balloon

    sub = QtWidgets.QMainWindow()
    sub.setWindowFlags(QtCore.Qt.Widget)
    sub.setDockOptions(_DOCK_OPTS)

    color = tuple(randint(20, 230) for _ in xrange(3))
    # addDocks(mainWindow, "Main Dock")
    Tools.InspectC(mainWindows)
    Tools.InspectM(mainWindows)
    mainWindow.show()
    mainWindow.raise_()
    return mainWindow


def main():
    app = QApplication(sys.argv)
    form = mainWindow()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()