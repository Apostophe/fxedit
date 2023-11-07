import os
import discord
import re

API_TOKEN = os.getenv('DISCORD_TOKEN')
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
guild = discord.Guild

if __name__ == "__main__":
	client.run(API_TOKEN)	

    
@client.event
async def on_message(message):
	message_content = message.content
	message_author = message.author
	print(message_content)
	pattern = re.compile('^https://twitter.com')
	if pattern.match(message_content):
		await message.delete()
		tmp = message_content.split('twitter')
		newmessage = "".join(tmp[0]+'fxtwitter'+tmp[1])
		await message.channel.send(newmessage+f" ({message.author.display_name})")
		await message.delete()
