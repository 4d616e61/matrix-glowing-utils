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

def format_event_json(event_json_data : str):
    try:
        return json.loads(event_json_data)
    except:
        eprint(f"Format error encountered while processing {event_json_data}")
    