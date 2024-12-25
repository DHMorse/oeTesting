import asyncio
import random
import time
import traceback

from typing import List, Dict, Any, Tuple

MY_USER_ID = 1214760182576324680

MY_USER_NAME = 'john5971'

EXCEPTION_OUTPUT_FILE_LOCATION = './exceptions.log'

TEST_OUTPUT_FILE_LOCATION = './tests.csv'

FAILED_TESTS_FILE_LOCATION = './failedTests.csv'

LOG_CHANNEL_ID = 1304829859549155328
TESTING_CHANNEL_ID = 1320533335054749817
OUTPUT_CHANNEL_ID = 1320988937149349959

COLORS = {
    'red': '\u001b[1;31m',
    'yellow': '\u001b[1;33m',
    'blue': '\u001b[1;34m',
    'green': '\u001b[1;32m',
    'reset': '\u001b[0m'
}

tests: List[Dict[str, any]] = []

    #[
    #    {
    #        'passed': bool,
    #        'expectedResult': any,
    #        'actualResult': any
    #        'test': str
    #    } 
    #]

async def writeExepctoinToLogFile(exception: Exception, traceback: str):
    with open(EXCEPTION_OUTPUT_FILE_LOCATION, 'a') as file:
        file.write(f'Exception: {exception}\nTraceback: {traceback}\n\n')

async def testStatsCommand(TESTING_CHANNEL, xp, level, money, lastLogin, daysLoggedInInARow, testContext: str = ''):
    # Check the stats command to see if the user's stats were updated correctly
    async with TESTING_CHANNEL.typing():
        await asyncio.sleep(random.randint(1, 5))
        await TESTING_CHANNEL.send('!stats')

    await asyncio.sleep(3)

    async for message in TESTING_CHANNEL.history(limit=1):
        # Checks Xp
        xpToCheck = f'[0;34mXp: {xp}'
        testName = f'stats Command Xp After {testContext}'
        try:
            tests.append({'passed': message.content.split('\n')[2] == xpToCheck, 
                            'expectedResult': xpToCheck, 
                            'actualResult': message.content.split('\n')[2], 
                            'test': testName})
        except Exception as e:
            tests.append({'passed': False, 
                            'expectedResult': xpToCheck, 
                            'actualResult': f'Exception: {e}', 
                            'test': testName})

        # Checks Level
        levelToCheck = f'[0;34mLevel: {level}'
        testName = f'stats Command Level After {testContext}'
        try:
            tests.append({'passed': message.content.split('\n')[3] == levelToCheck, 
                            'expectedResult': levelToCheck, 
                            'actualResult': message.content.split('\n')[3], 
                            'test': testName})
        except Exception as e:
            tests.append({'passed': False, 
                            'expectedResult': levelToCheck, 
                            'actualResult': f'Exception: {e}', 
                            'test': testName})

        # Checks Money
        moneyToCheck = f'[0;36mMoney: ${money}'
        testName = f'stats Command Money After {testContext}'
        try:
            tests.append({'passed': message.content.split('\n')[4] == moneyToCheck, 
                            'expectedResult': moneyToCheck, 
                            'actualResult': message.content.split('\n')[4], 
                            'test': testName})
        except Exception as e:
            tests.append({'passed': False, 
                            'expectedResult': moneyToCheck, 
                            'actualResult': f'Exception: {e}', 
                            'test': testName})
            
        # Checks Last Login (Seconds Since Epoch)
        secondsSinceEpochToCheck = '[0;36mLast Login (Seconds Since Epoch): ' + str(lastLogin)
        testName = f'stats Command Last Login (Seconds Since Epoch) After {testContext}'
        try:
            tests.append({'passed': message.content.split('\n')[5] == secondsSinceEpochToCheck, 
                            'expectedResult': secondsSinceEpochToCheck, 
                            'actualResult': message.content.split('\n')[5], 
                            'test': testName})
        except Exception as e:
            tests.append({'passed': False, 
                            'expectedResult': secondsSinceEpochToCheck, 
                            'actualResult': f'Exception: {e}', 
                            'test': testName})
            
        # Checks Last Login (UTC)
        utcTimeToCheck = f'[0;34mLast Login (UTC): {time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(lastLogin))} UTC'
        testName = f'stats Command Last Login (UTC) After {testContext}'
        try:
            tests.append({'passed': message.content.split('\n')[6] == utcTimeToCheck, 
                    'expectedResult': utcTimeToCheck, 
                    'actualResult': message.content.split('\n')[6], 
                    'test': testName})
        except Exception as e:
            tests.append({'passed': False, 
                    'expectedResult': utcTimeToCheck, 
                    'actualResult': f'Exception: {e}', 
                    'test': testName})
            
        # Checks Last Login (CST)
        cstTimeToCheck = f'[0;34mLast Login (CST): {time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(lastLogin - 21600))} CST'
        testName = f'stats Command Last Login (CST) After {testContext}'
        try:
            tests.append({'passed': message.content.split('\n')[7] == cstTimeToCheck, 
                    'expectedResult': cstTimeToCheck, 
                    'actualResult': message.content.split('\n')[7], 
                    'test': testName})
        except Exception as e:
            tests.append({'passed': False, 
                    'expectedResult': cstTimeToCheck, 
                    'actualResult': f'Exception: {e}', 
                    'test': testName})
            
        # Checks Last Login (EST)
        estTimeToCheck = f'[0;34mLast Login (EST): {time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(lastLogin - 18000))} EST'
        testName = f'stats Command Last Login (EST) After {testContext}'
        try:
            tests.append({'passed': message.content.split('\n')[8] == estTimeToCheck, 
                            'expectedResult': estTimeToCheck, 
                            'actualResult': message.content.split('\n')[8], 
                            'test': testName})
        except Exception as e:
            tests.append({'passed': False, 
                            'expectedResult': estTimeToCheck, 
                            'actualResult': f'Exception: {e}', 
                            'test': testName})
            
        # Checks Days Logged In In A Row
        daysLoggedInInARowToCheck = f'[0;36mDays Logged In In A Row: {str(daysLoggedInInARow)}'
        testName = f'stats Command Days Logged In In A Row After {testContext}'
        try:
            tests.append({'passed': message.content.split('\n')[9] == daysLoggedInInARowToCheck, 
                            'expectedResult': daysLoggedInInARowToCheck, 
                            'actualResult': message.content.split('\n')[9], 
                            'test': testName})
        except Exception as e:
            tests.append({'passed': False, 
                            'expectedResult': daysLoggedInInARowToCheck, 
                            'actualResult': f'Exception: {e}', 
                            'test': testName})



async def testIfHaveRole(OUR_MEMBER, roleList: List[str], testContext: str = ''):
    if roleList is not None:
        for roleName in roleList:
            try:
                WeHaveRole = False
                for role in OUR_MEMBER.roles:
                    if role.name == roleName:
                        WeHaveRole = True
                        break
                try:
                    exceptedResult = f'We\'d have the role `{roleName}`'
                    testName = f'Got Role `{roleName}` After Leveling Up After {testContext}'
                    tests.append({'passed': WeHaveRole, 
                                    'expectedResult': exceptedResult, 
                                    'actualResult': [role.name for role in OUR_MEMBER.roles], 
                                    'test': testName})
                except Exception as e:
                    tests.append({'passed': False,
                                    'expectedResult': exceptedResult,
                                    'actualResult': f'Exception: {e}',
                                    'test': testName})
            except Exception as e:
                await writeExepctoinToLogFile(e, traceback.format_exc())



async def testLoginMessage(TESTING_CHANNEL, type: str, amount: int, daysLoggedInInARow: int, testContext: str, 
                            message1ToCheck: str = 'You have made your daily login!'):
    # rewrite this function to work with money too along with cards
    index: int = 0
    async for message in TESTING_CHANNEL.history(limit=2):
        if index == 0:
            index += 1
            if type == 'xp':
                message0ToCheck = f'Congratulations! You have received {amount} XP for logging in {daysLoggedInInARow} days in a row!'
            elif type == 'money':
                message0ToCheck = f'Congratulations! You have received ${amount} for logging in {daysLoggedInInARow} days in a row!'
            testName = f'login message 0 After {testContext}'
            try:
                tests.append({'passed': message.content == message0ToCheck, 
                                    'expectedResult': message0ToCheck, 
                                    'actualResult': message.content, 
                                    'test': testName})
            except Exception as e:
                tests.append({'passed': False, 
                                'expectedResult': message0ToCheck, 
                                'actualResult': f'Exception: {e}', 
                                'test': testName})
        else:
            testName = f'login message 1 After {testContext}'
            try:
                tests.append({'passed': message.content == message1ToCheck, 
                                    'expectedResult': message1ToCheck, 
                                    'actualResult': message.content, 
                                    'test': testName})
            except Exception as e:
                tests.append({'passed': False,
                                'expectedResult': message1ToCheck,
                                'actualResult': f'Exception: {e}',
                                'test': testName})