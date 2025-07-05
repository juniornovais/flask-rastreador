
#ip local

import socket

ip_local = socket.gethostbyname(socket.gethostname())
print(f'IP Local: {ip_local}')

#ip público 
import requests

ip_publico = requests.get('https://api.ipify.org').text
print(f'IP Público: {ip_publico}')

#Enviar esse IP pra um serviço que retorna a localização

