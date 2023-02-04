import aiohttp
import asyncio
import time

token = input('Token: ')
server = input('Server: ')

headers = {'authorization': token, 
'content-type': 'application/json'}

cc_url = f'https://discord.com/api/v9/guilds/{server}/channels'
payload = {'type': 0, 'name': 'tears', 'permission_overwrites': []}

async def main():
    async with aiohttp.ClientSession() as session:
        st = time.time()
        complete = 0
        while 10 > complete:
            async with session.post(cc_url, headers=headers, json=payload) as cc:
                match cc.status:
                    case 201:
                        print(f'Complete {complete}/10 requests')
                        complete +=1

        et = time.time()
        elapsed_time = et - st
        print('Execution time:', elapsed_time, 'seconds')

asyncio.run(main())