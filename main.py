import sys
from PyQt4 import QtCore, QtGui, uic

qtCreatorFile = "app.ui"  # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)




class MyApp(QtGui.QMainWindow, Ui_MainWindow):
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		Ui_MainWindow.__init__(self)
		self.setupUi(self)
		self.button.clicked.connect(self.do_stuff)


	## All Logic Here

	def do_stuff(self):

		# Input Sentence
		sentance = self.textEdit.toPlainText()

		# Checking for checked radio buttons
		if self.rb1.isChecked():
			print("rb1")
		elif self.rb2.isChecked():
			print("rb2")
		elif self.rb3.isChecked():
			print("rb3")
		elif self.rb4.isChecked():
			print("rb4")

if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	window = MyApp()
	window.show()
	sys.exit(app.exec_())