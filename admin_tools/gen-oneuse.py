import requests
import cfg



endpoint = f"{cfg.base}/_synapse/admin/v1/registration_tokens/new"
payload_json = {
    "uses_allowed": 1
}
res = requests.post(endpoint, headers=cfg.auth_header, json=payload_json)
print(res.status_code)
print(res.content)
