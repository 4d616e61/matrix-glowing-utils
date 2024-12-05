import utils.matrix_utils as matrix_utils
import sys
import json
import pytz
from datetime import datetime

#change if u care(i dont)
tz = pytz.timezone('America/Los_Angeles')


import hashlib

def hash_string_to_int(string):
    # Create a hash object (SHA-256 is a good choice)
    hash_object = hashlib.sha256(string.encode())

    # Get the hexadecimal representation of the hash
    hex_digest = hash_object.hexdigest()

    # Convert the hexadecimal representation to an integer
    int_value = int(hex_digest, 16)

    # Return the absolute value to ensure a positive integer
    return abs(int_value)

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def gen_ts(unixtime) -> str:
    #divide might be not performant or whatever 
    return datetime.fromtimestamp(unixtime / 1000, tz).isoformat()
 

def convert_entry(inp : dict) -> dict:
    res = {
        #no ones gonna know...
        "id" : inp["origin_server_ts"],
        "type" : "Default",
        "timestamp" : gen_ts(inp["origin_server_ts"]),
        "timestampEdited": None,
        "callEndedTimestamp": None,
        "isPinned": None,
        "content": inp["content"]["body"],
        "author": {
            "id": str(hash_string_to_int(inp["sender"]))[:32],
            "name": inp["sender"],
            "discriminator": "0000",
            "nickname": inp["sender"],
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

def main():
    matrix_utils.init_pg()
    res_pg = matrix_utils.get_all_events_matching(f"room_id='{sys.argv[1]}' and type = 'm.room.message'")


    res_parsed = []
    for v in res_pg:
        res_parsed.append(json.loads(v[0]))

    res_parsed.sort(key= lambda d : d["origin_server_ts"])

    final_dict = {}

    final_dict["guild"] = {
        "id": "42690",
        "name": "room",
        "iconUrl": "https://example.com"
    }
    final_dict["channel"] = {
        "id": "1337",
        "type": "GuildTextChat",
        "categoryId": "420",
        "category": "channels",
        "name": "general",
        "topic": None
    }
    final_dict["daterange"] = {
        "after": None,
        "before": None
    }
    final_dict["exportedAt"] = gen_ts(0)
    final_dict["messageCount"] = len(res_parsed)
    res_events = []
    eprint("Converting... ")
    for v in res_parsed:
        #eprint(v)
        res_events.append(convert_entry(v))


    final_dict["messages"] = res_events

    print(json.dumps(final_dict))





if __name__ == "__main__":
    main()