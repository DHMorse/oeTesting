import selfcord
import random
import requests
import asyncio
import traceback
import os
import pytz

from datetime import datetime

from mySecrets import TOKEN
from globalVars import EXCEPTION_OUTPUT_FILE_LOCATION, MY_USER_ID, LOG_CHANNEL_ID, TESTING_CHANNEL_ID, tests
from globalVars import writeExepctoinToLogFile

from admin._1sendAMessage import send_a_message
from admin._2Stats import _2checkStats
from admin._3makeLoginRewards import makeLoginRewards
from admin._4login import login
from admin._5getLeaderboard import getLeaderboard

client = selfcord.Client()

TEST_OUTPUT_FILE_LOCATION = './tests.csv'

OUTPUT_CHANNEL_ID = 1320988937149349959

COLORS = {
    'red': '\u001b[1;31m',
    'yellow': '\u001b[1;33m',
    'blue': '\u001b[1;34m',
    'green': '\u001b[1;32m',
    'reset': '\u001b[0m'
}

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

    LOG_CHANNEL = client.get_channel(LOG_CHANNEL_ID)
    
    TESTING_CHANNEL = client.get_channel(TESTING_CHANNEL_ID)
    
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
    
    # 1. Send a message
    try:
        await send_a_message(TESTING_CHANNEL)
    except Exception as e:
        await writeExepctoinToLogFile(e, traceback.format_exc())

    await asyncio.sleep(1)

    # 2. Check Stats
    try:
        await _2checkStats(TESTING_CHANNEL)
    except Exception as e:
        await writeExepctoinToLogFile(e, traceback.format_exc())

    await asyncio.sleep(1)

    # 3. Make Login Rewards
    try:
        await makeLoginRewards(TESTING_CHANNEL)
    except Exception as e:
        await writeExepctoinToLogFile(e, traceback.format_exc())

    await asyncio.sleep(1)

    # 4. Login, check embed, got role `Level 1`, and stats
    try:
        await login(TESTING_CHANNEL, LOG_CHANNEL, OUR_MEMBER)
    except Exception as e:
        await writeExepctoinToLogFile(e, traceback.format_exc())

    await asyncio.sleep(1)

    # 5. Get Leaderboard
    try:
        await getLeaderboard(TESTING_CHANNEL)
    except Exception as e:
        await writeExepctoinToLogFile(e, traceback.format_exc())

    await asyncio.sleep(1)

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
            print(f"{COLORS['red']}Test {index}, \"{test['test']}\" failed. Expected: {test['expectedResult']}, Actual: {test['actualResult']} Type: {type(test['actualResult'])}{COLORS['reset']}")
            with open(TEST_OUTPUT_FILE_LOCATION, 'a') as file:
                file.write(f'''Test {index}, "{test['test']}", FAILED, "Expected: {test['expectedResult']} Actual: {test['actualResult']} Type: {type(test['actualResult'])}"\n''')
        else:
            print(f"{COLORS['green']}Test {index}, \"{test['test']}\" passed{COLORS['reset']}")
            with open(TEST_OUTPUT_FILE_LOCATION, 'a') as file:
                file.write(f'''Test {index}, "{test['test']}", PASSED, ""\n''')

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