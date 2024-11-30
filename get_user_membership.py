import utils.matrix_utils as matrix_utils
import sys


matrix_utils.init_pg()



res = matrix_utils.get_rooms_with_user(sys.argv[1])

for k in res[0]:
    print(k, matrix_utils.get_room_name_by_id(k))



