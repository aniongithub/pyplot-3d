from .basic import Sphere, Line, Arrow

import numpy as np


class   Uav:
    '''
    Draws a quadrotor at a given position, with a given attitude.
    '''

    def __init__(self, arm_length):
        '''
        Initialize the quadrotr plotting parameters.

        Params:
            arm_length: (float) length of the quadrotor arm

        Returns:
            None
        '''

        self.arm_length = arm_length

        self.b1 = np.array([1.0, 0.0, 0.0]).T
        self.b2 = np.array([0.0, 1.0, 0.0]).T
        self.b3 = np.array([0.0, 0.0, 1.0]).T

        # Center of the quadrotor
        self.body = Sphere(0.08, 'y')

        # Each motor
        self.motor1 = Sphere(0.05, 'r')
        self.motor2 = Sphere(0.05, 'g')
        self.motor3 = Sphere(0.05, 'b')
        self.motor4 = Sphere(0.05, 'b')

        # Arrows for the each body axis
        self.arrow_b1 = Arrow(self.b1, 'r')
        self.arrow_b2 = Arrow(self.b2, 'g')
        self.arrow_b3 = Arrow(self.b3, 'b')

        # Quadrotor arms
        self.arm_b1 = Line()
        self.arm_b2 = Line()
    

    def draw_at(self, ax, x=np.array([0.0, 0.0, 0.0]).T, R=np.eye(3), clear: bool = True):
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

        # First, clear the axis of all the previous plots
        if clear:
            ax.clear()

        # Center of the quadrotor
        self.body.draw_at(ax, x)

        # Each motor
        self.motor1.draw_at(ax, x + R.dot(self.b1) * self.arm_length)
        self.motor2.draw_at(ax, x + R.dot(self.b2) * self.arm_length)
        self.motor3.draw_at(ax, x + R.dot(-self.b1) * self.arm_length)
        self.motor4.draw_at(ax, x + R.dot(-self.b2) * self.arm_length)

        # Arrows for the each body axis
        self.arrow_b1.draw_from_to(ax, x, R.dot(self.b1) * self.arm_length * 1.8)
        self.arrow_b2.draw_from_to(ax, x, R.dot(self.b2) * self.arm_length * 1.8)
        self.arrow_b3.draw_from_to(ax, x, R.dot(self.b3) * self.arm_length * 1.8)

        # Quadrotor arms
        self.arm_b1.draw_from_to(ax, x, x + R.dot(-self.b1) * self.arm_length)
        self.arm_b2.draw_from_to(ax, x, x + R.dot(-self.b2) * self.arm_length)
