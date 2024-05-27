import ctypes
import os


class LoadCLib:
    def __init__(self, lib_path) -> None:
        self.lib_path = lib_path

    def c_lib_load(self):
        if os.name == "posix":
            return ctypes.CDLL(os.path.join(self.lib_path, "./lib.so"))
        elif os.name == "nt":
            return ctypes.CDLL(os.path.join(self.lib_path, "./lib.dll"), winmode=0)
