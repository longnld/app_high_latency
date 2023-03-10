import time
import psutil
import pydivert
import ipaddress
import queue
import threading
import logging
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
	list=[]
	if pid:
		connections = psutil.net_connections("tcp")
		for conn in connections:
			if conn.pid == pid and conn.status == "ESTABLISHED":
				app_ip, app_port = conn.laddr
				list.append([app_ip,app_port])
				logging.debug(f"pid {pid},Source IP: {app_ip}, Source Port: {app_port}")
		logging.debug(f'list app ip and port {list}')
		return list		
	else :
		pass

delay_queue = queue.Queue()
count = 0
def capture(filter_expression,delay):
	  # List to hold delayed packets
	with pydivert.WinDivert(filter_expression) as w:
		for packet in w:
			# Add packet to buffer
			delay_queue.put(packet)

			if delay_queue.qsize() == 10:
				injection_thread = threading.Thread(target=inject_delayed_packets, args=(w, delay_queue, delay))
				injection_thread.daemon = True
				injection_thread.start()
				print(injection_thread)
			print("capturing..")
	print("stop")
			
def inject_delayed_packets(w, delay_queue,delay):
	global count
	count += 1
	logging.debug(f'count {count}')
	temp_list = [delay_queue.get() for i in range(0,10) ]
	print(temp_list)
	# Wait until it's time to send the packet
	time_to_send = time.monotonic() + delay
	while time.monotonic() < time_to_send:
		time_left = time.sleep(time_to_send - time.monotonic())
		if time_left is not None and time_left > 0:
			time.sleep(time_left)
		# Send the packet
	for packet in temp_list:
		w.send(packet)
		# print(time.asctime()," queue ",delay_queue.qsize()," count :" ,count,end="\r",flush=True)
		# If the queue is now empty, exit the thread
	current_thread = threading.current_thread()
	print(f"Thread {current_thread.name} done")
