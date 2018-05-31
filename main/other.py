#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
import discord
from discord.ext import commands
from discord import utils
import asyncio
from random import choice
import json

with open('CYBORGBASEDATA.json') as json_data:
    basedata = json.load(json_data)
    prefix = basedata['prefix']

class other:
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def lenny(self, ctx):
        """Sends Lenny. Why having this?  ( ͡° ͜ʖ ͡° ) """
        await ctx.send(" ( ͡° ͜ʖ ͡° ) ")
        await ctx.message.delete()


    @commands.command()
    async def ping(self, ctx):
        ping = str(self.bot.latency * 1000)[:3]
        if int(ping) >= 200:
            em = discord.Embed(description=f"Pong! :ping_pong: \nThe ping is **{ping}**ms!", color=discord.Colour.red())
        elif int(ping) < 50:
            em = discord.Embed(description=f"Pong! :ping_pong: \nThe ping is **{ping}**ms!", color=discord.Colour.green())
        else:
            em = discord.Embed(description=f"Pong! :ping_pong: \nThe ping is **{ping}**ms!", color=discord.Colour.gold())
        await ctx.send(embed=em)


    @commands.command(aliases=['i'])
    async def invite(self, ctx, *, smth=None):
        auth = ctx.author
        guild = ctx.guild
        if smth == None:
            if guild.name == "Tryhard's Paradise":
                emb = discord.Embed(title="Tryhard Paradise Invite Link", description=f"{auth.mention} Here's the invite link for this server! Make sure you always share this one!\n :arrow_forward: `https://discord.gg/bFafcDF` :arrow_backward:", url="https://discord.gg/bFafcDF", colour=discord.Colour.dark_teal())
            elif guild.name == "Hypixel.net":
                emb = discord.Embed(title="Unnoficial Hypixel.net Discord Server Invite Link", description=f"{auth.mention} Here's the invite link for this server! Make sure you always share this one!\n :arrow_forward: `https://discord.gg/DrQCrkM` :arrow_backward:", url="https://discord.gg/bFafcDF", colour=discord.Colour.dark_red())
            await ctx.message.delete()
            await ctx.send(embed=emb)
        elif smth in ("Tryhard's Paradise", "Tryhard Paradise", "Tryhard"):
            emb = discord.Embed(title="Tryhard Paradise Invite Link", description=f"{auth.mention} Here's the invite link for the Tryhard's Paradise server! Make sure you always share this one!\n :arrow_forward: `https://discord.gg/bFafcDF` :arrow_backward:", url="https://discord.gg/bFafcDF", colour=discord.Colour.dark_teal())
            await ctx.message.delete()
            await ctx.send(embed=emb)
        elif smth in ("Hypixel.net", "hypixel", "hypixel.net", "Hypixel"):
            emb = discord.Embed(title="Unnoficial Hypixel.net Discord Server Invite Link", description=f"{auth.mention} Here's the invite link for this server! Make sure you always share this one!\n :arrow_forward: `https://discord.gg/DrQCrkM` :arrow_backward:", url="https://discord.gg/bFafcDF", colour=discord.Colour.dark_red())
            await ctx.send(embed=emb)
        else:
            await ctx.send(f"The server you specified is not valid or supported. {auth.mention}")


    @commands.command(aliases=['d'])
    async def dice(self, ctx):
        d = ['1', '2', '3', '4', '5', '6']
        chosen = choice(d)
        emR = discord.Embed(description="Rolling the dice...", color=discord.Colour.dark_gold())
        fm = await ctx.send(embed=emR)
        await asyncio.sleep(2)
        emC = discord.Embed(description=f"You rolled **{chosen}**!", color=discord.Colour.gold())
        await fm.delete()
        await ctx.send(embed=emC)


    @commands.command(aliases=['m8b'])
    async def magic8ball(self, ctx, *, smth=None):
        answers = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes definitely', 'You may rely on it', 'You can count on it', 'As I see it, yes', 'Most likely', 'Outlook good', 'Yes', 'Signs point to yes', 'Absolutely', 'Reply hazy try again', 'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again', "Don't count on it", 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful', "Chances aren't good"]
        if smth == None:
            em = discord.Embed(description=f"You haven't asked anything! {ctx.author.mention}", color=discord.Colour.blurple())
            await ctx.send(embed=em)
        else:
            em = discord.Embed(description=choice(answers), color=discord.Colour.blurple())
            await ctx.send(embed=em)

    @commands.command(aliases=['g'])
    async def git(self, ctx):
        em = discord.Embed(title="**Here's my GitHub repo!**", description="https://github.com/Tmpod/cyborgtoast", color=discord.Colour.darker_grey())
        await ctx.send(embed=em)


"""Defining this extension"""
def setup(bot):
    bot.add_cog(other(bot))