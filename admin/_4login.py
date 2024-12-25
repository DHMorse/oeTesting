import asyncio
import random
import traceback
import requests
import time
import pytz
import os

from globalVars import MY_USER_ID, MY_USER_NAME, tests
from globalVars import writeExepctoinToLogFile, testStatsCommand, testIfHaveRole, testLoginMessage

async def login(TESTING_CHANNEL, LOG_CHANNEL, OUR_MEMBER):
    async with TESTING_CHANNEL.typing():
        await asyncio.sleep(random.randint(3, 10))
        await TESTING_CHANNEL.send('!login')
    
    await asyncio.sleep(6)
    
    # Get the last two messages in the testing channel
    # and check if they are the expected messages
    index: int = 0
    async for message in TESTING_CHANNEL.history(limit=2):
        if index == 0:
            index += 1
            try:
                tests.append({'passed': message.content == 'Congratulations! You have received 10 XP for logging in 1 days in a row!', 
                                    'expectedResult': 'Congratulations! You have received 10 XP for logging in 1 days in a row!', 
                                    'actualResult': message.content, 
                                    'test': 'login message 0 After First Login'})
            except Exception as e:
                tests.append({'passed': False, 
                                'expectedResult': 'Congratulations! You have received 10 XP for logging in 1 days in a row!', 
                                'actualResult': f'Exception: {e}', 
                                'test': 'login message 0 After First Login'})
        else:
            try:
                tests.append({'passed': message.content == 'You have made your first daily login!', 
                                    'expectedResult': 'You have made your first daily login!', 
                                    'actualResult': message.content, 
                                    'test': 'login message 1 After First Login'})
            except Exception as e:
                tests.append({'passed': False,
                                'expectedResult': 'You have made your first daily login!',
                                'actualResult': f'Exception: {e}',
                                'test': 'login message 1 After First Login'})

    await asyncio.sleep(3)

    # Get the last message in the log channel
    # and check if the embed is the expected embed
    async for message in LOG_CHANNEL.history(limit=1):
        try:
            tests.append({'passed': message.embeds[0].to_dict()['description'] == '**Member:** \njohn5971\n\n**Account Level:** \n1', 
                            'expectedResult': '**Member:** \njohn5971\n\n**Account Level:** \n1', 
                            'actualResult': message.embeds[0].to_dict()['description'], 
                            'test': 'Level Up Embed Description After First Login'})
        except Exception as e:
            tests.append({'passed': False,
                            'expectedResult': '**Member:** \njohn5971\n\n**Account Level:** \n1',
                            'actualResult': f'Exception: {e}',
                            'test': 'Level Up Embed Description After First Login'})
        
        try:
            tests.append({'passed': message.embeds[0].to_dict()['title'] == 'Member Leveled Up', 
                        'expectedResult': 'Member Leveled Up', 
                        'actualResult': message.embeds[0].to_dict()['title'], 
                        'test': 'Level Up Embed Title After First Login'})
        except Exception as e:
            tests.append({'passed': False,
                            'expectedResult': 'Member Leveled Up',
                            'actualResult': f'Exception: {e}',
                            'test': 'Level Up Embed Title After First Login'})

    await asyncio.sleep(3)

    # Check if the user was given the role `Level 1`
    try:
        WeHaveRoleLevel1 = False
        for role in OUR_MEMBER.roles:
            if role.name == 'Level 1':
                WeHaveRoleLevel1 = True
                break
        try:
            tests.append({'passed': WeHaveRoleLevel1, 
                            'expectedResult': 'We\'d have the role `Level 1`', 
                            'actualResult': [role.name for role in OUR_MEMBER.roles], 
                            'test': 'Got Role `Level 1` After Leveling Up After First Login'})
        except Exception as e:
            tests.append({'passed': False,
                            'expectedResult': 'We\'d have the role `Level 1`',
                            'actualResult': f'Exception: {e}',
                            'test': 'Got Role `Level 1` After Leveling Up After First Login'})
    except Exception as e:
        await writeExepctoinToLogFile(e, traceback.format_exc())

    await asyncio.sleep(3)

    # Check the database to see if the user's stats were updated correctly
    response = requests.get(f'http://45.79.203.11:5001/users?userId={MY_USER_ID}')
    
    try:
        responseData = response.json()[0]
    except Exception as e:
        await writeExepctoinToLogFile(e, traceback.format_exc())

    try:    
        tests.append({'passed': responseData['daysLoggedInInARow'] == 1, 
                        'expectedResult': 1, 
                        'actualResult': responseData['daysLoggedInInARow'], 
                        'test': 'daysLoggedInInARow After First Login'})
    except Exception as e:
        tests.append({'passed': False, 'expectedResult': 1, 'actualResult': f'Exception: {e}', 'test': 'daysLoggedInInARow After First Login'})
    
    try:
        tests.append({'passed': responseData['lastLogin'] is not None, 
                        'expectedResult': not None, 
                        'actualResult': responseData['lastLogin'], 
                        'test': 'lastLogin After First Login'})
    except Exception as e:
        tests.append({'passed': False, 'expectedResult': not None, 'actualResult': f'Exception: {e}', 'test': 'lastLogin After First Login'})
    
    try:
        tests.append({'passed': responseData['money'] == 0, 
                        'expectedResult': 0, 
                        'actualResult': responseData['money'], 
                        'test': 'money After First Login'})
    except Exception as e:
        tests.append({'passed': False, 'expectedResult': 0, 'actualResult': f'Exception: {e}', 'test': 'money After First Login'})

    try:
        tests.append({'passed': responseData['userId'] == MY_USER_ID, 
                        'expectedResult': MY_USER_ID, 
                        'actualResult': responseData['userId'], 
                        'test': 'userId After First Login'})
    except Exception as e:
        tests.append({'passed': False, 'expectedResult': MY_USER_ID, 'actualResult': f'Exception: {e}', 'test': 'userId After First Login'})
    
    try:
        tests.append({'passed': responseData['username'] == MY_USER_NAME, 
                        'expectedResult': MY_USER_NAME, 
                        'actualResult': responseData['username'], 
                        'test': 'username After First Login'})
    except Exception as e:
        tests.append({'passed': False, 'expectedResult': MY_USER_NAME, 'actualResult': f'Exception {e}', 'test': 'username After First Login'})

    try:
        tests.append({'passed': responseData['xp'] == 15, 
                        'expectedResult': 15, 
                        'actualResult': responseData['xp'], 
                        'test': 'xp After First Login'})
    except Exception as e:
        tests.append({'passed': False, 'expectedResult': 15, 'actualResult': f'Exception: {e}', 'test': 'xp After First Login'})

    await asyncio.sleep(3)

    await testStatsCommand(TESTING_CHANNEL, xp=16, level=1, money=0, lastLogin=responseData['lastLogin'], daysLoggedInInARow=1, 
                            testContext='First Login')

    # Checks there is a json file send called {MY_USER_NAME}_items.json with a empty list in it
    # this needs to be updated and put in the checkStatsCommand function
    # but the generateCard command needs to be updated first
    try:
        tests.append({'passed': message.attachments[0].to_dict()['filename'] == f'{MY_USER_NAME}_items.json', 
                        'expectedResult': f'{MY_USER_NAME}_items.json', 
                        'actualResult': message.attachments[0].to_dict()['filename'], 
                        'test': 'stats Command Items After First Login Filename'})
    except Exception as e:
        tests.append({'passed': False, 
                        'expectedResult': f'{MY_USER_NAME}_items.json', 
                        'actualResult': f'Exception: {e}', 
                        'test': 'stats Command Items After First Login Filename'})
        
    try:
        tests.append({'passed': message.attachments[0].to_dict()['size'] == 2, 
                        'expectedResult': 2, 
                        'actualResult': message.attachments[0].to_dict()['size'], 
                        'test': 'stats Command Items After First Login Size'})
    except Exception as e:
        tests.append({'passed': False, 
                        'expectedResult': 2, 
                        'actualResult': f'Exception: {e}', 
                        'test': 'stats Command Items After First Login Size'})
        
    try:
        tests.append({'passed': message.attachments[0].to_dict()['content_type'] == 'application/json; charset=utf-8',
                        'expectedResult': 'application/json; charset=utf-8',
                        'actualResult': message.attachments[0].to_dict()['content_type'],
                        'test': 'stats Command Items After First Login Content Type'})
    except Exception as e:
        tests.append({'passed': False,
                        'expectedResult': 'application/json; charset=utf-8',
                        'actualResult': f'Exception: {e}',
                        'test': 'stats Command Items After First Login Content Type'})

    await asyncio.sleep(3)

    async with TESTING_CHANNEL.typing():
        await asyncio.sleep(random.randint(3, 10))
        await TESTING_CHANNEL.send('!login')
    
    await asyncio.sleep(3)
    
    async for message in TESTING_CHANNEL.history(limit=1):
        try:
            tests.append({'passed': message.content == 'You have already logged in today!', 
                                'expectedResult': 'You have already logged in today!', 
                                'actualResult': message.content, 
                                'test': 'login message after first login'})
        except Exception as e:
            tests.append({'passed': False, 
                            'expectedResult': 'You have already logged in today!', 
                            'actualResult': f'Exception: {e}', 
                            'test': 'login message after first login'})

    # Login 2
    await asyncio.sleep(3)

    async with TESTING_CHANNEL.typing():
        await asyncio.sleep(random.randint(3, 10))
        await TESTING_CHANNEL.send('!login 1.1')

    # Check if the user was given the role `Level 2`
    await testIfHaveRole(OUR_MEMBER, roleName='Level 2', testContext='Second Login')

    # Check to see if the messages are the expected messages
    await testLoginMessage(TESTING_CHANNEL, xp=30, daysLoggedInInARow=2, testContext='Second Login')

    # login 3
    await asyncio.sleep(3)

    async with TESTING_CHANNEL.typing():
        await asyncio.sleep(random.randint(3, 10))
        await TESTING_CHANNEL.send('!login 1.1')

    await testIfHaveRole(OUR_MEMBER, roleName='', testContext='Third Login', roleList=['Level 3', 'Level 4', 'Level 5', 'Level 6', 
                                                                                        'Level 7', 'Level 8', 'Level 9'])

    await testLoginMessage(TESTING_CHANNEL, xp=97, daysLoggedInInARow=3, testContext='Third Login')

    # Login 4
    await asyncio.sleep(3)

    async with TESTING_CHANNEL.typing():
        await asyncio.sleep(random.randint(3, 10))
        await TESTING_CHANNEL.send('!login 1.1')

    await testIfHaveRole(OUR_MEMBER, roleName='', testContext='Fourth Login', roleList=['Level 10', 'Level 11'])

    await testLoginMessage(TESTING_CHANNEL, xp=167, daysLoggedInInARow=4, testContext='Fourth Login')

    # login 5
    await asyncio.sleep(3)

    async with TESTING_CHANNEL.typing():
        await asyncio.sleep(random.randint(3, 10))
        await TESTING_CHANNEL.send('!login 1.1')

    # doesn't work because this is a money reward and our function only works with xp
    await testLoginMessage(TESTING_CHANNEL, xp=10, daysLoggedInInARow=5, testContext='Fifth Login')

    # Login 6
    await asyncio.sleep(3)

    async with TESTING_CHANNEL.typing():
        await asyncio.sleep(random.randint(3, 10))
        await TESTING_CHANNEL.send('!login 1.1')

    # login 7
    await asyncio.sleep(3)

    async with TESTING_CHANNEL.typing():
        await asyncio.sleep(random.randint(3, 10))
        await TESTING_CHANNEL.send('!login 1.1')

    # Login 8
    await asyncio.sleep(3)

    async with TESTING_CHANNEL.typing():
        await asyncio.sleep(random.randint(3, 10))
        await TESTING_CHANNEL.send('!login 1.1')

    # login 9
    await asyncio.sleep(3)

    async with TESTING_CHANNEL.typing():
        await asyncio.sleep(random.randint(3, 10))
        await TESTING_CHANNEL.send('!login 1.1')

    # Login 10
    await asyncio.sleep(3)

    async with TESTING_CHANNEL.typing():
        await asyncio.sleep(random.randint(3, 10))
        await TESTING_CHANNEL.send('!login 1.1')

    await testStatsCommand(TESTING_CHANNEL, xp=747, level=17, money=5, lastLogin=responseData['lastLogin'], daysLoggedInInARow=10,
                            testContext='10th Login')
    
    # check that 