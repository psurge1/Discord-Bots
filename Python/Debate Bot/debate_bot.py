import discord
import random
from discord.ext import commands, tasks
from itertools import cycle 

client = commands.Bot(command_prefix = 'b!')

# client.remove_command('help')

status = cycle(['Status 1','Status 2'])

order = "Order"
motion = "Motion"
inter = "Interruptable"
sec = "Secondable"
deb = "Debatable"
ame = "Amenable"
vot = "Vote"
yes = "Yes"
no = "No"
v_1 = "50% + 1"
v_2 = "Chair's Discretion"
v_3 = f'{v_1} or {v_2}'
v_4 = "2/3 majority"
list_test = []

precede = "Preceding Motion"
succeed = "Succeeding Motion"
list_of_dictionaries = [
{order:1,motion:"Point of Order",inter:yes,sec:no,
 deb:no,ame:no,vot:no},
{order:2,motion:"Point of Personal Privilege",inter:yes,sec:no,
 deb:no,ame:no,vot:no},
{order:3,motion:"Point of Inquiry",inter:yes,sec:no,
 deb:no,ame:no,vot:no},
{order:4,motion:"Point of Information",inter:no,sec:no,
 deb:no,ame:no,vot:no},
{order:5,motion:"Right of Reply",inter:no,sec:no,
 deb:no,ame:no,vot:v_2},
{order:6,motion:"Motion for a Round Robin",inter:no,sec:yes,
 deb:no,ame:no,vot:v_3},
{order:7,motion:"Motion for a Straw Poll",inter:no,sec:yes,
 deb:no,ame:no,vot:v_3},
{order:8,motion:"Motion for an Unmoderated Caucus",inter:no,sec:yes,
 deb:no,ame:yes,vot:v_1},
{order:9,motion:"Motion for a Moderated Caucus",inter:no,sec:yes,
 deb:no,ame:yes,vot:v_1},
{order:10,motion:"Motion to Table the Topic",inter:no,sec:yes,
 deb:'yes',ame:no,vot:v_4},
{order:11,motion:"Motion for a Roll Call Vote",inter:no,sec:yes,
 deb:no,ame:no,vot:v_1},
{order:12,motion:"Motion to Enter Voting Procedure",inter:no,sec:yes,
 deb:'yes',ame:no,vot:v_1},
{order:13,motion:"Motion to Limit/Extend Debate",inter:no,sec:yes,
 deb:no,ame:no,vot:v_1},
{order:14,motion:"Motion to Introduce a Draft Resolution",inter:no,sec:yes,
 deb:no,ame:no,vot:v_1},
{order:15,motion:"Motion to Adopt by Consensus",inter:no,sec:yes,
 deb:no,ame:no,vot:v_1},
{order:16,motion:"Motion to Introduce an Amendment",inter:no,sec:yes,
 deb:no,ame:no,vot:v_1},
{order:17,motion:"Motion to Reconsider",inter:no,sec:yes,
 deb:'yes',ame:no,vot:v_1},
{order:18,motion:"Motion to Open Session",inter:no,sec:yes,
 deb:no,ame:no,vot:v_1},
{order:19,motion:"Motion to Recess",inter:no,sec:yes,
 deb:no,ame:no,vot:v_1},
{order:20,motion:"Motion to Adjourn the Meeting",inter:no,sec:yes,
 deb:no,ame:no,vot:v_1},
{order:21,motion:"Motion to Set the Agenda",inter:no,sec:yes,
 deb:no,ame:no,vot:v_1},
]

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Debate'))
#    change_status.start()
    print ("Bot is ready.")

'''
@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))
'''

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
    for procedure in range(0,21):
        await ctx.send(f'{list_of_dictionaries[procedure][order]} {list_of_dictionaries[procedure][motion]}')

@client.command()
async def points(ctx):
    for point in range(0,5):
        await ctx.send(f'{list_of_dictionaries[point][order]} {list_of_dictionaries[point][motion]}')

@client.command()
async def motions(ctx):
    await ctx.send(f'Please wait a few moments \n ---------- \n')
    for m in range(5,21):
        await ctx.send(f'{list_of_dictionaries[m][order]} {list_of_dictionaries[m][motion]}')

@client.command()
async def p_order(ctx):
    for value in list_of_dictionaries[0]:
        await ctx.send(f'{value}: {list_of_dictionaries[0][value]}')

@client.command()
async def p_personalprivilege(ctx):
    for value in list_of_dictionaries[1]:
        await ctx.send(f'{value}: {list_of_dictionaries[1][value]}')

@client.command()
async def p_inquiry(ctx):
    for value in list_of_dictionaries[2]:
        await ctx.send(f'{value}: {list_of_dictionaries[2][value]}')

@client.command()
async def p_information(ctx):
    for value in list_of_dictionaries[3]:
        await ctx.send(f'{value}: {list_of_dictionaries[3][value]}')

@client.command()
async def rightofreply(ctx):
    for value in list_of_dictionaries[4]:
        await ctx.send(f'{value}: {list_of_dictionaries[4][value]}')

@client.command()
async def roundrobin(ctx):
    for value in list_of_dictionaries[5]:
        await ctx.send(f'{value}: {list_of_dictionaries[5][value]}')

@client.command()
async def strawpoll(ctx):
    for value in list_of_dictionaries[6]:
        await ctx.send(f'{value}: {list_of_dictionaries[6][value]}')

@client.command()
async def unmod(ctx):
    for value in list_of_dictionaries[7]:
        await ctx.send(f'{value}: {list_of_dictionaries[7][value]}')

@client.command()
async def mod(ctx):
    for value in list_of_dictionaries[8]:
        await ctx.send(f'{value}: {list_of_dictionaries[8][value]}')

@client.command()
async def tablethetopic(ctx):
    for value in list_of_dictionaries[9]:
        await ctx.send(f'{value}: {list_of_dictionaries[9][value]}')

@client.command()
async def rollcallvote(ctx):
    for value in list_of_dictionaries[10]:
        await ctx.send(f'{value}: {list_of_dictionaries[10][value]}')

@client.command()
async def entervotingprocedure(ctx):
    for value in list_of_dictionaries[11]:
        await ctx.send(f'{value}: {list_of_dictionaries[11][value]}')

@client.command(aliases=['limitdebate','extenddebate'])
async def limextdebate(ctx):
    for value in list_of_dictionaries[12]:
        await ctx.send(f'{value}: {list_of_dictionaries[12][value]}')

@client.command()
async def introducedraftresolution(ctx):
    for value in list_of_dictionaries[13]:
        await ctx.send(f'{value}: {list_of_dictionaries[13][value]}')

@client.command()
async def adoptbyconcensus(ctx):
    for value in list_of_dictionaries[14]:
        await ctx.send(f'{value}: {list_of_dictionaries[14][value]}')

@client.command()
async def introduceamendment(ctx):
    for value in list_of_dictionaries[15]:
        await ctx.send(f'{value}: {list_of_dictionaries[15][value]}')

@client.command()
async def reconsider(ctx):
    for value in list_of_dictionaries[16]:
        await ctx.send(f'{value}: {list_of_dictionaries[16][value]}')

@client.command()
async def opensession(ctx):
    for value in list_of_dictionaries[17]:
        await ctx.send(f'{value}: {list_of_dictionaries[17][value]}')

@client.command()
async def recess(ctx):
    for value in list_of_dictionaries[18]:
        await ctx.send(f'{value}: {list_of_dictionaries[18][value]}')

@client.command()
async def adjourn(ctx):
    for value in list_of_dictionaries[19]:
        await ctx.send(f'{value}: {list_of_dictionaries[19][value]}')

@client.command()
async def settheagenda(ctx):
    for value in list_of_dictionaries[20]:
        list_test.append(list_of_dictionaries[20][value])
        await ctx.send(f'{value}: {list_of_dictionaries[20][value]}')


client.run('')
