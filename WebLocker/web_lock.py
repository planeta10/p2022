import time
from datetime import datetime

#start_time = datetime(datetime.now().year, datetime.now().month, datetime.now().day, 9)
#finish_time = datetime(datetime.now().year, datetime.now().month, datetime.now().day, 20, 15)

#print(start_time)
#print(finish_time)

hosts = r'C:\Windows\System32\drivers\etc\hosts'
# hosts = '/etc/hosts'
redirect_url = '127.0.0.1'

blocked_sites = ['www.youtube.com', 'youtube.com', 'www.vk.com', 'vk.com']

while True:
    print('if')
    if 0<= int(datetime.now().strftime('%M'))<30:
        print('Доступ ограничен!')
        
        with open(hosts, 'r+') as file:
            src = file.read()
            
            for site in blocked_sites:
                if site in src:
                    pass
                else:
                    file.write(f'{redirect_url} {site}\n')
    elif 30<= int(datetime.now().strftime('%M'))<=59:
        with open(hosts, 'r+') as file:
            src = file.readlines()
            file.seek(0)
            
            for line in src:
                if not any(site in line for site in blocked_sites):
                    file.write(line)
            file.truncate()
        print('Доступ открыт!')
        
    time.sleep(10)
