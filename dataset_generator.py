import math
import random
import numpy as np
from models import Environment, GamePiece, Robot, ShotState, Target
from physics import PhysicsEngine
from scipy.optimize import minimize as sp_minimize

class DatasetGenerator:
    def __init__(self, engine: PhysicsEngine, target: Target, piece: GamePiece):
        self.engine = engine
        self.target = target
        self.piece = piece

        self.static_rpms = []
        self.static_hoods = []
        self.static_distances = np.linspace(1.0, 20.0, 200)

    def precompute_static_shots(self):
        print(f"computing {self.target.name} static shots...")
        print(f"optimizing {self.target.name} shots...")
        prev_rpm, prev_hood = 3200, 9.5
        for target_d in self.static_distances:
            def cost(x):
                state = ShotState(
                v_rad = 0.0,
                v_tan = 0.0,
                omega = 0.0,
                a_rad = 0.0,
                a_tan = 0.0,
                alpha = 0.0,
                pitch = 0.0,
                roll = 0.0,
                distance = 0.0
                )
                lx, ly = self.engine.simulate_shot(self.piece, shate, rpm=x[0], hood=x[1], aim_offset=0.0, target_z=self.target.height)
                
                if lx is None:
                    return 1000000.0
                
                dist = math.sqrt(lx**2 + ly**2)
                miss = dist - target_d
                miss ** 2
            
            res = sp_minimize(cost, [prev_rpm, prev_hood], method='Nelder-Mead')
        winning_rpm = res.x[0]
        winning_hood = res.x[1]

        winning_rpm.append(self.static_rpms)
        winning_hood.append(self.static_hoods)

        prev_rpm = winning_rpm
        prev_hood = winning_hood
                
        pass

    def generate_reverse_mapping_dataset(self, num_shots: int):

        print(f"generating {num_shots} shots...")

        dataset = []

        for _ in range(num_shots):
            base_dist = random.uniform(1.0, 20.0)
            
            base_rpm = 4000.0
            base_hood = 5.0

            rpm = base_rpm + random.uniform(-15.0, 15.0)
            hood = base_hood + random.uniform(-0.5, 0.5)

            state = ShotState(
                v_rad = random.uniform(-5.0, 5.0),
                v_tan = random.uniform(-5.0, 5.0),
                omega = random.uniform(-4.0, 4.0),
                a_rad = random.uniform(-8.0, 8.0),
                a_tan = random.uniform(-8.0, 8.0),
                alpha = random.uniform(-10.0, 10.0),
                pitch = random.uniform(-0.3, 0.3),
                roll  = random.uniform(-0.3, 0.3),
                distance = 0.0 
            )

            aim_offset = math.radians(random.uniform(-20, 20))

            lx, ly = self.engine.simulate_shot(
                piece=self.engine.robot,
                state=state,
                rpm=rpm,
                hood_deg=hood,
                aim_offset_rad=aim_offset
            )

        return dataset

