# Quantum Circuit Optimization with Noise

This Python script demonstrates demonstrates quantum circuit optimization using PennyLane with the introduction of depolarizing noise. The noisy quantum circuit consists of multiple layers of parameterized quantum gates with added depolarizing noise. The optimization is performed to minimize the cost function (using the Adam optimizer from PennyLane), which measures the squared difference between the noisy circuit predictions and target values.

Feel free to experiment with different values of `N_QUBITS`, `NOISE_STRENGTH`, `NUM_LAYERS`, `NUM_STEPS`, and `STEP_SIZE` to observe how they impact the optimization process.

### Quantum circuit optimization using PennyLane and PyTorch

This code illustrates a basic quantum circuit optimization using PennyLane and PyTorch, demonstrating how the circuit parameters evolve to minimize the cost function and provides insight into the optimization process with the help of visualization.

