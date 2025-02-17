import utils.postgres_query as postgres_query
import utils.misc as misc




def init_pg():
    postgres_query.init("synapse")



def get_event(event_id : str):
    return postgres_query.query(f"select json from event_json where event_id = '{event_id}'")[0][0]


#deprecated(kind of)
def get_room_name_by_id(room_id : str):
    res = postgres_query.query(f"select name from room_stats_state where room_id = '{room_id}'")
    if res[0][0] == None:
        return "Unnamed room_" + misc.hash_string_truncated(room_id)
    return res[0][0]

def get_room_info_by_id(room_id : str):
    res = postgres_query.query(f"select name, canonical_alias, topic, join_rules from room_stats_state where room_id = '{room_id}'")
    assert(len(res) == 1)
    res_e = res[0]

    name = res_e[0]
    alias = res_e[1]
    topic = res_e[2]
    join_rules = res_e[3]
    roomid_hash = misc.hash_string_truncated(room_id)
    if name == None:
        name = "Unnamed room_" + roomid_hash
    if alias == None:
        alias = "#no-alias-" + roomid_hash + ":example.com"
    if topic == None:
        topic = ""

    return {
        "name" : name,
        "alias" : alias,
        "topic" : topic,
        "join_rules" : join_rules
        
    }

def get_user_tokens(user_id : str):
    return postgres_query.query(f"select token from access_tokens where user_id = '{user_id}'")

def get_memberships_by_user_id(user_id : str):
    return postgres_query.query(f"select user_id, room_id, membership, event_stream_ordering from room_memberships where user_id = '{user_id}'")


def get_memberships_by_room_id(room_id : str):
    return  postgres_query.query(f"select user_id, room_id, membership, event_stream_ordering from room_memberships where room_id = '{room_id}'")


def get_rooms_with_user(user_id : str):
    rooms = {}
    res = get_memberships_by_user_id(user_id)
    res.sort(key=lambda tup : tup[3])
    for entry in res:
    #roomid -> latest state
        rooms[entry[1]] = entry[2]
    joins = []
    for k, v in rooms.items():
        if v != "join":
            continue
        joins.append(k)
    return (joins,rooms)



def get_all_events_matching(events_cond = "", events_json_cond = ""):
    if len(events_cond) != 0:
        events_cond = "where " + events_cond
    if len(events_json_cond) != 0:
        events_json_cond = "and " + events_json_cond
    inner = f"with eid as (select event_id from events {events_cond})"
    outer = f"select json, event_id from event_json where event_id = ANY (select event_id from eid) {events_json_cond}"
    return postgres_query.query(inner + outer)