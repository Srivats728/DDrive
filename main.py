import discord, os
import asyncio
import random
from keep_alive import keep_alive, get

client = discord.Client(intents=discord.Intents.all())


@client.event
async def on_ready():
  print('Logged in as')
  print(client.user.name)
  print(client.user.id)
  print('------')


@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.author.bot:
    if message.attachments:
      get(message.attachments[0].url)
  else:
    return


keep_alive()
client.run(os.getenv("token"))
