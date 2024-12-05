import utils.matrix_utils as matrix_utils
import sys
import json

matrix_utils.init_pg()



res_pg = matrix_utils.get_all_events_matching(f"room_id='{sys.argv[1]}' limit 1", "type=m.room.message")
res = []
for v in res_pg:
    v_parsed = json.loads(v[0])
    print(json.dumps(v_parsed, indent=4))
    res.append(v_parsed)




