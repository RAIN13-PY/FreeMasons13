import discord
from discord.ext import commands
import asyncio
import datetime
import sys
import sqlite3
import logging
import os
import traceback
import psutil
import time
import json



bot = commands.Bot(command_prefix='!', case_insensitive=True)

@bot.event
async def on_ready():
    print("succes")
    print(f'STATS GUILDS:{len(list(bot.guilds))} USERS:{(len(bot.users))}')
    return await bot.change_presence(activity=discord.Activity(type=3, name=f'watching {len(list(bot.guilds))} servers with {(len(bot.users))} members in them'))

initial_extensions = ['cogs.moderation']

if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'Failed to load extension {extension}', file=sys.stderr)
            traceback.print_exc()


@bot.command()
async def ping(ctx,):
    before = time.monotonic()
    await ctx.send(f'memory used: {psutil.virtual_memory()[2]}% Cpu usage used {psutil.cpu_percent()}%' )
    ping = (time.monotonic() - before) * 1000
    await ctx.send(content=f"Ping=`{int(ping)}ms`")
    
@bot.listen()
async def on_message(message):
    with open("/Users/14028/Desktop/FreeMasons/cogs/BlackList.json", 'r') as b:
        data = json.load(b)
    for x in data['BlackListWords']:
        if int(x['ID']) == 123:
            if any(word in message.content.split() for word in x['Words']):
                await message.delete()









bot.run("")
        
