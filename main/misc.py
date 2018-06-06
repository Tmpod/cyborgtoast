#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
import discord
from discord.ext import commands
from discord import utils
import asyncio
import random 
import json
import time


with open('CYBORGBASEDATA.json') as json_data:
    database = json.load(json_data)
prefix = database['prefixes']


greetings = ["Sup!", "Wassup!", "What's up!", "Greetings!", "Hello my good sir!", "Howdy!", "o/", ":wave:"]


def list_files(path, *extras, abs=False):
    p = os.path.join(path, *extras)
    if abs:
      p = os.path.absfile(p)
    
    for file in os.listdir(p):
        yield os.path.join(p, file)


class misc:
    def __init__(self, bot):
        self.bot = bot


    async def on_message(self, msg):
        if '<@!159053372010266624>' in msg.content:
            await msg.add_reaction("\N{BREAD}")
        elif '<@436617817043763200>' in msg.content:
            await msg.channel.send(random.choice(greetings))


    


    @commands.command()
    async def lenny(self, ctx):
        """Sends Lenny. Why having this?  ( ͡° ͜ʖ ͡° ) """
        await ctx.send(" ( ͡° ͜ʖ ͡° ) ")
        await ctx.message.delete()


    @commands.command(aliases=['pg'])
    async def ping(self, ctx):
        """Sends the current ping"""
        ping = str(self.bot.latency * 1000)[:3]
        if int(ping) >= 200:
            em = discord.Embed(description=f"Pong! :ping_pong: \nThe ping is **{ping}**ms!", color=discord.Colour.red())
        elif int(ping) < 50:
            em = discord.Embed(description=f"Pong! :ping_pong: \nThe ping is **{ping}**ms!", color=discord.Colour.green())
        else:
            em = discord.Embed(description=f"Pong! :ping_pong: \nThe ping is **{ping}**ms!", color=discord.Colour.gold())
        await ctx.send(embed=em)


    @commands.command(aliases=['bpg'])
    async def betterping(self, ctx):
        """A better-made version of ping"""
        start = time.monotonic()
        msg = await ctx.send(embed=discord.Embed(description="Pinging...", color=discord.Colour.dark_grey()))
        millis = (time.monotonic() - start) * 1000
        heartbeat = (ctx.bot.latency or (sum(ctx.bot.latencies) / len(ctx.bot.latencies))) * 1000
        await msg.edit(embed=discord.Embed(description=f'**Heartbeat:** {heartbeat:,.2f}ms\t**ACK:** {millis:,.2f}ms.', color=discord.Colour.blurple()))


    @commands.command(aliases=['si'])
    async def serverinvite(self, ctx, *, smth=None):
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


    @commands.command(aliases=['i'])
    async def invite(self, ctx):
        await ctx.send(embed=discord.Embed(title="Here's my invite link!", description=f"```{ctx.bot.invite}```")) 



    @commands.command(aliases=['d'])
    async def dice(self, ctx):
        d = ['1', '2', '3', '4', '5', '6']
        choice = random.choice(d)
        msg = await ctx.send(embed=discord.Embed(description="Rolling the dice...", color=discord.Colour.dark_gold()))
        await asyncio.sleep(2)
        await msg.edit(embed=discord.Embed(description=f"You rolled **{choice}**!", color=discord.Colour.dark_gold()))


    @commands.command(aliases=['c'])
    async def coin(self, ctx):
        msg = await ctx.send(embed=discord.Embed(description="Flipping the coin...", color=discord.Colour.dark_teal()))
        choice = random.choice(['Tales', 'Heads'])
        await asyncio.sleep(2)
        await msg.edit(embed=discord.Embed(description=f"You flipped **{choice}**!", color=discord.Colour.dark_teal()))


    @commands.command(aliases=['m8b'])
    async def magic8ball(self, ctx, *, smth=None):
        answers = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes definitely', 'You may rely on it', 'You can count on it', 'As I see it, yes', 'Most likely', 'Outlook good', 'Yes', 'Signs point to yes', 'Absolutely', 'Reply hazy try again', 'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again', "Don't count on it", 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful', "Chances aren't good"]
        if smth == None:
            await ctx.send(embed=discord.Embed(description=f"You haven't asked anything! {ctx.author.mention}", color=discord.Colour.blurple()))
        else:
            await ctx.trigger_typing()
            await asyncio.sleep(1)
            await ctx.send(embed=discord.Embed(description=random.choice(answers), color=discord.Colour.blurple()))

    @commands.command(aliases=['g', 'github', 'repo'])
    async def git(self, ctx):
        await ctx.send(embed=discord.Embed(title="**Here's my GitHub repo!**", description="https://github.com/Tmpod/cyborgtoast", color=discord.Colour(1)))


    @commands.command(aliases=['m'])
    async def meme(self, ctx, smth=None):
        max = list_files(".", "memes")
        if smth is None:
            memeID = random.randint(1, max)
            em = discord.Embed(description="MEEEME No.{memeID}", color=discord.Colour.purple())
            try:
                await ctx.send(file=discord.File(f"./memes/{memeID}.jpeg", filename=f"MEEEME No.{memeID}.jpeg"))
                await ctx.send(embed=em)
            except FileNotFoundError:
                try:
                    await ctx.send(file=discord.File(f"./memes/{memeID}.png", filename=f"MEEEME No.{memeID}.png"))
                    await ctx.send(embed=em)
                except FileNotFoundError:
                    await ctx.send(file=discord.File(f"./memes/{memeID}.jpg", filename=f"MEEEME No.{memeID}.jpg"))
                    await ctx.send(embed=em)
        elif smth == "max":
            await ctx.send(embed=discord.Embed(description=f":1234: The current number of memes is **{max}**", color=discord.Colour.purple()))
        else:
            try:
                Ismth = int(smth)
                try:
                    if Ismth <= max and Ismth > 0:
                        await ctx.send(file=discord.File(f"./memes/{Ismth}.jpeg", filename=f"MEEEME No.{Ismth}.jpeg"))
                    else:
                        await ctx.send(embed=discord.Embed(description=":octagonal_sign: That's not a valid ID!", color=discord.Colour.red()))
                except FileNotFoundError:
                    try:
                        await ctx.send(file=discord.File(f"./memes/{Ismth}.png", filename=f"MEEEME No.{Ismth}.png")) 
                    except FileNotFoundError:
                        await ctx.send(file=discord.File(f"./memes/{Ismth}.jpg", filename=f"MEEEME No.{Ismth}.jpg")) 
            except ValueError:
                        await ctx.send(embed=discord.Embed(description=":octagonal_sign: That's not a valid ID!", color=discord.Colour.red()))


"""Defining this extension"""
def setup(bot):
    bot.add_cog(misc(bot))
