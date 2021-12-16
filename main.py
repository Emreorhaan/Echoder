from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5 import QtGui
from echode import *
import clipboard
import sys
import os

class Main(QWidget):
	
	def __init__(self):
		super().__init__()
		self.mod = 1
		self.text = ""
		
		self.setWindowTitle("ECHODER")
		self.setGeometry(250,50,700,900)
		self.setFixedSize(700,900)

		self.modeText = QLabel(text = "Mode: ")
		self.inputLabel = QLabel(text = "Input Text: ")
		self.outputLabel = QLabel(text = "Translated Text: ")
		
		self.modeText.setFixedHeight(35)
		self.inputLabel.setFixedHeight(25)
		self.outputLabel.setFixedHeight(25)
		
		self.inputLabel.setObjectName("L1")
		self.outputLabel.setObjectName("L2")

		self.mode1 = QPushButton(text = "Encryp")
		self.mode2 = QPushButton(text = "Decryp")
		self.translate = QPushButton(text = "Translate")
		self.openButton = QPushButton()
		self.copyButton = QPushButton()
		self.saveButton = QPushButton()

		self.mode1.clicked.connect(self.enmode)
		self.mode2.clicked.connect(self.demode)
		self.translate.clicked.connect(self.encryption)
		self.openButton.clicked.connect(self.openfile)
		self.saveButton.clicked.connect(self.savef)
		self.copyButton.clicked.connect(self.copyf)


		self.mode1.setFixedSize(192, 62)
		self.mode2.setFixedSize(192, 62)
		self.translate.setFixedHeight(62)
		self.openButton.setFixedSize(62, 62)
		self.saveButton.setFixedSize(40, 40)

		self.openButton.setIcon(QtGui.QIcon("folder_black_24dp.svg"))
		self.copyButton.setIcon(QtGui.QIcon("content_copy_black_24dp.svg"))
		self.saveButton.setIcon(QtGui.QIcon("save_black_24dp.svg"))

		self.textData = QPlainTextEdit()
		self.cryptionData = QPlainTextEdit()

		self.textData.setFixedSize(665, 272)
		self.cryptionData.setFixedSize(665, 272)

		self.key1 = QLineEdit(text = "Key 1:")
		self.key2 = QLineEdit(text = "Key 2:")
		self.fileName = QLineEdit(text = "File Name:")

		self.key1.setFixedSize(192, 62)
		self.key2.setFixedSize(192, 62)
		self.fileName.setFixedHeight(40)

		self.VLay1 = QVBoxLayout()
		self.HLay1 = QHBoxLayout()
		self.HLay2 = QHBoxLayout()
		self.HLay3 = QHBoxLayout()

		self.HLay1.addWidget(self.mode1)
		self.HLay1.addWidget(self.mode2)
		self.HLay1.addStretch()
		self.HLay1.addWidget(self.openButton)

		self.HLay2.addWidget(self.key1)
		self.HLay2.addWidget(self.key2)
		self.HLay2.addWidget(self.translate)

		self.HLay3.addWidget(self.fileName)
		self.HLay3.addWidget(self.saveButton)
		
		self.VLay1.addWidget(self.modeText)
		self.VLay1.addLayout(self.HLay1)
		self.VLay1.addWidget(self.inputLabel)
		self.VLay1.addWidget(self.textData)
		self.VLay1.addLayout(self.HLay2)
		self.VLay1.addWidget(self.outputLabel)
		self.VLay1.addWidget(self.cryptionData)
		self.VLay1.addWidget(self.copyButton)
		self.VLay1.addLayout(self.HLay3)
		
		self.setLayout(self.VLay1)
		
		self.show()
		
	def encryption(self):
		
		if self.mod == 1:
			self.text = self.textData.toPlainText()
			self.key1t = self.key1.text()
			self.key2t = self.key2.text()
			self.key1t = self.key1t.replace("Key 1:","")
			self.key2t = self.key2t.replace("Key 2:","")
			
			try:
				self.key1t = int(self.key1t)
				self.key2t = int(self.key2t)
				
			except:
				pass

			self.text = echode.encryp(self.text,self.key1t,self.key2t)
			self.cryptionData.setPlainText(self.text)
	
		else:
			self.decryption()
		
	def decryption(self):
		self.text = self.textData.toPlainText()
		self.key1t = self.key1.text()
		self.key2t = self.key2.text()
		self.key1t = self.key1t.replace("Key 1:","")
		self.key2t = self.key2t.replace("Key 2:","")
			
		try:
			self.key1t = int(self.key1t)
			self.key2t = int(self.key2t)
				
		except:
			pass
				
		self.text = echode.decryp(self.text,self.key1t,self.key2t)
			
		self.cryptionData.setPlainText(self.text)
		
	def enmode(self):
		self.mod = 1
	
	def demode(self):
		self.mod = 0
		
	def copyf(self):
		clipboard.copy(self.cryptionData.toPlainText())
		
	def savef(self):
		self.fileurl = QFileDialog.getExistingDirectory(os.getenv("Desktop"))
		self.fileNameText = self.fileName.text().replace("File Name: ", "")
		
		if self.fileNameText == "":
			self.fileNameText = "cryption text.txt"

		self.file = open(self.fileurl + "//"+self.fileNameText+".txt","w")
		self.file.write(self.cryptionData.toPlainText())
		self.file.close()

	def openfile(self):
		self.fileurl = QFileDialog.getOpenFileName(os.getenv("Desktop"))
		self.filetext = ""

		for line in open(self.fileurl[0], 'r'):
			self.filetext += line

		self.textData.setPlainText(self.filetext)

		
if __name__ == '__main__':
	app = QApplication(sys.argv)
	style = """

	QLabel
	{
	color: rgba(255,255,255,255);
	font: 20pt 'Segoe UI';
	font-weight:700;
	}

	QLabel#L1,#L2
	{
	color: rgba(255,255,255,255);
	font: 10pt 'Segoe UI';
	font-weight:700;
	}
	
	QWidget
	{
	background: qlineargradient( x0:1 y0:1, x1:1 y2:1, stop:0 #BAC8E0 , stop:1 #6A85B6 );
	}
	
	QPlainTextEdit
	{
	background: rgba(255,255,255,60);
	color: #FFFFFF;
	border-radius: 15px;
	font: 10pt 'Segoe UI';
	font-weight:700;
	}
	
	QLineEdit
	{
	background: rgba(255,255,255,60);
	color: #FFFFFF;
	border-radius: 15px;
	font: 10pt 'Segoe UI';
	font-weight:700;
	}
	
	QPushButton
	{
	background: rgba(255,255,255,60);
	color: rgba(255,255,255,255);
	border-radius: 15px;
	icon-size: 30px;
	font: 17pt 'Segoe UI';
	font-weight:700;
	}


	QPushButton::hover
	{
		background: rgba(255,255,255,80);
	}
	"""
	app.setStyleSheet(style)
	app2 = Main()
	sys.exit(app.exec_())
	