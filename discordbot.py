import discord
from discord.ext import commands
import os

# files
import opensea

from dotenv import load_dotenv
load_dotenv()

description = ''

# investigate this more
# intents = discord.Intents.default()
# intents.members = True

bot = commands.Bot(command_prefix='!', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def floor(ctx, collection: str):
    print(collection)
    await ctx.send(opensea.get_collection(collection))

bot.run(os.environ['discord_key'])