from matplotlib.pyplot import draw
from .basic import Sphere, Line, Arrow

import numpy as np


class Uav:
    '''
    Draws a quadrotor at a given position, with a given attitude.
    '''

    def __init__(self, 
        arm_length = 1.0, arm_color = "g",
        body_radius = 0.5, body_color = "r", 
        motor_radius = 0.25, 
        motor_color = "b"):
        '''
        Initialize the quadrotor plotting parameters.

        Params:
            arm_length: (float) length of the quadrotor arm
            arm_color: (string) color of the quadrotor arms
            body_radius: (float) radius of the sphere representing the quadrotor body
            body_color: (string) color of the sphere representing the quadrotor body
            motor_radius: (float) radius of the spheres representing the quadrotor motors
            motor_color: (string) color of the spheres representing the quadrotor motors

        Returns:
            None
        '''

        self.arm_length = arm_length

        self.b1 = np.array([1.0, 0.0, 0.0]).T
        self.b2 = np.array([0.0, 1.0, 0.0]).T
        self.b3 = np.array([0.0, 0.0, 1.0]).T

        # Center of the quadrotor
        self.body = Sphere(body_radius, body_color)

        # Each motor
        self.motor1 = Sphere(motor_radius, motor_color)
        self.motor2 = Sphere(motor_radius, motor_color)
        self.motor3 = Sphere(motor_radius, motor_color)
        self.motor4 = Sphere(motor_radius, motor_color)

        # Quadrotor arms
        self.arm_b1 = Line(arm_color)
        self.arm_b2 = Line(arm_color)

        self.arm_color = arm_color

    def draw_at(self, ax, x=np.array([0.0, 0.0, 0.0]).T, R=np.eye(3)):
        '''
        Draw the quadrotor at a given position, with a given direction

        Args:
            ax: (matplotlib axis) the axis where the sphere should be drawn
            x: (3x1 numpy.ndarray) position of the center of the quadrotor, 
                default = [0.0, 0.0, 0.0]
            R: (3x3 numpy.ndarray) attitude of the quadrotor in SO(3)
                default = eye(3)
        
        Returns:
            None
        '''

        # Center of the quadrotor
        self.body.draw_at(ax, x)

        # Each motor
        self.motor1.draw_at(ax, x + R.dot(self.b1) * self.arm_length)
        self.motor2.draw_at(ax, x + R.dot(self.b2) * self.arm_length)
        self.motor3.draw_at(ax, x + R.dot(-self.b1) * self.arm_length)
        self.motor4.draw_at(ax, x + R.dot(-self.b2) * self.arm_length)

        # Quadrotor arms
        self.arm_b1.draw_from_to(ax, x, x + R.dot(self.b1) * self.arm_length)
        self.arm_b2.draw_from_to(ax, x, x + R.dot(self.b2) * self.arm_length)
        self.arm_b1.draw_from_to(ax, x, x + R.dot(-self.b1) * self.arm_length)
        self.arm_b2.draw_from_to(ax, x, x + R.dot(-self.b2) * self.arm_length)
