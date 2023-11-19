import os
import discord
import re
import random
#import json
#import requests

API_TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
guild = discord.Guild
    
@client.event
async def on_message(message):
	message_to_reply = None
	message_content = message.content.lower()
	message_author = message.author
	message_type = message.type
	pattern_twitter = re.compile('^https://twitter.com')
	pattern_x = re.compile('https://x.com')
	if message_type == discord.MessageType.reply:
		channel = client.get_channel(message.reference.channel_id)
		message_to_reply = await channel.fetch_message(message.reference.message_id)
	if pattern_twitter.match(message_content):
		await message.delete()
		tmp = message_content.split('twitter')
		newmessage = "".join(tmp[0]+'fxtwitter'+tmp[1])
		if message_to_reply:
			await message_to_reply.reply(newmessage+f" ({message.author.display_name})")
		else:	
			await message.channel.send(newmessage+f" ({message.author.display_name})")
	elif pattern_x.match(message_content):
		await message.delete()
		tmp = message_content.split('x.com')
		newmessage = "".join(tmp[0]+'fixupx.com'+tmp[1])
		if message_to_reply:
			await message_to_reply.reply(newmessage+f" ({message.author.display_name})")
		else:	
			await message.channel.send(newmessage+f" ({message.author.display_name})")
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

client.run(API_TOKEN)
