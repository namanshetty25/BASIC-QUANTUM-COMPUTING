import pennylane as qml
from pennylane import numpy as np
import matplotlib.pyplot as plt
n = 2
dev = qml.device('default.qubit', wires=n)
def oracle():
    qml.CZ(wires=[0, 1])  
def diffusion():
    for wire in range(n):
        qml.Hadamard(wires=wire)
    qml.PauliZ(wires=0)
    qml.PauliZ(wires=1)
    qml.CZ(wires=[0, 1])
    for wire in range(n):
        qml.Hadamard(wires=wire)
@qml.qnode(dev)
def gc():
    for wire in range(n):
        qml.Hadamard(wires=wire)
    oracle()
    diffusion()
    return qml.probs(wires=range(n))
results = gc()
print("\nMeasurement Results (Probabilities):")
print(results)
labels = ['00', '01', '10', '11']
plt.bar(labels, results)
plt.title("Grover's Algorithm Results")
plt.xlabel("Quantum State")
plt.ylabel("Probability")
plt.show()
print("\nCircuit Diagram:")
print(qml.draw(gc)())
