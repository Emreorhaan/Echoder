from PyQt5.QtWidgets import *
from PyQt5 import QtCore
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
		self.setFixedSize(700,800)
		
		self.VLay1 = QVBoxLayout()
		self.HLay1 = QHBoxLayout()
		self.HLay2 = QHBoxLayout()
		
		self.textbox1 = QPlainTextEdit()
		self.textbox1.setFixedSize(675, 200)
		
		self.keytxt1 = QLineEdit()
		self.keytxt2 = QLineEdit()
		self.fileName = QLineEdit()
		self.fileName.setText(("File Name: "))
		self.keytxt1.setText("key 1:  ")
		self.keytxt2.setText("key 2: ")
		
		self.keytxt1.setFixedSize(250,40)
		self.keytxt2.setFixedSize(250,40)
		self.fileName.setFixedSize(675,40)
		
		self.translate = QPushButton(text = "Translate")
		self.copy = QPushButton(text = "Copy Text")
		self.save = QPushButton(text = "Save Text")
		self.change = QPushButton(text = "Encryption")
		self.opnfile = QPushButton(text = "Open File")
		
		self.translate.clicked.connect(self.encryption)
		self.change.clicked.connect(self.changef)
		self.copy.clicked.connect(self.copyf)
		self.save.clicked.connect(self.savef)
		self.opnfile.clicked.connect(self.openfile)
		
		self.translate.setFixedSize(675,50)
		self.change.setFixedSize(675,50)
		self.copy.setFixedSize(300,50)
		self.save.setFixedSize(300,50)
		self.opnfile.setFixedSize(150, 40)
		
		self.head= QLabel("ECHODER")
		self.head.setAlignment(QtCore.Qt.AlignCenter)
		self.head.setObjectName("head")

		self.txt1 = QLabel("Text")
		self.txt1.setAlignment(QtCore.Qt.AlignCenter)
		self.txt1.setObjectName("txt1")
		
		self.txt2 = QLabel("Encryption Text")
		self.txt2.setAlignment(QtCore.Qt.AlignCenter)
		self.txt2.setObjectName("txt2")
		
		self.textbox2 = QPlainTextEdit()
	
		self.HLay1.addWidget(self.opnfile)
		self.HLay1.addWidget(self.keytxt1)
		self.HLay1.addWidget(self.keytxt2)
		
		self.HLay2.addWidget(self.copy)
		self.HLay2.addWidget(self.save)
		
		self.VLay1.addWidget(self.head)
		self.VLay1.addWidget(self.txt1)
		self.VLay1.addWidget(self.textbox1)
		self.VLay1.addLayout(self.HLay1)
		self.VLay1.addWidget(self.translate)
		self.VLay1.addWidget(self.change)
		self.VLay1.addWidget(self.txt2)
		self.VLay1.addWidget(self.textbox2)
		self.VLay1.addWidget(self.fileName)
		self.VLay1.addLayout(self.HLay2)
		
		self.setLayout(self.VLay1)
		
		self.show()
		
	def encryption(self):
		
		if self.mod == 1:
			self.text = self.textbox1.toPlainText()
			self.key1 = self.keytxt1.text()
			self.key2 = self.keytxt2.text()
			self.key1 = self.key1.replace("key 1: ","")
			self.key2 = self.key2.replace("key 2: ","")
			
			try:
				self.key1 = int(self.key1)
				self.key2 = int(self.key2)
				
			except:
				pass
				
			self.text = echode.encryp(self.text,self.key1,self.key2)
				
			self.textbox2.setPlainText(self.text)
	
		else:
			self.decryption()
		
	def decryption(self):
		self.text = self.textbox1.toPlainText()
		self.key1 = self.keytxt1.text()
		self.key2 = self.keytxt2.text()
		self.key1 = self.key1.replace("key 1: ","")
		self.key2 = self.key2.replace("key 2: ","")
			
		try:
			self.key1 = int(self.key1)
			self.key2 = int(self.key2)
				
		except:
			pass
				
		self.text = echode.decryp(self.text,self.key1,self.key2)
			
		self.textbox2.setPlainText(self.text)
		
	def changef(self):
		if self.mod == 1:
			self.mod = 0
			
			self.txt1.setText("Encryption Text")
			self.txt2.setText("Decryption Text")
			self.change.setText("Decryption")
			
		else:
			self.mod = 1
			
			self.txt1.setText("Text")
			self.txt2.setText("Encryption Text")
			self.change.setText("Encryption")
		
	def copyf(self):
		clipboard.copy(self.text)
		
	def savef(self):
		self.fileurl = QFileDialog.getExistingDirectory(os.getenv("Desktop"))
		self.fileNameText = self.fileName.text().replace("File Name: ", "")
		
		if self.fileNameText == "":
			self.fileNameText = "cryption text.txt"

		self.file = open(self.fileurl + "//"+self.fileNameText+".txt","w")
		self.file.write(self.text)
		self.file.close()

	def openfile(self):
		self.fileurl = QFileDialog.getOpenFileName(os.getenv("Desktop"))
		self.filetext = ""

		for line in open(self.fileurl[0], 'r'):
			self.filetext += line

		self.textbox1.setPlainText(self.filetext)

		
if __name__ == '__main__':
	app = QApplication(sys.argv)
	style = """
	QLabel#head
	{
	background: #FFFFFF;
	font-size: 15pt;
	color: #000000;
	border-radius: 15px;
	border: 2px solid black;
	}
	
	QLabel#txt1,#txt2
	{
	font-size: 15pt;
	color: #FFFFFF;
	}
	
	QLabel
	{
	color: #FFFFFF;
	font-size: 18pt;
	}
	
	QLabel#cryption
	{
	background: #FFFFFF;
	color: #000000;
	border-radius: 10px;
	font-size: 20px;
	border: 2px solid black;
	}
	
	QWidget
	{
	background: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 #8300FF, stop:1 #850066);
	}
	
	QPlainTextEdit
	{
	background: #FFFFFF;
	color: #000000;
	border-radius: 15px;
	font-size: 20px;
	border: 2px solid black;
	}
	
	QLineEdit
	{
	background: #FFFFFF;
	color: #000000;
	font-size: 15px;
	border-radius: 15px;
	border: 2px solid black;
	}
	
	QPushButton
	{
	background: #FFFFFF;
	color: #000000;
	border-radius: 15px;
	border: 2px solid black;
	}

	QPushButton::hover
	{
	background: #B117A0;
	color: #000000;
	border-radius: 15px;
	border: 2px solid black;	
	}

	"""
	app.setStyleSheet(style)
	app2 = Main()
	sys.exit(app.exec_())
	
	



