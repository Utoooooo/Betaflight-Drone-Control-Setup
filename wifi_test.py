# import socket
# import time
# import sys
#
# UDP_IP = "192.168.137.1"
# UDP_PORT = 12345
# sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
# sock.bind((UDP_IP, UDP_PORT))
# check = '123'
#
# while True:
#     data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
#     print("received message: %s at time %s" % (int.from_bytes(data,"big"), time.time()))
#
#     print(addr)
#     sock.sendto(check.encode(), addr)
# import socket
#
# UDP_IP = "192.168.137.227"  # IP address of the Arduino
# UDP_PORT = 8888  # Port number of the Arduino
# MESSAGE = "Hello, Arduino!"  # Data to be sent
#
# sock = socket.socket(socket.AF_INET,  # Internet
#                      socket.SOCK_DGRAM)  # UDP
# while True:
#     sock.sendto(bytes(MESSAGE, "utf-8"), (UDP_IP, UDP_PORT))
#     print(MESSAGE)
import Telelink
import numpy as np
import time

UDP_IP = "192.168.137.130"
UDP_Port = 8888
telem = Telelink.Telelink(UDP_IP, UDP_Port)

start_range = 1
end_range = 100

while True:
    arr = np.array([1, 2, 3, 4, 5], dtype=np.uint8)
    # print(arr)
    telem.send(arr)
    time.sleep(1)
    # telem.receive()
    # print(telem.data1)
    # print(time.time())
    # print(telem.data)
    # print(telem.data1)

# import socket
# import numpy as np
# import time
#
# UDP_IP = "192.168.137.65"  # IP address of the Arduino
# UDP_PORT = 8888  # Port number to use
#
# sock = socket.socket(socket.AF_INET,  # Internet
#                      socket.SOCK_DGRAM)  # UDP
# # sock.bind(('', UDP_PORT))  # Bind the socket to the port
#
# arr = np.array([1, 2, 3, 4, 5], dtype=np.uint8)  # Example array to send
# while True:
#     sock.sendto(arr.tobytes(), (UDP_IP, UDP_PORT))  # Convert array to bytes and send over UDP
#
#     # Wait for a response from the Arduino
#     response, address = sock.recvfrom(1024)  # Receive up to 1024 bytes of data
#
#     # Convert the response to an array and print it out
#     arr = np.frombuffer(response, dtype=np.uint8)
#     print("Received array:", arr, time.time())