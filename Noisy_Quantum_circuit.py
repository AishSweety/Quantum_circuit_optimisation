import pennylane as qml
import numpy as np

N_QUBITS = 2
NOISE_STRENGTH = 0.05
NUM_LAYERS = 3
NUM_STEPS = 500  # Increased number of steps
STEP_SIZE = 0.1  # Adjusted step size

dev = qml.device("default.mixed", wires=N_QUBITS, shots=1000)

@qml.qnode(dev)
def noisy_circuit(var_params, x=None):
    for i, xi in enumerate(x):
        qml.RX(xi, wires=i)
        qml.DepolarizingChannel(NOISE_STRENGTH, wires=i)

    for _ in range(NUM_LAYERS):
        for i in range(N_QUBITS):
            qml.Rot(var_params[i], var_params[i + N_QUBITS], var_params[i + 2 * N_QUBITS], wires=i)
        for i in range(N_QUBITS - 1):
            qml.CNOT(wires=[i, i + 1])

    return [qml.expval(qml.PauliZ(i)) for i in range(N_QUBITS)]

def noisy_cost(var_params, x=None, y=None):
    predictions = np.array(noisy_circuit(var_params, x=x))
    return np.sum((predictions - y) ** 2)

def optimize_with_noise():
    # Adjusting the initial parameters with a smaller range
    var_params = qml.numpy.random.uniform(low=-0.1, high=0.1, size=3 * N_QUBITS)
    true_thetas = np.pi * np.random.rand(N_QUBITS)

    initial_params = var_params.copy()

    # Using the Adam optimizer with an increased step size
    opt = qml.AdamOptimizer(stepsize=STEP_SIZE)

    for i in range(NUM_STEPS):
        # Evaluate the initial circuit with true parameters
        observed_values = np.array(noisy_circuit(var_params, x=true_thetas))

        # Pass true_thetas as the target values for the optimization
        var_params = opt.step(noisy_cost, var_params, x=true_thetas, y=true_thetas)

        # Print the cost every 50 steps
        if i % 50 == 0:
            print(f"Step {i+1}/{NUM_STEPS} - Cost: {noisy_cost(var_params, x=true_thetas, y=true_thetas)}")

    print("\nOptimization complete.")
    print("Initial parameters:", initial_params)
    print("Optimized parameters with noise:", var_params)
    print("Final cost with noise:", noisy_cost(var_params, x=true_thetas, y=true_thetas))

if __name__ == "__main__":
    optimize_with_noise()
