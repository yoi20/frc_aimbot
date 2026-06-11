from models import Environment, GamePiece, Robot, ShotState, Target
from physics import PhysicsEngine

calgary = Environment(
    gravity = 9.81,
    air_density = 1.14
)

fuel_2026 = GamePiece(
    name = "2026 Fuel",
    mass = 0.215,
    radius = 0.075,
    area = 0.0177,
    drag_coeff = 0.5,
    magnus_coeff = 0.3
)

hub = Target(
    name = "hub",
    height = 1.83
)

dump = Target(
    name = "dump",
    height = 0.97
)

atlas = Robot(
    turret_x_offset = 0.12543,
    turret_y_offset = 0,
    turret_z_offset = 0.2897,
    hood_offset_deg = 46.0,
    system_latency = 0.1
)

engine = PhysicsEngine(calgary, atlas)