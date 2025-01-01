import hashlib
import sys
import json

def get_hash(string : str) -> str:
    return hashlib.sha256(string.encode()).hexdigest()

def hash_string_to_int(string) -> str:
    int_value = int(get_hash(string), 16)
    return str(abs(int_value))

def hash_string_truncated(string : str, chars = 16):
    return get_hash(string)[:chars]




def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)



def __internal_fmt_event(sender, content) -> str:
    #silently drop event if missing body
    if not "body" in content.keys():
        return None
    body_nofmt = content["body"]
    #do 2 checks
    is_reply = "m.relates_to" in content.keys()
    if is_reply:
        is_reply = "m.in_reply_to" in content["m.relates_to"].keys()
    res = sender + ": "
    if is_reply:
        #assumption about formatting isnt necessarily correct
        body_pieces = body.split("\n\n")
        res += f"  Replying to {body_pieces[0]}:\n{body_pieces[1]}"
    else:
        res += body
    return res



def format_event_json(event_json_data : str):
    try:
        event = json.loads(event_json_data)
        sender = event["sender"]
        content = event["content"]
        return __internal_fmt_event(sender, content)
    except Exception as e:
        eprint(f"{e.with_traceback} encountered while processing {event_json_data}")
    