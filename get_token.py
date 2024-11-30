#!/bin/python
import utils.matrix_utils as matrix_utils
import sys
import json


matrix_utils.init_pg()
res = matrix_utils.get_user_tokens(sys.argv[1])[0][0]
print(res)
