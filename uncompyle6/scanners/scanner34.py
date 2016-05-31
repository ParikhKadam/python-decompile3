#  Copyright (c) 2015-2016 by Rocky Bernstein
"""
Python 3.4 bytecode scanner/deparser

This sets up opcodes Python's 3.4 and calls a generalized
scanner routine for Python 3.
"""

from __future__ import print_function

# import xdis

# bytecode verification, verify(), uses JUMP_OPs from here
# JUMP_OPs = xdis.opcodes.opcode_34.JUMP_OPs

from uncompyle6.scanners.scanner3 import Scanner3
class Scanner34(Scanner3):

    def __init__(self):
        super(Scanner3, self).__init__(3.4)
        return
    pass

if __name__ == "__main__":
    from uncompyle6 import PYTHON_VERSION
    if PYTHON_VERSION == 3.4:
        import inspect
        co = inspect.currentframe().f_code
        tokens, customize = Scanner34().disassemble(co)
        for t in tokens:
            print(t)
        pass
    else:
        print("Need to be Python 3.4 to demo; I am %s." %
              PYTHON_VERSION)
