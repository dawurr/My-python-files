import discord
from discord.ext.commands import bot
from discord.ext import commands
import random
import asyncio
import time

bot = commands.Bot(command_prefix='>')

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game('es kurwy'))
    print('bot is ready')

@bot.command()
async def spam(ctx):
    while 6 > 5:
        await ctx.send('@everyone\n@everyone\n@everyone\n@everyone\n@everyone\n@everyone\n@everyone\n@everyone\n@everyone\n@everyone\n@everyone\n@everyone\n@everyone\n@everyone\n@everyone\n@everyone\n@everyone\n@everyone')

@bot.command(aliases=['lilspam'])
async def lil_spam(ctx):
    await ctx.send('@everyone\n@everyone\n@everyone\n@everyone\n@everyone\n@everyone\n@everyone\n@everyone\n@everyone\n@everyone\n@everyone\n@everyone')

bot.run('TOKEN')
