# comment out dotenv before pushing
# from dotenv import load_dotenv

import json
import requests
import asyncio
import random
import os
import discord
# import Question
from data import *
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
# client = Question.Trivia()
# client.run(TOKEN)

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
    codewars_api_url = 'https://www.codewars.com/api/v1/code-challenges/'
    slugs = random.choice(codewars_slugs)
    api_call = codewars_api_url + slugs
    r = requests.get(api_call)
    json = r.json()
    channel = ctx.message.channel
    algo_name = json['name']
    algo_url = json['url']
    algo_rank = json['rank']['name']

    e = discord.Embed(
        title='It\'s algos time... I\'ll hand it over to the illustrious Kenny Cruz...')
    e.add_field(name='Name', value=algo_name, inline=False)
    e.add_field(name='URL', value=algo_url, inline=False)
    e.add_field(name='Rank', value=algo_rank, inline=False)

    await channel.send(embed=e)


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
    msg = 'I love Greece...\n'
    greece = random.choice(greece_pics)
    await ctx.send(msg + greece)


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


@bot.command(name='unit1labs', help='All Unit 1 Labs')
async def unit1_labs(ctx):

    for i in lab_unit1:
        await ctx.send(i)


@bot.command(name='unit2', help='All lectures for Unit 2')
async def unit2(ctx):

    for i in unit2_lectures:
        await ctx.send(i)


@bot.command(name='unit2hw', help='All Unit 2 HW')
async def unit2_hw(ctx):

    for i in hw_unit2:
        await ctx.send(i)


@bot.command(name='unit2labs', help='All Unit 2 Labs')
async def unit2_labs(ctx):

    for i in lab_unit2:
        await ctx.send(i)


@bot.command(name='unit3', help='All lectures for Unit 3')
async def unit3(ctx):

    for i in unit3_lectures:
        await ctx.send(i)


@bot.command(name='unit3hw', help='All Unit 3 HW')
async def unit3_hw(ctx):

    for i in hw_unit3:
        await ctx.send(i)


@bot.command(name='unit3labs', help='All Unit 3 Labs')
async def unit3_labs(ctx):

    for i in lab_unit3:
        await ctx.send(i)


@bot.command(name='unit4', help='All lectures for Unit 4')
async def unit4(ctx):

    for i in unit4_lectures:
        await ctx.send(i)


@bot.command(name='unit4hw', help='All Unit 4 HW')
async def unit4_hw(ctx):

    for i in hw_unit4:
        await ctx.send(i)


@bot.command(name='unit4labs', help='All Unit 4 Labs')
async def unit4_labs(ctx):

    for i in lab_unit4:
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
    ios_greece_url = 'http://api.openweathermap.org/data/2.5/weather?q=ios,gr&appid=ae98347c1a7e1fa54f1fe3e03a8d9f57'
    r = requests.get(ios_greece_url)
    response = requests.get(complete_url)
    json = response.json()
    x = r.json()
    channel = ctx.message.channel

    if json['cod'] != '404':
        async with channel.typing():
            y = json['main']
            city_name = json['name']
            current_temperature = y['temp']
            current_temperature_celcius = str(
                round(current_temperature - 273.15))
            current_temperature_f = str(
                round(((current_temperature - 273.15) * 1.8) + 32))
            current_pressure = y['pressure']
            current_humidity = y['humidity']
            z = json['weather']
            ios = x['main']
            ios_city = x['name']
            ios_current_temp = ios['temp']
            ios_current_temp_c = str(round(ios_current_temp - 273.15))
            ios_current_temp_f = str(
                round(((ios_current_temp - 273.15) * 1.8) + 32))
            ios_current_pressure = ios['pressure']
            ios_current_humidity = ios['humidity']
            ios_b = x['weather']
            ios_weather_desc = ios_b[0]['description']
            weather_description = z[0]['description']
            e = discord.Embed(title=f'Weather in {city_name}')
            e.add_field(name='Description',
                        value=f'**{weather_description}**', inline=False)
            e.add_field(name='Temperature(F)',
                        value=f'{current_temperature_f}', inline=False)
            e.add_field(name='Temperature(C)',
                        value=f'{current_temperature_celcius}', inline=False)
            e.add_field(name="Humidity(%)",
                        value=f"{current_humidity}%", inline=False)
            e.add_field(name="Atmospheric Pressure(hPa)",
                        value=f"{current_pressure}hPa", inline=False)
            e.add_field(name=f'But why go to {city_name} when you can go to {ios_city}, Greece!',
                        value='Look at the weather at Ios!', inline=False)
            e.add_field(name='Description',
                        value=f'**{ios_weather_desc}**', inline=False)
            e.add_field(name='Temperature(F)',
                        value=f'{ios_current_temp_f}', inline=False)
            e.add_field(name='Temperature(C)',
                        value=f'{ios_current_temp_c}', inline=False)
            e.add_field(name="Humidity(%)",
                        value=f"{ios_current_humidity}%", inline=False)
            e.add_field(name="Atmospheric Pressure(hPa)",
                        value=f"{ios_current_pressure}hPa", inline=False)
            e.set_thumbnail(url="https://i.ibb.co/CMrsxdX/weather.png")
            e.set_footer(text=f"Requested by {ctx.author.name}")

        await channel.send(embed=e)
    else:
        await channel.send('Please enter a valid zipcode')

bot.run(TOKEN)
