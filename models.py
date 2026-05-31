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

    print("")
    fuel_2026.print_specs()

