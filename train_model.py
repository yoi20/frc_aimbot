from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler
import numpy as np
import struct

dataset = np.loadtxt("output/training_data.csv", delimiter=",")

X = dataset[:, :10]
y = dataset[:, 10:]


scaler_X = StandardScaler()
scaler_y = StandardScaler()

X_scaled = scaler_X.fit_transform(X)
y_scaled = scaler_y.fit_transform(y)


# training the model
model = MLPRegressor(hidden_layer_sizes=(512, 512, 256), activation='relu')
model.fit(X_scaled, y_scaled)

print(model.score(X_scaled, y_scaled))


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
    # to finish later
    pass

