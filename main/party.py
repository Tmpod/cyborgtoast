#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
import discord
from discord.ext import commands
from discord import utils
import asyncio
import json

with open('CYBORGBASEDATA.json') as json_data:
    basedata = json.load(json_data)
    prefix = basedata['prefix']

class party:
    def __init__(self, bot):
        self.bot = bot


    @commands.group(aliases=['p'])
    async def party(self, ctx=None):
        """Party managment commands"""
        if ctx.invoked_subcommand is None:
            a = ctx.message.author
            await ctx.send(f":octagonal_sign: You haven't specified which command to execute! Try `{prefix}help` to see which commands are available. " + a.mention)


    @party.command(aliases=['c'])
    async def create(sefl, ctx, *, smth=None):
        guild = ctx.guild
        illum = utils.get(guild.roles, name="Illuminati △")
        bots = utils.get(guild.roles, name="Bots")
        overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False),
        guild.me: discord.PermissionOverwrite(read_messages=True, send_messages=True),
        illum: discord.PermissionOverwrite(read_messages=True),
        bots: discord.PermissionOverwrite(read_messages=True, send_messages=True)
        }
        if smth is None:
            cat = await guild.create_category_channel(ctx.author.nick + "'s Party", overwrites = overwrites)
        else:
            cat = await guild.create_category_channel(smth, overwrites = overwrites)
        chan = await guild.create_text_channel("party-textin", overwrites=overwrites, category=cat, reason=None)
        vc = await guild.create_voice_channel("Party Voice", overwrites=overwrites, category=cat, reason=None)
        await ctx.send(":white_check_mark: Party successfuly created!")


    @party.command(aliases=['d'])
    async def disband(self, ctx):
        cat = ctx.channel.category
        if cat.name in ("Staff Team", "Textin'", "Music 🎧", "Looking to play", "Important Stuff Here", None, "test 💾"):
            await ctx.send(f":octagonal_sign: You cannot execute that command here! {ctx.author.mention}")
        else:
            await ctx.send("Disbanding party in 5 seconds!")
            await asyncio.sleep(5)
            for i in cat.channels:
                await i.delete()
            await cat.delete()


    @party.command(aliases=['a'])
    async def add(self, ctx, *, smth):
        cat = ctx.channel.category
        overwrites = cat.overwrites
        user = utils.find(lambda m: m.name == smth, ctx.guild.members)
        userN = utils.find(lambda m: m.nick == smth, ctx.guild.members)
        if user != None:
            await cat.set_permissions(user, read_messages=True, send_messages=True)
        elif userN != None:
            await cat.set_permissions(userN, read_messages=True, send_messages=True)
        else:
            await ctx.send(f":octagonal_sign: There's no user with that name or nick! {ctx.author.mention}")


"""Defining this extension"""
def setup(bot):
    bot.add_cog(party(bot))