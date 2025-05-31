# This example requires the 'message_content' intent.

import discord
import psutil
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
processes = list(p.name() for p in psutil.process_iter())
count = processes.count("minecraft_server")# This is where you put the name of the server process
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!Status'):
        print('Status command received')
        #await message.channel.send('Hello!')
        if 0 == count:
            await message.channel.send('Server is Offline')
        else:
            await message.channel.send('Server is Online')

print('Starting the bot...')

client.run('') #put your bot token here that you get from discord.com/developers/applications
