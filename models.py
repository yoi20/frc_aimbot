class Environment:
    def __init__(self, gravity: float, air_density: float):
        self.gravity = gravity
        self.air_density = air_density


class GamePiece:
    def __init__(self, name: str, mass: float, radius: float, area: float, drag_coeff: float, magnus_coeff: float):
        self.name = name
        self.mass = mass
        self.radius = radius
        self.area = area
        self.drag_coeff = drag_coeff
        self.magnus_coeff = magnus_coeff

    def print_specs(self):
        print(f"{self.name} specs")
        print(f"mass: {self.mass} kg")
        print(f"radius: {self.radius} m")
        print(f"drag coefficient: {self.drag_coeff}")

class Target:
    def __init__(self, name: str, height: float):
        self.name = name
        self.height = height

class Robot:
    def __init__(self, turret_x_offset: float, turret_y_offset:float, turret_z_offset: float, hood_offset_deg: float, system_latency: float):
        self.turret_x_offset = turret_x_offset
        self.turret_y_offset = turret_y_offset
        self.turret_z_offset = turret_z_offset
        self.hood_offset_deg = hood_offset_deg
        self.system_latency = system_latency

class ShotState:
    def __init__(self, a_rad: float, a_tan: float, alpha: float, v_rad: float, v_tan:float, omega:float, pitch:float, roll:float, distance:float):
        self.a_rad = a_rad
        self.a_tan = a_tan
        self.alpha = alpha
        self.v_rad = v_rad
        self.v_tan = v_tan
        self.omega = omega
        self.pitch = pitch
        self.roll = roll
        self.distance = distance



