import utils.matrix_utils as matrix_utils
import sys
import json
from utils.misc import *
matrix_utils.init_pg()


#example: "sender='@tete:pettan.cc' and type='m.room.message'" "json like '%https://e_hentai.org%'"
res = matrix_utils.get_all_events_matching(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else "")

for v in res:
    #print("MESSAGE:")
    json_data = v[0]
    dat = format_event_json(json_data)
    if dat == None:
        continue
    print(dat)
    
    



