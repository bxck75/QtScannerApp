# Requirements
from PyQt5 import QtCore , QtGui, QtWidgets, uic
from PyQt5.QtCore import (QByteArray, QDate, QDateTime, QEvent, QPoint, QRect,pyqtSlot,
        QRegExp, QSettings, QSize, Qt, QTime, QTimer)
from PyQt5.QtGui import QColor,QFont, QIcon, QRegExpValidator, QValidator
from PyQt5.QtWidgets import (QAbstractItemView, QAction, QApplication,
        QComboBox, QDialog, QDialogButtonBox, QFileDialog, QGridLayout,QWidget,QDockWidget,
        QGroupBox, QHBoxLayout,QHeaderView, QInputDialog, QItemDelegate, QLabel, QLineEdit,QProgressDialog,
        QMainWindow, QMessageBox, QStyle, QStyleOptionViewItem, QListWidget, QTableWidget,QSpinBox,
        QTableWidgetItem, QTreeWidget, QTreeWidgetItem, QVBoxLayout,QFormLayout,QPushButton,QSlider)
import nmap,sqlmap,json,subprocess,re,os,sys,inspect
from random import randint
import modules.ScanDo as ScanDo
import modules.Helper as Helper

from modules.MyConsole import IPythonWidget
import Scanner_rc

# research info
    # Resources
        # Run this command to make the resource file
        # pyrcc4 -py3 F:\computing\Payrollv22\icon.qrc -o icon_rc.py
    # Ipython class methods
        # <class 'modules.MyConsole.IPythonWidget'>
        # --- PaintDeviceMetric
        # --- RenderFlag
        # --- RenderFlags
        # --- _CallTipRequest
        # --- _CompletionRequest
        # --- _ExecutionRequest
        # --- _PromptBlock
        # --- __class__
        # <class 'modules.MyConsole.IPythonWidget'>
        # --- class_config_rst_doc
        # --- class_config_section
        # --- class_get_help
        # --- class_get_trait_help
        # --- class_own_trait_events
        # --- class_own_traits
        # --- class_print_help
        # --- class_trait_names
        # --- class_traits
        # --- section_names
        # --- trait_events
    # console commands examples
        # console.execute('print "Hello World."\r')
        # console.execute('import nmap\r')
        # console.execute('nmp=nmap.PortScanner()\r')
        # console.execute("nmp.scan('192.168.178','80')\r")
    # General info
        # print(IPythonWidget.class_get_help())
        # self.PScanner = nmap.PortScanner()
        # self.t = IPythonWidget()
        # self.qt_console = QTC.Main_Init('["namp":["-iR 10","--open -Pn -n -v"]]')
        # self.QScanner = sqlmap()
        # self.Hp.InspectC(MyConsole)
        # self.Hp.InspectM(MyConsole)
        # test2.(['foo',''])
        # self.setProperty("windowOpacity", 0.9);
        # print(self.windowIcon())

class MyWindow(QtWidgets.QMainWindow):
    
# init!!!!
    def __init__(self):
        super(MyWindow,self).__init__()
        # debug 
        self.Hp = Helper.Tools()
        self.Hp.InspectC(IPythonWidget)
        self.Hp.InspectM(IPythonWidget)
        # load layout
        uic.loadUi('nice1.ui',self)# <----------Template!!!!
        # layout settings
        self.console_commands = []
        # self.showFullScreen()
        self.hide()
        self.setWindowTitle("Scanner")
        # set dockers
        self.placeholder = QWidget()
        self.rand_color = tuple(randint(112, 230) for _ in range(3))
        self.rand_color2 = tuple(randint(200, 230) for _ in range(3))

        self.ComboBox_1 = QComboBox()
        self.ComboBox_1.addItem("Page 1");
        self.ComboBox_1.addItem("Page 2");
        # pageComboBox->addItem(tr("Page 3"));
        
        AllItems = [self.ComboBox_1.itemText(i) for i in range(self.ComboBox_1.count())]
        print(self.ComboBox_1.itemText(0))
        # self.ComboBox_1.currentIndexChanged.connect(self.display(self.ComboBox_1.WidgetIndex(int(self.ComboBox_1.itemText(0)))))
        # self.setStyleSheet("background-color: rgb(%d, %d, %d)" % self.rand_color)
        # self.setStyleSheet("highlight: rgb(%d, %d, %d)" % self.rand_color2) 
        # self.LostDockButton = QDialogButtonBox()
        # self.Hp.InspectC(QDialogButtonBox)
        # self.Hp.InspectM(QDialogButtonBox.StandardButtons)
        # self.createTable()
        self.TopDockPlaceholder = self.setupDock(self.placeholder,'top',True)
        # self.setupDock(self.console(),'bottom')
        # self.setupDock(self.console(),'top')

    def display(self,i):
        self.stackedWidget.setCurrentIndex(i)

# Setup dockers
    def setupDock(self,content,dock_pos,fake=False):
        pos_switcher = {
            "top"   : Qt.TopDockWidgetArea,
            "bottom": Qt.BottomDockWidgetArea,
            "left"  : Qt.LeftDockWidgetArea,
            "right" : Qt.RightDockWidgetArea
        }
        position = pos_switcher.get(dock_pos, "Invalid Dock position")            
        s = QWidget()
        vboxlayout = QGridLayout()
        vboxlayout.addWidget(content)
        s.setLayout(vboxlayout)
        self.qdock = QDockWidget()
        self.qdock.setStyleSheet("background-color: gray")
        self.qdock.setWindowFlags(Qt.FramelessWindowHint)
        self.qdock.setWidget(s)
        self.addDockWidget(position, self.qdock)
        fake = True    
# Slider Handlers
    # nmap random qty scan slider
        self.NmapRandomCount = 4
        self.horizontalSlider_Nmap_Random.setMinimum(5)
        self.horizontalSlider_Nmap_Random.setMaximum(1500)
        self.horizontalSlider_Nmap_Random.setValue(int(self.NmapRandomCount))
        self.horizontalSlider_Nmap_Random.setTickPosition(QSlider.TicksBelow)
        self.horizontalSlider_Nmap_Random.setTickInterval(10)
        self.horizontalSlider_Nmap_Random.valueChanged.connect(self.valuechange_nmap_slider)
    # inurlbr page qty slider
        self.InurlPageCount = 1
        self.horizontalSlider_Inurlbr_Pages.setMinimum(1)
        self.horizontalSlider_Inurlbr_Pages.setMaximum(15)
        self.horizontalSlider_Inurlbr_Pages.setValue(int(self.InurlPageCount))
        self.horizontalSlider_Inurlbr_Pages.setTickPosition(QSlider.TicksBelow)
        self.horizontalSlider_Inurlbr_Pages.setTickInterval(1)
        self.horizontalSlider_Inurlbr_Pages.valueChanged.connect(self.valuechange_inurl_slider)
# button trigger
        self.pushButton_1.setText('Nmap random '+str(self.NmapRandomCount))
        self.pushButton_1.clicked.connect(lambda: self.pushButton_1_Callback())
        self.pushButton_2.setText('Nmap Custom Scan')
        self.pushButton_2.clicked.connect(lambda: self.pushButton_2_Callback())
        self.pushButton_3.setText('Inurlbr dork '+str(self.InurlPageCount)+' pages')
        self.pushButton_3.clicked.connect(lambda: self.pushButton_3_Callback())
        self.listWidget_Save.setText('Save Output')
    # listWidget save 
        self.listWidget_file = 'resource/listwidget.lst'
        self.listWidget_Save.clicked.connect(lambda: self.listWidget_Save_Callback())
    # textfield 1
        self.SaveButtonText_1_Callback_file = 'resource/nmap_presets.lst'
        self.SaveButtonText_1.clicked.connect(lambda: self.SaveButtonText_1_Callback())
        for i in self.Hp.ReadListFromFile(self.SaveButtonText_1_Callback_file):
            self.plainTextEdit_1.appendPlainText(i)
    # textfield 2
        self.SaveButtonText_2_Callback_file = 'resource/shop_dorks.lst'
        self.SaveButtonText_2.clicked.connect(lambda: self.SaveButtonText_2_Callback())
        for i in self.Hp.ReadListFromFile(self.SaveButtonText_2_Callback_file):
            self.plainTextEdit_2.appendPlainText(i)
    # textfield 3
        self.SaveButtonText_3_Callback_file = 'resource/console_history.ipy'
        self.SaveButtonText_3.clicked.connect(lambda: self.SaveButtonText_3_Callback())
        for i in self.Hp.ReadListFromFile(self.SaveButtonText_3_Callback_file):
            self.plainTextEdit_3.appendPlainText(i)
    # textfield 4
        self.SaveButtonText_4_Callback_file = 'resource/loot.lst'
        self.SaveButtonText_4.clicked.connect(lambda: self.SaveButtonText_4_Callback())
        for i in self.Hp.ReadListFromFile(self.SaveButtonText_4_Callback_file):
            self.plainTextEdit_4.appendPlainText(i)
# Styles
        #Styles
        self.FontSize = "font:16px;"
        self.SelectionColor = "selection-color: blue;"
        self.SelectionColor = "selection-color: light-gray;"
        self.FontColor = "color: green;"
        self.FontColor = "color: white;"
        self.BackgroundColor = "selection-background-color: white;"
        self.BackgroundColor= "selection-background-color: white;"
        self.RoundBorders = "border-width: 2px;border-radius: 10px;"
        print(self.RoundBorders)
        #Style settings
        self.listWidget.setStyleSheet(self.RoundBorders)

         #.setStyleSheet(self.RoundGrayRoundBorders)
# text field save callbacks
    def SaveButtonText_1_Callback(self):
        print(self.SaveButtonText_1_Callback_file)
        self.Hp.saveFile(self.SaveButtonText_1_Callback_file,self.plainTextEdit_1)
    def SaveButtonText_2_Callback(self):
        print(self.SaveButtonText_2_Callback_file)
        self.Hp.saveFile(self.SaveButtonText_2_Callback_file,self.plainTextEdit_2)
    def SaveButtonText_3_Callback(self):
        print(self.SaveButtonText_3_Callback_file)
        self.Hp.saveFile(self.SaveButtonText_3_Callback_file,self.plainTextEdit_3)
    def SaveButtonText_4_Callback(self):
        print(self.SaveButtonText_4_Callback_file)
        self.Hp.saveFile(self.SaveButtonText_4_Callback_file,self.plainTextEdit_4)
    def listWidget_Save_Callback(self):
        print(self.listWidget_file)
        print(self.listWidget.count())
        with open(self.listWidget_file, 'a') as theFile:
            for i in range(self.listWidget.count()):
                theFile.write(''.join([str(self.listWidget.item(i).text()), '\n']))
        for i in self.Hp.ReadListFromFile(self.SaveButtonText_4_Callback_file):
            self.plainTextEdit_4.appendPlainText(i)
        # self.Hp.saveFile(self.listWidget_file,self.listWidget)
# buttons callback
    def pushButton_1_Callback(self):                
        print('nmap command button pushed')
        ok,ports = self.getItemsDialog('nmap_ports')
        print("picked ports : "+ports)
        print('Finding '+str(self.NmapRandomCount)+' random Targets...')
        if ok:
            self.ports = ports
            self.Output = self.NmRandomScan()

    def pushButton_2_Callback(self):                
        print('nmap command button pushed')
        ok,args = self.getItemsDialog('nmap_presets')
        print("picked args : "+args)
        if ok:
            ok,ip = self.getText('nmap_ip')
            print("picked ip : "+ip)
            if ok:
                self.Output = self.NmCustomScan(ip,args)

    def pushButton_3_Callback(self):                
        print('InurlBr command button pushed')
        ok,item = self.getItemsDialog('shop_dorks')
        print("picked dork : "+item)
        if ok:
            self.Output = self.PhpInurlbr(item)
# value changers
    def valuechange_nmap_slider(self):
            # print('size set to'+str(self.horizontalSlider_Nmap_Random.value()))
            size = self.horizontalSlider_Nmap_Random.value()
            self.pushButton_1.setText('Nmap scan '+str(size)+' random ips')
            self.horizontalSlider_Nmap_Random.setFont(QFont("Arial",size))
            self.NmapRandomCount = str(size)

    def valuechange_inurl_slider(self):          
            # print('size set to'+str(self.horizontalSlider_Nmap_Random.value()))
            size = self.horizontalSlider_Inurlbr_Pages.value()
            self.pushButton_3.setText('Inurlbr dork '+str(size)+ ' pages')
            self.horizontalSlider_Inurlbr_Pages.setFont(QFont("Arial",size))
            self.InurlPageCount = str(size)
    
    def createTable(self):       # Create table
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(4)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setItem(0,0, QTableWidgetItem("Cell (1,1)"))
        self.tableWidget.setItem(0,1, QTableWidgetItem("Cell (1,2)"))
        self.tableWidget.setItem(1,0, QTableWidgetItem("Cell (2,1)"))
        self.tableWidget.setItem(1,1, QTableWidgetItem("Cell (2,2)"))
        self.tableWidget.setItem(2,0, QTableWidgetItem("Cell (3,1)"))
        self.tableWidget.setItem(2,1, QTableWidgetItem("Cell (3,2)"))
        self.tableWidget.setItem(3,0, QTableWidgetItem("Cell (4,1)"))
        self.tableWidget.setItem(3,1, QTableWidgetItem("Cell (4,2)"))
        self.tableWidget.move(0,0)
 
        # table selection change
        self.tableWidget.doubleClicked.connect(self.on_click)
 
    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())
 
# get data dialogs
    # get list items dialogs
    def getItemsDialog(self,type):
        if type == 'shop_dorks':
            itemsfromfile = self.Hp.ReadListFromFile('resource/'+type+'.lst')
            result = QInputDialog.getItem(self, "select input dialog","choose dork", itemsfromfile, 0, False)
            if not (result is None):
                print(result)          
                item,ok = result
                print(ok,item)
                
                if ok == True and item is not None:
                    print(ok,item)
                    
                    return(ok,item)

        if type == 'nmap_presets':
            itemsfromfile = self.Hp.ReadListFromFile('resource/'+type+'.lst')
            result = QInputDialog.getItem(self, "select input dialog","choose dork", itemsfromfile, 0, False)
            if not (result is None):
                print(result)          
                item,ok = result
                print(ok,item)
                
                if ok == True and item is not None:
                    print(ok,item)
                    
                    return(ok,item)

        if type == 'nmap_ports':
            itemsfromfile = self.Hp.ReadListFromFile('resource/'+type+'.lst')
            result = QInputDialog.getItem(self, "select input dialog","choose ports", itemsfromfile, 0, False)
            if not (result is None):
                print(result)          
                item,ok = result
                print(ok,item)
                
                if ok == True and item is not None:
                    print(ok,item)
                    
                    return(ok,item)

        if type == 'console_history':
            itemsfromfile = self.Hp.ReadListFromFile('resource/'+type+'.ipy')
            result = QInputDialog.getItem(self, "select input dialog", "choose dork", itemsfromfile, 0, False)
            if not (result is None):
                print(result)          
                item,ok = result
                print(ok,item)
                
                if ok == True and item is not None:
                    print(ok,item)
                    
                    return(ok,item)
    # get text input dialogs

    def getText(self,type):
        if type == 'nmap_ip':
            result = QInputDialog.getText(self, 'Text Input Dialog', 'Enter the '+type+':')
            if not (result is None):
                print(result)          
                text,ok = result
                print(ok,text)
                
                if ok == True and text is not None:
                    print(ok,text)
                    
                    return(ok,text)
        if type == 'nmap_ports':
            result = QInputDialog.getText(self, 'Text Input Dialog', 'Enter the '+type+':')
            if not (result is None):
                print(result)          
                text,ok = result
                print(ok,text)
                
                if ok == True and text is not None:
                    print(ok,text)
                    
                    return(ok,text)
# helpers
    def console(self):
        #setup console    
        cmds = self.console_commands    
        self.console_widget = IPythonWidget()
        for cmd in self.console_commands:
            print(cmd)
            self.console_widget.execute(cmd)
            self.console_widget.setStyleSheet(self.RoundBorders)
        return self.console_widget

    def console_exec(self):
        cmds = self.console_commands        
        console = IPythonWidget()
        console.gui_completion='droplist'
        for cmd,args in cmds:
            final = '!'+cmd+' '+args+'\r'
            print(final,'command  send...')
            console.execute(final)

    def switch_demo(self,argument):
        switcher = {
            'top'  : "Qt.TopDockWidgetArea",
            'bottom'   : "Qt.BottomDockWidgetArea",
            'left'   : "Qt.LeftDockWidgetArea",
            'right'   : "Qt.RightDockWidgetArea"
        }
        return(switcher.get(argument, "Invalid Dock position"))

    def LogEntry(self,entry):
        print('Log entry')
        print(entry)
        ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')
        self.listWidget.addItem(ansi_escape.sub('', str(entry)))
# Scannners
    def NmRandomScan(self):
        self.LogEntry('Wait please Random Nmap Scan is running......')
        nmaphosts='-iR '+str(self.NmapRandomCount)
        nmapargs='-Pn -n -p '+str(self.ports) 
        self.console_commands = ["import modules.Helper as Helper\r",
                                "from IPython.utils import io\r",
                                "import nmap,os,sys,re,subprocess\r",
                                "Nm = nmap.PortScanner()\r",
                                'Nm.scan(hosts=" '+nmaphosts+' ", arguments=" '+nmapargs+'")\r',
                                "hosts_list = [(x, Nm[x]['status']['state']) for x in Nm.all_hosts()]\r",
                                "ip_list = [(hosts_list[x][0]) for x in range(len(hosts_list))]",
                                "filename = 'resource/outfile.lst'\r",
                                "with open(filename, 'a') as outfile:\r",
                                "\tfor entries in ip_list:\r",
                                "\t\toutfile.write(entries)",
                                "\t\toutfile.write(',')\r",
                                "%save -r -a resource/console_history 0-500\r"] # backup of the ipy screen
        self.LogEntry('Nmap has finished!')
        # self.removeDockWidget(self.fdock)
        #self.removeDockWidget(self.qdock)       
        self.setupDock(self.console(),'right')

    def NmCustomScan(self,ip,args):
        self.nm = nmap.PortScanner()
        self.nm.scan(hosts=ip,arguments=args)
        self.LogEntry(self.nm.command_line())
        # hosts_list1 = [(x, self.nm[x]['tcp']) for x in self.nm.all_hosts()]
        hosts_list2 = [(x, self.nm[x]['tcp'][80]) for x in self.nm.all_hosts()]
        print(hosts_list2)
        hosts_list = [(x, self.nm[x]['status']['state']) for x in self.nm.all_hosts()]
        for host, status in hosts_list:
            self.LogEntry('{0}:{1}'.format(host, status))
            for name,state in hosts_list2:
                print(name,state)

    def NmLocalScan(self):
        self.nm = nmap.PortScanner()
        self.nm.scan(hosts='192.168.178.0/24', arguments='-p 22-443')
        self.LogEntry(self.nm.command_line())
        hosts_list = [(x, self.nm[x]['status']['state']) for x in self.nm.all_hosts()]
        for host, status in hosts_list: 
            self.LogEntry('{0}:{1}'.format(host, status))

    def PhpInurlbr(self,dork):
        self.LogEntry('Wait please InurlBr is running......')
        SearchEnginesCsv = str('1,2,3,4,5,6')
        print(dork)
        print(SearchEnginesCsv)
        out_file = 'resources/Inurl_Loot.txt'
        print(out_file)
        self.console_commands = ["import modules.Helper as Helper\r",
                                "from modules.Helper import Tools\r"
                                "from IPython.utils import * \r",
                                "import nmap,os,sys,re,subprocess\r",
                                "!php /usr/bin/inurlbr.php --dork "+str(dork)+" --exploit-get \"\'0x27%27\'\" -q "+str(SearchEnginesCsv)+" --mp "+str(self.InurlPageCount)+" -s "+str(out_file)+" --tor-random\r",
                                "%save -r -a /root/stuff/Qt5/Scanner/resource/console_history 0-500\r",
                                "!cat resource/"+out_file+".ipy\r"]
        for i in self.Hp.ReadListFromFile('output/PhpInurl.txt'):
            self.LogEntry(i)
        self.LogEntry('Inurlbr has finished!')
        #self.removeDockWidget(self.qdock)       
        self.setupDock(self.console(),'right')
        # result = subprocess.Popen("php /usr/bin/inurlbr.php --dork "+dork+" --exploit-get "'0x27%27'" -q 1,2,3 --mp 2 -s PhpInurl.txt --tor-random &",
        #                    shell=True,
        #                    stdout=subprocess.PIPE,
        #                    universal_newlines=True).communicate()[0]
        # r = [line for line in result.split('\n') if line.strip() != '']
        # for i in r:
        #     self.LogEntry(i)
# test /debug
    def test(self):
        
        self.nm = nmap.PortScanner()
        # self.nm.scan(hosts='192.168.178.0/24', arguments='-p 22-443')
        # # a more usefull example :
        # for host in self.nm.all_hosts():
        #     print((host, self.nm[host]))
        #     self.LogEntry('----------------------------------------------------')
        #     self.LogEntry('Host : %s (%s)' % (host, self.nm[host]['addresses']['ipv4']))
        #     self.LogEntry('Ports : %s' % self.nm[host]['tcp'].keys())

    def progressBar(self,cmd):
        
        self.progress = QProgressDialog(QWidget,"Please Wait!", "Cancel", 0, 100)
        self.progress.setWindowModality(QtCore.Qt.WindowModal)
        self.progress.setAutoReset(True)
        self.progress.setAutoClose(True)
        self.progress.setMinimum(0)
        self.progress.setMaximum(100)
        self.progress.resize(500,100)
        self.progress.setWindowTitle("Loading, Please Wait! (Cloudflare Protection)")
        self.progress.show()
        self.progress.setValue(0)
        #content = cmd
        #print content
        #content = ccurl(cmd,"")
        content = subprocess.check_output(cmd)
        
        self.progress.setValue(100)
        self.progress.hide()
        #print content
        return content

    def AsyncScan(self,ports):

        self.asynclog = []
        self.ports = ports
        self.network = '-iR '+str(self.NmapRandomCount)
        self.arguments = ' -Pn -n -sV -p '+self.ports
        self.nma = nmap.PortScannerAsync()
        self.nma.scan(hosts=self.network, arguments=self.arguments, callback=self.async_callback_result)
        while self.nma.still_scanning():
            print("Waiting >>>")
            print(self.asynclog)
            self.nma.wait(2) 

    def async_callback_result(self,host, scan_result):
        print('------------------')
        print(scan_result['nmap']['command_line'])
        print(scan_result['scan'][host]['addresses']['ipv4'])
        # print(host, scan_result)
        print('------------------')
        self.HasPort(host, scan_result)

    def HasPort(self,host, scan_result):
        for port in self.ports.split(','):
            if(scan_result['scan'][host].has_tcp(int(port))):
                    if(scan_result['scan'][host]['tcp'][int(port)]['state'] == 'open'):
                        print(scan_result['scan'][host]['tcp'][int(port)])
                        print(str(scan_result['scan'][host]['addresses']['ipv4'])+str(port)+str(scan_result['scan'][host]['tcp'][int(port)]['state']))
                    else:
                        print(port + " not open but "+scan_result['scan'][host]['tcp'][int(port)]['state'])
#Function Main Start
if __name__ == '__main__':
    app= QtWidgets.QApplication(sys.argv)
    windows = MyWindow()
    windows.show()
    sys.exit(app.exec_())