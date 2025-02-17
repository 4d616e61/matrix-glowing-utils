import utils.matrix_utils as matrix_utils
import utils.misc as misc
import sys
import json
import pytz
from datetime import datetime

#change if u care(i dont)
tz = pytz.timezone('America/Los_Angeles')




def get_channel_name(room_id : str):
    return matrix_utils.get_room_name_by_id(room_id)
def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def gen_ts(unixtime) -> str:
    #divide might be not performant or whatever 
    return datetime.fromtimestamp(unixtime / 1000, tz).isoformat()
 

def format_author(orig_author : str) -> str:
    return orig_author.replace(":", "_")
def convert_entry(inp : dict) -> dict:
    sender = inp["sender"]
    #idk if this works, but i hope it does
    sender_uid = misc.hash_string_truncated(sender, 32)
    msg_id = int(misc.hash_string_truncated(inp["event_id"], 32), 16)
    res = {
        "id" : msg_id,
        "type" : "Default",
        "timestamp" : gen_ts(inp["origin_server_ts"]),
        "timestampEdited": None,
        "callEndedTimestamp": None,
        "isPinned": None,
        "content": inp["content"]["body"] 
        if "body" in inp["content"].keys() 
        else "",
        "author": {
            "id": sender_uid,
            "name": sender,
            "discriminator": "0000",
            "nickname": sender,
            "color": None,
            "isBot": False,
            "roles": [],
            "avatarUrl": "https://example.com"
        },
        "attachments": [],
        "embeds": [],
        "stickers": [],
        "reactions": [],
        "mentions": []
    }

    
    return res

def dump_room(roomid):
    res_pg = matrix_utils.get_all_events_matching(f"room_id='{roomid}' and type = 'm.room.message'")


    res_parsed = []
    for v in res_pg:
        obj = json.loads(v[0])
        obj["event_id"] = v[1]
        res_parsed.append(obj)

    res_parsed.sort(key= lambda d : d["origin_server_ts"])

    final_dict = {}

    final_dict["guild"] = {
        "id": "42690",
        "name": "room",
        "iconUrl": "https://example.com"
    }
    final_dict["channel"] = {
        "id": misc.hash_string_truncated(roomid, 32),
        "type": "GuildTextChat",
        "categoryId": "420",
        "category": "channels",
        "name": get_channel_name(roomid),
        "topic": None
    }
    final_dict["daterange"] = {
        "after": None,
        "before": None
    }
    final_dict["exportedAt"] = gen_ts(res_parsed[0]["origin_server_ts"])
    final_dict["messageCount"] = len(res_parsed)
    res_events = []
    eprint("Converting... ")
    for v in res_parsed:
        #eprint(v)
        res_events.append(convert_entry(v))


    final_dict["messages"] = res_events

    return json.dumps(final_dict)
def main():
    matrix_utils.init_pg()
    if len(sys.argv) <= 1:
        return

    for roomid in sys.argv[1:]:
        res = dump_room(roomid)
        with open(roomid + ".json", "w+") as f:
            f.write(res)





if __name__ == "__main__":
    main()