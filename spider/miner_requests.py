import requests
import json

from credentials import GITHUB_TOKEN

query = 'Apache SkyWalking'

def scrape(base_url, type:str, args):
  
  target = f'{base_url}code?q={query} {args}'
  print(target)
  headers = {
    'Authorization': f'Token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3.text-match+json',
  }
  response = requests.request('GET', target, headers=headers).text
  parsed = json.loads(response)
  print(length:=json.dumps(parsed, indent=4, sort_keys=True))
  print(f'total length = {len(length)}')

  return parsed