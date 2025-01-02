import hashlib
import sys
import json
import traceback

def get_hash(string : str) -> str:
    return hashlib.sha256(string.encode()).hexdigest()

def hash_string_to_int(string) -> str:
    int_value = int(get_hash(string), 16)
    return str(abs(int_value))

def hash_string_truncated(string : str, chars = 16):
    return get_hash(string)[:chars]




def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def __fmt_media(sender, content):
    res = sender + ": \n"
    res += f"Image: {content["url"]}"  
    if "body" in content.keys():
        res += "\n" + body
    return res

def __fmt_text(sender, content):
    #silently drop event if missing body
    if not "body" in content.keys():
        return None
    body_nofmt = content["body"]
    #do 2 checks
    is_reply = "m.relates_to" in content.keys()
    if is_reply:
        is_reply = "m.in_reply_to" in content["m.relates_to"].keys()
    
    if is_reply:
        try:
            res = sender + ": "
            #assumption about formatting isnt necessarily correct
            body_pieces = body_nofmt.split("\n\n")
            res += f"\n  Replying to \"{body_pieces[0]}\":\n{body_pieces[1]}"
            return res;
        except:
            #silently fall back for now, idrc
            pass
    res = sender + ": "
    res += body_nofmt
    return res


def __internal_fmt_event(sender, content, msgtype) -> str:
    if msgtype == "m.image":
        return __fmt_media(sender, content)
    return __fmt_text(sender, content)



def format_event_json(event_json_data : str):
    try:
        event = json.loads(event_json_data)
        sender = event["sender"]
        content = event["content"]
        msgtype = content["msgtype"]
        return __internal_fmt_event(sender, content, msgtype)
    except Exception as e:
        eprint(f"{traceback.format_exc()} encountered while processing {event_json_data}")
    
def json_reserialize(event_json_data : str):
    return json.dumps(json.loads(event_json_data), indent=4)