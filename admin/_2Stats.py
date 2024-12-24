import random
import asyncio

from globalVars import MY_USER_NAME, tests

async def _2checkStats(TESTING_CHANNEL):
    async with TESTING_CHANNEL.typing():
        await asyncio.sleep(random.randint(1, 5))
        await TESTING_CHANNEL.send('!stats')
    
    await asyncio.sleep(3)

    async for message in TESTING_CHANNEL.history(limit=1):
        try:
            tests.append({'passed': message.content == f'''{MY_USER_NAME}\'s Stats:
```ansi
[0;34mXp: 2
[0;34mLevel: 0
[0;36mMoney: $0
[0;36mLast Login (Seconds Since Epoch): None
[0;34mLast Login (UTC): None
[0;34mLast Login (CST): None
[0;34mLast Login (EST): None
[0;36mDays Logged In In A Row: 0
```''', 
                            'expectedResult': f'''{MY_USER_NAME}\'s Stats:
```ansi
[0;34mXp: 2
[0;34mLevel: 0
[0;36mMoney: $0
[0;36mLast Login (Seconds Since Epoch): None
[0;34mLast Login (UTC): None
[0;34mLast Login (CST): None
[0;34mLast Login (EST): None
[0;36mDays Logged In In A Row: 0
```''', 
                            'actualResult': message.content, 
                            'test': 'stats Command After First Message'})
        except Exception as e:
            tests.append({'passed': False, 'expectedResult': f'''{MY_USER_NAME}\'s Stats:
```ansi
[0;34mXp: 2
[0;34mLevel: 0
[0;36mMoney: $0
[0;36mLast Login (Seconds Since Epoch): None
[0;34mLast Login (UTC): None
[0;34mLast Login (CST): None
[0;34mLast Login (EST): None
[0;36mDays Logged In In A Row: 0
```''' , 'actualResult': f'Exception: {e}', 'test': 'stats Command After First Message'})
            
    await asyncio.sleep(3)

    # Checks there is a json file send called {MY_USER_NAME}_items.json with a empty list in it
    try:
        tests.append({'passed': message.attachments[0].to_dict()['filename'] == f'{MY_USER_NAME}_items.json', 
                        'expectedResult': f'{MY_USER_NAME}_items.json', 
                        'actualResult': message.attachments[0].to_dict()['filename'], 
                        'test': 'stats Command Items After First stats Filename'})
    except Exception as e:
        tests.append({'passed': False, 
                        'expectedResult': f'{MY_USER_NAME}_items.json', 
                        'actualResult': f'Exception: {e}', 
                        'test': 'stats Command Items After First stats Filename'})
        
    try:
        tests.append({'passed': message.attachments[0].to_dict()['size'] == 2, 
                        'expectedResult': 2, 
                        'actualResult': message.attachments[0].to_dict()['size'], 
                        'test': 'stats Command Items After First stats Size'})
    except Exception as e:
        tests.append({'passed': False, 
                        'expectedResult': 2, 
                        'actualResult': f'Exception: {e}', 
                        'test': 'stats Command Items After First stats Size'})
        
    try:
        tests.append({'passed': message.attachments[0].to_dict()['content_type'] == 'application/json; charset=utf-8',
                        'expectedResult': 'application/json; charset=utf-8',
                        'actualResult': message.attachments[0].to_dict()['content_type'],
                        'test': 'stats Command Items After First stats Content Type'})
    except Exception as e:
        tests.append({'passed': False,
                        'expectedResult': 'application/json; charset=utf-8',
                        'actualResult': f'Exception: {e}',
                        'test': 'stats Command Items After First stats Content Type'})