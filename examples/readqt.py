import sys
import PyQt5
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import (QApplication, QCheckBox, QGridLayout, QGroupBox,
                             QMenu, QPushButton, QRadioButton, QVBoxLayout, QWidget, QSlider)

class DataCaptureThread(QThread):
    def collectProcessData():
        print ("Collecting Process Data")

    def __init__(self):
        QThread.__init__(self)
        #declaring the timer
        self.dataCollectionTimer = PyQt5.QtCore.QTimer()
        self.dataCollectionTimer.timeout.connect(self.collectProcessData)
    def run(self):
        self.dataCollectionTimer.start(1000);
        loop = QEventLoop()
        loop.exec_()
        
class Window(QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.datacap = DataCaptureThread()
        self.datacap.run()
        
        

        
        grid = QGridLayout()
        grid.addWidget(self.createExampleGroup(), 0, 0)
        grid.addWidget(self.createExampleGroup(), 1, 0)
        grid.addWidget(self.createExampleGroup(), 0, 1)
        grid.addWidget(self.createExampleGroup(), 1, 1)
        self.setLayout(grid)

        self.setWindowTitle("PyQt5 Sliders")
        self.resize(400, 300)

    def startThread(self):
        self.datacap.start()

    def stopThread(self):
        self.datacap.terminate()
        
    def createExampleGroup(self):
        groupBox = QGroupBox("Slider Example")

        radio1 = QRadioButton("&Radio horizontal slider")

        slider = QSlider(Qt.Horizontal)
        slider.setFocusPolicy(Qt.StrongFocus)
        slider.setTickPosition(QSlider.TicksBothSides)
        slider.setTickInterval(10)
        slider.setSingleStep(1)

        radio1.setChecked(True)

        vbox = QVBoxLayout()
        vbox.addWidget(radio1)
        vbox.addWidget(slider)
        vbox.addStretch(1)
        groupBox.setLayout(vbox)

        return groupBox

if __name__ == '__main__':
    app = QApplication(sys.argv)
    clock = Window()
    #clock.startThread()
    clock.show()
    #clock.stopThread()
    sys.exit(app.exec_())
