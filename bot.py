from PIL import ImageFont, Image, ImageDraw
from discord.ext import commands
import discord.utils
import discord
import random
import json

def gen_text(text) -> str:
    """ function that renders the image and returns the discord.File """
    text = text.replace('|', '\n')
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
    await ctx.send("https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions={}".format(285777147807793153, 117760))

@bot.command()
async def credits(ctx):
    """ credits """
    await ctx.send(")

@bot.command(pass_context=True)
async def say(ctx, *, message):
    """ Mr MrFilloFluffy says... """
    try:
        print(message, gen_text(message))
        await ctx.send(file=gen_text(message))
    except Exception as e:
        print('something went wong {}'.format(e))


def loadCreds():
    with open('creds.json') as f:
        return json.load(f)

bot.run(loadCreds()['token'])
