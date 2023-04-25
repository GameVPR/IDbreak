import requests
from subprocess import Popen, PIPE, check_output
import datetime
from os import getenv, system
import cpuinfo
import gpustat


# ----------------------------------------------------------------------- #

disk = check_output('wmic diskdrive get caption').decode().split('\n')[1].strip()
system('title IDbreak V0.2')
response = requests.get('https://ipinfo.io/json')
data = response.json()
idbver = "V0.1"
uuid = Popen('wmic csproduct get uuid', stdin=PIPE, stdout=PIPE, stderr=PIPE)
t1 = datetime.datetime.now()
d1 = datetime.date.today()
time = t1.strftime("%H:%M:%S")
cname = getenv('COMPUTERNAME')
uname = getenv('USERNAME')
c = cpuinfo.get_cpu_info()
cpu = c['brand_raw']
gpu_stats = gpustat.GPUStatCollection.new_query()
gpu = gpu_stats.gpus[0].name

# ----------------------------------------------------------------------- #

output_uuid, error_uuid = uuid.communicate()
uuid = output_uuid.decode().strip().split('\n')[1].strip()
    
# ----------------------------------------------------------------------- #


if 'error' in data:
    print(f"Error: {data['message']}")
else:
    ip = data['ip']
    country = data['country']
    city = data['city']
    reg = data['region']
    org = data['org']
    loc = data['loc']
    pos = data['postal']
    tzo = data['timezone']

    with open('u.id', 'w') as f:
        f.write(f'~----- IDbreak {idbver} -----~\n')
        f.write(f'\n#--INFORMATION--#\n')
        f.write(f'IP Address: {ip}\n')
        f.write(f'Address: {pos} | {city}, {reg}, {country} ({loc})\n')
        f.write(f'Organisation: {org}\n')
        f.write(f'Time: {d1}, {time} ({tzo})\n')
        f.write(f'\n#--MACHINE--#\n')
        f.write(f'UUID: {uuid}\n')
        f.write(f'Computer Name: {cname}\n')
        f.write(f'User Name: {uname}\n')
        f.write(f'CPU: {cpu}\n')
        f.write(f'GPU: {gpu}\n')
        f.write(f'Storage: {disk}\n')

    print("Information saved to u.id")
