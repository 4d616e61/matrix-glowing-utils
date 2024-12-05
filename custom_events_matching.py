import utils.matrix_utils as matrix_utils
import sys
import json

matrix_utils.init_pg()



res = matrix_utils.get_all_events_matching(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else "")

for v in res:
    print("MESSAGE:")
    (json.loads(v[0])["content"]["body"])




