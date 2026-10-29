import numpy as np
from typing import Callable


class InvoluteCutter:
    def __init__(self, module, pressure_angle, tooth_count) -> None:
        self.module = module
        self.pressure_angle = pressure_angle
        self.tooth_count = tooth_count

        self.pitch_diameter = self.module*self.tooth_count
        self.base_diameter = self.pitch_diameter * np.cos(self.pressure_angle)
        self.tip_diameter = self.pitch_diameter + (2*self.module)

        pass

    def involute(self,u,v):

        base_radius = self.base_diameter / 2

        x0 = u
        y0 = base_radius*np.cos(v) + base_radius*v*np.sin(v)        # add shift coefficient to all trignomentric arguments
        z0 = base_radius*np.sin(v) - base_radius*v*np.cos(v)

    def addendum(self,u,v):

        tip_radius = self.tip_diameter / 2

        x0 = u
        y0 = tip_radius*np.cos(v)
        z0 = tip_radius*np.sin(v)


class Transform:
    def __init__(self,input_vector:np.ndarray):
        self.input_vector = input_vector
        pass

    def rotate_x(self,angle:float):
        R_x = np.array([
            [1, 0, 0],
            [0, np.cos(angle), -np.sin(angle)],
            [0, np.sin(angle),  np.cos(angle)]
            ])
        return Transform(R_x @ self.input_vector)

    def rotate_y(self,angle:float):
        R_y = np.array([
            [np.cos(angle), 0, np.sin(angle)],
            [0, 1, 0],
            [-np.sin(angle), 0, np.cos(angle)]
            ])
        return Transform(R_y @ self.input_vector)

    def rotate_z(self,angle:float):
        R_z = np.array([
            [np.cos(angle), -np.sin(angle), 0],
            [np.sin(angle),  np.cos(angle), 0],
            [0, 0, 1]
            ])
        return Transform(R_z @ self.input_vector)

    def translate(self, translation_vector):
        return Transform(self.input_vector+translation_vector)

    def output(self):
        return self.input_vector




if __name__ == "__main__":
    pass