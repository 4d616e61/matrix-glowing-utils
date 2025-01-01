import utils.matrix_utils as matrix_utils
import sys
import json

matrix_utils.init_pg()


#example: "sender='@tete:pettan.cc' and type='m.room.message'" "json like '%https://e_hentai.org%'"
res = matrix_utils.get_all_events_matching(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else "")

for v in res:
    #print("MESSAGE:")
    try:
        print(json.loads(v[0])["content"]["body"])
    except:
        pass



