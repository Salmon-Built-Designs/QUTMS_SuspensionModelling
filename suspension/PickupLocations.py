from sympy import *
import numpy as np
from math import sqrt

class PickupLocations:

    def __init__(self, frontChassis, rearChassis, sphericalHolder, position):
        self.frontChassis = frontChassis
        self.rearChassis = rearChassis
        self.sphericalHolder = sphericalHolder

        if position == 'Top' or position == 'Bottom' or position == 'top' or position == 'bottom':
            self.position = position
        else:
            raise Exception("Error: Position must be top or bottom")

    def calculate_spherical_holders(self, interval, min, max):
        A = np.matrix([
            [1,0,0,-(self.rearChassis.get_x()-self.frontChassis.get_x())],
            [0,1,0,-(self.rearChassis.get_y()-self.frontChassis.get_y())],
            [0,0,1,-(self.rearChassis.get_z()-self.frontChassis.get_z())],
            [(self.rearChassis.get_x()-self.frontChassis.get_x()), (self.rearChassis.get_y()-self.frontChassis.get_y()), (self.rearChassis.get_z()-self.frontChassis.get_z()), -1]
        ])

        b = np.transpose(np.matrix([
            [self.frontChassis.get_x(), self.frontChassis.get_y(), self.frontChassis.get_z(), self.sphericalHolder.get_x()*(self.rearChassis.get_x()-self.frontChassis.get_x()) + self.sphericalHolder.get_y()*(self.rearChassis.get_y()-self.frontChassis.get_y()) + self.sphericalHolder.get_z()*(self.rearChassis.get_z()-self.frontChassis.get_z()) ]
        ]))

        sol = np.linalg.solve(A,b)

        Point_Rotation = [sol[0].tolist()[0][0], sol[1].tolist()[0][0], sol[2].tolist()[0][0]]
        Radius = sqrt((Point_Rotation[0] - self.sphericalHolder.get_x())**2 + (Point_Rotation[1] - self.sphericalHolder.get_y())**2 + (Point_Rotation[2] - self.sphericalHolder.get_z())**2)
        print(Radius)
        pass

    def calc_SH(self, interval, min, max):
        self.calculate_spherical_holders(interval, min, max)