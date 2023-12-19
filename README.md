# Quantum Circuit Optimization with Noise

This Python script demonstrates demonstrates quantum circuit optimization using PennyLane with the introduction of depolarizing noise. 

The noisy quantum circuit consists of multiple layers of parameterized quantum gates with added depolarizing noise. The optimization is performed to minimize the cost function (using the Adam optimizer from PennyLane), which measures the squared difference between the noisy circuit predictions and target values.


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

