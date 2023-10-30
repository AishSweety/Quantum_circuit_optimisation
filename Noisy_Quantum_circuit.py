import pennylane as qml
import numpy as np

N_QUBITS = 4
NOISE_STRENGTH = 0.05
NUM_LAYERS = 3
NUM_STEPS = 200
STEP_SIZE = 0.05

dev = qml.device("default.mixed", wires=N_QUBITS, shots=1000)

@qml.qnode(dev)
def noisy_circuit(var_params, x=None):
    # Encoding using a loop for more qubits
    for i, xi in enumerate(x):
        qml.RX(xi, wires=i)
        qml.DepolarizingChannel(NOISE_STRENGTH, wires=i)

    # More layers in the variational part
    for _ in range(NUM_LAYERS):
        for i in range(N_QUBITS):
            qml.RX(var_params[i], wires=i)
            qml.RY(var_params[i + N_QUBITS], wires=i)
        for i in range(N_QUBITS - 1):
            qml.CNOT(wires=[i, i + 1])

    # Measurement
    return [qml.expval(qml.PauliZ(i)) for i in range(N_QUBITS)]

def noisy_cost(var_params, x=None, y=None):
    predictions = np.array(noisy_circuit(var_params, x=x))
    return np.sum((predictions - y) ** 2)

def optimize_with_noise():
    var_params = qml.numpy.random.rand(2 * N_QUBITS)
    true_thetas = np.pi * np.random.rand(N_QUBITS)
    observed_values = np.array(noisy_circuit(var_params, x=true_thetas))

    # Using the Adam optimizer
    opt = qml.AdamOptimizer(stepsize=STEP_SIZE)

    for _ in range(NUM_STEPS):
        var_params = opt.step(noisy_cost, var_params, x=true_thetas, y=observed_values)

    print("Optimized parameters with noise:", var_params)
    print("Final cost with noise:", noisy_cost(var_params, x=true_thetas, y=observed_values))

if __name__ == "__main__":
    optimize_with_noise()
