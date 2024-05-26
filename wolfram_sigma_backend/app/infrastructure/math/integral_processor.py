import ctypes

import sympy as sp

from wolfram_sigma_backend.app.infrastructure.math.load_lib import LoadCLib


class IntegralProcessorFromCLib:
    def __init__(self, lib_path="wolfram_sigma_backend/math/integral"):
        self.lib = LoadCLib(lib_path).c_lib_load()

    @staticmethod
    def __convert_string_to_func(string):
        try:
            expr = sp.sympify(string)
            symbols = expr.free_symbols
            symbols_list = list(symbols)

            def func(**kwargs):
                for symbol in symbols:
                    if symbol.name not in kwargs:
                        raise ValueError(f"Missing value for variable '{symbol}'")

                subs = {symbol: kwargs[symbol.name] for symbol in symbols}
                return float(expr.evalf(subs=subs))

            return func, symbols_list
        except SyntaxError:
            raise SyntaxError("Invalid equation")

    # def calculate_definite_integral(self, equation: str):
    #     func, symbol_list = self.__convert_string_to_func(equation)
    #     c_f = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)(func)
    #     result = ctypes.c_double()
    #
    #     code = self.lib.indefiniteIntegral(c_f, a, b, num_points, ctypes.byref(result)))
    #
    # def calculate_indefinite_integral(self):
    #     ...
