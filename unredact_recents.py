#!/bin/python
import utils.matrix_utils as matrix_utils
import sys
import json
from utils.misc import *


matrix_utils.init_pg()

limit = 16
if len(sys.argv) > 1:
    limit = int(sys.argv[1]) 
    

res_redact_events = matrix_utils.get_all_events_matching(f"type='m.room.redaction' order by origin_server_ts desc limit {limit}")
events_final = []
for ev in res_redact_events:
    ev = json.loads(ev[0])
    try:
        events_final.append(matrix_utils.get_event(ev["redacts"]))
    except:
        pass
for ev in events_final:

    
    print(json_reserialize(ev))

print("\n\n\n")

for ev in events_final:

    
    print(format_event_json(ev))
    