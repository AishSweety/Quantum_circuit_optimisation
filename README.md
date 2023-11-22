# Quantum Circuit Optimization with Noise

This repository contains a Python script that demonstrates the optimization of parameters in a quantum circuit in the presence of noise using the PennyLane quantum machine learning library.

The noisy quantum circuit consists of multiple layers of parameterized quantum gates with added depolarizing noise. The optimization is performed to minimize the cost function, which measures the squared difference between the noisy circuit predictions and target values.

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

The provided Python script (`Noisy_Quantum_circuit.py`) demonstrates quantum circuit optimization using PennyLane with the introduction of depolarizing noise. Here's an in-depth overview of the key components:

## Quantum Circuit

- The quantum circuit is designed with `N_QUBITS` qubits and `NUM_LAYERS` layers of parameterized gates.
- Depolarizing noise is added using `qml.DepolarizingChannel` to each qubit with a strength defined by `NOISE_STRENGTH`.

## Optimization Process

- The script utilizes the Adam optimizer from PennyLane (`qml.AdamOptimizer`) to minimize the cost function.
- The cost function (`noisy_cost`) measures the squared difference between the noisy circuit predictions and target values.

## Adjustable Parameters

- `N_QUBITS`: Number of qubits in the quantum circuit.
- `NOISE_STRENGTH`: Strength of depolarizing noise in the circuit.
- `NUM_LAYERS`: Number of layers in the quantum circuit.
- `NUM_STEPS`: Number of optimization steps.
- `STEP_SIZE`: Step size for the Adam optimizer.

## How to Run

1. Install dependencies:
    ```bash
    pip install pennylane numpy
    ```

2. Run the script:
    ```bash
    python Noisy_Quantum_circuit.py
    ```

## Expected Results

After execution, the script provides the following insights:

- Initial and optimized parameters with noise.
- Final cost with noise.
- Progress updates, including the cost every 50 optimization steps.

Feel free to explore and tweak the script's parameters to observe their impact on the quantum circuit optimization process.

**A sample result might be:** 

```Step 1/500 - Cost: 0.42117200580613057
Step 51/500 - Cost: 0.00532150966495609
Step 101/500 - Cost: 0.0009827634183996485
Step 151/500 - Cost: 0.003632380964203527
Step 201/500 - Cost: 0.008309205200032511
Step 251/500 - Cost: 0.003367313941022975
Step 301/500 - Cost: 0.004483429754468289
Step 351/500 - Cost: 0.0004644365611147626
Step 401/500 - Cost: 0.0016671744886384318
Step 451/500 - Cost: 0.0009698926507689575

Optimization complete.
Initial parameters: [-0.0053129   0.02964236 -0.03075332  0.00614341 -0.08388644 -0.08074193]
Optimized parameters with noise: [ 0.2750713  -0.17449515 -0.74842674  1.19032489  0.04084672 -0.80055725]
Final cost with noise: 0.0019116677791764314
```


Feel free to experiment with different values of `N_QUBITS`, `NOISE_STRENGTH`, `NUM_LAYERS`, `NUM_STEPS`, and `STEP_SIZE` to observe how they impact the optimization process.


For any questions or issues, please refer to the [PennyLane documentation](https://pennylane.ai/qml/) or the [PennyLane GitHub repository](https://github.com/PennyLaneAI/pennylane).



