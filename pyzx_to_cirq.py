import numpy as np

import pyzx as zx
import cirq

gate_colection = {
    "CNOT": cirq.CNOT,
    "CCZ": cirq.CCZ,
    "TOFFOLI": cirq.TOFFOLI,
    "Z": cirq.Z,
    "X": cirq.X,
    "Y": cirq.Y,
    "HAD": cirq.H,
    "S": cirq.S,
    "S*":  cirq.S ** -1,
    "T": cirq.T,
    "T*": cirq.T ** -1,
}

def to_cirq_circuit(gc):

    nr_qubits = gc.qubits
    q_list = []
    for i in range(nr_qubits):
        q_list.append(cirq.NamedQubit("q" + str(i)))

    gates = gc.gates

    cq_gates = []
    for i in gates:
        i = str(i)
        qubits_id = []
        s = i.find("(")
        ss = i.find(")")
        name = i[0:s]
        # print(name)

        while s < ss - 1:
            qubits_id.append(int(i[s + 1]))
            s = s + 2
        # print(qubits_id)

        nrq = len(qubits_id)
        if nrq == 1:
            cq_gate = gate_colection[name](q_list[qubits_id[0]])
        if nrq == 2:
            cq_gate = gate_colection[name](q_list[qubits_id[0]], q_list[qubits_id[1]])
        if nrq == 3:
            cq_gate = gate_colection[name](
                q_list[qubits_id[0]], q_list[qubits_id[1]], q_list[qubits_id[2]]
            )

        cq_gates.append(cq_gate)

        circuit = cirq.Circuit()
        circuit.append(cq_gates)

    return circuit
