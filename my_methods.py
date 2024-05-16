from math import inf
from my_math import Math_functions

from methods.m_three_point import m_three_point
from methods.m_straightening import m_straightening
from methods.m_chase import m_chase
from methods.m_constant_angle import m_constant_angle
from methods.m_parallel_approach import m_parallel_approach
from methods.m_proportional_convergence import m_proportional_convergence

class Methods():
    data = None

    def __init__(self, data):
        self.data = data
        self.math_f = Math_functions()

        self.xb, self.yb = data["initial"]["baseX"], data["initial"]["baseY"]
        self.coeff = data["initial"]["rocketSpeedCoeff"]
        self.coeff_aim = data["initial"]["aimSpeedCoeff"]
        self.max_dist = data["initial"]["catchDistance"]
        self.f0, self.f1 = data["initial"]["aimPhiTMinus3"], data["initial"]["aimPhiTMinus2"]
        self.r0, self.r1 = data["initial"]["aimRTMinus3"], data["initial"]["aimRTMinus2"]
        self.t = data["initial"]["oneTimeInterval"]

        (self.v_x, self.v_y) = self.math_f.speed(
            self.r0, self.f0, self.r1, self.f1, 1, self.coeff_aim)
        self.v_aim = - ((self.v_x**2 + self.v_y**2) ** 0.5)
        self.v_c = self.v_aim * self.coeff

    def three_point(self, is_catch=False):
        return m_three_point(self, is_catch)

    def straightening(self, is_catch=False, m=1):
        return m_straightening(self, is_catch, m)

    def chase(self, is_catch=False):
        return m_chase(self, is_catch)
    
    def constant_angle(self, is_catch=False):
        return m_constant_angle(self, is_catch)

    def parallel_approach(self, is_catch=False):
        return m_parallel_approach(self, is_catch)
    
    def proportional_convergence(self, is_catch=False, k=1):
        if k==inf:
            return m_parallel_approach(self, is_catch)
        return m_proportional_convergence(self, is_catch, k)
