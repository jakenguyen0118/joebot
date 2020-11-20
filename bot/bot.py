# comment out dotenv before pushing
# from dotenv import load_dotenv

import json
import requests
import asyncio
import random
import os
import discord
from data import *
# import Trivia
# from Question import Question
# from trivia_questions import *
from discord.ext import commands

intents = discord.Intents.all()
intents.members = True
intents.messages = True

# comment out loadenv before pushing
# load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('GUILD_TOKEN')
WEATHERAPI = os.getenv('WEATHERAPI')

bot = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='!', intents=intents)
# Trivia = Trivia.Trivia(bot)


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
        f'Hi {member.name}, welcome to JoeBot\'s Playground! Use the !help command in the server to get started.'
    )


@bot.command(name='article', help='Read some interesting articles!')
async def article(ctx):
    parameters = {'per_page': 50, 'page': random.randint(1, 460)}
    r = requests.get('https://dev.to/api/articles', params=parameters)
    article_url = r.json()[random.randint(0, 50)]['url']
    e = discord.Embed(title='Check this out...')
    e.add_field(name='Article', value=article_url, inline=False)
    await ctx.send(embed=e)


@bot.command(name='exit', help='Link to submit our exit tickets.')
async def exit(ctx):

    response = "https://docs.google.com/forms/d/e/1FAIpQLSdCHYfZzSxaGurK5vf5ams5n7cdE7UCa4hghwYAlEhE_A_gFA/viewform"
    e = discord.Embed(title='Exit tickets...')
    e.add_field(name='SEIR-831 Exit Tickets', value=response, inline=False)
    await ctx.send(embed=e)


@bot.command(name='hwlink', help='Link to submit your hw.')
async def hwlink(ctx):

    response = "HW Submission\n https://docs.google.com/forms/d/1pyy5-MMDmUkkupg8m659ZGNawQpGFz71HSXcv_xAx2g/viewform?edit_requested=true"
    e = discord.Embed(title='HW Submission...')
    e.add_field(name='SEIR-831 HW Submission', value=response, inline=False)
    await ctx.send(embed=e)


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
    msg = f'https://www.youtube.com/channel/UCoc4UCEetAt3htM3hV1dQgQ'
    e = discord.Embed(title='Alex\'s YouTube...')
    e.add_field(name='I am not as good as Alex at making YouTube tutorials(for now)... so go check out his channel instead of mine.',
                value=msg, inline=False)
    await ctx.send(embed=e)


@bot.command(name='devnursery', help='All things you wish to learn taught by Alex Merced.')
async def devnursery(ctx):
    msg = f'Go to https://main.devnursery.com/'
    e = discord.Embed(title='DevNursery')
    e.add_field(name='Wish to learn anything and everything?',
                value=msg, inline=False)
    await ctx.send(embed=e)


@bot.command(name='nasa', help='JoeBot\'s favorite website')
async def nasa(ctx):
    msg = f'https://mars.nasa.gov/'
    e = discord.Embed(title='NASA Mars')
    e.add_field(name='I love this NASA website on Mars... Click on the link and open up your chrome dev tools to investigate their tech...', value=msg, inline=False)
    await ctx.send(embed=e)


@bot.command(name='greece', help='JoeBot\'s favorite destination')
async def greece(ctx):

    response = random.choice(greece_pics)
    e = discord.Embed(title='I love Greece...')
    e.add_field(name='I can\'t wait to go here...', value=response, inline=False)
    await ctx.send(embed=e)


@bot.command(name='partytime', help='Recommendation for drinks')
async def partytime(ctx):

    drink = random.choice(drinks)
    e = discord.Embed(title='Party Time')
    e.add_field(name='I recommend...', value=drink, inline=False)
    await ctx.send(embed=e)


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


@bot.command(name='projects', help='I am so proud of my students\' projects, so please take a look!')
async def projects(ctx):

    msg = random.choice(unit_projects)
    e = discord.Embed(title='Student Projects')
    e.add_field(name='Check out...', value=msg, inline=False)
    await ctx.send(embed=e)


@bot.command(name='weather', help='JoeBot will check the weather of any location you desire!')
async def weather(ctx, *, zipcode: int):
    weather_zip = str(zipcode).zfill(5)
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + 'zip=' + weather_zip + '&appid=' + WEATHERAPI
    response = requests.get(complete_url)
    json = response.json()
    channel = ctx.message.channel

    if json['cod'] != '404':
        async with channel.typing():
            y = json['main']
            city_name = json['name']
            current_temperature = y['temp']
            current_temperature_celcius = str(round(current_temperature - 273.15))
            current_temperature_f = str(round(((current_temperature - 273.15) * 1.8) + 32))
            current_pressure = y['pressure']
            current_humidity = y['humidity']
            z = json['weather']
            weather_description = z[0]['description']
            e = discord.Embed(title=f'Weather in {city_name}')
            e.add_field(name='Description', value=f'**{weather_description}**', inline=False)
            e.add_field(name='Temperature(F)', value=f'**{current_temperature_f}**', inline=False)
            e.add_field(name='Temperature(C)', value=f'**{current_temperature_celcius}**', inline=False)
            e.add_field(name="Humidity(%)", value=f"**{current_humidity}%**", inline=False)
            e.add_field(name="Atmospheric Pressure(hPa)", value=f"**{current_pressure}hPa**", inline=False)
            e.set_thumbnail(url="https://i.ibb.co/CMrsxdX/weather.png")
            e.set_footer(text=f"Requested by {ctx.author.name}")
            
        await channel.send(embed=e)
    else:
        await channel.send('City not found.')


# @bot.command(name='trivia', help='Test your general or coding knowledge with JoeBot!')
# async def trivia(ctx):
#     e = discord.Embed(title='Welcome to JoeBot Trivia!')
#     e.add_field(name='Which category would you like to be tested on?', value='0. Quit\n1. General\n2. Javascript\n3. React', inline=True)
#     await ctx.send(embed=e)

#     @bot.event
#     async def on_message(message):
#         # def run_trivia(questions):
#         #     score = 0
#         #     random.shuffle(questions)
#         #     for index, question in questions:
#         #         print(question.prompt)
#         #         answer = input("Please answer with a, b, c, d or quit: ")
#         #         if answer == question.answer:
#         #             print("Correct!")
#         #             score += 1
#         #         elif answer == "quit":
#         #             print("Sorry you didn\'t finish the game, but you scored " + str(score) + " points!")
#         #             quit()
#         #         else:
#         #             print("You did not answer correctly... The answer was " + question.answer)
#         #     print("You got " + str(score) + " questions correct!")

#         if message.content.startswith('0'):
#             channel = message.channel
#             await channel.send('Thank you for playing JoeBot trivia!')
#             quit()
        
#         if message.content.startswith('1'):
#             channel = message.channel
#             await channel.send('Starting JoeBot\'s General Trivia...')

#         if message.content.startswith('2'):
#             channel = message.channel
#             await channel.send('Starting JoeBot\'s Javascript Trivia...')

#         if message.content.startswith('3'):
#             channel = message.channel
#             await channel.send('Starting JoeBot\'s React Trivia...')
            


bot.run(TOKEN)
