# BASIC-QUANTUM-COMPUTING

This repository contains a collection of basic quantum computing projects implemented using Python. Each project demonstrates a fundamental concept or algorithm in quantum computing, making this repository a great starting point for beginners.

## Projects Overview

### 1. Quantum Circuit Simulation

This project uses PennyLane and Matplotlib to simulate a quantum circuit with 3 qubits. The circuit applies a series of quantum gates to the qubits and visualizes the probability distribution of the output states as a bar chart. It provides insight into how quantum operations transform quantum states and how their measurement probabilities can be visualized.

**Key Features:**
- 3-qubit quantum circuit simulation
- Application of multiple quantum gates
- Visualization of output state probabilities

### 2. Bloch Sphere Visualization

The Bloch_sphere project visualizes a single qubit’s quantum state on the Bloch sphere using the QuTiP library. By specifying spherical coordinates θ and 𝜙, the script calculates the corresponding Cartesian coordinates and displays the state vector on a 3D Bloch sphere. This geometric representation helps illustrate how quantum states are oriented in three-dimensional space.

**Key Features:**
- Visualization of a qubit’s state on the Bloch sphere
- Uses QuTiP for accurate quantum state representation
- Interactive 3D plotting of state vectors

### 3. Simple Quantum Circuit

Simple_quantum_circuit demonstrates the use of several fundamental quantum gates using PennyLane. The circuit operates on 3 qubits and applies Pauli-X, Hadamard, and CNOT gates. The resulting quantum state is measured, and the probabilities of the possible outcomes are visualized using a bar chart.

**Key Features:**
- Demonstrates basic quantum gates (X, H, CNOT)
- Visualizes the effects of gates on a quantum circuit
- Uses PennyLane and Matplotlib for simulation and plotting

### 4. Grover’s Algorithm

This project implements Grover’s search algorithm to find the target state |11> among four possible states (|00>, |01>, |10>, |11>). The algorithm amplifies the probability of the target state, making it much more likely to be measured than the other states. This example highlights the power of quantum algorithms in searching unsorted data sets.

**Key Features:**
- Implementation of Grover's search algorithm
- Amplifies and visualizes the target state probability
- Illustrates quantum speedup for basic search problems

---

## Getting Started

### Requirements

- Python 3.x
- [PennyLane](https://pennylane.ai/)
- [Matplotlib](https://matplotlib.org/)
- [QuTiP](http://qutip.org/)

Install dependencies with:
```bash
pip install pennylane matplotlib qutip
```

### Running the Examples

Clone the repository and navigate to the project directory:
```bash
git clone https://github.com/namanshetty25/BASIC-QUANTUM-COMPUTING.git
cd BASIC-QUANTUM-COMPUTING
```

Run any of the scripts with:
```bash
python script_name.py
```
For Jupyter notebooks, open them using:
```bash
jupyter notebook
```

---

## License

This repository is licensed under the MIT License.

## Author

Created by [namanshetty25](https://github.com/namanshetty25)

---
