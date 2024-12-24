import asyncio
import random
import traceback

from globalVars import tests
from globalVars import writeExepctoinToLogFile

async def getLeaderboard(TESTING_CHANNEL, TEST_OUTPUT_FILE_LOCATION):
    async with TESTING_CHANNEL.typing():
        await asyncio.sleep(random.randint(5, 10))
        async for command in TESTING_CHANNEL.slash_commands():
            if command.name == "leaderboard":
                await command(TESTING_CHANNEL)

    await asyncio.sleep(3)

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