import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!help'):
        await message.channel.send(f'')
    if message.content.startswith('!easteregg'):
        await message.channel.send(f'U0001f642')



client.run("Tokın")
