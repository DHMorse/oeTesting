import selfcord
import time
import random
import requests
import asyncio

from typing import List, Dict

from mySecrets import TOKEN

client = selfcord.Client()

MY_USER_ID = 1214760182576324680


COLORS = {
    'red': '\u001b[1;31m',
    'yellow': '\u001b[1;33m',
    'blue': '\u001b[1;34m',
    'green': '\u001b[1;32m',
    'reset': '\u001b[0m'
}

async def writeExepctoinToLogFile(exception: Exception):
    with open('./exceptions.log', 'a') as file:
        file.write(f'{exception}\n')

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

    LOG_CHANNEL = client.get_channel(1304829859549155328)
    
    TESTING_CHANNEL = client.get_channel(1320533335054749817)
    
    OUR_MEMBER = await LOG_CHANNEL.guild.fetch_member(MY_USER_ID)
    
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
                with open('./Tests.log', 'a') as file:
                    file.write(f"I already had role `Level {i}`.\n")
                await OUR_MEMBER.remove_roles(OUR_MEMBER.roles[i])
        except:
            pass

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
        await writeExepctoinToLogFile(e)
    
    try:
        tests.append({0: {'passed': responseData['daysLoggedInInARow'] == 0, 'expectedResult': 0, 'actualResult': responseData['daysLoggedInInARow'], 'test': 'daysLoggedInInARow'}})
    except Exception as e:
        await writeExepctoinToLogFile(e)

    try:
        tests.append({1: {'passed': responseData['lastLogin'] == None, 'expectedResult': None, 'actualResult': responseData['lastLogin'], 'test': 'lastLogin'}})
    except Exception as e:
        await writeExepctoinToLogFile(e)

    try:
        tests.append({2: {'passed': responseData['money'] == 0, 'expectedResult': 0, 'actualResult': responseData['money'], 'test': 'money'}})
    except Exception as e:
        await writeExepctoinToLogFile(e)

    try:
        tests.append({3: {'passed': responseData['userId'] == 1214760182576324680, 'expectedResult': 0, 'actualResult': responseData['userId'], 'test': 'userId'}})
    except Exception as e:
        await writeExepctoinToLogFile(e)

    try:
        tests.append({4: {'passed': responseData['username'] == 'john5971', 'expectedResult': 'john5971', 'actualResult': responseData['username'], 'test': 'username'}})
    except Exception as e:
        await writeExepctoinToLogFile(e)

    try:
        tests.append({5: {'passed': responseData['xp'] == 1, 'expectedResult': 1, 'actualResult': responseData['xp'], 'test': 'xp'}})
    except Exception as e:
        await writeExepctoinToLogFile(e)

    await asyncio.sleep(random.randint(5, 10))
    
    await TESTING_CHANNEL.send('!makeloginrewards 300')
    
    await asyncio.sleep(random.randint(5, 10))
    
    await TESTING_CHANNEL.send('!login')
    
    await asyncio.sleep(20)
    
    index: int = 0
    async for message in TESTING_CHANNEL.history(limit=2):
        if index == 0:
            index += 1
            try:
                tests.append({6: 
                                {
                                    'passed': message.content == 'Congratulations! You have received 10 XP for logging in 1 days in a row!', 
                                    'expectedResult': 'Congratulations! You have received 10 XP for logging in 1 days in a row!', 
                                    'actualResult': message.content, 
                                    'test': 'login message 0'}})
            except Exception as e:
                await writeExepctoinToLogFile(e)
        else:
            try:
                tests.append({7: 
                                {
                                    'passed': message.content == 'You have made your first daily login!', 
                                    'expectedResult': 'You have made your first daily login!', 
                                    'actualResult': message.content, 
                                    'test': 'login message 1'}})
            except Exception as e:
                await writeExepctoinToLogFile(e)

    async for message in LOG_CHANNEL.history(limit=1):
        try:
            tests.append({8: 
                            {'passed': message.embeds[0].to_dict()['description'] == '**Member:** \njohn5971\n\n**Account Level:** \n1', 
                            'expectedResult': '**Member:** \njohn5971\n\n**Account Level:** \n1', 
                            'actualResult': message.embeds[0].to_dict()['description'], 
                            'test': 'Level Up Embed Description'}})
        except Exception as e:
            await writeExepctoinToLogFile(e)
        try:
            tests.append({9: 
                        {'passed': message.embeds[0].to_dict()['title'] == 'Member Leveled Up', 
                        'expectedResult': 'Member Leveled Up', 
                        'actualResult': message.embeds[0].to_dict()['title'], 
                        'test': 'Level Up Embed Title'}})
        except Exception as e:
            await writeExepctoinToLogFile(e)
        try:
            tests.append({10: 
                            {'passed': OUR_MEMBER.roles[1].name == 'Level 1', 
                            'expectedResult': 'Level 1', 
                            'actualResult': OUR_MEMBER.roles[1].name, 
                            'test': 'Got Role `Level 1` After Leveling Up'}})
        except Exception as e:
            await writeExepctoinToLogFile(e)
    
    await asyncio.sleep(5)

    response = requests.get(f'http://45.79.203.11:5001/users?userId={MY_USER_ID}')
    
    try:
        responseData = response.json()[0]
    except Exception as e:
        print(e)
        print(responseData.json())

    try:    
        tests.append({11: 
                        {'passed': responseData['daysLoggedInInARow'] == 1, 
                        'expectedResult': 1, 
                        'actualResult': responseData['daysLoggedInInARow'], 
                        'test': 'daysLoggedInInARow After Login'}})
    except Exception as e:
        await writeExepctoinToLogFile(e)
    
    try:
        tests.append({12: 
                        {'passed': responseData['lastLogin'] is not None, 
                        'expectedResult': not None, 
                        'actualResult': responseData['lastLogin'], 
                        'test': 'lastLogin After Login'}})
    except Exception as e:
        await writeExepctoinToLogFile(e)
    
    try:
        tests.append({13: 
                        {'passed': responseData['money'] == 0, 
                        'expectedResult': 0, 
                        'actualResult': responseData['money'], 
                        'test': 'money After Login'}})
    except Exception as e:
        await writeExepctoinToLogFile(e)

    try:
        tests.append({14: 
                        {'passed': responseData['userId'] == 1214760182576324680, 
                        'expectedResult': 0, 
                        'actualResult': responseData['userId'], 
                        'test': 'userId After Login'}})
    except Exception as e:
        await writeExepctoinToLogFile(e)
    
    try:
        tests.append({15: 
                        {'passed': responseData['username'] == 'john5971', 
                        'expectedResult': 'john5971', 
                        'actualResult': responseData['username'], 
                        'test': 'username After Login'}})
    except Exception as e:
        await writeExepctoinToLogFile(e)

    try:
        tests.append({16: 
                        {'passed': responseData['xp'] == 13, 
                        'expectedResult': 13, 
                        'actualResult': responseData['xp'], 
                        'test': 'xp After Login'}})
    except Exception as e:
        await writeExepctoinToLogFile(e)

    for index, test in enumerate(tests):
        if not test[index]['passed']:
            print(f"{COLORS['red']}Test {index}, \"{test[index]['test']}\" failed. Expected: {test[index]['expectedResult']}, Actual: {test[index]['actualResult']} Type: {type(test[index]['actualResult'])}{COLORS['reset']}")
            with open('./Tests.log', 'a') as file:
                file.write(f"Test {index}, \"{test[index]['test']}\" failed. Expected: {test[index]['expectedResult']}, Actual: {test[index]['actualResult']} Type: {type(test[index]['actualResult'])}\n")
        else:
            print(f"{COLORS['green']}Test {index}, \"{test[index]['test']}\" passed{COLORS['reset']}")
            with open('./Tests.log', 'a') as file:
                file.write(f"Test {index}, \"{test[index]['test']}\" passed\n")


# Run the bot with your token
client.run(TOKEN)