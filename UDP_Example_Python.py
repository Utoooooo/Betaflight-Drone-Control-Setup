import Telelink
import numpy as np
import time

UDP_IP = <ESP32 IP address>
UDP_Port = <Port number>
telem = Telelink.Telelink(UDP_IP, UDP_Port)

while True:
    arr = np.array([1, 2, 3, 4, 5], dtype=np.uint8)
    telem.send(arr)
    telem.receive()
    time.sleep(1)
