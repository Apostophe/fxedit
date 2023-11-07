import os
import discord
import re
import random
import json
import requests

API_TOKEN = os.getenv('DISCORD_TOKEN')
TENOR_TOKEN = os.getenv('TENOR_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
guild = discord.Guild
    
@client.event
async def on_message(message):
	message_content = message.content.lower()
	message_author = message.author
	print(message_content)
	pattern_twitter = re.compile('^https://twitter.com')
	pattern_x = re.compile('https://x.com')
	if pattern_twitter.match(message_content):
		await message.delete()
		tmp = message_content.split('twitter')
		newmessage = "".join(tmp[0]+'fxtwitter'+tmp[1])
		await message.channel.send(newmessage+f" ({message.author.display_name})")
		await message.delete()
	elif pattern_x.match(message_content):
		await message.delete()
		tmp = message_content.split('x.com')
		newmessage = "".join(tmp[0]+'fixupx.com'+tmp[1])
		await message.channel.send(newmessage+f" ({message.author.display_name})")
		await message.delete()
	if client.user.mentioned_in(message):
		if 't\'as les cramptés' in message_content:
			await message.channel.send("https://tenor.com/view/quoicoubeh-david-la-caill%C3%A9-apagnan-gif-27709036")
		elif 'oui' in message_content:
			await message.channel.send("STITI")
		elif 'comment' in message_content:
			await message.channel.send("DANT DE BORD")
		elif 'quoi' in message_content and 'https://tenor.com/view/quoicoubeh-david-la-caill%C3%A9-apagnan-gif-27709036' not in message_content:
			if random.randint(0, 1):
				await message.channel.send("QOUBEH")
			else:
				await message.channel.send("FEUR !")
		else:
			await get_gif(message,message.channel)
			
async def get_gif(searchTerm,channel):  
	response = requests.get("https://tenor.googleapis.com/v2/search?q={}&key={}&limit=50".format(searchTerm, TENOR_TOKEN))
	data = response.json()
	gif = random.choice(data["results"])
	await channel.send(return gif['media'][0]['gif']['url'])

client.run(API_TOKEN)
