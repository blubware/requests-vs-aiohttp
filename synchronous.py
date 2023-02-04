import requests
import time

token = input('Token: ')
server = input('Server: ')

headers = {'authorization': token, 
'content-type': 'application/json'}

cc_url = f'https://discord.com/api/v9/guilds/{server}/channels'
payload = {'type': 0, 'name': 'tears', 'permission_overwrites': []}

def main():
    st = time.time()
    complete = 0
    while 10 > complete:
        cc = requests.post(cc_url, headers=headers, json=payload)
        match cc.status_code:
            case 201:
                print(f'Complete {complete}/10 requests')
                complete +=1

    et = time.time()
    elapsed_time = et - st
    print('Execution time:', elapsed_time, 'seconds')

main()