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
"Very doubtful.",
"Bitch don't bother me right now"]
    await ctx.send(f"Question: {question} \nAnswer: {random.choice(responses)}")


@client.command(aliases = ["pun", "Pun"])
async def _pun(ctx):
    puns = ["I knew a woman who owned a taser. Man, she was stunning!",
"I meant to look for my missing watch, but I could never find the time.",
"Did you hear about that great new shovel? It's groundbreaking.",
"The whiteboard is remarkable.",
"Inspecting mirrors is a job I could really see myself doing.",
"Two antennas got married last Saturday. The reception was fantastic.",
"Writing with a dull pencil is pointless.",
"The golfer brought an extra pair of pants in case he got a hole in one.",
"Why does Peter Pan fly all the time? He Neverlands.",
"I wondered why the baseball was getting bigger. Then it hit me.",
"I did a performance about puns. Really it was just a play on words.",
"What do you call an alligator in a vest? An investigator.",
"What would you call a fish with a missing eye? A fsh, probably.",
"What do you call a piece of toast at the zoo? Bread in captivity."
]
    PunsEmbed = discord.Embed(
        description=random.choice(puns), 
        color=0x4B0082)
    await ctx.channel.send(embed = PunsEmbed)

@client.command()
async def PickupLine(ctx):
    pickups =  ["Well, here I am. What are your other two wishes?",
"Hey, my name's Micorsoft. Can I crash at your place tonight?",
"Are you french? Because Eiffel for you.",
"Do you like raisins? How do you feel about a date?",
"There is something wrong with my cellphone. It doesn't have your number in it.",
"If I could rearrange the alphabet, I'd put U and I together.",
"I'm so sorry! I'm so clumsy, I just happened to fall for you.",
"Are you from Tennessee? Because you're the only 10 I see!",
"Are you a parking ticket? Because you've got FINE written all over you.",
"I must be in a museum, because you truly are a work of art.",
"Do you believe in love at first sight - or should I walk by again?",
"I'm no photographer, but I can picture us together.",
"Feel my shirt. Know what it's made of? Boyfriend material.",
"If you were a chicken, you'd be impeccable.",
"I'm learning about important dates in history. Wanna be one of them?"
]
    PickupsEmbed = discord.Embed(
        description=random.choice(pickups), 
        color=0xff00ff)
    
    await ctx.channel.send(embed = PickupsEmbed)


@client.command()
async def Roast(ctx, *, member: discord.Member):
    roasts = ["You're as useless as the ueue in queue.",
"Mirrors can't talk. Lucky for you they can't laugh either.",
"Hey, you have something on your chin. No, the third one.",
"You're the reason the gene pool needs a lifeguard.",
"If I had a face like yours, I'd sue my parents.",
"Your only chance of getting laid is to crawl up a chicken's butt and wait.",
"Some day you'll go far... and I hope you stay there.",
"You must have been born on a highway, cuz that's where most accidents happen.",
"If laughter is the best medicine, your face must be curing the world.",
"I'm glad to see you're not letting your education get in the way of your ignorance.",
"Is your ass jealous of the amount of shit that just came out of your mouth?",
"So, a thought crossed your mind? Must have been a short trip.",
"If I wanted to kill myself, I'd jump from your ego to your IQ.",
"When I see your face, there's not a thing I would change... except the direction I was walking in.",
"If I had a dollar for every time you said something smart, I'd be broke.",
"When you were born, the doctor threw you out the window, but the window threw you back.",
"I love what you've done with your hair. How do you get it to come out of the nostrils like that?"
]
    roastsEmbed = discord.Embed(
        description=str(member) + ", " + random.choice(roasts),
        color=0xFF0000)

    await ctx.channel.send(embed = roastsEmbed)
    

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
        color=0xff8c00)
    await ctx.channel.send(embed=SlapEmbed)

@client.command(aliases = ["helpteach", "help learn"])
async def learn(ctx):
    InstructionEmbed = discord.Embed(
        description="Enter the command \'teach\', with a parameter in the form of futurecommand_response. With this, you will be able to enter the command \'learned\' in the future and get the response. Example: *teach slap_ouch. \n \n *learned slap \n ouch. \n \n IMPORTANT: the futurecommand part can only be one word.", 
        color=0x1520A6)
    await ctx.channel.send(embed = InstructionEmbed)

data = {"Place holder": "This is a placeholder for testing", "good":"bad"}

def add(a, b):
    data[a] = b

def get(a):
    if (a in data):
        return data[a]
    else :
        return "command doesn't exist"

names = []
def getAliase(a):
    for i in data.keys():
        names.append(str(i))
    return names

@client.command()
async def teach(ctx, lesson):
    a = lesson.split("_")
    add(a[0], a[1])
    await ctx.channel.send(get(a[0]))
    await ctx.channel.send(data.keys())

@client.command(aliases = ["learnedcommand"])
async def learned(ctx, learned):
    await ctx.channel.send(get(learned))

#@client.command(aliases = ["gay", "howgay", "gaytest"])
#async def gaytest(ctx, name):
#    if name == "vinniethepooh#2308" or name == "CHEWBACHY#0561"
#        gay_rate = randint(70, 100)
#    else:
#        gay_rate = randint(1, 100)
#    await ctx.send(f"{name} is {gay_rate}% gay.")

client.run("Njk2NDczNTA1MzE0ODk3OTQw.XopPfw.rl3qaCbxQXjD5ZfIyVfk5_K0pQQ")