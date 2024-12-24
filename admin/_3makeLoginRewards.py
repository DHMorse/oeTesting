import asyncio
import random

from globalVars import tests

async def makeLoginRewards(TESTING_CHANNEL):
    async with TESTING_CHANNEL.typing():
        await asyncio.sleep(random.randint(5, 15))
        await TESTING_CHANNEL.send('!makeloginrewards')

    await asyncio.sleep(3)

    async for message in TESTING_CHANNEL.history(limit=1):
        try:
            tests.append({'passed': message.content == '''```ansi
[1;31mPlease provide the number of levels for which to create login rewards.[0m
```''', 
                            'expectedResult': '''```ansi
[1;31mPlease provide the number of levels for which to create login rewards.[0m
```''', 
                            'actualResult': message.content, 
                            'test': 'Make Login Rewards Command'})
        except Exception as e:
            tests.append({'passed': False, 
                            'expectedResult': '''```ansi
[1;31mPlease provide the number of levels for which to create login rewards.[0m
```''', 
                            'actualResult': f'Exception: {e}', 
                            'test': 'Make Login Rewards Command'})
            
    await asyncio.sleep(3)

    async with TESTING_CHANNEL.typing():
        await asyncio.sleep(random.randint(5, 15))
        await TESTING_CHANNEL.send('!makeloginrewards 300')

    await asyncio.sleep(3)

    async for message in TESTING_CHANNEL.history(limit=1):
        try:
            tests.append({'passed': message.content == '```ansi\n[1;34mLogin rewards for 300 levels have been successfully created.[0m\n```', 
                            'expectedResult': '```ansi\n[1;34mLogin rewards for 300 levels have been successfully created.[0m\n```', 
                            'actualResult': message.content, 
                            'test': 'Make Login Rewards Command'})
        except Exception as e:
            tests.append({'passed': False, 
                            'expectedResult': '```ansi\n[1;34mLogin rewards for 300 levels have been successfully created.[0m\n```', 
                            'actualResult': f'Exception: {e}', 
                            'test': 'Make Login Rewards Command'})