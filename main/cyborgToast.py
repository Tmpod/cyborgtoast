#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
"""
MIT License

Copyright (c) 2018 

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
__version__ = '0.9.5'
"""Imports"""
# import hypixelapi as hype
import discord
from discord import utils
from discord.ext import commands
from discord.utils import get
from discord.utils import find
from random import choice
import asyncio
import logging
import traceback
import sys
import json


"""Bot inicialization"""
logging.basicConfig(level='INFO')
logger = logging.getLogger('cyborgtoast.py')

with open('CYBORGBASEDATA.json') as json_data:
    basedata = json.load(json_data)
    prefix = basedata['prefix']
    TOKEN = basedata['token'] #I define the prefix before hand so that I can use it anywhere else easily.

bot = commands.Bot(description="This is party manager bot and it has some Hypixel related commands as well as random querks. [InDev]", command_prefix=prefix)



"""Boot-up"""
@bot.event
async def on_ready():
    creator = (await bot.application_info()).owner
    print(f"""\n===========================
I'm ready!
Welcome to {bot.user.name}!
ID: {str(bot.user.id)}
Creator: {creator}
Current prefix: {prefix}
Python Version: {sys.version_info[0]}
Discord Version: {discord.version_info[0]}
CyborgToast Version: {__version__}
===========================\n""")
    async def change_activities():
        options = ('Minesweeper', 'Pong', 'Tic-tac toe', 'with the Discord API', 'with the Hypixel API')
        timeout = 60
        watch = discord.Activity(type=discord.ActivityType.watching, name=f"for {prefix}help")
        stream = discord.Streaming(url="https://www.twitch.tv/tmpod", name="bits of information")
        listen = discord.Activity(type=discord.ActivityType.listening, name="to beeps and bops")
        while True:
            game = discord.Game(name=choice(options))
            possb = choice([watch, stream, game, listen])
            await bot.change_presence(activity=possb)
            await asyncio.sleep(timeout)
    # To fire up the worker in the background:
    bot.loop.create_task(change_activities())

    """Removing the default help command"""
    bot.remove_command('help')

    """Loading extensions"""
    extensions = ['hypixel', 'party', 'debugcog', 'other', 'help']
    for extension in extensions:
        try:
            bot.load_extension(extension)
        except Exception:
            logger.error(f'Failed to load {extension} with error:\n{traceback.format_exc()}')

    """Sending a boot-up message to a channel"""
    channel = bot.get_channel(451776576237993984)
    guild = bot.get_guild(419789888419004418)
    if guild.name == "Tryhard's Paradise":
        em = discord.Embed(description=f":white_check_mark: **{bot.user.name} successfuly booted-up!**", color=discord.Colour.green())
        await channel.send(embed=em)



"""Execution"""
bot.run(TOKEN)

"""For more info about stuff in this file check out my Bot Template at https://github.com/Tmpod/discord.py-botTemplate """
