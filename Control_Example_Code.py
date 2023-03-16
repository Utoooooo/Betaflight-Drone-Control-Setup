import DroneControl as dc
import Telelink
import time

ref = 50
dt = 1 / 64
hover_point = 1300

pid_z = dc.PID_Controller(dt, kp=0.4, ki=0.9, kd=0.3)
pid_vz = dc.P_Controller(dt, kp=0.9)

# Initialises sending commands to drone
uart_port = 'COM3'
link = Telelink.Command(uart_port, baudrate=115200)

actuation = 0

start_time = time.time()
prev_height = 0

UDP_IP = <UDP_IP>
UDP_Port = <UDP_Port>
telem = Telelink.Telelink(UDP_IP, UDP_Port)

while True:
    telem.receive()
    height = telem.data
    # p for velocity, then pid for actuation
    v_z = (height - prev_height) / dt
    v_target = pid_vz.update(ref, float(prev_height))
    print(f'Current Velocity Z: {v_z}, target velocity: {v_target}')
    print(f'Current Position Z: {height}, target position: {ref}')
    actuation = pid_z.update(v_target, v_z) + hover_point
    if actuation > 2000:
        actuation = 2000
    elif actuation < 1000:
        actuation = 1000
    ################################
    # Update motor commands on drone
    ################################
    prev_height = height
    link.drone_control_update(link, thrust=actuation)

