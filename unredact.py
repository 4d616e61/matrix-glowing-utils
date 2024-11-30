#!/bin/python
import matrix_utils
import sys
import json


matrix_utils.init_pg()
res = matrix_utils.get_event(sys.argv[1])
print("RAW JSON:")
print(json.dumps(json.loads(res), indent=4))

print("\n\n\n")
print("MESSAGE:")
print(json.loads(res)["content"]["body"])
