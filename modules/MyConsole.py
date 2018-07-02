import sip
sip.setapi(u'QDate', 2)
sip.setapi(u'QDateTime', 2)
sip.setapi(u'QString', 2)
sip.setapi(u'QTextStream', 2)
sip.setapi(u'QTime', 2)
sip.setapi(u'QUrl', 2)
sip.setapi(u'QVariant', 2)
# from PyQt4.QtGui import *
from qtconsole.rich_jupyter_widget import RichJupyterWidget
from qtconsole.inprocess import QtInProcessKernelManager
from IPython.lib import guisupport

class IPythonWidget(RichJupyterWidget):
    def __init__(self, parent=None, **kwargs):
        super(self.__class__, self).__init__(parent)
        self.app = app = guisupport.get_app_qt4()
        self.kernel_manager = kernel_manager = QtInProcessKernelManager()
        kernel_manager.start_kernel()

        self.kernel = kernel = kernel_manager.kernel
        kernel.gui = 'qt4'
        self.kernel_client = kernel_client = kernel_manager.client()
        kernel_client.start_channels()

if __name__ == '__main__':
    app = QApplication([])
    i = IPythonWidget()
    i.show()
    i.execute('print("Hello World.")\r')
    app.exec_()


#     def Main_Init(self):
#         if (len(sys.argv) == 2):
#             print ("Thanks for passing ", sys.argv[1])

#             app = QApplication([])
#             i = self.run_kernel()
#             i.show()
#             # for command,args in sys.argv[1]:
#             #     i.execute(command,args)

#             # i.execute('import nmap\r')
#             i.execute('arg1 = "hallo"\r')
#             # i.execute("print(arg1)")
#             # i.execute('nmp=nmap.PortScanner()\r')
#             # i.execute("nmp.scan('192.168.178','80')\r")

#             app.exec_()
#         else:
#             print ("Oops no args.")

# if __name__ == '__main__':
#     app = QApplication([])
#     i = IPythonWidget()
#     i.show()
#     # for command,args in sys.argv[1]:
#     #     i.execute(command,args)

#     # i.execute('import nmap\r')
#     i.execute('arg1 = "hallo"\r')
#     # i.execute("print(arg1)")
#     # i.execute('nmp=nmap.PortScanner()\r')
#     # i.execute("nmp.scan('192.168.178','80')\r")

#     app.exec_()