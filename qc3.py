from qiskit import QuantumCircuit, QuantumRegister
from qiskit.quantum_info import Statevector
import qiskit.quantum_info as qi
import numpy as np
from math import pi
import qiskit


def figure_it_out_1():
    """Simplified version of the test circuit 1.

    Original test circuit (sketch):

        h(0)
        z(0)
        h(0)
        cnot(0,1)
        cnot(1,0)
        cnot(0,1)
        h(1)
        z(1)
        h(1)

    Estrategias usadas para simplificar (a nivel conceptual):

    - Identidad de cambio de base con Hadamard:
          H Z H = X
      Por lo tanto:
          H(0) Z(0) H(0) = X(0)
          H(1) Z(1) H(1) = X(1)

      Es decir, los bloques H–Z–H en cada qubit se reducen a una sola
      puerta de Pauli X en ese qubit.

    - Reconocer el patrón SWAP en las CNOT:
          SWAP(0,1) = CNOT(0→1) · CNOT(1→0) · CNOT(0→1)

      El bloque central de tres CNOT del test es exactamente esta
      descomposición de SWAP.

    - Al analizar el operador completo, se puede verificar (por
      cálculo de matrices) que todo el circuito original es
      equivalente a un único SWAP entre los dos qubits (hasta fase
      global, que no afecta la equivalencia de operadores).

    Límite de puertas:
        solo 1 puerta (SWAP), que cuenta como 1.
        → <= 3, se cumple.
    """
    qr = QuantumRegister(2)
    qc = QuantumCircuit(qr)

    # Circuito simplificado: solo un SWAP entre los dos qubits
    qc.swap(0, 1)

    return qi.Operator(qc)


def figure_it_out_2():
    """Simplified version of the test circuit 2.

    Circuito del test (resumen):

        h(0)
        h(0)
        z(0)
        h(0)
        cnot(0,1)
        h(0)
        h(1)
        cnot(0,1)
        h(0)
        h(1)
        cnot(0,1)
        h(1)
        z(1)
        h(1)

    Estrategias usadas:

    - Cancelación de Hadamards consecutivos:
          H · H = I
      Las primeras dos H(0) se anulan, y se pueden reagrupar otras
      H(0)/H(1) para simplificar capas de 1 qubit.

    - De nuevo, usar H Z H = X para reducir bloques de tres puertas
      (H–Z–H) a una sola Pauli en el qubit correspondiente.

    - Al simplificar las capas de 1 qubit y mirar el bloque de CNOT,
      el núcleo entanglante vuelve a ser el patrón:

          CNOT(0→1) · CNOT(1→0) · CNOT(0→1) = SWAP(0,1)

    - El operador global del circuito del test resulta equivalente a:

          H en el qubit 0
          seguido de un SWAP(0,1)

      Es decir, el circuito simplificado es: H(0); SWAP(0,1).

    Límite de puertas:
        1 puerta H + 1 puerta SWAP = 2 puertas
        → <= 4, se cumple.
    """
    qr = QuantumRegister(2)
    qc = QuantumCircuit(qr)

    # Circuito simplificado: H en q0 y luego SWAP
    qc.h(0)
    qc.swap(0, 1)

    return qi.Operator(qc)


def figure_it_out_3():
    """Simplified version of the test circuit 3.

    Circuito del test:

        x(0)
        h(0)
        cnot(0,1)
        z(0)
        x(1)
        cnot(0,1)
        z(0)
        x(1)
        h(1)

    Estrategias usadas:

    - Identidades con H y Pauli:
          H X H = Z
          H Z H = X

      Permiten reagrupar y simplificar cadenas de X, Z y H en el
      qubit 0.

    - Patrones con X en el target de CNOT:
      Reorganizando las X(1) alrededor de CNOT(0→1) y usando que
      puertas en qubits distintos conmutan, se ve que el efecto
      entanglante neto desaparece y el operador completo del test
      se puede escribir como un producto de puertas de 1 qubit.

    - Por cálculo de matrices (4x4) se verifica que el operador del
      circuito del test es exactamente equivalente a:

          H en qubit 0
          H en qubit 1
          seguido de Z en qubit 0

      Es decir, el circuito simplificado es: H(0); H(1); Z(0).

    Límite de puertas:
        2 Hadamards + 1 Z = 3 puertas
        → <= 3, se cumple.
    """
    qr = QuantumRegister(2)
    qc = QuantumCircuit(qr)

    # Circuito simplificado: solo puertas de 1 qubit
    qc.h(0)
    qc.h(1)
    qc.z(0)

    return qi.Operator(qc)
