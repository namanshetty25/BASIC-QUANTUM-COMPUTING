import pennylane as qml
from pennylane import numpy as np
import matplotlib.pyplot as plt
n=3
dev=qml.device("default.qubit",wires=n)
@qml.qnode(dev)
def quantum_circuit():
    qml.PauliX(wires=1)
    qml.Hadamard(wires=1)   
    qml.PauliX(wires=0)
    qml.PauliX(wires=2)
    qml.CNOT(wires=[0,2])
    return qml.state()
state=quantum_circuit()
print("Final state=",state)
drawer=qml.draw(quantum_circuit)
print(drawer())
def plot_bar(state):
    probs=np.abs(state)**2
    plt.bar(range(len(probs)),probs)
    plt.xticks(range(len(probs)),['000','001','010','011','100','101','110','111'])
    plt.xlabel('Basic States')
    plt.ylabel('Probability')
    plt.title('Qubit State probabilities')
    plt.show()
plot_bar(state)