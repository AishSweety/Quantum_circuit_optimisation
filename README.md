# Noisy_Quantum_circuit
A quantum machine learning algorithm to optimize a noisy quantum circuit's parameters
Overview
Quantum sensors are devices that use quantum properties to make highly precise measurements, such as detecting electromagnetic fields.

In this code, we use a quantum circuit to encode a time-dependent external parameter (magnetic field frequency) and optimize the circuit's parameters to estimate the correct parameter value.

The optimization is performed on a noisy quantum device, which adds various types of noise to the quantum operations. The optimization algorithm aims to find the optimal parameters that minimize the difference between the estimated and actual values of the external parameter.

The code uses PennyLane to define and optimize the quantum circuit, and the optimization algorithm employed is the Adam optimizer.

Code Explanation
Here is an explanation of the key components of the code:

Device Setup
N_QUBITS: Number of qubits used in the quantum circuit.
NUM_LAYERS: Number of layers in the variational circuit.
NUM_STEPS: Number of optimization steps.
STEP_SIZE: Step size for the Adam optimizer.
Noisy Quantum Device Setup
UNKNOWN_FREQUENCY: The actual external parameter we aim to estimate. It is a random frequency between 0.1 and 0.5.

DEPOLARIZING_NOISE_STRENGTH, PHASE_DAMPING_NOISE_STRENGTH, AMPLITUDE_DAMPING_NOISE_STRENGTH: Parameters representing the noise strength of the quantum device.

dev: The quantum device, configured with the specified noise model.

Quantum Circuit Definition
quantum_sensor: This function defines the quantum circuit. It encodes the external parameter using a sequence of quantum gates. The parameter to estimate, UNKNOWN_FREQUENCY, is used to apply a RZ gate on each qubit. Noisy channels (depolarizing, phase damping, amplitude damping) are added to simulate noise in the device. The variational circuit follows, where the parameters are optimized. The measurement is performed in the X basis, and the expectation value of Pauli-X is returned.

cost: This function calculates the cost of the quantum circuit by comparing its output to a reference value.

optimize_sensor: The main optimization function. It initializes parameters, performs optimization steps, and prints the progress.

estimate_frequency: This function calculates the estimated frequency based on the phase differences in the circuit's outputs.

Inside the if __name__ == "__main__": block, the code runs the optimize_sensor function to estimate the external parameter.

Output
The code prints the optimization progress at each step, including the cost and the estimated frequency. Once the optimization is completed, the final estimated frequency and the actual frequency are displayed.

Running the Code
Ensure you have PennyLane and other required packages installed in your Python environment.
Copy and paste the provided code into a Python script or Jupyter Notebook.
Run the script.
Observe the optimization progress and the final estimated frequency.
