class Environment:
    def __init__(self, gravity: float = 9.81, air_density: float = 1.14):
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

if __name__ == "__main__":

    fuel_2026 = GamePiece(
        name="2026 Fuel",
        mass=0.215,
        radius=0.075,
        area=0.0177,
        drag_coeff=0.5,
        magnus_coeff=0.3
    )

    hub = Target(
        name="hub",
        height=1.83
    )

    dump = Target(
        name="dump",
        height=0.97
    )

    atlas = Robot(
        turret_x_offse = 0.12543,
        turret_y_offset = 0,
        turret_z_offset = 0.2897,
        hood_offset_deg = 46.0,
        system_latency= 0.1
    )

    print("")
    fuel_2026.print_specs()

