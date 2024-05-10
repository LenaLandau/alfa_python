# python -m compileall bytecode.py =>
# __pycache__/bytecode.cpython-312.pyc

import dis

def beispiel():
	return "Hallo Welt"

dis.dis(beispiel)
#   4           0 LOAD_CONST               1 ('Hallo Welt')
#               2 RETURN_VALUE

def beispiel2(x):
	return x * x + 42

dis.dis(beispiel2)
# 11           0 LOAD_FAST                0 (x)
# 2 LOAD_FAST                0 (x)
# 4 BINARY_MULTIPLY
# 6 LOAD_CONST               1 (42)
# 8 BINARY_ADD
# 10 RETURN_VALUE
