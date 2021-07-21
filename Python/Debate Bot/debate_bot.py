import discord
import random
import csv
from discord.ext import commands, tasks
from itertools import cycle 

client = commands.Bot(command_prefix = 'b!')

# client.remove_command('help')

status = cycle(['Status 1','Status 2'])

file_name = 'parliamentary_procedure.csv'

categories = []
motions = []
row_count = 0
points = 5

with open(file_name, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    categories = next(csvreader)
    for row in csvreader:
        motions.append(row)
        row_count += 1
    attributes = len(motions[0])

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Debate'))
#    change_status.start()
    print ("Bot is ready.")

@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

'''
@client.command(pass_context=True)
async def help():
    author = ctx.message.author
'''

@client.command(aliases=['hi','hello','sup'])
async def _hi(ctx):
    greetings = [
        'Hi there',
        'Howdy',
        'Greetings',
        'Hey',
        'What’s up?',
        'Hey!',
        'Good to see you',
        'Great to see you',
        'Nice to see you',
        'Long time no see!'
        ]
    choice = random.choice(greetings)
    await ctx.send(f'{choice}')

@client.command()
async def clear(ctx, amount=1):
    await ctx.channel.purge(limit=amount+1)

@client.command()
async def parlipro(ctx):
    await ctx.send(f'Please wait a few moments \n ---------- \n')
    for procedure in motions:
        await ctx.send(f'{procedure[0]} {procedure[1]}')

@client.command(aliases=['points'])
async def point(ctx):
    for p in range(points):
        await ctx.send(f'{motions[p][0]} {motions[p][1]}')

@client.command(aliases=['motions'])
async def motion(ctx):
    await ctx.send(f'Please wait a few moments \n ---------- \n')
    for m in range(points,row_count):
        await ctx.send(f'{motions[m][0]} {motions[m][1]}')

@client.command()
async def p_order(ctx):
    for value in range(attributes):
        await ctx.send(f'{categories[value]}: {motions[0][value]}')

@client.command()
async def p_personalprivilege(ctx):
    for value in range(attributes):
        await ctx.send(f'{categories[value]}: {motions[1][value]}')

@client.command()
async def p_inquiry(ctx):
    for value in range(attributes):
        await ctx.send(f'{categories[value]}: {motions[2][value]}')

@client.command()
async def p_information(ctx):
    for value in range(attributes):
        await ctx.send(f'{categories[value]}: {motions[3][value]}')

@client.command()
async def rightofreply(ctx):
    for value in range(attributes):
        await ctx.send(f'{categories[value]}: {motions[4][value]}')

@client.command()
async def roundrobin(ctx):
    for value in range(attributes):
        await ctx.send(f'{categories[value]}: {motions[5][value]}')

@client.command()
async def strawpoll(ctx):
    for value in range(attributes):
        await ctx.send(f'{categories[value]}: {motions[6][value]}')

@client.command()
async def unmod(ctx):
    for value in range(attributes):
        await ctx.send(f'{categories[value]}: {motions[7][value]}')

@client.command()
async def mod(ctx):
    for value in range(attributes):
        await ctx.send(f'{categories[value]}: {motions[8][value]}')

@client.command()
async def tablethetopic(ctx):
    for value in range(attributes):
        await ctx.send(f'{categories[value]}: {motions[9][value]}')

@client.command()
async def rollcallvote(ctx):
    for value in range(attributes):
        await ctx.send(f'{categories[value]}: {motions[10][value]}')

@client.command()
async def entervotingprocedure(ctx):
    for value in range(attributes):
        await ctx.send(f'{categories[value]}: {motions[11][value]}')

@client.command(aliases=['limitdebate','extenddebate'])
async def limextdebate(ctx):
    for value in range(attributes):
        await ctx.send(f'{categories[value]}: {motions[12][value]}')

@client.command()
async def introducedraftresolution(ctx):
    for value in range(attributes):
        await ctx.send(f'{categories[value]}: {motions[13][value]}')

@client.command()
async def adoptbyconcensus(ctx):
    for value in range(attributes):
        await ctx.send(f'{categories[value]}: {motions[14][value]}')

@client.command()
async def introduceamendment(ctx):
    for value in range(attributes):
        await ctx.send(f'{categories[value]}: {motions[15][value]}')

@client.command()
async def reconsider(ctx):
    for value in range(attributes):
        await ctx.send(f'{categories[value]}: {motions[16][value]}')

@client.command()
async def opensession(ctx):
    for value in range(attributes):
        await ctx.send(f'{categories[value]}: {motions[17][value]}')

@client.command()
async def recess(ctx):
    for value in range(attributes):
        await ctx.send(f'{categories[value]}: {motions[18][value]}')

@client.command()
async def adjourn(ctx):
    for value in range(attributes):
        await ctx.send(f'{categories[value]}: {motions[19][value]}')

@client.command()
async def settheagenda(ctx):
    for value in range(attributes):
        await ctx.send(f'{categories[value]}: {motions[20][value]}')

@client.command()
async def invite(ctx):
    await ctx.send('')

client.run('')
