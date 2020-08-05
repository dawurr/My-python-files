import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix = '/')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('J KURWA D'))
    print('Bot is ready!')

@client.command()
async def ping(ctx):
    await ctx.send(f'Bots ping: {round(client.latency * 1000)}ms')

@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = ['Yes', 'No', 'Maybe']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

client.run('TOKEN')
