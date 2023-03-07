from PyQt5 import QtCore, QtGui, QtWidgets
from latency_injecton import *

class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(662, 463)

		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")

		self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
		self.textEdit.setGeometry(QtCore.QRect(0, 0, 211, 411))
		self.textEdit.setObjectName("textEdit")

		self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
		self.scrollArea.setGeometry(QtCore.QRect(220, 0, 441, 281))
		self.scrollArea.setWidgetResizable(True)
		self.scrollArea.setObjectName("scrollArea")

		self.scrollAreaWidgetContents = QtWidgets.QWidget()
		self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 439, 279))
		self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

		self.saveButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
		self.saveButton.setGeometry(QtCore.QRect(300, 230, 93, 28))
		self.saveButton.setObjectName("saveButton")
		self.saveButton.clicked.connect(self.save)

		self.delayLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
		self.delayLabel.setGeometry(QtCore.QRect(30, 40, 111, 16))
		self.delayLabel.setObjectName("delayLabel")


		self.delayValue = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
		self.delayValue.setGeometry(QtCore.QRect(180, 40, 151, 22))
		self.delayValue.setObjectName("delayValue")
		self.delayValue.valueChanged.connect(self.limitValues)
 
		self.stopButton = QtWidgets.QPushButton("Toggle",self.scrollAreaWidgetContents)
		self.stopButton.setGeometry(QtCore.QRect(30, 230, 93, 28))
		self.stopButton.setObjectName("stopButton")
		self.stopButton.clicked.connect(self.statusToggle)

		self.disable_toggle = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
		self.disable_toggle.setGeometry(QtCore.QRect(30, 80, 101, 20))
		self.disable_toggle.setObjectName("disable_toggle")


		self.expiredLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
		self.expiredLabel.setGeometry(QtCore.QRect(30, 140, 111, 16))
		self.expiredLabel.setObjectName("expiredLabel")

		self.expiredTime = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
		self.expiredTime.setGeometry(QtCore.QRect(180, 130, 161, 21))
		self.expiredTime.setObjectName("expiredTime")
		self.expiredTime.setReadOnly(True)

		self.settingsLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
		self.settingsLabel.setGeometry(QtCore.QRect(10, 0, 121, 16))
		self.settingsLabel.setObjectName("settingsLabel")

		self.scrollArea.setWidget(self.scrollAreaWidgetContents)

		self.scrollArea_2 = QtWidgets.QScrollArea(self.centralwidget)
		self.scrollArea_2.setGeometry(QtCore.QRect(220, 280, 441, 131))
		self.scrollArea_2.setWidgetResizable(True)
		self.scrollArea_2.setObjectName("scrollArea_2")

		self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
		self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 439, 129))
		self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")

		self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
		self.label_4.setGeometry(QtCore.QRect(10, 10, 121, 16))
		self.label_4.setObjectName("label_4")

		self.checkBox_2 = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
		self.checkBox_2.setGeometry(QtCore.QRect(20, 50, 161, 20))
		self.checkBox_2.setObjectName("checkBox_2")

		self.pushButton_3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
		self.pushButton_3.setGeometry(QtCore.QRect(30, 80, 93, 28))
		self.pushButton_3.setObjectName("pushButton_3")

		self.pushButton_4 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
		self.pushButton_4.setGeometry(QtCore.QRect(262, 80, 121, 28))
		self.pushButton_4.setObjectName("pushButton_4")

		self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
		self.textEdit.raise_()
		self.scrollArea_2.raise_()
		self.scrollArea.raise_()

		MainWindow.setCentralWidget(self.centralwidget)

		self.menubar = QtWidgets.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 662, 26))
		self.menubar.setObjectName("menubar")
		MainWindow.setMenuBar(self.menubar)

		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
	
		MainWindow.setStatusBar(self.statusbar)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)


	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
		self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
										"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
										"p, li { white-space: pre-wrap; }\n"
										"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
										"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
		self.saveButton.setText(_translate("MainWindow", "Save"))
		self.delayLabel.setText(_translate("MainWindow", "Delay in (seconds) "))
		self.expiredLabel.setText(_translate("MainWindow", "Disable after day"))
		self.stopButton.setText(_translate("MainWindow", "Start"))
		self.disable_toggle.setText(_translate("MainWindow", "Auto Disable"))
		# self.expiredTime.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
		# 								"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
		# 								"p, li { white-space: pre-wrap; }\n"
		# 								"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
		# 								"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
		# 								"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
		self.settingsLabel.setText(_translate("MainWindow", "Network Setting"))
		self.label_4.setText(_translate("MainWindow", "Application Setting"))
		self.checkBox_2.setText(_translate("MainWindow", "Auto start with window"))
		self.pushButton_3.setText(_translate("MainWindow", "Add licenses"))
		self.pushButton_4.setText(_translate("MainWindow", "Change Password"))
	
	def statusToggle(self):
		pass
		
	def limitValues(self):
		if self.delayValue.value() > 30 :
			self.delayValue.setValue(30) 
		
	def save(self):
		delay_value = self.delayValue.value()
		print(f"Delay value 	:{delay_value}")
		print(f"Remain time     :{self.expiredTime.text()}")
		import pickle
		with open('settings.dat', 'rb') as f:
			data = pickle.load(f)

		# Modify the data as required
		data['delay'] = delay_value

		# Save the updated data back to the file
		with open('settings.dat', 'wb') as f:
			pickle.dump(data, f)
		



def read_settings():
	import pickle
	with open("settings.dat", "rb") as f:
		data = f.read()

	# Deserialize the binary data into a Python object
	settings = pickle.loads(data)

	# Access the settings values
	return [settings["expired"],settings["delay"]]


def run_scripts(running,delay,pid):
	if running:
		if pid :
			mt5_instance = get_app_ip_and_port(pid)
			filter_expression = (f'inbound and tcp.DstPort == {mt5_instance[1]} and ip.DstAddr == {mt5_instance[0]} ')
			try:
				while running : 
					  # delay in milliseconds
					print(f"Pid {pid} ,Delay {delay}s",end="\r",flush=True)
					latency_injection(filter_expression,delay)
			except Exception as e:
				logging.error(f"Unexpected error: {e}")


if __name__ == "__main__":
	import sys
	from datetime import datetime

	

	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)

	settings = read_settings()
	expired_date = settings[0]
	setting_delay = settings[1]
	today = datetime.now()
	delta = expired_date - today
	if delta.total_seconds() >= 0:
		ui.expiredTime.setText("{}".format(delta.days))
	ui.delayValue.setValue(setting_delay)
	MainWindow.show()
	timer = QtCore.QTimer()
	running = False 
	pid = 0
	def run():
		global running
		if running:
			delay = ui.delayValue.value()
			ui.statusbar.showMessage('Running...')
			run_scripts(running ,delay,pid)	
			
		if not app.hasPendingEvents():
			app.processEvents()


	def toggle_running():
		global running
		running = not running
		if running:
			ui.stopButton.setText('Stop')
			timer.timeout.connect(run)
			timer.start(10)
		else:
			ui.stopButton.setText('Start')
			ui.statusbar.showMessage('Stopped')
			timer.stop()

	try :
		pid = get_pid()
		ui.stopButton.clicked.connect(toggle_running)
	except:
		pid = None
		ui.statusbar.showMessage('Please open MT5')	
	

	sys.exit(app.exec_())	

	
