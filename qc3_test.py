import qc3
from qiskit import QuantumCircuit, QuantumRegister
from qiskit.quantum_info import Statevector, Operator
import numpy as np
import qiskit.quantum_info as qi

##########################
#DON'T MODIFY THIS FILE! ONLY RUN IT TO SEE TEST RESULTS
##########################
def test_figure_it_out_1():
    """ Tests a function 

    Args: 
        None
    """
    qr=QuantumRegister(2)
    qc=QuantumCircuit(qr)
    qc.h(0)
    qc.z(0)
    qc.h(0)
    qc.cnot(0,1)
    qc.cnot(1,0)
    qc.cnot(0,1)
    qc.h(1)
    qc.z(1)
    qc.h(1)
    print(qc.draw())
    assert qi.Operator(qc).equiv(qc3.figure_it_out_1())
    print("SUCCESSFUL TEST")

##########################
#DON'T MODIFY THIS FILE! ONLY RUN IT TO SEE TEST RESULTS
##########################
def test_figure_it_out_2():
    """ Tests a function

    Args: 
        None
    """

    qr=QuantumRegister(2)
    qc=QuantumCircuit(qr)
    qc.h(0)
    qc.h(0)
    qc.z(0)
    qc.h(0)
    qc.cnot(0,1)
    qc.h(0)
    qc.h(1)
    qc.cnot(0,1)
    qc.h(0)
    qc.h(1)
    qc.cnot(0,1)
    qc.h(1)
    qc.z(1)
    qc.h(1)
    print(qc.draw())
    assert qi.Operator(qc).equiv(qc3.figure_it_out_2())
    print("SUCCESSFUL TEST")

##########################
#DON'T MODIFY THIS FILE! ONLY RUN IT TO SEE TEST RESULTS
##########################
def test_figure_it_out_3():
    """ Tests a function 

    Args: 
        None
    """
    qr=QuantumRegister(2)
    qc=QuantumCircuit(qr)
    qc.x(0)
    qc.h(0)
    qc.cnot(0,1)
    qc.z(0)
    qc.x(1)
    qc.cnot(0,1)
    qc.z(0)
    qc.x(1)
    qc.h(1)
    print(qc.draw())
    assert qi.Operator(qc).equiv(qc3.figure_it_out_3())
    print("SUCCESSFUL TEST")

##########################
#DON'T MODIFY THIS FILE! ONLY RUN IT TO SEE TEST RESULTS
##########################
if __name__ == '__main__':
    """ Run this to verify if tests are failing"""

    test_figure_it_out_1()
    test_figure_it_out_2()
    test_figure_it_out_3()
