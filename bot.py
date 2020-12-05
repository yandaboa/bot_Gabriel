import discord
import random
from discord.ext import commands
from random import randint

import discord
import logging

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

client = commands.Bot(command_prefix = "mar ")

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.command()
async def ping(ctx):
    await ctx.send(f"Your's truly's bot ping is: {round(client.latency * 1000)} ms")

@client.command()
async def talk(ctx):
    await ctx.send(f"I do not serve any master, type \'?\' to get a list of commands.")

@client.command(aliases = ["8ball", "eightball"])
async def _8ball(ctx, *, question):
    responses = ["It is certain.", 
"It is decidedly so.",
"Without a doubt.",
"Yes - definitely.",
"You may rely on it.",
"As I see it, yes.",
"Most likely.",
"Outlook good.",
"Yes.",
"Signs point to yes.",
"Reply hazy, try again.",
"Ask again later.",
"Better not tell you now.",
"Cannot predict now.",
"Concentrate and ask again.",
"Don't count on it.",
"My reply is no.",
"My sources say no.",
"Outlook not so good.",
"Very doubtful."]
    await ctx.send(f"Question: {question} \nAnswer: {random.choice(responses)}")

@client.event
async def on_member_join(member):
    channel = client.get_channel(680879232490274865)
    await channel.send(f"{member} has just joined us. Welcome!")

@client.event
async def on_member_remove(member):
    channel = client.get_channel(680879232490274865)
    await channel.send(f"{member} has left us. Get outa here bro.")

@client.command()
@commands.has_permissions(administrator=True)
async def clear(ctx, amount = 5):
    amount += 1
    await ctx.channel.purge(limit=amount)

@commands.command()
@commands.has_permissions(kick_members=True)
async def kick(self, ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'User {member} has been kicked')

@client.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason = None):
    await member.ban(reason=reason)

@client.command(aliases = ["diceroll", "rolldice"])
async def dice_roll(ctx, range_1 = 6):
    result = randint(1, range_1)
    await ctx.send("The dice roll of d" + str(range_1) + " gave you a result of " + str(result))

#@client.command(aliases = ["gay", "howgay", "gaytest"])
#async def gaytest(ctx, name):
#    if name == "vinniethepooh#2308" or name == "CHEWBACHY#0561"
#        gay_rate = randint(70, 100)
#    else:
#        gay_rate = randint(1, 100)
#    await ctx.send(f"{name} is {gay_rate}% gay.")


client.run("Njk2NDczNTA1MzE0ODk3OTQw.XopPfw.rl3qaCbxQXjD5ZfIyVfk5_K0pQQ")