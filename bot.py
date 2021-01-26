# bot.py
import os

import discord
from dotenv import load_dotenv

import random
from datetime import datetime

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        print(guild.name)

        print(
            f'\t{client.user} is connected to the following guild:\n'
            f'\t{guild.name}(id: {guild.id})\n'
        )
        print('\n')

@client.event
async def on_message(message):
    approved_messages = ['!Cheems! Cheems! Give me Cheems!', 'Cheems! Cheems! Give me Cheems!', '!Cheems', '!cheems']

    random.seed(datetime.now())
    lobster = [pic for pic in os.listdir('lobster-pics')]

    if message.author == client.user:
        return
    for i in approved_messages:
        if message.content == i:
            await message.channel.send(file=discord.File('lobster-pics/' + random.choice(lobster)))


client.run(TOKEN)