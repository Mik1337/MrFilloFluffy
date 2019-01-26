from PIL import ImageFont, Image, ImageDraw
from discord.ext import commands
import discord.utils
import discord
import random
import json

def msg_split(text:str) -> str:
    """
    text wrap,
    ps: got it working in my 3rd or something try and I can't
        for the life of me care enough to make this `eligant` so ¯\_(ツ)_/¯
    """
    text_array = text.split(' ')
    text_length = [len(i)+1 for i in text_array]
    length = len(text_length)
    j=0
    for i in range(length):
        if sum(text_length[j:i]) >= 15:
            text_array.insert(i,'\n')
            j=i
    return ' '.join(text_array)

def gen_text(text:str, wrap) -> str:
    """ function that renders the image and returns the discord.File """
    if not wrap:
        text = text.replace('|', '\n')
    else:
        text = msg_split("{} {}".format(text, wrap))
    image = Image.open('/home/mik/Desktop/python/MrFillofluffy/MrFilloFluffy.png')
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("/home/mik/Desktop/python/MrFillofluffy/font/comic-sans-ms/COMIC.TTF",23)
    draw.text(xy=(216, 150),text=text,fill=(30, 30, 30), font=font)
    entropy = ''.join(random.choice("abcedfghijklmnopqrstuvwxyz1234567890") for i in range(10))
    image.save('./fluffs/fluff-{}.png'.format(entropy))
    file = discord.File('./fluffs/fluff-{}.png'.format(entropy), filename="MrFluffSays.png")
    return file

client = discord.Client ()
bot = commands.Bot(command_prefix='fluffy ', description='Mr FilloFluffy says...')

@bot.event
async def on_ready():
    print ('online')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    await bot.process_commands(message)

@bot.command()
async def invite(ctx):
    """ sends invite link to bot """
    rl = 'https://discordapp.com/oauth2/authorize?client_id=285777147807793153&scope=bot&permissions=117760'
    msg = discord.Embed (
        title = 'Invite Link',
        description = 'Invite me to yer server with this >.<',
        image = bot.user.avatar_url,
        url = rl
    ).set_author(name = bot.user.name,url = rl, icon_url = bot.user.avatar_url )
    await ctx.send(embed=msg)

@bot.command()
async def credits(ctx):
    """ credits """
    await ctx.send("https://github.com/Mik1337/MrFilloFluffy")

@bot.command(pass_context=True)
async def say(ctx, *, message):
    """ Mr MrFilloFluffy says... """
    message = message.split(' ')
    *message, wrap = message
    message = " ".join(message)
    try:
        await ctx.send(file=gen_text(text=message, wrap=(False if wrap == '!wrap' else wrap)))
    except Exception as e:
        print('something went wong {}'.format(e))

def loadCreds():
    with open('creds.json') as f:
        return json.load(f)

bot.run(loadCreds()['token'])
