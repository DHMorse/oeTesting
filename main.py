import selfcord
import requests
import asyncio
import traceback
import os
import pytz
import time
from datetime import datetime

from mySecrets import TOKEN
from helperFunctions import writeExepctoinToLogFile

from globalVars import COLORS, tests
from globalVars import EXCEPTION_OUTPUT_FILE_LOCATION, FAILED_TESTS_FILE_LOCATION, TEST_OUTPUT_FILE_LOCATION
from globalVars import MY_USER_ID, MY_USER_NAME
from globalVars import LOG_CHANNEL_ID, TESTING_CHANNEL_ID, OUTPUT_CHANNEL_ID

from admin._1sendAMessage import send_a_message
from admin._2Stats import _2checkStats
from admin._3makeLoginRewards import makeLoginRewards
from admin._4login import login
from admin._5getLeaderboard import getLeaderboard
from admin._6levelToXp import levelToXp

from admin._8testCensorship import testCensorship

client = selfcord.Client()

@client.event
async def on_ready():
    testStartTime = time.time()
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

    print('Finished: 1. Send a message')

    await asyncio.sleep(1)

    # 2. Check Stats
    try:
        await _2checkStats(TESTING_CHANNEL)
    except Exception as e:
        await writeExepctoinToLogFile(e, traceback.format_exc())

    print('Finished: 2. Check Stats')

    await asyncio.sleep(1)

    # 3. Make Login Rewards
    try:
        await makeLoginRewards(TESTING_CHANNEL)
    except Exception as e:
        await writeExepctoinToLogFile(e, traceback.format_exc())

    print('Finished: 3. Make Login Rewards')

    await asyncio.sleep(1)

    # 4. Login, check embed, got role `Level 1`, and stats
    try:
        await login(TESTING_CHANNEL, LOG_CHANNEL, OUR_MEMBER)
    except Exception as e:
        await writeExepctoinToLogFile(e, traceback.format_exc())

    print('Finished: 4. Login')

    await asyncio.sleep(1)

    # 5. Get Leaderboard
    try:
        await getLeaderboard(TESTING_CHANNEL)
    except Exception as e:
        await writeExepctoinToLogFile(e, traceback.format_exc())

    print('Finished: 5. Get Leaderboard')

    await asyncio.sleep(1)

    # 6. Level to XP, and that we get the role `Level 2`
    try:
        await levelToXp(TESTING_CHANNEL, OUR_MEMBER)
    except Exception as e:
        await writeExepctoinToLogFile(e, traceback.format_exc())
    
    print('Finished: 6. Level to XP')

    await asyncio.sleep(1)

    # 8. Test Censorship
    try:
        await testCensorship(TESTING_CHANNEL)
    except Exception as e:
        await writeExepctoinToLogFile(e, traceback.format_exc())

    print('Finished: 8. Test Censorship')

    await asyncio.sleep(1)

    for index, test in enumerate(tests):
        if not test['passed']:
            print(f"{COLORS['red']}Test {index}, \"{test['test']}\" failed. Expected: {test['expectedResult']}, Actual: {test['actualResult']} Type: {type(test['actualResult'])}{COLORS['reset']}")
            with open(TEST_OUTPUT_FILE_LOCATION, 'a') as file:
                file.write(f'''Test {index}, "{test['test']}", FAILED, "Expected: {test['expectedResult']} Actual: {test['actualResult']} Type: {type(test['actualResult'])}"\n''')
            
            if not os.path.exists(FAILED_TESTS_FILE_LOCATION):
                with open(FAILED_TESTS_FILE_LOCATION, 'w') as file:
                    file.write(f'''CST Time: {cst_time.strftime(time_format)}
EST Time: {est_time.strftime(time_format)}
UTC Time: {utc_now.strftime(time_format)}
Category, Test Name, Status, Message
''')
            with open(FAILED_TESTS_FILE_LOCATION, 'a') as file:
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

        if os.path.exists(FAILED_TESTS_FILE_LOCATION):
            await OUTPUT_CHANNEL.send(file=selfcord.File(FAILED_TESTS_FILE_LOCATION))

        await OUTPUT_CHANNEL.send(file=selfcord.File(TEST_OUTPUT_FILE_LOCATION))
        os.remove(TEST_OUTPUT_FILE_LOCATION)

        elapsed_time_seconds = time.time() - testStartTime
        elapsed_time_minutes = elapsed_time_seconds / 60
        await OUTPUT_CHANNEL.send(f'Tests took {elapsed_time_seconds:.2f} seconds ({elapsed_time_minutes:.2f} minutes).')

        if not os.path.exists(FAILED_TESTS_FILE_LOCATION):
            await OUTPUT_CHANNEL.send('All tests passed.')
        else:
            os.remove(FAILED_TESTS_FILE_LOCATION)

    except Exception as e:
        await writeExepctoinToLogFile(e, traceback.format_exc())

# Run the bot with your token
client.run(TOKEN)