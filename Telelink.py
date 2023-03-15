import socket
import time
import numpy as np
import serial


class Telelink:
    def __init__(self, udp_ip, udp_port=8888):
        """

        :param udp_ip: IP address of the board
        :param udp_port: Port number of the board
        """
        self.UDP_IP = udp_ip
        self.UDP_Port = udp_port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
        self.data = []
        self.addr = []

    def send(self, request):
        self.sock.sendto(request.tobytes(), (self.UDP_IP, self.UDP_Port))

    def receive(self):
        # print("buff")
        data, self.addr = self.sock.recvfrom(1024)
        self.data = np.frombuffer(data, dtype=np.int8)


class Throttle:
    def __init__(self, port, baudrate):
        self.port = port
        self.baudrate = baudrate
        self.timeout = 0.1
        self.link = serial.Serial(port=port, baudrate=115200, timeout=0.1)

    def drone_control_update(self,

                             roll=1500, pitch=1500, thrust=1000, yaw=1500):
        #########################################
        # Use pySerial Library
        #########################################
        throttle = ("<%s,%s,%s,%s,>" % (int(thrust), int(yaw), int(roll), int(pitch)))
        print(throttle)
        self.link.write(bytes(str(throttle), 'utf-8'))
        time.sleep(0.001)
