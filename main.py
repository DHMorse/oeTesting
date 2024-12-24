import selfcord
import time
import random
import requests
import asyncio
import traceback
import os
import pytz

from datetime import datetime
from typing import List, Dict
from mySecrets import TOKEN

client = selfcord.Client()

MY_USER_ID = 1214760182576324680

TEST_OUTPUT_FILE_LOCATION = './tests.csv'

EXCEPTION_OUTPUT_FILE_LOCATION = './exceptions.log'

OUTPUT_CHANNEL_ID = 1320988937149349959

COLORS = {
    'red': '\u001b[1;31m',
    'yellow': '\u001b[1;33m',
    'blue': '\u001b[1;34m',
    'green': '\u001b[1;32m',
    'reset': '\u001b[0m'
}

async def writeExepctoinToLogFile(exception: Exception, traceback: str):
    with open(EXCEPTION_OUTPUT_FILE_LOCATION, 'a') as file:
        file.write(f'{exception}\n')

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

    LOG_CHANNEL = client.get_channel(1304829859549155328)
    
    TESTING_CHANNEL = client.get_channel(1320533335054749817)
    
    OUR_MEMBER = await LOG_CHANNEL.guild.fetch_member(MY_USER_ID)
    
    OUTPUT_CHANNEL = client.get_channel(OUTPUT_CHANNEL_ID)
    
    if os.path.exists(TEST_OUTPUT_FILE_LOCATION):
        await OUTPUT_CHANNEL.send(file=selfcord.File(TEST_OUTPUT_FILE_LOCATION))
        os.remove(TEST_OUTPUT_FILE_LOCATION)

    # Define the format
    time_format = "%Y-%m-%d %H:%M:%S"

    # Get the current UTC time
    utc_now = datetime.now(pytz.utc)

    # Convert to CST and EST
    cst_tz = pytz.timezone("US/Central")
    est_tz = pytz.timezone("US/Eastern")

    cst_time = utc_now.astimezone(cst_tz)
    est_time = utc_now.astimezone(est_tz)


    with open(TEST_OUTPUT_FILE_LOCATION, 'w') as file:
        file.write(f'''CST Time: {cst_time.strftime(time_format)}
EST Time: {est_time.strftime(time_format)}
UTC Time: {utc_now.strftime(time_format)}
Category, Test Name, Status, Message
''')

    await asyncio.sleep(5)

    response = requests.get(f'http://45.79.203.11:5001/users?userId={MY_USER_ID}')

    responseData = response.json()

    try:
        if not 'error' in responseData and responseData['error'] == 'no such table: users':
            print(f"{COLORS['red']}You need to remove me from the database :){COLORS['reset']}")
            return
    except:
        pass

    for i in range(1, 101):
        try:
            if OUR_MEMBER.roles[i].name == f'Level {i}':
                print(f"{COLORS['yellow']}I already had role `Level {i}` removing it now.{COLORS['reset']}")
                
                with open(TEST_OUTPUT_FILE_LOCATION, 'a') as file:
                    file.write(f"WARNING, \"Role Assigment\", WARNING, \"I already had role `Level {i}`.\"\n")
                
                await OUR_MEMBER.remove_roles(OUR_MEMBER.roles[i])
        except:
            pass

    async with TESTING_CHANNEL.typing():
        await asyncio.sleep(random.randint(1, 5))
        await TESTING_CHANNEL.send('69')

    tests: List[Dict[int, Dict[str, any]]] = []

    #{
    #    int('testInt'): {
    #        'passed': bool,
    #        'expectedResult': any,
    #        'actualResult': any
    #        'test': str
    #    } 
    #}

    response = requests.get(f'http://45.79.203.11:5001/users?userId={MY_USER_ID}')

    try:
        responseData = response.json()[0]
    except Exception as e:
        await writeExepctoinToLogFile(e, traceback.format_exc())
    
    try:
        tests.append({0: {'passed': responseData['daysLoggedInInARow'] == 0, 'expectedResult': 0, 'actualResult': responseData['daysLoggedInInARow'], 'test': 'daysLoggedInInARow'}})
    except Exception as e:
        tests.append({0: {'passed': False, 'expectedResult': 0, 'actualResult': f'Exception: {e}', 'test': 'daysLoggedInInARow'}})

    try:
        tests.append({1: {'passed': responseData['lastLogin'] == None, 'expectedResult': None, 'actualResult': responseData['lastLogin'], 'test': 'lastLogin'}})
    except Exception as e:
        tests.append({1: {'passed': False, 'expectedResult': None, 'actualResult': f'Exception: {e}', 'test': 'lastLogin'}})

    try:
        tests.append({2: {'passed': responseData['money'] == 0, 'expectedResult': 0, 'actualResult': responseData['money'], 'test': 'money'}})
    except Exception as e:
        tests.append({2: {'passed': False, 'expectedResult': 0, 'actualResult': f'Exception: {e}', 'test': 'money'}})

    try:
        tests.append({3: {'passed': responseData['userId'] == 1214760182576324680, 'expectedResult': 0, 'actualResult': responseData['userId'], 'test': 'userId'}})
    except Exception as e:
        tests.append({3: {'passed': False, 'expectedResult': 0, 'actualResult': f'Exception: {e}', 'test': 'userId'}})

    try:
        tests.append({4: {'passed': responseData['username'] == 'john5971', 'expectedResult': 'john5971', 'actualResult': responseData['username'], 'test': 'username'}})
    except Exception as e:
        tests.append({4: {'passed': False, 'expectedResult': 'john5971', 'actualResult': f'Exception: {e}', 'test': 'username'}})

    try:
        tests.append({5: {'passed': responseData['xp'] == 1, 'expectedResult': 1, 'actualResult': responseData['xp'], 'test': 'xp'}})
    except Exception as e:
        tests.append({5: {'passed': False, 'expectedResult': 1, 'actualResult': f'Exception: {e}', 'test': 'xp'}})

    async with TESTING_CHANNEL.typing():
        await asyncio.sleep(random.randint(5, 15))
        await TESTING_CHANNEL.send('!makeloginrewards 300')

    async for message in TESTING_CHANNEL.history(limit=1):
        try:
            tests.append({6: 
                            {'passed': message.content == '```ansi\n[1;34mLogin rewards for 300 levels have been successfully created.[0m\n```', 
                            'expectedResult': '```ansi\n[1;34mLogin rewards for 300 levels have been successfully created.[0m\n```', 
                            'actualResult': message.content, 
                            'test': 'Make Login Rewards Command'}})
        except Exception as e:
            tests.append({6: 
                            {'passed': False, 
                            'expectedResult': '```ansi\n[1;34mLogin rewards for 300 levels have been successfully created.[0m\n```', 
                            'actualResult': f'Exception: {e}', 
                            'test': 'Make Login Rewards Command'}})

    async with TESTING_CHANNEL.typing():
        await asyncio.sleep(random.randint(3, 10))
        await TESTING_CHANNEL.send('!login')
    
    await asyncio.sleep(20)
    
    index: int = 0
    async for message in TESTING_CHANNEL.history(limit=2):
        if index == 0:
            index += 1
            try:
                tests.append({7: 
                                {
                                    'passed': message.content == 'Congratulations! You have received 10 XP for logging in 1 days in a row!', 
                                    'expectedResult': 'Congratulations! You have received 10 XP for logging in 1 days in a row!', 
                                    'actualResult': message.content, 
                                    'test': 'login message 0'}})
            except Exception as e:
                tests.append({7: 
                                {'passed': False, 
                                'expectedResult': 'Congratulations! You have received 10 XP for logging in 1 days in a row!', 
                                'actualResult': f'Exception: {e}', 
                                'test': 'login message 0'}})
                #await writeExepctoinToLogFile(e)
        else:
            try:
                tests.append({8: 
                                {
                                    'passed': message.content == 'You have made your first daily login!', 
                                    'expectedResult': 'You have made your first daily login!', 
                                    'actualResult': message.content, 
                                    'test': 'login message 1'}})
            except Exception as e:
                tests.append({8:
                                {'passed': False,
                                'expectedResult': 'You have made your first daily login!',
                                'actualResult': f'Exception: {e}',
                                'test': 'login message 1'}})
                #await writeExepctoinToLogFile(e)

    async for message in LOG_CHANNEL.history(limit=1):
        try:
            tests.append({9: 
                            {'passed': message.embeds[0].to_dict()['description'] == '**Member:** \njohn5971\n\n**Account Level:** \n1', 
                            'expectedResult': '**Member:** \njohn5971\n\n**Account Level:** \n1', 
                            'actualResult': message.embeds[0].to_dict()['description'], 
                            'test': 'Level Up Embed Description'}})
        except Exception as e:
            tests.append({9:
                            {'passed': False,
                            'expectedResult': '**Member:** \njohn5971\n\n**Account Level:** \n1',
                            'actualResult': f'Exception: {e}',
                            'test': 'Level Up Embed Description'}})
            #await writeExepctoinToLogFile(e)
        
        try:
            tests.append({10: 
                        {'passed': message.embeds[0].to_dict()['title'] == 'Member Leveled Up', 
                        'expectedResult': 'Member Leveled Up', 
                        'actualResult': message.embeds[0].to_dict()['title'], 
                        'test': 'Level Up Embed Title'}})
        except Exception as e:
            tests.append({10:
                            {'passed': False,
                            'expectedResult': 'Member Leveled Up',
                            'actualResult': f'Exception: {e}',
                            'test': 'Level Up Embed Title'}})
            #await writeExepctoinToLogFile(e)
        
        try:
            WeHaveRoleLevel1 = False
            for role in OUR_MEMBER.roles:
                if role.name == 'Level 1':
                    WeHaveRoleLevel1 = True
                    break
            try:
                tests.append({11: 
                                {'passed': WeHaveRoleLevel1, 
                                'expectedResult': 'We\'d have the role `Level 1`', 
                                'actualResult': [role.name for role in OUR_MEMBER.roles], 
                                'test': 'Got Role `Level 1` After Leveling Up'}})
            except Exception as e:
                tests.append({11:
                                {'passed': False,
                                'expectedResult': 'We\'d have the role `Level 1`',
                                'actualResult': f'Exception: {e}',
                                'test': 'Got Role `Level 1` After Leveling Up'}})
        except Exception as e:
            await writeExepctoinToLogFile(e, traceback.format_exc())
    
    await asyncio.sleep(5)

    response = requests.get(f'http://45.79.203.11:5001/users?userId={MY_USER_ID}')
    
    try:
        responseData = response.json()[0]
    except Exception as e:
        print(e)
        print(responseData.json())

    try:    
        tests.append({12: 
                        {'passed': responseData['daysLoggedInInARow'] == 1, 
                        'expectedResult': 1, 
                        'actualResult': responseData['daysLoggedInInARow'], 
                        'test': 'daysLoggedInInARow After Login'}})
    except Exception as e:
        tests.append({12: {'passed': False, 'expectedResult': 1, 'actualResult': f'Exception: {e}', 'test': 'daysLoggedInInARow After Login'}})
    
    try:
        tests.append({13: 
                        {'passed': responseData['lastLogin'] is not None, 
                        'expectedResult': not None, 
                        'actualResult': responseData['lastLogin'], 
                        'test': 'lastLogin After Login'}})
    except Exception as e:
        tests.append({13: {'passed': False, 'expectedResult': not None, 'actualResult': f'Exception: {e}', 'test': 'lastLogin After Login'}})
    
    try:
        tests.append({14: 
                        {'passed': responseData['money'] == 0, 
                        'expectedResult': 0, 
                        'actualResult': responseData['money'], 
                        'test': 'money After Login'}})
    except Exception as e:
        tests.append({14: {'passed': False, 'expectedResult': 0, 'actualResult': f'Exception: {e}', 'test': 'money After Login'}})

    try:
        tests.append({15: 
                        {'passed': responseData['userId'] == 1214760182576324680, 
                        'expectedResult': 0, 
                        'actualResult': responseData['userId'], 
                        'test': 'userId After Login'}})
    except Exception as e:
        tests.append({15: {'passed': False, 'expectedResult': 0, 'actualResult': f'Exception: {e}', 'test': 'userId After Login'}})
    
    try:
        tests.append({16: 
                        {'passed': responseData['username'] == 'john5971', 
                        'expectedResult': 'john5971', 
                        'actualResult': responseData['username'], 
                        'test': 'username After Login'}})
    except Exception as e:
        tests.append({16: {'passed': False, 'expectedResult': 'john5971', 'actualResult': f'Exception {e}', 'test': 'username After Login'}})

    try:
        tests.append({17: 
                        {'passed': responseData['xp'] == 13, 
                        'expectedResult': 13, 
                        'actualResult': responseData['xp'], 
                        'test': 'xp After Login'}})
    except Exception as e:
        tests.append({17: {'passed': False, 'expectedResult': 13, 'actualResult': f'Exception: {e}', 'test': 'xp After Login'}})

    async with TESTING_CHANNEL.typing():
        await asyncio.sleep(random.randint(5, 10))
        async for command in TESTING_CHANNEL.slash_commands():
            if command.name == "leaderboard":
                await command(TESTING_CHANNEL)

    await asyncio.sleep(5)

    async for message in TESTING_CHANNEL.history(limit=1):
        try:
            tests.append({18: 
                            {'passed': message.embeds[0].to_dict()['title'] == 'Level Leaderboard', 
                            'expectedResult': 'Leaderboard', 
                            'actualResult': message.embeds[0].to_dict()['title'], 
                            'test': 'Level Leaderboard Embed Title'}})
        except Exception as e:
            tests.append({18: 
                            {'passed': False, 
                            'expectedResult': 'Leaderboard', 
                            'actualResult': f'Exception: {e}', 
                            'test': 'Level Leaderboard Embed Title'}})

    try:
        with open (TEST_OUTPUT_FILE_LOCATION, 'a') as file:
            file.write('WARNING, "Leaderboard Display", WARNING, "The leaderboard data that is displayed cannot be checked, as of right now."\n')
    except Exception as e:
        await writeExepctoinToLogFile(e, traceback.format_exc())

    async with TESTING_CHANNEL.typing():
        await asyncio.sleep(random.randint(5, 10))
        async for command in TESTING_CHANNEL.slash_commands():
            if command.name == "generatecard":
                await command(TESTING_CHANNEL, prompt='An anime sword fighter.')

    await asyncio.sleep(30)

    async for message in TESTING_CHANNEL.history(limit=1):
        try:
            tests.append({19: 
                            {'passed': message.attachments[0].url.endswith('.png') or message.attachments[0].url.endswith('.jpg'), 
                            'expectedResult': 'Image', 
                            'actualResult': 'Image', 
                            'test': 'Generated Card'}})
        except Exception as e:
            tests.append({19: {'passed': False, 'expectedResult': 'Image', 'actualResult': f'Exception: {e}', 'test': 'Generated Card'}})

    async with TESTING_CHANNEL.typing():
        await asyncio.sleep(random.randint(5, 10))
        await TESTING_CHANNEL.send('!leveltoxp 1')

    await asyncio.sleep(5)

    async for message in TESTING_CHANNEL.history(limit=1):
        try:
            tests.append({20: 
                            {'passed': message.content == '```ansi\n[1;34mLevel 1 requires 10 XP.[0m\n```', 
                            'expectedResult': '```ansi\n[1;34mLevel 1 requires 10 XP.[0m\n```', 
                            'actualResult': message.content, 
                            'test': 'Level to XP Command `Level 1`'}})
        except Exception as e:
            tests.append({20: 
                            {'passed': False, 
                            'expectedResult': '```ansi\n[1;34mLevel 1 requires 10 XP.[0m\n```', 
                            'actualResult': f'Exception: {e}', 
                            'test': 'Level to XP Command `Level 1`'}})
            
    async with TESTING_CHANNEL.typing():
        await asyncio.sleep(random.randint(5, 10))
        await TESTING_CHANNEL.send('!leveltoxp 10')

    await asyncio.sleep(5)

    async for message in TESTING_CHANNEL.history(limit=1):
        try:
            tests.append({21: 
                            {'passed': message.content == '```ansi\n[1;34mLevel 10 requires 100 XP.[0m\n```', 
                            'expectedResult': '```ansi\n[1;34mLevel 10 requires 100 XP.[0m\n```', 
                            'actualResult': message.content, 
                            'test': 'Level to XP Command `Level 10`'}})
        except Exception as e:
            tests.append({21: 
                            {'passed': False, 
                            'expectedResult': '```ansi\n[1;34mLevel 10 requires 100 XP.[0m\n```', 
                            'actualResult': f'Exception: {e}', 
                            'test': 'Level to XP Command `Level 10`'}})
            
    async with TESTING_CHANNEL.typing():
        await asyncio.sleep(random.randint(5, 10))
        await TESTING_CHANNEL.send('!leveltoxp 69')

    await asyncio.sleep(5)

    async for message in TESTING_CHANNEL.history(limit=1):
        try:
            tests.append({22: 
                            {'passed': message.content == '```ansi\n[1;34mLevel 69 requires 1625964693 XP.[0m\n```', 
                            'expectedResult': '```ansi\n[1;34mLevel 69 requires 1625964693 XP.[0m\n```', 
                            'actualResult': message.content, 
                            'test': 'Level to XP Command `Level 69`'}})
        except Exception as e:
            tests.append({22: 
                            {'passed': False, 
                            'expectedResult': '```ansi\n[1;34mLevel 69 requires 1625964693 XP.[0m\n```', 
                            'actualResult': f'Exception: {e}', 
                            'test': 'Level to XP Command `Level 69`'}})

    for index, test in enumerate(tests):
        if not test[index]['passed']:
            print(f"{COLORS['red']}Test {index}, \"{test[index]['test']}\" failed. Expected: {test[index]['expectedResult']}, Actual: {test[index]['actualResult']} Type: {type(test[index]['actualResult'])}{COLORS['reset']}")
            with open(TEST_OUTPUT_FILE_LOCATION, 'a') as file:
                file.write(f'''Test {index}, "{test[index]['test']}", FAILED, "Expected: {test[index]['expectedResult']} Actual: {test[index]['actualResult']} Type: {type(test[index]['actualResult'])}"\n''')
        else:
            print(f"{COLORS['green']}Test {index}, \"{test[index]['test']}\" passed{COLORS['reset']}")
            with open(TEST_OUTPUT_FILE_LOCATION, 'a') as file:
                file.write(f'''Test {index}, "{test[index]['test']}", PASSED, ""\n''')

    await asyncio.sleep(5)

    try:
        if os.path.exists(EXCEPTION_OUTPUT_FILE_LOCATION):
            await OUTPUT_CHANNEL.send(file=selfcord.File(EXCEPTION_OUTPUT_FILE_LOCATION))
            os.remove(EXCEPTION_OUTPUT_FILE_LOCATION)

        await OUTPUT_CHANNEL.send(file=selfcord.File(TEST_OUTPUT_FILE_LOCATION))
        os.remove(TEST_OUTPUT_FILE_LOCATION)

    except Exception as e:
        await writeExepctoinToLogFile(e, traceback.format_exc())

# Run the bot with your token
client.run(TOKEN)