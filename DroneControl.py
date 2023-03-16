import time
import serial
import math
import numpy as np

print("droneControlFunctions Imported")

class PID_Controller:

    def __init__(self, dt, kp=1, ki=0.8, kd=0):
        """Initialise PID controller for drone"""

        self.kp = kp
        self.ki = ki
        self.kd = kd

        self.dt = dt

        self.integral = 0
        self.olderror = 0

    def update(self, ref, state):
        """Update step for PID controller"""
        e = ref - state
        # Speed limiter
        if e > 100:
            e = 100
        elif e < -100:
            e = -100
        self.integral = self.integral + e * self.dt
        i = self.integral
        d = e - self.olderror
        self.olderror = e

        velocity = self.kp * e + self.ki * i + self.kd * d

        return velocity


class P_Controller:
    def __init__(self, dt, kp=1):
        """Initialise PID controller for drone velocity"""
        self.kp = kp
        self.dt = dt
        self.actuation = 0

    def update(self, ref, state):
        """Update step for PID controller"""
        e = ref - state
        # Speed limiter
        if e > 100:
            e = 100
        elif e < -100:
            e = -100

        self.actuation = self.kp * e


class KalmanFilter:
    def __init__(self, process_noise, measurement_noise):
        self.process_noise = process_noise
        self.measurement_noise = measurement_noise
        self.state_vector = np.zeros((2, 1))  # [position; velocity]
        self.state_covariance = np.identity(2)  # [covariance of position; covariance of velocity]

    def predict(self, delta_time):
        # predict state
        self.state_vector[1, 0] += delta_time * 9.8  # acceleration due to gravity
        self.state_vector[0, 0] += self.state_vector[1, 0] * delta_time

        # predict covariance
        F = np.array([[1, delta_time], [0, 1]])
        self.state_covariance = np.dot(F, np.dot(self.state_covariance, F.T)) + self.process_noise

    def update(self, measurement):
        # Kalman gain
        H = np.array([1, 0]).reshape((1, 2))
        S = np.dot(H, np.dot(self.state_covariance, H.T)) + self.measurement_noise
        K = np.dot(self.state_covariance, np.dot(H.T, np.linalg.inv(S)))

        # update state and covariance
        self.state_vector += np.dot(K, (measurement - np.dot(H, self.state_vector)))
        self.state_covariance -= np.dot(K, np.dot(H, self.state_covariance))