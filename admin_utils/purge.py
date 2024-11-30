import cfg
import requests



endpoint = f"{cfg.base}/_synapse/admin/v1/rooms/"
def purge(room_id : str):
  print(f"purging {room_id}")
  payload_json = {
  #    "room_id": room_id
  }
  res = requests.delete(endpoint + room_id, headers=cfg.auth_header, json=payload_json)
  print(res.status_code)
  print(res.content)


while True:
  roomid = input()
  roomid.replace(" ", "")
  purge(roomid)
