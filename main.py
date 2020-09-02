import os
import discord
import random
from discord.ext import commands

TOKEN = os.environ['DISCORD_TOKEN']
client = commands.Bot(command_prefix = '.')

players = {}
pTokens = {}

emojiTokens = ['↖️', '↗️', '↘️', '↙️', '🤖']
playerLock = False

readyNum = 0
members = {}

@client.event
async def on_ready():
    print("Bot is ready!")
    players.clear()
    
@client.event
async def on_reaction_add(reaction, user):
    if reaction.message.author != client.user:
        return
    if user == client.user:
        return

    
client.run('token')
