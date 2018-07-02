from qtconsole.rich_ipython_widget import RichJupyterWidget
from qtconsole.inprocess import QtInProcessKernelManager
from PyQt5 import QtCore , QtGui, QtWidgets, uic
from PyQt5.QtCore import (QByteArray, QDate, QDateTime, QEvent, QPoint, QRect,
        QRegExp, QSettings, QSize, Qt, QTime, QTimer)
from PyQt5.QtGui import QColor,QFont, QIcon, QRegExpValidator, QValidator
from PyQt5.QtWidgets import (QAbstractItemView, QAction, QApplication,
        QComboBox, QDialog, QDialogButtonBox, QFileDialog, QGridLayout,QWidget,
        QGroupBox, QHeaderView, QInputDialog, QItemDelegate, QLabel, QLineEdit,QProgressDialog,
        QMainWindow, QMessageBox, QStyle, QStyleOptionViewItem, QListWidget, QTableWidget,
        QTableWidgetItem, QTreeWidget, QTreeWidgetItem, QVBoxLayout,QFormLayout,QPushButton,QSlider,QDockWidget)
import subprocess
# from qtconsole import QtInProcessKernelManager
def put_ipy(parent):
    kernel_manager = QtInProcessKernelManager()
    kernel_manager.start_kernel()
    kernel = kernel_manager.kernel
    kernel.gui = 'qt4'

    kernel_client = kernel_manager.client()
    kernel_client.start_channels()
    kernel_client.namespace  = parent

    def stop():
        kernel_client.stop_channels()
        kernel_manager.shutdown_kernel()

    layout = QtWidgets.QVBoxLayout(parent)
    widget = RichJupyterWidget(parent=parent)
    layout.addWidget(widget)
    widget.kernel_manager = kernel_manager
    widget.kernel_client = kernel_client
    widget.exit_requested.connect(stop)
    ipython_widget = widget
    ipython_widget.show()
    kernel.shell.push({'widget':widget,'kernel':kernel, 'parent':parent})

    return {'widget':widget,'kernel':kernel}

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    win = QtWidgets.QWidget(None)
    win.show()
    put_ipy(win)
    sys.exit(app.exec_())
    # app= QtWidgets.QApplication(sys.argv)
    # windows = MyWindow()
    # windows.show()
    # sys.exit(app.exec_())