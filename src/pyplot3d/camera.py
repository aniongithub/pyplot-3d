from .basic import Line, Sphere

import numpy as np


class Camera:
    '''
    Draws a line at a given position, with a given attitude.
    '''

    def __init__(self, c='b', x=np.array([0.0, 0.0, 0.0]).T, R=np.eye(3)):
        '''
        Initialize the camera.
        Params:
            direction: (3x1 numpy.ndarray) direction of the arrow
            c: (string) color of the arrow, default = 'b'
            x: (3x1 numpy.ndarray) origin of the camera, 
                default = [0.0, 0.0, 0.0]
            R: (3x1 numpy.ndarray) attitude of the camera, 
                default = eye(3)
                
        Returns:
            None
        '''

        self.color = c
        self.x = x
        self.R = R
        
        d = 0.3
        w = 0.2
        h = 0.1
        p1 = np.array([d, w, h])
        p2 = np.array([d, -w, h])
        p3 = np.array([d, -w, -h])
        p4 = np.array([d, w, -h])
        self.l1 = Line(self.ax, 'b', x, p1)
        self.l2 = Line(self.ax, 'b', x, p2)
        self.l3 = Line(self.ax, 'b', x, p3)
        self.l4 = Line(self.ax, 'b', x, p4)
        self.l5 = Line(self.ax, 'r', p1, p2)
        self.l6 = Line(self.ax, 'r', p2, p3)
        self.l7 = Line(self.ax, 'r', p3, p4)
        self.l8 = Line(self.ax, 'r', p4, p1)

        self.origin = Sphere(self.ax, 0.02, 'y')


    def draw(self, ax):
        '''
        Draw a camera with the initially defined parameter when the class was
        instantiated.
        Args:
            ax: (matplotlib axis) the axis where the line should be drawn
        
        Returns:
            None
        '''
        
        self.l1.draw(ax)
        self.l2.draw(ax)
        self.l3.draw(ax)
        self.l4.draw(ax)
        self.l5.draw(ax)
        self.l6.draw(ax)
        self.l7.draw(ax)
        self.l8.draw(ax)
        self.origin.draw(ax)
    

    def draw_at(self, ax, x=np.array([0.0, 0.0, 0.0]).T, R=np.eye(3)):
        '''
        Draw the camera at a given point and attitude.
        Args:
            ax: (matplotlib axis) the axis where the line should be drawn
            x: (3x1 numpy.ndarray) position of camera,
                default = [0.0, 0.0, 0.0]
            R: (3x1 numpy.ndarray) attitude of the camera, 
                default = eye(3)
        
        Returns:
            None
        '''
        
        d = 0.5
        w = 0.4
        h = 0.3
        p1 = x + R@np.array([d, w, h])
        p2 = x + R@np.array([d, -w, h])
        p3 = x + R@np.array([d, -w, -h])
        p4 = x + R@np.array([d, w, -h])

        self.l1.draw_from_to(ax, x, p1)
        self.l2.draw_from_to(ax, x, p2)
        self.l3.draw_from_to(ax, x, p3)
        self.l4.draw_from_to(ax, x, p4)
        self.l5.draw_from_to(ax, p1, p2)
        self.l6.draw_from_to(ax, p2, p3)
        self.l7.draw_from_to(ax, p3, p4)
        self.l8.draw_from_to(ax, p4, p1)
        self.origin.draw_at(ax, x)