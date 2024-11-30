import requests
import cfg
import sys
import urllib

endpoint = f"{cfg.base}/_synapse/admin/v1/reset_password/{urllib.parse.quote_plus(input('Enter username: '))}"
payload_json = {
    "new_password": input("Enter new password: ")
}
res = requests.post(endpoint, headers=cfg.auth_header, json=payload_json)
print(res.status_code)
print(res.content)
