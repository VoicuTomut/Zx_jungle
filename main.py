import pyzx as zx

from ansatz_and_gates import add_ansatz_gzb

def main():
    print("Hello World!")

    # zx.settings.drawing_backend = "matplotlib"
    zx.settings.mode = "shell"


    qubits = 10  # Amount of qubits in circuit.
    depth = 11  # Depth of circuit.

    """
        Random CHP circuit
    """
    p_had = 0.2  # probability that each gate is a Hadamard gate.
    p_t = 0.2  # probability that each gate is a T gate (or if clifford is set, S gate).
    clifford = False  # when set to True, the phase gates are S gates instead of T gates.
    circuit1 = zx.generate.CNOT_HAD_PHASE_circuit(
        qubits=qubits, depth=depth, p_had=p_had, p_t=p_t, clifford=clifford
    )
    zx.draw(circuit1).savefig("1.png")

    """
        Random Clifford+T circuit
    """
    p_t = 0.2  # Probability that each gate is a T-gate.
    p_s = 0.3  # Probability that each gate is a S-gate.
    p_hsh = 0.1  # Probability that each gate is a HSH-gate.
    p_cnot = 0.3  # Probability that each gate is a CNOT-gate.
    circuit2 = zx.generate.cliffordT(
        qubits=qubits,
        depth=depth,
        p_t=p_t,
        p_s=p_s,
        p_hsh=p_hsh,
        p_cnot=p_cnot,
        backend=None,
    )
    zx.draw(circuit2).savefig("2.png")

    """
        Random Clifford circuit
    """
    no_hadamard = False  # Whether hadamard edges are allowed to be placed.
    t_gates = False  #
    circuit3 = zx.generate.cliffords(
        qubits=qubits, depth=depth, no_hadamard=no_hadamard, t_gates=t_gates,
        backend=None
    )
    zx.draw(circuit3).savefig("3.png")

    """
        Ansatz test
    """
    nr_q = 5
    nr_p = 2
    circuit = zx.Circuit(qubit_amount = nr_q)
    add_ansatz_gzb(circuit, nr_q,nr_p, initialize=True)
    zx.draw(circuit).savefig("4.png")

if __name__ == "__main__":
    main()

