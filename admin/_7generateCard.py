import random
import asyncio
import requests
import traceback

from globalVars import MY_USER_ID, MY_USER_NAME, tests
from globalVars import writeExepctoinToLogFile

async def generateCard(TESTING_CHANNEL):
    async with TESTING_CHANNEL.typing():
        await asyncio.sleep(random.randint(5, 15))
        async for command in TESTING_CHANNEL.slash_commands():
            if command.name == "generatecard":
                await command(TESTING_CHANNEL, prompt='An anime sword fighter.')

    await asyncio.sleep(30)

    async for message in TESTING_CHANNEL.history(limit=1):
        try:
            tests.append({'passed': message.attachments[0].url.endswith('.png') or message.attachments[0].url.endswith('.jpg'), 
                            'expectedResult': 'Image', 
                            'actualResult': 'Image', 
                            'test': 'Generated Card'})
        except Exception as e:
            tests.append({'passed': False, 'expectedResult': 'Image', 'actualResult': f'Exception: {e}', 'test': 'Generated Card'})
