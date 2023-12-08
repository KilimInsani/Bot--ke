import discord
import python2
import requests
import datetime
from discord.ext import commands

x = datetime.datetime.now()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='@', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} Göreve hazır!')

@bot.command()
async def topla(ctx, topla1 = 0, topla2 =0):
    await ctx.send(topla1+topla2)

@bot.command()
async def çarp(ctx, topla1 = 1, topla2 =1):
    await ctx.send(topla1*topla2)

@bot.command()
async def böl(ctx, böl1=1, böl2=1):
    await ctx.send(böl1/böl2)

@bot.command()
async def çıkart(ctx, çıkart1 = 0, çıkart2 =0):
    await ctx.send(çıkart1-çıkart2)

@bot.command()
async def saat_tarih(ctx):
    await ctx.send(x)

@bot.command()
async def image3(ctx):
    with open('Resimler\TRmem3.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
