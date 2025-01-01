#!/bin/python
import utils.matrix_utils as matrix_utils
import sys
import json


matrix_utils.init_pg()

limit = 16
if len(sys.argv) >= 1:
    limit = int(sys.argv[1]) 
    

res_redact_events = matrix_utils.get_all_events_matching(f"type='m.room.redaction' order by origin_server_ts desc limit {limit}")
events_final = []
for ev in res_redact_events:
    print(ev)
    events_final.append(ev)
print("RAW JSON:")
print()

print("\n\n\n")
print("MESSAGE:")
print(json.loads(res)["content"]["body"])
 