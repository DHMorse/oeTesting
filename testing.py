import selfcord
import time
import random
import asyncio
from mySecrets import TOKEN

client = selfcord.Client()

MY_USER_ID = 1214760182576324680

@client.event
async def on_ready():
    TESTING_CHANNEL = client.get_channel(1320533335054749817)

    #async with TESTING_CHANNEL.typing():
    #    await asyncio.sleep(random.randint(5, 10))
    #    async for command in TESTING_CHANNEL.slash_commands():
    #        if command.name == "leaderboard":
    #            await command(TESTING_CHANNEL)

    #await asyncio.sleep(5)

    async for message in TESTING_CHANNEL.history(limit=1):
        #print(message)
        #print(message.content)
        #print(message.attachments)
        print(message.attachments[0].to_dict())
        #print(message.attachments[0].url)
    
# Run the bot with your token
client.run(TOKEN)
