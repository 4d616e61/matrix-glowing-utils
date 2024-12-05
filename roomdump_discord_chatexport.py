import utils.matrix_utils as matrix_utils
import sys
import json

matrix_utils.init_pg()

def convert_entry(inp : dict) -> dict:
    pass


res_pg = matrix_utils.get_all_events_matching(f"room_id='{sys.argv[1]}' and type = 'm.room.message' limit 10")
res_pg.sort(key= lambda d : d["origin_server_ts"])
res = []
for v in res_pg:
    v_parsed = json.loads(v[0])
    print(json.dumps(v_parsed, indent=4))
    res.append(v_parsed)




