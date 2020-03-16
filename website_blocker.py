import time
# importing datetime and setting it as variable dt
from datetime import datetime as dt

import pandas
# Host path 
host_path = '/etc/hosts'

host_temp = 'hosts'
# Redirection to disabled page
redirect = '127.0.0.1'
# A list of websites which I want to block
websites_list = ['www.facebook.com', 'facebook.com']

while True: 
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 17):
        print('Blah Blah Blah ')

        with open(host_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in websites_list):
                    file.write(line)
            file.truncate()
            print(content)


    else: 
        print('Currently in working hours...')

        with open(host_path, 'r+') as file:
            content = file.read()
            for website in websites_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + '\t' + website + '\n')


    # using a time import to allow the script to sleep for 5 seconds - allowing for memory efficiency 
    time.sleep(5)

# I need to direct to path 
# Input password 
# Activate ç