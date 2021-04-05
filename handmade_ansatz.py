from handmade_gates import add_GZB

import numpy as np
import pyzx as zx


def add_ansatz_gzb(c,nr_q,nr_p, initialize=True):
    '''
    c: quanutm circuit
    nr_q: number of qubits
    nr_p: nuber of qubits initialize in state 1
    initialize
    '''

    if initialize==True:
        for i in range(nr_p):
            c.add_gate("NOT",i)


    #ansatz
    it=0
    start=nr_p-1
    limit=nr_q

    while start!=-1:
        
        cq=start
        tq=start+1
        
        while tq<limit:
            add_GZB(c,cq,tq,np.random.normal(0,1,1)[0]*2*np.pi)
            cq=cq+1
            tq=tq+1
            it=it+1

        start=start-1
        limit=limit-1

