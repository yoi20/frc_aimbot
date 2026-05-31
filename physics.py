from models import GamePiece, Environment, Robot, ShotState
import math

class PhysicsEngine:
    def __init__(self, env: Environment, robot: Robot):
        self.env = env
        self.robot = robot
        
        self.gravity = env.gravity
        self.density = env.air_density

    def calculate_acceleration(self, piece: GamePiece, vx: float, vy: float, vz: float, omega: float):
        v = math.sqrt(vx**2 + vy**2 + vz**2)

        if v == 0:
            return 0.0, 0.0, -self.gravity

        r_drag = (self.density * piece.drag_coeff * piece.area) / (2.0 * piece.mass)
        s_mag = (self.density * piece.magnus_coeff * piece.radius * piece.area) / (2.0 * piece.mass)

        ax = -r_drag * v * vx + s_mag * omega * vz
        ay = -r_drag * v * vy
        az = -self.gravity - r_drag * v * vz - s_mag * omega * vx

        return ax, ay, az
    
    # euler integration tests
    def simulate_euler(self, piece:GamePiece, x:float, y:float, z:float, vx:float, vy:float, vz:float, omega:float, time_step:float):
        while z > 0:
            ax, ay, az = self.calculate_acceleration(piece, vx, vy, vz, omega)
            vx += ax * time_step
            vy += ay * time_step
            vz += az * time_step
            x += vx * time_step
            y += vy * time_step
            z += vz * time_step
        return x, y

