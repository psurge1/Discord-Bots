import discord
import random
from discord.ext import commands, tasks
from itertools import cycle 

client = commands.Bot(command_prefix = '')

# client.remove_command('help')

status = cycle(['Pranking','Trolling'])

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

meme_phrase = []

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Testing'))
    change_status.start()
    print ("Bot is ready.")

@tasks.loop(seconds=5)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

@client.command(aliases=[''])
async def memes(ctx):
    for number in range (5):
        meme_phrase = ''
        for num in range (40):
            meme_phrase = '@everyone ' + meme_phrase + random.choice(alphabet)
        await ctx.send(meme_phrase)

@client.command(aliases=['hi','hello','sup'])
async def greetings(ctx):
    greetings = [
        'Hi there!',
        'Howdy!',
        'Greetings',
        'Hey',
        'What’s up?',
        'Hey!',
        'Good to see you!',
        'Great to see you!',
        'Nice to see you!',
        'Long time no see!'
        ]
    choice = random.choice(greetings)
    await ctx.send(f'{choice}')    

@client.command()
async def clear(ctx, amount=2):
    await ctx.channel.purge(limit=amount+1)

@client.command()
async def invite_bot(ctx):
    await ctx.send('<https://discord.com/api/oauth2/authorize?client_id=832696265212821514&permissions=162816&scope=bot>')


client.run('ODMyNjk2MjY1MjEyODIxNTE0.YHni1A.t09QeJz3Od6qaP7uwsjQ9cppzSg')
