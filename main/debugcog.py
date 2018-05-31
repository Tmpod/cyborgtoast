#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
import discord
from discord.ext import commands
from discord import utils
import reprlib
import json

with open('CYBORGBASEDATA.json') as json_data:
    basedata = json.load(json_data)
    prefix = basedata['prefix']


owner = 159053372010266624
def is_owner():
    def predicate(ctx):
        return int(ctx.message.author.id) == owner
    return commands.check(predicate)


class debugcog:
    def __init__(self, bot):
        self.bot = bot


    @is_owner()
    @commands.group(aliases=['db'])
    async def debug(self, ctx=None):
        """Party managment commands"""
        if ctx.invoked_subcommand is None:
            a = ctx.message.author
            await ctx.send(f":octagonal_sign: You haven't specified which command to execute! Try `{prefix}help` to see which commands are available. " + a.mention)


    @debug.command()
    async def test(self, ctx):
        """Just retrieves a bunch of useful data"""
        auth = ctx.author
        guild = ctx.guild
        cat = ctx.channel.category
        chan = ctx.channel
        if str(auth) == "Tmpod#0836":
            output = f"```{auth}\n\n{auth.nick}\n\n{auth.roles}\n\n{guild.name}\n\n{cat.name}\n\n{cat.channels}\n\n{chan.name}\n\n{self.bot.guilds}\n\n{self.bot.latency}```"
            await ctx.send(output)
            await ctx.send(reprlib.repr(cat.name))
            print(reprlib.repr(cat.name))
            print(self.bot.guilds[1:])
        else:
            await ctx.send(":octagonal_sign: You are not my creator! Cya!")
        if cat.name == "test 💾":
            print("foo")
        await ctx.message.delete()


    @debug.command()
    async def test2(self, ctx):
        """Another test command"""
        auth = ctx.author
        guild = ctx.guild
        if str(auth) == "Tmpod#0836":
            # vc = guild.voice_channels(category=ctx.channel.category)
            cat = ctx.channel.category
            await ctx.send(f"```{cat.channels}```")
            await ctx.send(f"```{cat.overwrites}```")
        else:
            await ctx.send(":octagonal_sign: You are not my creator! Cya!")


    @debug.command()
    async def test3(self, ctx, *,smth):
        """And yet another one"""
        if str(ctx.author) == "Tmpod#0836":
            user = utils.find(lambda m: m.nick == smth, ctx.guild.members)
            await ctx.send(f"```{user}```")
            print(user)
        else:
            await ctx.send(":octagonal_sign: You are not my creator! Cya!")
            

    @debug.command()
    async def test4(self, ctx):
        channel = utils.get(ctx.guild.channels, name="bot-beta")
        await ctx.send(f"`Random message sent to {channel}`")
        await channel.send("RANDOM MESSAGE")


    @debug.command()
    async def test5(self, ctx):
        cat = ctx.channel.category
        await ctx.send(cat.mention)


    @debug.command(aliases=['r'])
    async def reload(ctx, *, smth=None):
        if smth == None:
            await ctx.send("You haven't specified which cog to reload!")
        elif str(smth) in extensions:
            try:
                bot.unload_extension(smth)
                bot.load_extension(smth)
                await ctx.send(f":white_check_mark: Successfuly reloaded **{smth}** !")
            except:
                await ctx.send(":x: An error occured during this process. Please refer to the shell.")
        else:
            await ctx.send(":x: That cog name is not valid!")


"""Defining this extension"""
def setup(bot):
    bot.add_cog(debugcog(bot))