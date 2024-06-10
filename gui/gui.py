import sys 
import xml.etree.ElementTree as ET
from PySide6 import QtWidgets, QtGui, QtCore, QtWebEngineWidgets, QtWebEngineCore

url="https://google.de"

def get_location_list():
    tree = ET.parse("./data/karteDeutschland.xml")
    root = tree.getroot()
    locationList = []
    for node in root.iter('node'):
        locationList.append(node.get('id'))
    return locationList


class GUI(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        locationList = get_location_list()
        self.startLocation = QtWidgets.QListWidget(self)
        self.destLocation = QtWidgets.QListWidget(self)
        for location in locationList:
            self.startLocation.addItem(location)
            self.destLocation.addItem(location)
        self.browser = QtWebEngineWidgets.QWebEngineView()
        self.browser.load(QtCore.QUrl(url))
        
        self.startText = QtWidgets.QLabel('Start Location')
        self.destText = QtWidgets.QLabel('Destination')
        self.button = QtWidgets.QPushButton('Calculate')
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.startText)
        self.layout.addWidget(self.startLocation)
        self.layout.addWidget(self.destText)
        self.layout.addWidget(self.destLocation)
        self.layout.addWidget(self.button)
        self.button.clicked.connect(self.buttonClicked)
        self.layout.addWidget(self.browser)
    @QtCore.Slot()
    def buttonClicked(self):
              pass


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    widget = GUI()
    widget.resize(800, 400)
    widget.show()
    sys.exit(app.exec_())
    