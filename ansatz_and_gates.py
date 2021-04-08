"""
The following gates are constructed using circuit identities from
https://arxiv.org/pdf/quant-ph/9503016.pdf
"""
import numpy as np

# import pyzx as zx
# from fractions import Fraction

def add_ansatz_gzb(c, nr_q, nr_p, initialize=True):
    """
    c: quantum circuit
    nr_q: number of qubits
    nr_p: number of qubits initialized in state 1
    initialize
    """

    if initialize == True:
        for i in range(nr_p):
            c.add_gate("NOT", i)

    # Ansatz
    it = 0
    start = nr_p - 1
    limit = nr_q

    while start != -1:

        cq = start
        tq = start + 1

        while tq < limit:
            add_GZB(c, cq, tq, np.random.normal(0, 1, 1)[0] * 2 * np.pi)
            cq = cq + 1
            tq = tq + 1
            it = it + 1

        start = start - 1
        limit = limit - 1

def add_CRZ(c, cq, tq, t):
    """
    c: quantum circuit
    cq: control qubit
    tq: target qubit
    t: theta
    """

    c.add_gate("ZPhase", tq, phase=t / 2)
    c.add_gate("CNOT", cq, tq)
    c.add_gate("ZPhase", tq, phase=-t / 2)
    c.add_gate("CNOT", cq, tq)


def add_CRX(c, cq, tq, t):
    """
    c: quantum circuit
    cq: control qubit
    tq: target qubit
    t: theta
    """
    c.add_gate("HAD", tq)
    c.add_gate("ZPhase", tq, phase=t / 2)
    c.add_gate("CNOT", cq, tq)
    c.add_gate("ZPhase", tq, phase=-t / 2)
    c.add_gate("CNOT", cq, tq)
    c.add_gate("HAD", tq)


def add_CRY(c, cq, tq, t):
    """
    c: quantum circuit
    cq: control qubit
    tq: target qubit
    t: theta
    """
    c.add_gate("S", tq, adjoint=True)
    c.add_gate("HAD", tq)
    add_CRZ(c, cq, tq, t)
    c.add_gate("HAD", tq)
    c.add_gate("S", tq)


def add_GZB(c, q1, q2, t):
    """
    c: quantum circuit
    cq: control qubit
    tq: target qubit
    t: theta
    """
    """
    add_GZB_matrix:
           [[1,0,0,0]
           [0,cos(t),sin(t),0]
           [0,sin(t),-cos(t),0]
           [0,0,0,-1]]
    """

    c.add_gate("CNOT", q1, q2)
    c.add_gate("Z", q1)
    add_CRY(c, q2, q1, np.pi - 2 * t)
    c.add_gate("CNOT", q1, q2)
