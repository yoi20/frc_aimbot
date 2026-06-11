from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import numpy as np
import struct
from config import engine, hub, fuel_2026
from models import ShotState
import math
import random
from tqdm import tqdm

dataset = np.loadtxt("output/training_data.csv", delimiter=",")

X = dataset[:, :10]
y = dataset[:, 10:]


scaler_X = StandardScaler()
scaler_y = StandardScaler()

X_scaled = scaler_X.fit_transform(X)
y_scaled = scaler_y.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y_scaled, test_size=0.1, random_state=42
)


# training the model
model = MLPRegressor(
    hidden_layer_sizes=(512, 512, 256), 
    activation='relu',
    solver='adam',
    max_iter=4000,
    tol=1e-6,
    batch_size=4096,
    learning_rate_init=0.001,
    early_stopping=True,
    validation_fraction=0.1,
    n_iter_no_change=50,
    verbose=True,
)

model.fit(X_train, y_train)

y_pred = scaler_y.inverse_transform(model.predict(X_test))
y_true = scaler_y.inverse_transform(y_test)

print(model.score(X_test, y_test))

def validate_physics(model, scaler_X, scaler_y, engine, target, piece):
    hits = 0
    for _ in tqdm(range(100), desc="validating shots"):
        dist = random.uniform(2.0, 10.0)
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
        inputs = np.array([[dist, target.height, state.v_rad, state.v_tan, state.omega, state.a_rad, state.a_tan, state.alpha, state.pitch, state.roll]])

        scaled_inputs = scaler_X.transform(inputs)
        prediction = model.predict(scaled_inputs)
        outputs = scaler_y.inverse_transform(prediction)[0]

        lx, ly = engine.simulate_shot(piece=piece, state=state, rpm=outputs[0], hood_deg=outputs[1], aim_offset_rad=outputs[2], target_z=target.height)

        real_dist = math.sqrt(lx**2 + ly**2)
        if abs(real_dist - dist) < 0.3:
            hits += 1

    print(f"hit rate: {hits}/100")



# export to binary to put into deploy folder
def export_binary(model, path):
    with open(path, 'wb') as f:
        f.write(struct.pack('>i', len(model.coefs_)))
        for x in scaler_X.mean_:
            f.write(struct.pack('>d', float(x)))
        for x in scaler_X.scale_:
            f.write(struct.pack('>d', float(x)))
        for x in scaler_y.mean_:
            f.write(struct.pack('>d', float(x)))
        for x in scaler_y.scale_:
            f.write(struct.pack('>d', float(x)))
            
        for weights, biases in zip(model.coefs_, model.intercepts_):
            f.write(struct.pack('>i', weights.shape[0]))
            f.write(struct.pack('>i', weights.shape[1]))

            for w in weights.flatten():
                f.write(struct.pack('>d', float(w)))
            
            for b in biases:
                f.write(struct.pack('>d', float(b)))


export_binary(model, "output/neuralnetwork.bin")
validate_physics(model, scaler_X, scaler_y, engine, hub, fuel_2026)
            
            
            

