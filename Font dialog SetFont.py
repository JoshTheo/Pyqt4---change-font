import sys
from PyQt4 import QtGui

class Main(QtGui.QWidget):
   def __init__(self):
      super(Main, self).__init__()
      self.initUI()
   def initUI(self):
      vbox = QtGui.QVBoxLayout()
      btn = QtGui.QPushButton('Button', self)
      btn.setSizePolicy(QtGui.QSizePolicy.Fixed,
                        QtGui.QSizePolicy.Fixed)
      btn. move(20, 20)
      vbox.addWidget(btn)

      btn.clicked.connect(self.showDialog)
     
      self.label = QtGui.QLabel('Change', self)
      self.abel.move(12, 12)

      vbox.addWidget(self.label)
      self.setLayout(vbox)

      self.resize(500, 600)
      self.setWindowTitle("Font dialog")
      self.show()
   def showDialog(self):
      font, ok = QtGui.QFontDialog.getFont()
      if ok :
         self.label.setFont(font)

if __name__ == '__name__':
   app = QtGui.QApplication(sys.argv)
   main = Main()
   sys.exit(app.exec_())
   
   
