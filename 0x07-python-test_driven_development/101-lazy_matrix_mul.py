#!/usr/bin/python3
"""
Defines a function that multiplies 2 matrices by using NumPy.

Parameters:
    m_a (matrix)
    m_b (matrix)
"""


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using numpy

    Parameters:
    m_a (matrix): The first matrix
    m_b (matrix): The second matrix

    Returns:
        The product of the two matrices.
    """
    # m_a = ([1, 2], [3, 4])
    # m_b = [[1, 2], [3, 4]]
    return np.matmul(m_a, m_b)
