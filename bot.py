import discord
import random
from discord.ext import commands
from random import randint

client = commands.Bot(command_prefix = "*")

@client.command()
async def info(ctx):
    InfoEmbed = discord.Embed(title="Hi! I'm the Gabriel Bot", 
        description="I have many different functions.", 
        color=0x00ff00)
    InfoEmbed.set_thumbnail(url="https://i.pinimg.com/600x315/6b/47/05/6b47050f0f15b955cf725609749e1c87.jpg")
    InfoEmbed.add_field(name="Commands", value="write commands here", inline=False)
    await ctx.channel.send(embed=InfoEmbed)
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.command()
async def ping(ctx):
    await ctx.channel.send(f"Your's truly's bot ping is: {round(client.latency * 1000)} ms")

@client.command()
async def talk(ctx):
    await ctx.channel.send(f"I do not serve any master.")

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
    await channel.channel.send(f"{member} has just joined us. Welcome!")

@client.event
async def on_member_remove(member):
    channel = client.get_channel(680879232490274865)
    await channel.channel.send(f"{member} has left us. Get outa here bro.")

@client.command()
@commands.has_permissions(administrator=True)
async def clear(ctx, amount = 5):
    amount += 1
    await ctx.channel.purge(limit=amount)

@commands.command()
@commands.has_permissions(kick_members=True)
async def kick(self, ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.channel.send(f'User {member} has been kicked')

@client.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason = None):
    await member.channel.ban(reason=reason)

@client.command(aliases = ["diceroll", "rolldice"])
async def dice_roll(ctx, range_1 = 6):
    result = randint(1, range_1)
    await ctx.send("The dice roll of d" + str(range_1) + " gave you a result of " + str(result))
@client.command()
async def slap(ctx, member: discord.Member, *, reason):
    SlapEmbed = discord.Embed(
        description=str(ctx.author) + " has slapped " + str(member) + " " + reason + "!", 
        color=0x00ff00)
    await ctx.channel.send(embed=SlapEmbed)

#@client.command(aliases = ["gay", "howgay", "gaytest"])
#async def gaytest(ctx, name):
#    if name == "vinniethepooh#2308" or name == "CHEWBACHY#0561"
#        gay_rate = randint(70, 100)
#    else:
#        gay_rate = randint(1, 100)
#    await ctx.send(f"{name} is {gay_rate}% gay.")


client.run("Njk2NDczNTA1MzE0ODk3OTQw.XopPfw.rl3qaCbxQXjD5ZfIyVfk5_K0pQQ")