#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor.

    Args:
        matrix (list): List of lists of integers or floats representing a matrix.
        div (int or float): Divisor to divide each element of the matrix by.

    Returns:
        A new matrix with each element divided by the divisor and rounded to 2 decimal places.

    Raises:
        TypeError: If the input matrix is not a list of lists of integers or floats, or if the divisor is not a number.
        ValueError: If the input matrix is empty, or if the length of any row in the matrix is different from the others.
        ZeroDivisionError: If the divisor is 0.

    Examples:
        >>> matrix_divided([[1, 2, 3], [4, 5, 6]], 2)
        [[0.5, 1.0, 1.5], [2.0, 2.5, 3.0]]

        >>> matrix_divided([[1, 2, 3], [4, 5, 6]], 0)
        Traceback (most recent call last):
        ...
        ZeroDivisionError: division by zero

        >>> matrix_divided([[1, 2, 3], [4, "5", 6]], 2)
        Traceback (most recent call last):
        ...
        TypeError: matrix must be a matrix (list of lists) of integers/floats

        >>> matrix_divided([], 2)
        Traceback (most recent call last):
        ...
        ValueError: matrix cannot be empty

        >>> matrix_divided([[1, 2, 3], [4, 5], [6, 7, 8]], 2)
        Traceback (most recent call last):
        ...
        ValueError: Each row of the matrix must have the same size

    """
    # Check that the divisor is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check that the matrix is a list of lists of integers or floats
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix) or not all(isinstance(elem, (int, float)) for row in matrix for elem in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check that the matrix is not empty
    if len(matrix) == 0:
        raise ValueError("matrix cannot be empty")

    # Check that each row of the matrix has the same length
    row_lengths = set(len(row) for row in matrix)
    if len(row_lengths) > 1:
        raise ValueError("Each row of the matrix must have the same size")

    # Divide each element of the matrix by the divisor and round to 2 decimal places
    return [[round(elem / div, 2) for elem in row] for row in matrix]
