import ctypes

import numpy as np

from wolfram_sigma_backend.app.infrastructure.math.load_lib import LoadCLib


class MatrixProcessorFromCLib:
    def __init__(self, lib_path="wolfram_sigma_backend/math/matrix") -> None:
        self.lib = LoadCLib(lib_path).c_lib_load()

    def matrix_multiplication(
        self, first_matrix: list[list[float]], second_matrix: list[list[float]], num_threads: int = 1
    ) -> np.array:
        self.lib.matrixMultiplication.argtypes = [
            ctypes.POINTER(ctypes.c_double),
            ctypes.POINTER(ctypes.c_double),
            ctypes.POINTER(ctypes.c_double),
            ctypes.c_int,
            ctypes.c_int,
            ctypes.c_int,
            ctypes.c_int,
            ctypes.c_int,
        ]
        self.lib.matrixMultiplication.restype = ctypes.c_char_p

        row_first, column_first = np.array(first_matrix, dtype=np.float64).shape
        row_second, column_second = np.array(second_matrix, dtype=np.float64).shape
        result_matrix = np.zeros((row_first, column_second), dtype=np.float64)
        code = self.lib.matrixMultiplication(
            np.array(first_matrix, dtype=np.float64).ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
            np.array(second_matrix, dtype=np.float64).ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
            result_matrix.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
            row_first,
            column_second,
            column_first,
            row_second,
            num_threads,
        )
        if code.decode("utf-8") != "OK":
            raise ValueError(f"{code.decode('utf-8')}")
        else:
            return result_matrix

    def matrix_determinate(self, matrix: list[list[float]], num_threads: int = 1):
        self.lib.determinant.argtypes = [
            ctypes.POINTER(ctypes.c_double),
            ctypes.POINTER(ctypes.c_double),
            ctypes.c_int,
            ctypes.c_int,
        ]
        self.lib.determinant.restype = ctypes.c_char_p
        result = ctypes.c_double()
        code = self.lib.determinant(
            np.array(matrix, dtype=np.float64).ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
            ctypes.byref(result),
            np.array(matrix, dtype=np.float64).shape[0],
            num_threads,
        )
        if code.decode("utf-8") != "OK":
            raise ValueError(f"{code.decode('utf-8')}")
        else:
            return "{:.6f}".format(result.value)

    def inverse_matrix(self, matrix: list[list[float]]):
        self.lib.inverseMatrix.argtypes = [
            ctypes.POINTER(ctypes.c_double),
            ctypes.POINTER(ctypes.c_double),
            ctypes.c_int,
        ]
        self.lib.inverseMatrix.restype = ctypes.c_char_p
        result_matrix = np.zeros(
            (np.array(matrix, dtype=np.float64).shape[0], np.array(matrix, dtype=np.float64).shape[0]), dtype=np.float64
        )

        code = self.lib.inverseMatrix(
            np.array(matrix, dtype=np.float64).ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
            result_matrix.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
            np.array(matrix, dtype=np.float64).shape[0],
        )
        if code.decode("utf-8") != "OK":
            raise ValueError(f"{code.decode('utf-8')}")
        else:
            return result_matrix
