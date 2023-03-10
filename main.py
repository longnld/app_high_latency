from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal
from latency_injecton import *
import pickle
import ipaddress
import logging
logging.basicConfig(filename='app.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s: %(message)s')

	
def read_settings():
	try:
		with open("settings.dat", "rb") as f:
			data = f.read()

		# Deserialize the binary data into a Python object
		settings = pickle.loads(data)

		# Access the settings values
		return [settings["expired"],settings["delay"],settings["running"]]
	except FileNotFoundError:
		raise("File does not exist")
	
def get_remain_days(expired_day):

	from datetime import datetime
	today = datetime.now()
	delta = expired_day - today

	if delta.total_seconds() >= 0:
		return delta.days
	
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
		# self.saveButton.clicked.connect(self.save)

		self.delayLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
		self.delayLabel.setGeometry(QtCore.QRect(30, 40, 111, 16))
		self.delayLabel.setObjectName("delayLabel")


		self.delayValue = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
		self.delayValue.setGeometry(QtCore.QRect(180, 40, 151, 22))
		self.delayValue.setObjectName("delayValue")
		# self.delayValue.valueChanged.connect(self.limitValues)
 
		self.stopButton = QtWidgets.QPushButton("Toggle",self.scrollAreaWidgetContents)
		self.stopButton.setGeometry(QtCore.QRect(30, 230, 93, 28))
		self.stopButton.setObjectName("stopButton")
		# self.stopButton.clicked.connect(self.statusToggle)

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
		self.stopButton.setText(_translate("MainWindow", "Stop"))
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
	
 		
class MainWindow(QtWidgets.QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.settings = read_settings()
		self.running = self.settings[2]
		if self.running:
			self.ui.stopButton.setText("Stop")
		else:
			self.ui.stopButton.setText("Start")
			
		self.ui.delayValue.setValue(self.settings[1])
		self.ui.expiredTime.setText(f"{get_remain_days(self.settings[0])}")

		self.ui.delayValue.valueChanged.connect(self.limitValues)
		self.ui.stopButton.clicked.connect(self.toggle_running)
		self.ui.saveButton.clicked.connect(self.save)

		
	def print_complete(self):
		print("completed")
	
	def limitValues(self):
		if self.ui.delayValue.value() > 30 :
			self.ui.delayValue.setValue(30)

	def toggle_running(self):
		global pid 
		pid = get_pid()
		logging.debug(f"Pid {pid}")
		if pid is None :
			print(f"{time.asctime()} Didnt open MT5...",end="\r",flush=True)
			self.ui.statusbar.showMessage("PLEASE OPEN METATRADER 5")
		else:
			self.running = not self.running
			mt5_instance = get_app_ip_and_port(pid)
			delay = self.ui.delayValue.value()
			filter_expression=""
			if isinstance(ipaddress.ip_address(mt5_instance[0][0]),ipaddress.IPv4Address):
				filter_expression = (f'inbound and tcp.DstPort == {mt5_instance[0][1]} and ip.DstAddr == {mt5_instance[0][0]} ')
			else:
				filter_expression = (f'inbound and tcp.DstPort == {mt5_instance[0][1]} ')
			logging.debug(f"filter expression {filter_expression}")
			
			if self.running:
					self.ui.stopButton.setText("Stop")
					self.ui.statusbar.showMessage("Running...")
					try:
						global t 
						t = threading.Thread(target=capture,args=[filter_expression,delay])
						t.start()
					except Exception as e:
						logging.error(f"Unexpected error: {e}")
	
			else:
		
				self.ui.stopButton.setText("Start")
				self.ui.statusbar.showMessage("Stopped")

	
		
	def save(self):
		
		print(f"Delay value 	:{self.ui.delayValue.value()}")
		print(f"Remain time     :{self.ui.expiredTime.text()}")
		with open('settings.dat', 'rb') as f:
			data = pickle.load(f)
		# Modify the data as required
		data['delay']   = self.ui.delayValue.value()
		data['running'] = self.running
		# Save the updated data back to the file
		with open('settings.dat', 'wb') as f:
			pickle.dump(data, f)

if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	main = MainWindow()
	main.show()
	
	sys.exit(app.exec_())	

	

























# settings = read_settings()
	# expired_date = settings[0]
	# setting_delay = settings[1]
	
	
	# running = False 
	
	# def run():
	# 	global running
	# 	if running:
	# 		delay = ui.delayValue.value()
	# 		ui.statusbar.showMessage('Running...')
	# 		run_scripts(running ,delay,pid)	
			
	# 	if not app.hasPendingEvents():
	# 		app.processEvents()


	# def toggle_running():
	# 	global running,script_runner
	# 	running = not running
	# 	print(running)
	# 	if running:
	# 		ui.stopButton.setText('Stop')
	# 		script_runner = ScriptRunner(running, ui.delayValue.value(), pid)
	# 		script_runner.start()
	# 	else:
	# 		ui.stopButton.setText('Start')
	# 		ui.statusbar.showMessage('Stopped')
	# 		script_runner.stop()
	# 		script_runner.wait()
	# 		del script_runner
	# def check_pid():
	# 	"""
	# 	Check for the MT5 terminal process ID until it is found.
	# 	"""
	# global pid
	# pid = get_pid()
	# if pid is not None:
	# 	ui.stopButton.clicked.connect(toggle_running)
	# 	timer.stop()
	# else:
	# 	ui.statusbar.showMessage('Please open MT5')
	# while running:
	# 	timer = QtCore.QTimer()
	# 	timer.timeout.connect(check_pid)
	# 	timer.start(1000)














# def run_scripts(running,delay,pid):
# 	if running:
# 		if pid :


# class ScriptRunner(QtCore.QThread):
	
# 	def __init__(self, running, delay, pid, parent=None):
# 		super().__init__(parent)
# 		self.running = running
# 		self.delay = delay
# 		self.pid = pid
# 		self.stop_event = threading.Event()
# 	def run(self):
# 		while self.running and not self.stop_event.is_set():
# 			run_scripts(self.running, self.delay, self.pid)
# 			self.delay(1)

# 	def stop(self):
# 		self.stop_event.set()
	