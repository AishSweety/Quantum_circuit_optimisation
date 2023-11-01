# Noisy_Quantum_circuit

This repository contains a Python script that demonstrates the optimization of parameters in a quantum circuit in the presence of noise using the PennyLane quantum machine learning library.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Code Description](#code-description)
- [How to Run](#how-to-run)
- [Expected Results](#expected-results)

## Prerequisites
- Python 3.6 or higher
- PennyLane library (install using `pip install pennylane`)
- NumPy library (install using `pip install numpy`)

## Code Description
The provided Python script `noisy_optimization.py` demonstrates the optimization of a noisy quantum circuit using PennyLane. Below is an overview of the key components:

1. **Importing Libraries**: The necessary libraries, including PennyLane and NumPy, are imported at the beginning of the script.

2. **Constants**:

**N_QUBITS**: The number of qubits in the quantum circuit.
**NOISE_STRENGTH**: The strength of depolarizing noise applied to each qubit.
**NUM_LAYERS**: The number of layers in the variational part of the circuit.
**NUM_STEPS**: The number of optimization steps.
**STEP_SIZE**: The step size for the Adam optimizer.

3.  **Quantum Device Initialization**: A quantum device is initialized using PennyLane's qml.device. It is set to a default mixed-state quantum device with a specified numberof qubits and a number of shots (measurements).

4. **Quantum Circuit Definition**: The code defines a quantum circuit using PennyLane. The circuit includes:
   - Encoding of input data using RX gates.
   - Application of depolarizing noise to each qubit.
   - Variational layers consisting of RX and RY gates, as well as CNOT gates for entanglement.
   - Measurement of Pauli-Z operators on each qubit.

5. **Cost Function**: The `noisy_cost` function calculates the cost of the quantum circuit. It computes predictions by running the circuit and calculates the sum of squared differences between the predictions and the target values.

6. **Optimization**: The `optimize_with_noise` function is responsible for optimizing the circuit's parameters. It performs optimization using the Adam optimizer for a specified number of steps. In each step, it updates the parameters based on the cost function.

7. **Main Execution**: The `optimize_with_noise` function is called when the script is run.

## How to Run
1. Ensure you have Python, PennyLane, and NumPy installed on your system.

2. Download the `noisy_optimization.py` script from this repository.

3. Open a terminal or command prompt and navigate to the directory containing the script.

4. Run the script using the following command: ````python noisy_optimization.py````


## Expected Results
When you run the script, it will optimize the parameters of the quantum circuit with noisy operations using the Adam optimizer. You can expect the following results to be printed:

1. The optimized parameters with noise.
2. The final cost with noise, which indicates how well the quantum circuit's predictions match the target values.

These results provide insights into how noise affects the optimization process and the final parameter values of the quantum circuit.

**A sample result might be:** 

``Optimized parameters with noise: [ 0.92412072 -0.03054978 -0.22668299 -0.15816225  0.63331806  0.52812374  0.27499776  0.84965232] Final cost with noise: 0.002784``


Feel free to experiment with different values of `N_QUBITS`, `NOISE_STRENGTH`, `NUM_LAYERS`, `NUM_STEPS`, and `STEP_SIZE` to observe how they impact the optimization process.

For any questions or issues, please refer to the [PennyLane documentation](https://pennylane.ai/qml/) or the [PennyLane GitHub repository](https://github.com/PennyLaneAI/pennylane).



