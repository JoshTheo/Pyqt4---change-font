import sip
sip.setapi('QString', 2)
sip.setapi('QVariant', 2)
from PyQt4 import QtGui, QtCore

class MainWindow(QtGui.QMainWindow):
   MaxRecentFiles = 5
   windowList = []

   def __init__(self):
      super(MainWindow, self).__init__()
      self.recentFilesActs = []
      self.setAttributes(QtCore.Qt.WA_DeleteOnClose)

      self.textEdit = QtGui.QtextEdit()
      self.CentralWidget(self.textEdit)

      self.createStatusBar()
      self.createAction()
      self.createMenus()

      self.setWindowTitle("Text Editor")
      self.show()

   def newFile(self):
      other = MainWindow()
      MainWindow.windowList.append(other)
      other.show()
      
   def open(self):
      fileName = QtGui.QGFileDialog.getOpenFileName(self)
      if fileName:
         self.loadFile(fileName)

   def save(self):
      if self.cureFile:
         self.saveFile(self.curFile)
      else:
         sefl.saveAs
      
   def saveAs(self):
      fileName = QtGui.QFileDialog.getSaveFileName(self)
      if fileName:
         self.saveFile(fileName)

   def openRecentFile(self):
      action  = self.sender()
      if action:
         self.loadFile(action.data())

   def about(self):
      QtGui.MessageBox.about(self, "About recent files", "<b>This app free</b>")
   def createAction(self):
      self.newAct = QtGui.QAction("&New", self, shortcut=QtGui.QKeySequence.New,
                                  toolTip="New file", triggered=self.newFile)
      self.openAct = QtGui.QAction("&Open", self, shortcut=QtGui.QKeySequence.Open,
                                   toolTip="Open an existing file" , triggered = self.open)
      self.saveAct = QtGui.QAction("&Save", self, shortcut=QtGui.QKeySequence,
                                   toolTip="Save the application", triggered=self.save)
      self.saveAsAct = QtGui.QAction("&SaveAs", self, shortcut=QtGui.QKeySequence.SaveAs, toolTip="SaveAs the file",
                                     triggered=self.saveAs)
      for i in range(MainWindow.MaxRecentFiles):
         self.recentFilesActs.append(QtGui.QAction(self, visible=False, triggered=sefl.openRecentFile))
         
      self.exitAct = QtGui.QAction("&About", self, statusTip="Show the application's box",
                                   triggered=self.about)
      self.aboutQtAct=QtGui.QAction("About &Qt", self, statusTip="Show the Qt", triggered=QtGui.qApp.aboutQt)

   def createMenus(self):
      self.fileMenu = self.menuBar().addMenu("&File")
      self.fileMenu.addAction(self.newAct)
      self.fileMenu.addAction(self.openAct)
      self.fileMenu.addAction(self.saveAct)
      self.fileMenu.addAction(self.saveAsAct)
      self.separatorAct = self.fileMenu.addSeparator()
      for i in range(MainWindow.MaxRecentFiles):
         self.fileMenu.addAction(self.recentFilesAct[i])
      self.fileMenu.addSeparator()
      self.fileMenu.addAction(self.exitAct)
      self.updateRecentFileActions()

      self.menuBar().addSeparator()

      self.help = self.menuBar().addMenu("&Help")
      self.help.addAction(self.aboutAct)
      self.help.addAction(self.aboutQtAct)
   def loadFile(self, fileName):
      file = QtCore.QFile(fileName)
      if not file.open(QtCore.QFile.ReadOnly | QtCore.QFile.Text):
         QtGui.QMessageBox.warning(self, "Recent Files", "Cannot read file %s:\n%s." %(fileName, file.errorString())
         return
      instr = QtCore.QTextStream(file)
      QtGui.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
      self.textEdit.setPlaintText(instr.readAll())
      QtGui.QApplication.restoreOverrideCursor()

      self.setCurrentFile(fileName)
      self.statusBar().showMessage("File loaded", 1000)
   def saveFile(self, fileName):
      file = QtCore.QFile(fileName):
      if not file.open(QtCore.QFile.ReadOnly | QtCore.QFile.Text):
         QtGui.QMessageBox.warning(self, "Recent File", "Cannot read file%s:\n%s" %(file.errorString())
         return
      outstr = QtCore.QTextStream(file)
      QtGui.QApplications.setOverrideCursor(QtCore.Qt.WaitCursor)
      outstr << self.textEdit.toPlainText()
      QtGui.QApplication.restoreOverrideCursor()

   def setCurrentFile(self, fileName):
      self.curFile = fileName
      if self.curFile:
         self.setWindowTitle("%s - Recent Files", % self.strippedName(self.curFile)
      else:
            self.setWindowTitle("Recent Files")

      try:
            files.remove(fileName)
      except ValueError:
         pass
      files.insert(0, fileName)

      del files[MainWindow.MaxRecentFiles:]
      settings.setValue('recentFileList', files)
      for widget in QtGui.QApplication.topLevelWidgets():
         if isinstance(widget, MainWindow):
            widget.updateRecentFileActions()
   def updateRecentFileActions(self):
            

if __name__ =='__main__':
   import sys

   app = QtGui.QApplication(sys.argv)
   main = MainWindow()
   main.show()
   sys.exit(app.exec_())
                                    
