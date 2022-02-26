import discord
import os

# files
import opensea

from dotenv import load_dotenv
load_dotenv()

client = discord.Client()

@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
	if (message.author == client.user):
		return

	if (message.content.startswith('!floor')):
		messageArgs = message.content.split()
		await message.channel.send(opensea.get_collection(messageArgs[1]))

client.run(os.environ['discord_key'])