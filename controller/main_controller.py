import sys
import PySide2
from PySide2.QtWidgets import QMainWindow, QApplication, QDialog, QWidget
from PySide2.QtCore import Qt
from UI import UI # main ui
from controller import visual_controller
import os
os.environ['QT_MAC_WANTS_LAYER'] = '1'
class MainWindow(QMainWindow,visual_controller.MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = UI.Ui_MainWindow() 
        self.ui.setupUi(self)
        self.setWindowTitle("PROJECT")
        visual_controller.MainWindow.__init__(self, self.ui)
        
    def paintEvent(self, e):
        pass
    def quit(self):
        sys.exit(app.exec_())
    def open_view(self):
        self.interface.destroy()
        self.show()
        
if __name__ == "__main__":
    QApplication.setStyle('Fusion')
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())