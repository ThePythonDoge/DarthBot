import discord as d
import random
import requests
from lxml import html
client = d.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
client.run('MzYzMDg0ODMxOTMzODU3Nzk0.DK8EnQ.j_zBpWJJGruxHXbbF0EPBW0bYfI')

@client.event
async def on_message(message):
    if message.content.startswith('!test'):
        print("testing")
        await add_reaction(message, ':military_medal: ')
