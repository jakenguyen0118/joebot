from dotenv import load_dotenv
import asyncio
import random
import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True  # Subscribe to the privileged members intent.


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('GUILD_TOKEN')

bot = discord.Client()
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    for guild in bot.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{bot.user.name} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')


@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to SEIR-831 JoeBot server!'
    )


@bot.command(name='learn', help='Learn new skills or tech!')
async def learn(ctx):

    what_to_learn = [
        'D3 - https://d3js.org/',
        'Newline - https://www.newline.co/',
        'D3 - https://bl.ocks.org/',
        'D3 In Depth - https://www.d3indepth.com/force-layout/',
        'Framer Motion - https://www.framer.com/motion/',
        'Angular - https://angular.io/',
        'Free Intro to Python - https://www.codecademy.com/learn/learn-python'
    ]

    response = random.choice(what_to_learn)
    await ctx.send(response)


@bot.command(name='exit', help='Link to submit our exit tickets.')
async def exit(ctx):

    response = "Exit Tickets…https://docs.google.com/forms/d/e/1FAIpQLSdCHYfZzSxaGurK5vf5ams5n7cdE7UCa4hghwYAlEhE_A_gFA/viewform"
    await ctx.send(response)

bot.run(TOKEN)
