import requests
import json
ip = requests.get('https://api.ipify.org').text

dados = requests.get(f'https://ipinfo.io/{ip}/json').json()
print(f'IP: {dados['ip']}')
print(json.dumps(dados, indent=4, ensure_ascii=False))

