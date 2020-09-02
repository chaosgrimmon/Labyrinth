import os, discord, random
from discord.ext import commands

TOKEN = os.environ['DISCORD_TOKEN']
client = commands.Bot(command_prefix = '.')

players = {}
pTokens = {}

emojiTokens = ['↖️', '↗️', '↘️', '↙️', '🤖']
playerLock = False
