import utils.matrix_utils as matrix_utils
import sys


matrix_utils.init_pg()



res1 = matrix_utils.get_rooms_with_user(sys.argv[1])
res2 = matrix_utils.get_rooms_with_user(sys.argv[2])

for k in res1[0]:
    if k in res2[0]:
        print(k, matrix_utils.get_room_name_by_id(k))



