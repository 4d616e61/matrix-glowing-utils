#!/bin/python
import utils.matrix_utils as matrix_utils
import sys
import json

matrix_utils.init_pg()
res = matrix_utils.get_all_events_matching(f"type='m.room.member' and room_id='{sys.argv[1]}' order by origin_server_ts desc limit 1")
res = json.loads(res[0][0])
print(json.dumps(res["auth_events"], indent=4))