import os
import requests
import json

api_key = "95e134ba19d34425951637f22a62fdda"
base_url = "https://iapp.openai.azure.com/"
deployment_name ="iapp"

url = base_url + "/openai/deployments/" + deployment_name + "/completions?api-version=2022-12-01"
print(url)
prompt = "Once upon a time"
payload = {        
    "prompt":prompt
    }

r = requests.post(url, 
      headers={
        "api-key": api_key,
        "Content-Type": "application/json"
      },
      json = payload
    )

response = json.loads(r.text)
formatted_response = json.dumps(response, indent=4)

print(formatted_response)