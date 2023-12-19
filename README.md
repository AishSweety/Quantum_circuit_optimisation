### Quantum Sensor Training

This Python code implements a quantum machine learning algorithm for training a quantum sensor to estimate a target value. The quantum sensor is represented by a parameterized quantum circuit consisting of a Hadamard gate (H) and a rotation-y gate (RY) with a variable parameter theta. The algorithm employs the parameter-shift rule, a quantum gradient descent technique, to iteratively update the parameter theta and minimize the cost function, which measures the difference between the quantum sensor's output and the target value. The training process involves simulating the quantum circuit using Qiskit, evaluating the cost function based on measurement outcomes, and adjusting theta accordingly. The algorithm iterates through epochs, printing cost and updated theta until convergence. The final plot visualizes the cost function's evolution, and the trained parameter theta provides an optimized state for the quantum sensor, closely estimating the target value. The code concludes by printing the trained theta and displaying the training progress.

### Quantum Circuit Optimization with Noise

This Python script demonstrates demonstrates quantum circuit optimization using PennyLane with the introduction of depolarizing noise. The noisy quantum circuit consists of multiple layers of parameterized quantum gates with added depolarizing noise. The optimization is performed to minimize the cost function (using the Adam optimizer from PennyLane), which measures the squared difference between the noisy circuit predictions and target values.

Feel free to experiment with different values of `N_QUBITS`, `NOISE_STRENGTH`, `NUM_LAYERS`, `NUM_STEPS`, and `STEP_SIZE` to observe how they impact the optimization process.

### Quantum circuit optimization using PennyLane and PyTorch

This code illustrates a basic quantum circuit optimization using PennyLane and PyTorch, demonstrating how the circuit parameters evolve to minimize the cost function and provides insight into the optimization process with the help of visualization.

### Quantum weather predictor
This code implements a quantum machine learning model for weather prediction using PennyLane. It defines a quantum circuit (`weather_circuit`) that processes a sequence of the last 7 days' weather data and is trained to minimize the mean squared error between quantum predictions and actual weather conditions. The model utilizes a gradient descent optimizer and is trained on randomly generated weather sequences. The code includes a function (`predict`) for making predictions based on the trained quantum circuit and visualizes the trained circuit for a randomly generated weather sequence.
