#!/bin/python
import utils.matrix_utils as matrix_utils
import sys


matrix_utils.init_pg()
res = matrix_utils.get_user_tokens(sys.argv[1])
print(res)
