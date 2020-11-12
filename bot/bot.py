from dotenv import load_dotenv
import asyncio
import random
import os
import discord
from unit_hw import hw_unit1, hw_unit2, hw_unit3, hw_unit4
from unit_lectures import unit1_lectures, unit2_lectures, unit3_lectures, unit4_lectures
from bonus import bonus_lectures
from ipa import drinks
from greece_pics import greece_pics
from what_to_learn import what_to_learn
from dates import date_suggestions
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

@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to SEIR-831 JoeBot server!'
    )

@bot.command(name='learn', help='Learn new skills or tech!')
async def learn(ctx):

    response = random.choice(what_to_learn)
    await ctx.send(response)

@bot.command(name='exit', help='Link to submit our exit tickets.')
async def exit(ctx):

    response = "Exit Tickets…\nhttps://docs.google.com/forms/d/e/1FAIpQLSdCHYfZzSxaGurK5vf5ams5n7cdE7UCa4hghwYAlEhE_A_gFA/viewform"
    await ctx.send(response)

@bot.command(name='hwlink', help='Link to submit your hw.')
async def hwlink(ctx):

    response = "HW Submission\n https://docs.google.com/forms/d/1pyy5-MMDmUkkupg8m659ZGNawQpGFz71HSXcv_xAx2g/viewform?edit_requested=true"
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
    msg = f'I am not as good as Alex at making YouTube tutorials(for now)... so go check out his channel instead of mine.\nhttps://www.youtube.com/channel/UCoc4UCEetAt3htM3hV1dQgQ'
    await ctx.send(msg)

@bot.command(name='devnursery', help='All things you wish to learn taught by Alex Merced.')
async def devnursery(ctx):
    msg = f'Wish to learn anything and everything? Go to https://main.devnursery.com/'
    await ctx.send(msg)

@bot.command(name='nasa', help='JoeBot\'s favorite website')
async def nasa(ctx):
    msg = f'I love this NASA website on Mars... Click on the link and open up your chrome dev tools to investigate their tech.\n https://mars.nasa.gov/'
    await ctx.send(msg)

@bot.command(name='greece', help='JoeBot\'s favorite destination')
async def greece(ctx):

    love_greece = 'I love Greece... \n'
    response = random.choice(greece_pics)
    msg = love_greece + response
    await ctx.send(msg)

@bot.command(name='partytime', help='Recommendation for drinks')
async def partytime(ctx):

    msg = 'I would recommend '
    drink = random.choice(drinks)
    response = msg + drink
    await ctx.send(response)

@bot.command(name='unit1', help='All lectures for Unit 1')
async def unit1(ctx):

    for i in unit1_lectures:
        await ctx.send(i)

@bot.command(name='unit1hw', help='All Unit 1 HW')
async def unit1_hw(ctx):

    for i in hw_unit1:
        await ctx.send(i)

@bot.command(name='unit2', help='All lectures for Unit 2')
async def unit2(ctx):

    for i in unit2_lectures:
        await ctx.send(i)

@bot.command(name='unit2hw', help='All Unit 2 HW')
async def unit2_hw(ctx):

    for i in hw_unit2:
        await ctx.send(i)

@bot.command(name='unit3', help='All lectures for Unit 3')
async def unit3(ctx):

    for i in unit3_lectures:
        await ctx.send(i)

@bot.command(name='unit3hw', help='All Unit 3 HW')
async def unit3_hw(ctx):

    for i in hw_unit3:
        await ctx.send(i)

@bot.command(name='unit4', help='All lectures for Unit 4')
async def unit4(ctx):

    for i in unit4_lectures:
        await ctx.send(i)

@bot.command(name='unit4hw', help='All Unit 4 HW')
async def unit4_hw(ctx):

    for i in hw_unit4:
        await ctx.send(i)

@bot.command(name='bonuslecture', help='Bonus Lectures during project week')
async def bonus_lecture(ctx):

    for i in bonus_lectures:
        await ctx.send(i)

@bot.command(name='datenight', help='Love Guru JoeBot will give suggestions for dates')
async def date_night(ctx):

    msg = random.choice(date_suggestions)
    await ctx.send(msg)

bot.run(TOKEN)