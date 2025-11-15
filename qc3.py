from qiskit import QuantumCircuit,  QuantumRegister
from qiskit.quantum_info import Statevector
from math import pi
import qiskit
import numpy as np
import qiskit.quantum_info as qi

def figure_it_out_1():
    """ Simplify the circuit from the test with the strategies we saw in class. You should get
        get a circuit with at most 3 gates. This will be inspected manually. If you pass the test with
        more gates, you will get a 0 as your grade (A swap gate or a cnot gate counts as 1 gate)
    Circuito Original del Taller 3:
        qc.h(0)
        qc.z(0)
        qc.h(0)
        qc.cnot(0,1)
        qc.cnot(1,0)
        qc.cnot(0,1)
        qc.h(1)
        qc.z(1)
        qc.h(1)
    
    SIMPLIFICACIONES:
        Paso 1: H(0)·Z(0)·H(0) = X(0)  [Identity: HZH = X]
        Paso 2: CNOT(0,1)·CNOT(1,0)·CNOT(0,1) = SWAP(0,1)  [Identity: 3 CNOTs = SWAP]
        Paso 3: H(1)·Z(1)·H(1) = X(1)  [Identity: HZH = X]
        
    RESULTADO: X(0) → SWAP(0,1) → X(1) = 3 gates (SE CUMPLE CON 3 COMPUERTAS)
    
    Args: 
        None
    """
    qr=QuantumRegister(2)
    qc=QuantumCircuit(qr)
    #begins your code 
    # Paso 1: H·Z·H = X on qubit 0
    qc.x(0)

    # Paso 2: Three CNOTs = SWAP
    qc.swap(0, 1)

    # Paso 3: H·Z·H = X on qubit 1
    qc.x(1)
    #ends your code 
    return qi.Operator(qc)

def figure_it_out_2():
    """ Simplify the circuit from the test with the strategies we saw in class. You should get
        get a circuit with at most 4 gates. This will be inspected manually. If you pass the test with
        more gates, you will get a 0 as your grade (A swap gate or a cnot gate counts as 1 gate)
    Circuito Original del Taller 3:
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
    
    SIMPLIFICACIONES:
        Paso 1: H(0)·H(0) = I  [Identity: H·H = I, gates cancel]
        Paso 2: After cancellation: Z(0)·H(0)·[middle section]·H(1)·Z(1)·H(1)
        Paso 3: Middle section with CNOTs and Hadamards = SWAP
        Paso 4: H(1)·Z(1)·H(1) = X(1)  [Identity: HZH = X]
        
    RESULTADO: Z(0) → H(0) → SWAP(0,1) → X(1) = 4 gates (SE CUMPLE CON 4 COMPUERTAS)
    

    Args: 
        None
    """
    qr=QuantumRegister(2)
    qc=QuantumCircuit(qr)
    #begins your code 
    # Paso 1: First two H(0) cancel, leaving Z(0)
    qc.z(0)

    # Paso 2: Z·H remains on qubit 0
    qc.h(0)

    # Paso 3: Middle section simplifies to SWAP
    qc.swap(0, 1)

    # Paso 4: H·Z·H = X on qubit 1
    qc.x(1)
    #ends your code 
    return qi.Operator(qc)

def figure_it_out_3():
    """ Simplify the circuit from the test with the strategies we saw in class. You should get
        get a circuit with at most 3 gates. This will be inspected manually. If you pass the test with
        more gates, you will get a 0 as your grade (A swap gate or a cnot gate counts as 1 gate)
    
    Circuito Original del Taller 3:
        qc.x(0)
        qc.h(0)
        qc.cnot(0,1)
        qc.z(0)
        qc.x(1)
        qc.cnot(0,1)
        qc.z(0)
        qc.x(1)
        qc.h(1)
    
    SIMPLIFICACIONES:
        Paso 1: X(0)·H(0) = H(0)·Z(0)  [Identity: XH = HZ]
        Paso 2: Two Z(0) gates cancel: Z(0)·Z(0) = I  [Identity: Z·Z = I]
        Paso 3: Two X(1) gates cancel: X(1)·X(1) = I  [Identity: X·X = I]
        Paso 4: After all cancellations, remains: H(0)·CNOT(0,1)·H(1)
        
    RESULTADO: H(0) → CNOT(0,1) → H(1) = 3 gates (SE CUMPLE CON 3 COMPUERTAS)
    Args: 
        None
    """
    qr=QuantumRegister(2)
    qc=QuantumCircuit(qr)
    #begins your code 
    qc.h(0)
    qc.cnot(0, 1)
    qc.h(1)
    #ends your code 
    return qi.Operator(qc)

