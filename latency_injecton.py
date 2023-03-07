import time
import psutil
import pydivert
import logging
from PyQt5.QtCore import QBuffer
logging.basicConfig(filename='app.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s: %(message)s')

def get_pid():
	process_name = ['terminal64.exe','terminal32.exe']
	for process in psutil.process_iter():
		if process.name() in process_name:
			pid = process.pid
			return pid
	else:
		return None


def get_app_ip_and_port(pid):
	if pid:
		connections = psutil.net_connections("tcp")
		for conn in connections:
			if conn.pid == pid and conn.status == "ESTABLISHED":
				app_ip, app_port = conn.laddr
				logging.debug(f"pid {pid},Source IP: {app_ip}, Source Port: {app_port}")
				return [app_ip,app_port]
	else :
		pass


def latency_injection(filter_expression,delay):
	with pydivert.WinDivert(filter_expression) as w:
		buffer_size = 4096 
		packet = w.recv(buffer_size)
		last_send_time = time.monotonic()
		if packet:
			if time.monotonic() - last_send_time >= delay :
				original_data = bytes(packet.raw)

				# Wait for the specified amount of time to simulate latency
				time.sleep(delay)

				# Reinject the original packet into the network
				w.send(original_data)
	print("doneeeeeeeeeeeeeeeeeeeeeeee")

			





	