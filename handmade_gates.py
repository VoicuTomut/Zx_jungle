import numpy as np
import pyzx as zx
from fractions import Fraction

def add_CRZ(c,cq,tq,t):
    '''
    c: quantum circuit 
    cq: contol qubit
    tq: target qubit
    t: theta 
    '''
    
    c.add_gate("ZPhase", tq, phase=t/2)
    c.add_gate("CNOT",cq,tq)
    c.add_gate("ZPhase", tq, phase=-t/2)
    c.add_gate("CNOT",cq,tq)



def add_CRX(c,cq,tq,t):
    '''
    c: quantum circuit 
    cq: contol qubit
    tq: target qubit
    t: theta 
    '''
    c.add_gate("HAD", tq)
    c.add_gate("ZPhase", tq, phase=t/2)
    c.add_gate("CNOT",cq,tq)
    c.add_gate("ZPhase", tq, phase=-t/2)
    c.add_gate("CNOT",cq,tq)
    c.add_gate("HAD", tq)


def add_CRY(c,cq,tq,t):
    '''
    c: quantum circuit 
    cq: contol qubit
    tq: target qubit
    t: theta 
    '''
    c.add_gate("S", tq ,adjoint=True)
    c.add_gate("HAD", tq)
    add_CRZ(c,cq,tq,t)
    c.add_gate("HAD", tq)
    c.add_gate("S",tq)


def add_GZB(c,q1,q2,t):
    '''
    c: quantum circuit 
    cq: contol qubit
    tq: target qubit
    t: theta 
    '''
    '''
    add_GZB_matrix:
           [[1,0,0,0]
           [0,cos(t),sin(t),0]
           [0,sin(t),-cos(t),0]
           [0,0,0,-1]]
    '''

    c.add_gate("CNOT",q1,q2)
    c.add_gate("Z", q1 )
    add_CRY(c,q2,q1,np.pi-2*t)
    c.add_gate("CNOT",q1,q2)