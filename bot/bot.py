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
        'React Native - https://reactnative.dev/',
        'Auth for Ruby on Rails - https://tuts.alexmercedcoder.com/ruby-tut/',
        'DevNursery - https://main.devnursery.com/'
    ]

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

    love_greece = 'I love Greece... \n'
    response = random.choice(greece_pics)
    msg = love_greece + response
    await ctx.send(msg)


@bot.command(name='partytime', help='Recommendation for drinks')
async def partytime(ctx):
    drinks = [
        'Chase\'s preferred brand of Pickle Beer - https://untappd.com/b/martin-house-brewing-company-best-maid-sour-pickle-beer/2646998',
        'Lawson\'s Finest Liquids\' Little Sip - https://oct.co/essays/lawsons-little-sip-review',
        'Tree House\'s Juice Machine - https://oct.co/essays/tree-house-juice-machine-review',
        'Other Half\'s All Together IPA - https://oct.co/essays/other-half-all-together-ipa-review',
        'New England Brewing Company\'s Fuzzy Baby Ducks - https://oct.co/essays/new-england-fuzzy-baby-ducks-review',
        'Abomination\'s Wandering Into the Fog Mosaic - https://oct.co/essays/wandering-fog-mosaic-abomination-review',
        'O\'so\'s Hop Debacle - https://oct.co/essays/oso-hop-debacle-review',
        'Half Acre\'s Double Daisy Cutter - https://oct.co/essays/half-acre-double-daisy-cutter-review',
        'Omnipollo\'s Lustro - https://oct.co/essays/omnipollo-lustro-review',
        'Equilibrium\'s Energy Equals - https://oct.co/essays/equilbrium-energy-equals-review',
        'Short Throw\'s Code of the Streets - https://oct.co/essays/short-throw-code-streets-review',
        'American Solera\'s Terpy Galaxy - https://oct.co/essays/american-solera-terpy-galaxy-review',
        'Offshoot\'s Retreat - https://oct.co/essays/offshoot-retreat-review',
        'Talea\'s Mangotango - https://oct.co/essays/talea-mangotango-review',
        'Phase Three\'s Crème - https://oct.co/essays/phase-three-creme-review',
        'WeldWorks\' Juicy Bits - https://oct.co/essays/weldwerks-juicy-bits-review',
        'Nod Hill\'s Mood for a Day - https://oct.co/essays/hazy-ipa-mood',
        'Hi-Wire\'s Hi-Pitch Mosaic IPA - https://oct.co/essays/hi-wire-hi-pitch-mosaic-ipa-review',
        'Elysian\'s Dayglow - https://oct.co/essays/elysian-dayglow-ipa-review',
        'New Belgium\'s Voodoo Ranger 1985 IPA - https://oct.co/essays/new-belgium-voodoo-ranger-1985-review',
        'Fat Orange Cat x Nightmare Brewing\'s Feed Me a Stray Cat - https://oct.co/essays/fat-orange-cat-nightmare-feed-me-stray-cat-review',
        'Bell\'s Light Hearted Ale - https://oct.co/essays/bells-light-hearted-review'
    ]

    msg = 'I would recommend '
    drink = random.choice(drinks)
    response = msg + drink
    await ctx.send(response)


@bot.command(name='unit1', help='All lectures for Unit 1')
async def unit1(ctx):
    unit1_lectures = [
        'Intro to HTML and CSS - https://git.generalassemb.ly/SEIR-831/intro-to-html-and-css\n',
        'Flexbox - https://git.generalassemb.ly/SEIR-831/intro-to-flexbox\n',
        'CSS Grid - https://git.generalassemb.ly/SEIR-831/intro-to-css-grid\n',
        'Responsive Design - https://git.generalassemb.ly/SEIR-831/responsive-web-design\n',
        'Datatypes and JS Basics - https://git.generalassemb.ly/SEIR-831/intro_to_datatypes\n',
        'Control Flow - https://git.generalassemb.ly/SEIR-831/intro_to_control_flow\n',
        'Arrays - https://git.generalassemb.ly/SEIR-831/intro_to_arrays\n',
        'Objects - https://git.generalassemb.ly/SEIR-831/intro_to_objects\n',
        'Javascript Functions - https://git.generalassemb.ly/SEIR-831/js-functions\n',
        'Array Methods and Callback - https://git.generalassemb.ly/SEIR-831/js-array-methods\n',
        'Intro to JQuery - https://git.generalassemb.ly/SEIR-831/js-intro-to-jquery\n',
        'JQuery Capture Input - https://git.generalassemb.ly/SEIR-831/js-dom-capture-input\n',
        'AJAX - https://git.generalassemb.ly/SEIR-831/js-jquery-ajax\n',
        'Google Sheet API - https://git.generalassemb.ly/SEIR-831/js-google-sheet-as-json-using-ajax?organization=SEIR-831&organization=SEIR-831'
    ]

    for i in unit1_lectures:
        await ctx.send(i)


@bot.command(name='unit1hw', help='All Unit 1 HW')
async def unit1_hw(ctx):
    unit1_hw = [
        'Instagram Quotes - https://git.generalassemb.ly/SEIR-831/W01D01-HW',
        'Startup Matchmaker - https://git.generalassemb.ly/SEIR-831/W01D02-HW',
        'Grid Layouts - https://git.generalassemb.ly/SEIR-831/W01D03-HW',
        'Responsive Design - https://git.generalassemb.ly/SEIR-831/W01D04-HW',
        'JS Practice - https://git.generalassemb.ly/SEIR-831/W1D05-Homework/blob/master/README.md',
        'Tamagotchi - https://git.generalassemb.ly/SEIR-831/Tamagotchi',
        'Functions Practice - https://git.generalassemb.ly/SEIR-831/W02D03-HW',
        'Random Imager - https://git.generalassemb.ly/SEIR-831/W02D04-HW/blob/master/README.md'
    ]

    for i in unit1_hw:
        await ctx.send(i)


@bot.command(name='unit2hw', help='All Unit 2 HW')
async def unit2_hw(ctx):
    unit2_hw = [
        'React Dashboard - https://git.generalassemb.ly/SEIR-831/W04D01',
        'Films Part 1 - https://git.generalassemb.ly/SEIR-831/W04D02-HW',
        'Films Part 2 - https://git.generalassemb.ly/SEIR-831/W04D03-HW',
        'Films Part 3 - https://git.generalassemb.ly/SEIR-831/W04D04-HW',
        'Korilla Receipts - https://git.generalassemb.ly/SEIR-831/W04D05-HW/blob/master/README.md',
        'Weather App - https://git.generalassemb.ly/SEIR-831/W05D01-HW?organization=SEIR-831&organization=SEIR-831',
        'iStocks - https://git.generalassemb.ly/SEIR-831/W05D02-HW?organization=SEIR-831&organization=SEIR-831'
    ]

    for i in unit2_hw:
        await ctx.send(i)


@bot.command(name='unit2', help='All lectures for Unit 2')
async def unit2(ctx):
    unit2_lectures = [
        'Intro to React and Components - https://git.generalassemb.ly/SEIR-831/react-intro-to-react-and-components/blob/master/1.%20intro-to-react.md',
        'Nested Components - https://git.generalassemb.ly/SEIR-831/react-intro-to-react-and-components/blob/master/3.%20nested-components.md',
        'Passing React Props - https://git.generalassemb.ly/SEIR-831/react-passing-props',
        'Intro to State - https://git.generalassemb.ly/SEIR-831/react-intro-to-state',
        'Complex Version of State - https://git.generalassemb.ly/SEIR-831/react-intro-to-state/blob/master/complex-versions-of-state.md',
        'Lifting State - https://git.generalassemb.ly/SEIR-831/react-intro-to-state/blob/master/lifting-state.md',
        'Controlled v. Uncontrolled Inputs - https://git.generalassemb.ly/SEIR-831/react-controlled-vs-uncontrolled-inputs',
        'React and AJAX - https://git.generalassemb.ly/SEIR-831/react-fetching-data-public',
        'React useEffect - https://git.generalassemb.ly/SEIR-831/react_useffect',
        'React Router - https://git.generalassemb.ly/SEIR-831/react-router',
        'React useContext - https://git.generalassemb.ly/SEIR-831/react-useContext'
    ]

    for i in unit2_lectures:
        await ctx.send(i)


@bot.command(name='unit3', help='All lectures for Unit 3')
async def unit3(ctx):
    unit3_lectures = [
        'Intro to Express - https://git.generalassemb.ly/SEIR-831/express-intro-to-express?organization=SEIR-831&organization=SEIR-831',
        'URL and Query Parameters - https://git.generalassemb.ly/SEIR-831/express-url-and-query-parameters?organization=SEIR-831&organization=SEIR-831',
        'Express CRUD - https://git.generalassemb.ly/SEIR-831/express-crud-router',
        'Express Router - https://git.generalassemb.ly/SEIR-831/express-crud-router',
        'Intro to MongoDB - https://git.generalassemb.ly/SEIR-831/mongo-intro?organization=SEIR-831&organization=SEIR-831',
        'Intro to Mongoose - https://git.generalassemb.ly/SEIR-831/intro-to-mongoose',
        'Express with Mongoose Full CRUD - https://git.generalassemb.ly/SEIR-831/express-mongoose-crud',
        'Express with React - https://git.generalassemb.ly/SEIR-831/ExpressFrontendDeploy',
        'Deployment - https://git.generalassemb.ly/SEIR-831/ExpressFrontendDeploy/blob/master/deploy.md',
        'Group Git - https://git.generalassemb.ly/SEIR-831/git-group-git'
    ]

    for i in unit3_lectures:
        await ctx.send(i)


@bot.command(name='unit3hw', help='All Unit 3 HW')
async def unit3_hw(ctx):
    unit3_hw = [
        'Birds - https://git.generalassemb.ly/SEIR-831/W07D01-HW',
        'Pokemon - https://git.generalassemb.ly/SEIR-831/W07D02-HW?organization=SEIR-831&organization=SEIR-831',
        'MongoDB Query Practice - https://git.generalassemb.ly/SEIR-831/W07D03-HW',
        'Mongoose Practice - https://git.generalassemb.ly/SEIR-831/W07D04-HW/blob/master/README.md',
        'Cookbook API - https://git.generalassemb.ly/SEIR-831/Cookbook-API/blob/master/README.md',
        'Cookbook API Part 2 - https://git.generalassemb.ly/SEIR-831/W08D01-HW',
        'MERN Lab - https://git.generalassemb.ly/SEIR-831/mern-lab?organization=SEIR-831&organization=SEIR-831'
    ]

    for i in unit3_hw:
        await ctx.send(i)


@bot.command(name='unit4', help='All lectures for Unit 4')
async def unit4(ctx):
    unit4_lectures = [
        'Intro to Ruby - https://git.generalassemb.ly/SEIR-831/ruby-intro-to-ruby',
        'Ruby Arrays and Hashes - https://git.generalassemb.ly/SEIR-831/ruby-intro-to-ruby/blob/master/ARRAYS_HASH.md',
        'Ruby Blocks Enumerables - https://git.generalassemb.ly/SEIR-831/ruby_blocks_enumerables',
        'Ruby Classes - https://git.generalassemb.ly/SEIR-831/ruby_classes',
        'SQL - https://git.generalassemb.ly/SEIR-831/sql-intro',
        'Intro to Rails - https://git.generalassemb.ly/SEIR-831/intro_to_rails',
        'Rails Controller - https://git.generalassemb.ly/SEIR-831/rails_controllers/blob/master/morning_rails_controllers.md'
    ]

    for i in unit4_lectures:
        await ctx.send(i)


@bot.command(name='unit4hw', help='All Unit 4 HW')
async def unit4_hw(ctx):
    unit4_hw = [
        'Ruby Practice - https://git.generalassemb.ly/SEIR-831/W10D01-HW?organization=SEIR-831&organization=SEIR-831',
        'Ruby Algos - https://git.generalassemb.ly/SEIR-831/W10D02-HW',
        'Dojo Fighter - https://git.generalassemb.ly/SEIR-831/RubyDojoFighter',
        'NFL SQL - https://git.generalassemb.ly/SEIR-831/W10D04-HW',
        'Glitch in the Matrix - https://git.generalassemb.ly/SEIR-831/glitch_in_the_matrix',
        'Tweetr - https://git.generalassemb.ly/SEIR-831/W11D01-HW/blob/master/README.md'
    ]

    for i in unit4_hw:
        await ctx.send(i)


bot.run(TOKEN)
