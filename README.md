### Quantum Sensor Training

This Python code implements a simple quantum machine learning algorithm for training a quantum sensor to estimate a target value. The quantum sensor is represented by a parameterized quantum circuit consisting of a Hadamard gate (H) and a rotation-y gate (RY) with a variable parameter theta. The algorithm employs the parameter-shift rule, a quantum gradient descent technique, to update the parameter theta and minimize the cost function, which measures the discrepancy between the quantum sensor's output and the target value.

The training process involves iteratively adjusting the parameter theta based on the observed outcomes of quantum measurements. The quantum circuit is simulated using the Qiskit framework, and the counts of measurement outcomes are used to evaluate the cost function. The cost function represents the difference between the measured probability of obtaining a '0' outcome and the target value. The parameter-shift rule calculates the gradient of the cost function with respect to theta and updates the parameter accordingly.

The algorithm iterates through multiple epochs, printing the cost and updated theta at each step. It continues training until the cost falls below a specified convergence threshold. The final plot visualizes the cost function's evolution over epochs. The trained parameter theta represents the optimized state of the quantum sensor, providing an estimate close to the target value. The code concludes by printing the trained theta and displaying the training progress through the plotted graph.

### Quantum Circuit Optimization with Noise

This Python script demonstrates demonstrates quantum circuit optimization using PennyLane with the introduction of depolarizing noise. The noisy quantum circuit consists of multiple layers of parameterized quantum gates with added depolarizing noise. The optimization is performed to minimize the cost function (using the Adam optimizer from PennyLane), which measures the squared difference between the noisy circuit predictions and target values.

Feel free to experiment with different values of `N_QUBITS`, `NOISE_STRENGTH`, `NUM_LAYERS`, `NUM_STEPS`, and `STEP_SIZE` to observe how they impact the optimization process.

### Quantum circuit optimization using PennyLane and PyTorch

This code illustrates a basic quantum circuit optimization using PennyLane and PyTorch, demonstrating how the circuit parameters evolve to minimize the cost function and provides insight into the optimization process with the help of visualization.

