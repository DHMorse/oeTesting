import asyncio
import random
import traceback

from globalVars import tests

from helperFunctions import writeExepctoinToLogFile

async def levelToXp(TESTING_CHANNEL, OUR_MEMBER):
    async with TESTING_CHANNEL.typing():
        await asyncio.sleep(random.randint(5, 10))
        await TESTING_CHANNEL.send('!leveltoxp')

    await asyncio.sleep(3)

    async for message in TESTING_CHANNEL.history(limit=1):
        try:
            tests.append({'passed': message.content == '```ansi\n[1;31mPlease provide a level to convert to XP.[0m\n```', 
                            'expectedResult': '```ansi\n[1;31mPlease provide a level to convert to XP.[0m\n```', 
                            'actualResult': message.content, 
                            'test': 'Level to XP Command `Level 1`'})
        except Exception as e:
            tests.append({'passed': False, 
                            'expectedResult': '```ansi\n[1;31mPlease provide a level to convert to XP.[0m\n```', 
                            'actualResult': f'Exception: {e}', 
                            'test': 'Level to XP Command no level provided'})

    await asyncio.sleep(3)

    async with TESTING_CHANNEL.typing():
        await asyncio.sleep(random.randint(5, 10))
        await TESTING_CHANNEL.send('!leveltoxp 1')

    await asyncio.sleep(3)

    async for message in TESTING_CHANNEL.history(limit=1):
        try:
            tests.append({'passed': message.content == '```ansi\n[1;34mLevel 1 requires 10 XP.[0m\n```', 
                            'expectedResult': '```ansi\n[1;34mLevel 1 requires 10 XP.[0m\n```', 
                            'actualResult': message.content, 
                            'test': 'Level to XP Command `Level 1`'})
        except Exception as e:
            tests.append({'passed': False, 
                            'expectedResult': '```ansi\n[1;34mLevel 1 requires 10 XP.[0m\n```', 
                            'actualResult': f'Exception: {e}', 
                            'test': 'Level to XP Command `Level 1`'})

    await asyncio.sleep(3)

    async with TESTING_CHANNEL.typing():
        await asyncio.sleep(random.randint(5, 10))
        await TESTING_CHANNEL.send('!leveltoxp 10')

    await asyncio.sleep(3)

    async for message in TESTING_CHANNEL.history(limit=1):
        try:
            tests.append({'passed': message.content == '```ansi\n[1;34mLevel 10 requires 100 XP.[0m\n```', 
                            'expectedResult': '```ansi\n[1;34mLevel 10 requires 100 XP.[0m\n```', 
                            'actualResult': message.content, 
                            'test': 'Level to XP Command `Level 10`'})
        except Exception as e:
            tests.append({'passed': False, 
                            'expectedResult': '```ansi\n[1;34mLevel 10 requires 100 XP.[0m\n```', 
                            'actualResult': f'Exception: {e}', 
                            'test': 'Level to XP Command `Level 10`'})

    await asyncio.sleep(3)

    async with TESTING_CHANNEL.typing():
        await asyncio.sleep(random.randint(5, 10))
        await TESTING_CHANNEL.send('!leveltoxp 69')

    await asyncio.sleep(3)

    async for message in TESTING_CHANNEL.history(limit=1):
        try:
            tests.append({'passed': message.content == '```ansi\n[1;34mLevel 69 requires 1625964693 XP.[0m\n```', 
                            'expectedResult': '```ansi\n[1;34mLevel 69 requires 1625964693 XP.[0m\n```', 
                            'actualResult': message.content, 
                            'test': 'Level to XP Command `Level 69`'})
        except Exception as e:
            tests.append({'passed': False, 
                            'expectedResult': '```ansi\n[1;34mLevel 69 requires 1625964693 XP.[0m\n```', 
                            'actualResult': f'Exception: {e}', 
                            'test': 'Level to XP Command `Level 69`'})
            
    # Check that we received the `Level 2` role

    await asyncio.sleep(3)

    # Check if the user was given the role `Level 1`
    try:
        WeHaveRoleLevel2 = False
        for role in OUR_MEMBER.roles:
            if role.name == 'Level 2':
                WeHaveRoleLevel2 = True
                break
        try:
            tests.append({'passed': WeHaveRoleLevel2, 
                            'expectedResult': 'We\'d have the role `Level 2`', 
                            'actualResult': [role.name for role in OUR_MEMBER.roles], 
                            'test': 'Got Role `Level 2` After Leveling Up After Command `!leveltoxp 69` was used'})
        except Exception as e:
            tests.append({'passed': False,
                            'expectedResult': 'We\'d have the role `Level 1`',
                            'actualResult': f'Exception: {e}',
                            'test': 'Got Role `Level 2` After Leveling Up After Command `!leveltoxp 69` was used'})
    except Exception as e:
        await writeExepctoinToLogFile(e, traceback.format_exc())