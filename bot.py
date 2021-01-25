# bot.py
import os

import discord
from dotenv import load_dotenv

import random

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
    lobster = [pic for pic in os.listdir('lobster-pics')]

    if message.author == client.user:
        return

    if message.content == '!Hello' or '!hello':
        response = "Hello There"
        await message.channel.send(file=discord.File('lobster-pics/' + random.choice(lobster)))


client.run(TOKEN)