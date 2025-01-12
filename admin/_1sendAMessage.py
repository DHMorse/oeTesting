import random
import asyncio
import requests
import traceback

from globalVars import MY_USER_ID, MY_USER_NAME, tests

from helperFunctions import writeExepctoinToLogFile

async def send_a_message(TESTING_CHANNEL):
    async with TESTING_CHANNEL.typing():
        await asyncio.sleep(random.randint(1, 5))
        await TESTING_CHANNEL.send('69')

    await asyncio.sleep(3)

    response = requests.get(f'http://45.79.203.11:5001/users?userId={MY_USER_ID}')

    try:
        responseData = response.json()[0]
    except Exception as e:
        await writeExepctoinToLogFile(e, traceback.format_exc())

    try:
        tests.append({'passed': responseData['daysLoggedInInARow'] == 0, 
                        'expectedResult': 0, 
                        'actualResult': responseData['daysLoggedInInARow'], 
                        'test': 'daysLoggedInInARow After First Message'})
    except Exception as e:
        tests.append({'passed': False, 'expectedResult': 0, 'actualResult': f'Exception: {e}', 'test': 'daysLoggedInInARow After First Message'})

    try:
        tests.append({'passed': responseData['lastLogin'] == None, 
                        'expectedResult': None, 
                        'actualResult': responseData['lastLogin'], 
                        'test': 'lastLogin After First Message'})
    except Exception as e:
        tests.append({'passed': False, 'expectedResult': None, 'actualResult': f'Exception: {e}', 'test': 'lastLogin After First Message'})

    try:
        tests.append({'passed': responseData['money'] == 0, 
                        'expectedResult': 0, 
                        'actualResult': responseData['money'], 
                        'test': 'money After First Message'})
    except Exception as e:
        tests.append({'passed': False, 'expectedResult': 0, 'actualResult': f'Exception: {e}', 'test': 'money After First Message'})

    try:
        tests.append({'passed': responseData['userId'] == MY_USER_ID, 
                        'expectedResult': MY_USER_ID, 
                        'actualResult': responseData['userId'], 
                        'test': 'userId After First Message'})
    except Exception as e:
        tests.append({'passed': False, 'expectedResult': MY_USER_ID, 'actualResult': f'Exception: {e}', 'test': 'userId After First Message'})

    try:
        tests.append({'passed': responseData['username'] == MY_USER_NAME, 
                        'expectedResult': MY_USER_NAME, 
                        'actualResult': responseData['username'], 
                        'test': 'username After First Message'})
    except Exception as e:
        tests.append({'passed': False, 'expectedResult': MY_USER_NAME, 'actualResult': f'Exception: {e}', 'test': 'username After First Message'})

    try:
        tests.append({'passed': responseData['xp'] == 1, 
                        'expectedResult': 1, 
                        'actualResult': responseData['xp'], 
                        'test': 'xp After First Message'})
    except Exception as e:
        tests.append({'passed': False, 'expectedResult': 1, 'actualResult': f'Exception: {e}', 'test': 'xp  After First Message'})