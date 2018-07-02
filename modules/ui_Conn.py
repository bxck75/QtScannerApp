from PyQt5 import QtCore , QtGui, QtWidgets, uic
import sys
from PyQt5.QtCore import (QByteArray, QDate, QDateTime, QEvent, QPoint, QRect,
        QRegExp, QSettings, QSize, Qt, QTime, QTimer)
from PyQt5.QtGui import QColor, QIcon, QRegExpValidator, QValidator
from PyQt5.QtWidgets import (QAbstractItemView, QAction, QApplication,
        QComboBox, QDialog, QDialogButtonBox, QFileDialog, QGridLayout,
        QGroupBox, QHeaderView, QInputDialog, QItemDelegate, QLabel, QLineEdit,
        QMainWindow, QMessageBox, QStyle, QStyleOptionViewItem, QTableWidget,
        QTableWidgetItem, QTreeWidget, QTreeWidgetItem, QVBoxLayout)
import subprocess
import nmap
import json
class MyWindow(QtWidgets.QMainWindow):
    
    def __init__(self):

        super(MyWindow,self).__init__()
        uic.loadUi('Scanner.ui',self)
        self.pushButton_1.setText('nmap random 10')
        self.pushButton_1.clicked.connect(lambda: self.pushButton_1_Callback())
        self.pushButton_2.setText('nmap localhost')
        self.pushButton_2.clicked.connect(lambda: self.pushButton_2_Callback())

    def _shell_exec(self,cmd):    
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        return p.communicate()[0]
        self.r = str(result)
        return result

    def pushButton_1_Callback(self):                
        print('nmap command button pushed')
        CMD = 'ls' #sys.argv[1]
        #self.Output = self._shell_exec(CMD)
        self.Output = self.NmScan()
        # self.LogEntry("Uphost : "+self.Output['nmap']['scanstats']['uphosts'])
        # self.LogEntry("Downhosts : "+self.Output['nmap']['scanstats']['downhosts'])

    def pushButton_2_Callback(self):                
        print('nmap command button pushed')
        CMD = 'ls' #sys.argv[1]
        #self.Output = self._shell_exec(CMD)
        self.Output = self.NmScanLocal()
        
    def LogEntry(self,entry):
        print('Log entry')
        self.listWidget.addItem(entry)
        # for i in self.Output.splitlines():
        #     self.listWidget.addItem(str(i,'utf-8'))

    def NmScan(self):
        self.nm = nmap.PortScanner()
        self.nm.scan(arguments='-n -iR 10 -sP -PE -PA21,23,80,3389')
        hosts_list = [(x, self.nm[x]['status']['state']) for x in self.nm.all_hosts()]
        for host, status in hosts_list:
            # print('{0}:{1}'.format(host, status))
            self.LogEntry('{0}:{1}'.format(host, status))
        # self.nm.scan(hosts='192.168.1.0/24', arguments='-n -sP -PE -PA21,23,80,3389')
        # return self.nm.scan('127.0.0.1', '22-443')

    def NmScanLocal(self):
        self.nm = nmap.PortScanner()
        self.nm.scan(hosts='192.168.178.0/24', arguments='-p 22-443')
        hosts_list = [(x, self.nm[x]['status']['state']) for x in self.nm.all_hosts()]
        for host, status in hosts_list:
            # print('{0}:{1}'.format(host, status))
            print(self.nm.command_line()) 
            self.LogEntry('{0}:{1}'.format(host, status))
            



if __name__ == '__main__':

    app= QtWidgets.QApplication(sys.argv)
    windows = MyWindow()
    windows.show()
    sys.exit(app.exec_())