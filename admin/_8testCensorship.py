import random
import asyncio

from globalVars import CLEAN_MESSAGES, tests

async def messageIsNotDeleted(TESTING_CHANNEL, ourMessage):
    async for message in TESTING_CHANNEL.history(limit=1):
        return message.content == ourMessage

async def testCensorship(TESTING_CHANNEL):
    for index, message in enumerate(CLEAN_MESSAGES):
        async with TESTING_CHANNEL.typing():
            await asyncio.sleep(random.randint(1, 5))
            await TESTING_CHANNEL.send(message)

        await asyncio.sleep(5)

        try:
            tests.append({'passed': await messageIsNotDeleted(TESTING_CHANNEL, message), 
                            'expectedResult': False, 
                            'actualResult': await messageIsNotDeleted(TESTING_CHANNEL, message), 
                            'test': f'Message {index} was not censored'})
        except:
            tests.append({'passed': False, 'expectedResult': False, 'actualResult': f'Exception: {e}', 'test': f'Message {index} was not censored'})