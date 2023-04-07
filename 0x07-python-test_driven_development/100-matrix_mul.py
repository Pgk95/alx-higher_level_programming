#!/usr/bin/python3
def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices.

    Args:
        m_a (list[list]): The first matrix.
        m_b (list[list]): The second matrix.

    Raises:
        TypeError: If m_a or m_b is not a list, if m_a or m_b is not a list of lists, if one element of those list of lists is not an integer or a float, or if m_a or m_b is not a rectangle.
        ValueError: If m_a or m_b is empty, or if m_a and m_b cannot be multiplied.

    Returns:
        list[list]: The resulting matrix.
    """
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list" if not isinstance(m_a, list) else "m_b must be a list")

    if not all(isinstance(row, list) for row in m_a) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_a must be a list of lists" if not all(isinstance(row, list) for row in m_a) else "m_b must be a list of lists")

    if not m_a or not m_b:
        raise ValueError("m_a can't be empty" if not m_a else "m_b can't be empty")

    if not all(isinstance(elem, (int, float)) for row in m_a for elem in row) or not all(isinstance(elem, (int, float)) for row in m_b for elem in row):
        raise TypeError("m_a should contain only integers or floats" if not all(isinstance(elem, (int, float)) for row in m_a for elem in row) else "m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a) or not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_a must be of the same size" if not all(len(row) == len(m_a[0]) for row in m_a) else "each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            elem = 0
            for k in range(len(m_b)):
                elem += m_a[i][k] * m_b[k][j]
            row.append(elem)
        result.append(row)

    return result
