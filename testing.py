import selfcord
import time
import random
import requests

from typing import List, Dict

from mySecrets import TOKEN

client = selfcord.Client()

MY_USER_ID = 1214760182576324680


@client.event
async def on_ready():
    channel = client.get_channel(1320533335054749817)
    print(channel.history(limit=2))

# Run the bot with your token
client.run(TOKEN)