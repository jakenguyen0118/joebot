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
        'Free Intro to Python - https://www.codecademy.com/learn/learn-python',
        'Django - https://www.djangoproject.com/',
        'Python - https://www.python.org/',
        'Typescript - https://www.typescriptlang.org/',
        'Gatsby - https://www.gatsbyjs.com/',
        'NextJS - https://nextjs.org/',
        'React Native - https://reactnative.dev/'
    ]

    response = random.choice(what_to_learn)
    await ctx.send(response)


@bot.command(name='exit', help='Link to submit our exit tickets.')
async def exit(ctx):

    response = "Exit Tickets…https://docs.google.com/forms/d/e/1FAIpQLSdCHYfZzSxaGurK5vf5ams5n7cdE7UCa4hghwYAlEhE_A_gFA/viewform"
    await ctx.send(response)


@bot.command(name='hwlink', help='Link to submit your hw.')
async def hwlink(ctx):

    response = "HW Submission - https://docs.google.com/forms/d/1pyy5-MMDmUkkupg8m659ZGNawQpGFz71HSXcv_xAx2g/viewform?edit_requested=true"
    await ctx.send(response)


@bot.command(name='saveme', help='Joe will ask you to share screen so that he can save you.')
async def saveme(ctx):
    msg = f'What is the problem {ctx.author.mention}? Let\'s share your screen...'
    await ctx.send(msg)


@bot.command(name='algos', help='Hand it over to the illustrious Kenny Cruz.')
async def algos(ctx):
    msg = f'It\'s algos time... I will hand it off to the ever so illustrious Kenny Cruz.'
    await ctx.send(msg)


@bot.command(name='alex', help='Alex\'s YouTube Channel')
async def alex(ctx):
    msg = f'I am not as good as Alex at making YouTube tutorials(for now)... so go check out his channel instead of mine. https://www.youtube.com/channel/UCoc4UCEetAt3htM3hV1dQgQ'
    await ctx.send(msg)


@bot.command(name='nasa', help='JoeBot\'s favorite website')
async def nasa(ctx):
    msg = f'I love this NASA website on Mars... Click on the link and open up your chrome dev tools to investigate their tech. https://mars.nasa.gov/'
    await ctx.send(msg)


@bot.command(name='greece', help='JoeBot\'s favorite destination')
async def greece(ctx):
    greece_pics = [
        'https://images.unsplash.com/photo-1533105079780-92b9be482077?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60',
        'https://images.unsplash.com/photo-1533104816931-20fa691ff6ca?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60',
        'https://images.unsplash.com/photo-1504512485720-7d83a16ee930?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60',
        'https://images.unsplash.com/photo-1506929562872-bb421503ef21?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60',
        'https://images.unsplash.com/photo-1530841377377-3ff06c0ca713?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60',
        'https://images.unsplash.com/photo-1560703650-ef3e0f254ae0?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60',
        'https://images.unsplash.com/photo-1508855173839-a6d69c12573a?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60',
        'https://images.unsplash.com/photo-1536514072410-5019a3c69182?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60',
        'https://images.unsplash.com/photo-1498712964741-5d33ab9e5017?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60'
    ]

    love_greece = 'I love Greece...'
    response = random.choice(greece_pics)
    msg = love_greece + response
    await ctx.send(msg)
    

bot.run(TOKEN)
