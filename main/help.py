#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
import discord
from discord.ext import commands
import json

with open('CYBORGBASEDATA.json') as json_data:
    basedata = json.load(json_data)
    prefix = basedata['prefix']


class help:
    def __init__(self, bot):
        self.bot = bot


    @commands.group(aliases=['h'])
    async def help(self, ctx):
        if ctx.invoked_subcommand is None:
            a = ctx.message.author
            emb = discord.Embed(title="__**CyborgToast Help**__", colour=discord.Colour(11756839), description=f"Here is the normal-user available command list. The prefix for this bot is currently `{prefix}` . You have to **always** put it right before the key command words without any spaces. _Example:_ `{prefix}help w`")
            emb.set_thumbnail(url="https://discordemoji.com/assets/emoji/ThinkingInverted.png")
            emb.set_footer(text="CyborgToast Bot help page | For more info DM me @Tmpod#0836", icon_url="https://cdn.discordapp.com/attachments/421358461473783819/437591960874778645/cyborgtoast.png")
            emb.add_field(name="*hypixel <subcommand>*", value=f"This category contains some Hypixel related commands. Do `{prefix}help hypixel` to check all the Hypixel related commands! You may also use `hy` instead of the default command.")
            emb.add_field(name="*party <subcommand>*", value=f"This category contains the party management commands. Do `{prefix}help party` to check all the Hypixel related commands! You may also use `p` instead of the default command.")
            emb.add_field(name="*lenny*", value="Sends Lenny. Why having this? ( ͡° ͜ʖ ͡° )")
            emb.add_field(name="*invite*", value="Shows you the correct invite link to share with other people! You may also use `i` instead of the default command.")
            emb.add_field(name="*help*", value="Shows this message. You can use `help w` to get this message in a DM to you! You may also use `h` instead of the default command")
            await ctx.send(embed=emb)
            await ctx.message.delete()


    @help.command(aliases=['w', 'dm'])
    async def whisper(self, ctx):
        a = ctx.message.author
        emb = discord.Embed(title="__**CyborgToast Help**__", colour=discord.Colour(11756839), description=f"Here is the normal-user available command list. The prefix for this bot is currently `{prefix}` . You have to **always** put it right before the key command words without any spaces. _Example:_ `{prefix}help w`")
        emb.set_thumbnail(url="https://discordemoji.com/assets/emoji/ThinkingInverted.png")
        emb.set_footer(text="CyborgToast Bot help page | For more info DM me @Tmpod#0836", icon_url="https://cdn.discordapp.com/attachments/421358461473783819/437591960874778645/cyborgtoast.png")
        emb.add_field(name="*hypixel <subcommand>*", value=f"This category contains some Hypixel related commands. Do `{prefix}help hypixel` to check all the Hypixel related commands! You may also use `hy` instead of the default command.")
        emb.add_field(name="*lenny*", value="Sends Lenny. Why having this? ( ͡° ͜ʖ ͡° )")
        emb.add_field(name="*invite*",value="Shows you the correct invite link to share with other people! You may also use `i` instead of the default command.")
        emb.add_field(name="*help*", value="Shows this message. You can use `help w` to get this message in a DM to you! You may also use `h` instead of the default command")
        await ctx.author.send(embed=emb)
        await ctx.message.delete()


    @help.command(aliases=['hy', 'hypixel'])
    async def hypixelhelp(self, ctx, whisper=None):
        a = ctx.message.author
        sWhisper = str(whisper)
        emb = discord.Embed(title="__**CyborgToast Help**__", colour=discord.Colour(11756839), description=f"Here are the Hypixel related commands. These are subcommands from the main `{prefix}hypixel` command (which can also be `{prefix}hy`). Here's an example of how to use these commands: `{prefix}hypixel rankinfo BonjourCroquette`. Don't forget to use `{prefix}` before your commands!")
        emb.set_thumbnail(url="https://discordemoji.com/assets/emoji/ThinkingInverted.png")
        emb.set_footer(text="CyborgToast Bot help page | For more info DM me @Tmpod#0836", icon_url="https://cdn.discordapp.com/attachments/421358461473783819/437591960874778645/cyborgtoast.png")
        emb.add_field(name="*rankinfo <IGN>*", value="This command tells you what Hypixel rank the player you typed in has. You may also use `rinfo` or `ri` instead of the default command.")
        emb.add_field(name="*getrank <IGN>*", value="This command will assign the Hypixel rank as a role on this Discord server, if the Hypixel profile name you provided has your Discord account linked. You may also use `gr` instead of the default command.")
        emb.add_field(name="*getbedwarslevel <IGN>*", value="This command will assign the Bedwars level as a role on this Discord server, if the Hypixel profile name you provided has your Discord account linked. You may also use `getbwlevel`, `getbwlvl`, `gbwl` or `bw` instead of the default command.")
        emb.add_field(name="*link*", value="This will teach you how to link a Discord account to a Hypixel profile!")
        if sWhisper == "w" or sWhisper == "dm":
            await ctx.author.send(embed=emb)
        elif whisper == None:
            await ctx.send(embed=emb)
        else:
            await ctx.send("That's not a valid argument!")
        await ctx.message.delete()


    @help.command(aliases=['p'])
    async def party(self, ctx, whisper=None):
        a = ctx.message.author
        sWhisper = str(whisper)
        emb = discord.Embed(title="__**CyborgToast Help**__", colour=discord.Colour(11756839), description=f"Here are the Hypixel related commands. These are subcommands from the main `{prefix}hypixel` command (which can also be `{prefix}hy`). Here's an example of how to use these commands: `{prefix}hypixel rankinfo BonjourCroquette`. Don't forget to use `{prefix}` before your commands!")
        emb.set_thumbnail(url="https://discordemoji.com/assets/emoji/ThinkingInverted.png")
        emb.set_footer(text="CyborgToast Bot help page | For more info DM me @Tmpod#0836", icon_url="https://cdn.discordapp.com/attachments/421358461473783819/437591960874778645/cyborgtoast.png")
        emb.add_field(name="*create <party name>*", value="Create a party with the given name. If no name is given the party will be called <THEPARTYMASTERNICK>'s Part")
        emb.add_field(name="*remove <party name>*", value="TODO.")
        emb.add_field(name="*disband*", value="Kinda done.")
        if sWhisper == "w" or sWhisper == "dm":
            await ctx.author.send(embed=emb)
        elif whisper == None:
            await ctx.send(embed=emb)
        else:
            await ctx.send("That's not a valid argument!")
        await ctx.message.delete()


"""Defining this extension"""
def setup(bot):
    bot.add_cog(help(bot))