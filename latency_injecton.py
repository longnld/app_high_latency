import time
import psutil
import pydivert
import logging

logging.basicConfig(filename='app.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s: %(message)s')

def get_pid():
    process_name = ['terminal64.exe','terminal32.exe']
    for process in psutil.process_iter():
        if process.name() in process_name:
            pid = process.pid
            return pid
    else:
        raise ValueError(f"No running process found with name {process_name}")


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
        buffer_size = 1000
        
        packet_buffer = []
        last_send_time = time.monotonic()
        for packet in w:
            try:
                logging.debug(f"Received packet {packet.src_addr}:{packet.src_port} -> {packet.dst_addr}:{packet.dst_port}")                
                packet_buffer.append(packet)
                if len(packet_buffer) >= buffer_size or time.monotonic() - last_send_time >= delay :
                    print(packet_buffer)
                    time.sleep(delay )
                    for buffered_packet in packet_buffer:
                        w.send(buffered_packet)
                        # scapy_packet = IP(buffered_packet.raw)
                        # # write packet to pcap file
                        # wrpcap('pcap_file.pcap', scapy_packet, append=True)
                    packet_buffer = []
                    last_send_time = time.monotonic()
            except Exception  as e:
                logging.error(f"Error injecting latency: {e}")





    