#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
import discord
from discord.ext import commands
import json

with open('CYBORGBASEDATA.json') as json_data:
    database = json.load(json_data)
prefix = database["prefixes"]


class help:
    def __init__(self, bot):
        self.bot = bot


    @commands.group(aliases=['h'])
    async def help(self, ctx):
        if ctx.invoked_subcommand is None:
            emb = discord.Embed(title="__**CyborgToast Help**__", colour=discord.Colour(11756839), description=f"Here is the normal-user available command list. The prefix(es) for this bot is(are) currently `{prefix}` . You have to **always** put it right before the key command words without any spaces. _Example:_ `{prefix}help w`")
            emb.set_thumbnail(url="https://discordemoji.com/assets/emoji/ThinkingLoaf.png")
            emb.set_footer(text="CyborgToast Bot help page | For more info DM me @Tmpod#0836", icon_url="https://cdn.discordapp.com/attachments/421358461473783819/437591960874778645/cyborgtoast.png")
            emb.add_field(name="*hypixel <subcommand>*", value=f"This category contains some Hypixel related commands. Do `{prefix}help hypixel` to check all the Hypixel related commands! You may also use `hy` instead of the default command.")
            emb.add_field(name="*party <subcommand>*", value=f"This category contains the party management commands. Do `{prefix}help party` to check all the Hypixel related commands! You may also use `p` instead of the default command.")
            emb.add_field(name="*misc*", value=f"Random assortment of miscellaneous commands! Do `{prefix}help misc` to show that help page!")
            emb.add_field(name="*help*", value="Shows this message. You can use `help w` to get this message in a DM to you! You may also use `h` instead of the default command")
            await ctx.send(embed=emb)


    @help.command(aliases=['w', 'dm'])
    async def whisper(self, ctx):
        emb = discord.Embed(title="__**CyborgToast Help**__", colour=discord.Colour(11756839), description=f"Here is the normal-user available command list. The prefix(es) for this bot is(are) currently `{prefix}` . You have to **always** put it right before the key command words without any spaces. _Example:_ `{prefix}help w`")
        emb.set_thumbnail(url="https://discordemoji.com/assets/emoji/ThinkingLoaf.png")
        emb.set_footer(text="CyborgToast Bot help page | For more info DM me @Tmpod#0836", icon_url="https://cdn.discordapp.com/attachments/421358461473783819/437591960874778645/cyborgtoast.png")
        emb.add_field(name="*hypixel <subcommand>*", value=f"This category contains some Hypixel related commands. Do `{prefix}help hypixel` to check all the Hypixel related commands! You may also use `hy` instead of the default command.")
        emb.add_field(name="*help*", value="Shows this message. You can use `help w` to get this message in a DM to you! You may also use `h` instead of the default command")
        await ctx.author.send(embed=emb)


    @help.command(aliases=['hy'])
    async def hypixel(self, ctx, whisper=None):
        sWhisper = str(whisper)
        emb = discord.Embed(title="__**CyborgToast Help**__", colour=discord.Colour(11756839), description=f"Here are the Hypixel related commands. These are subcommands from the main `{prefix}hypixel` command (which can also be `{prefix}hy`). Here's an example of how to use these commands: `{prefix}hypixel rankinfo BonjourCroquette`. Don't forget to use `{prefix}` before your commands!")
        emb.set_thumbnail(url="https://discordemoji.com/assets/emoji/ThinkingLoaf.png")
        emb.set_footer(text="CyborgToast Bot help page | For more info DM me @Tmpod#0836", icon_url="https://cdn.discordapp.com/attachments/421358461473783819/437591960874778645/cyborgtoast.png")
        emb.add_field(name="*rankinfo <IGN>*", value="This command tells you what Hypixel rank the player you typed in has. You may also use `rinfo` or `ri` instead of the default command.")
        emb.add_field(name="*getrank <IGN>*", value="This command will assign the Hypixel rank as a role on this Discord server, if the Hypixel profile name you provided has your Discord account linked. You may also use `gr` instead of the default command.")
        emb.add_field(name="*getbedwarslevel <IGN>*", value="This command will assign the Bedwars level as a role on this Discord server, if the Hypixel profile name you provided has your Discord account linked. You may also use `getbwlevel`, `getbwlvl`, `gbwl` or `bw` instead of the default command.")
        emb.add_field(name="*howtolink*", value="This will teach you how to link a Discord account to a Hypixel profile! You may also use `htl` instead of the default command.")
        if sWhisper == "w" or sWhisper == "dm":
            await ctx.author.send(embed=emb)
        elif whisper == None:
            await ctx.send(embed=emb)
        else:
            await ctx.send(embed=discord.Embed(description="That's not a valid argument!", color=discord.Colour.red()))


    @help.command(aliases=['p'])
    async def party(self, ctx, whisper=None):
        sWhisper = str(whisper)
        emb = discord.Embed(title="__**CyborgToast Help**__", colour=discord.Colour(11756839), description=f"Here are the party management related commands. These are subcommands from the main `{prefix}hypixel` command (which can also be `{prefix}hy`). Here's an example of how to use these commands: `{prefix}hypixel rankinfo BonjourCroquette`. Don't forget to use `{prefix}` before your commands!")
        emb.set_thumbnail(url="https://discordemoji.com/assets/emoji/ThinkingLoaf.png")
        emb.set_footer(text="CyborgToast Bot help page | For more info DM me @Tmpod#0836", icon_url="https://cdn.discordapp.com/attachments/421358461473783819/437591960874778645/cyborgtoast.png")
        emb.add_field(name="*create <party name>*", value="Create a party with the given name. If no name is given the party will be called <THEPARTYMASTERNICK/NAME>'s Party. You may also use `c` instead of the default command.")
        emb.add_field(name="*add <username/nick>*", value="Adds the given person to your party. You may also use `a` instead of the default command.")        
        emb.add_field(name="*remove <party name>*", value="[TODO]Disbands the the given party. You must have admin prefileges for that action. You may also use `r` instead of the default command.")
        emb.add_field(name="*disband*", value="Disbands the party in which the command is executed. It will prompt a confirmation message to which you have to react with :white_check_mark: to confirm or with :octagonal_sign: to stop the action. You may also use `d` instead of the default command.")
        if sWhisper == "w" or sWhisper == "dm":
            await ctx.author.send(embed=emb)
        elif whisper == None:
            await ctx.send(embed=emb)
        else:
            await ctx.send(embed=discord.Embed(description="That's not a valid argument!", color=discord.Colour.red()))


    @help.command(aliases=['m','miscellaneous'])
    async def misc(self, ctx, whisper=None):
        sWhisper = str(whisper)
        emb = discord.Embed(title="__**CyborgToast Help**__", colour=discord.Colour(11756839), description=f"Here are the miscellaneous commands. Don't forget to use `{prefix}` before your commands!")
        emb.set_thumbnail(url="https://discordemoji.com/assets/emoji/ThinkingLoaf.png")
        emb.set_footer(text="CyborgToast Bot help page | For more info DM me @Tmpod#0836", icon_url="https://cdn.discordapp.com/attachments/421358461473783819/437591960874778645/cyborgtoast.png")
        emb.add_field(name="*lenny*", value="Sends Lenny. Why having this? ( ͡° ͜ʖ ͡° )")
        emb.add_field(name="*invite*",value="Shows the invite link for CyborgToast! You may also use `i` instead of the default command.")
        emb.add_field(name="*serverinvite*",value="Shows you the correct invite link of some servers to share with other people! You may also use `si` instead of the default command.")
        emb.add_field(name="*dice*", value="Rolls a dice. You may also use `d` instead of the default command.")
        emb.add_field(name="*magic8ball <your question>*", value="Ask a question to the all-seing Magic8Ball. You may also use `m8b` instead of the default command.")
        emb.add_field(name="*coin*", value="Flips a coin. You may also use `c` instead of the default command.")
        emb.add_field(name="*meme [ID]*", value="Sends a random meme from the library if the ID is not specified. If it is, then the bot will send the corresponding meme. You can suggest some by contacting Tmpod#0836! You may also use `m` instead of the default command.")
        emb.add_field(name="*ping*", value="Shows the current bot ping. You may also use `pg` instead of the default command.")
        emb.add_field(name="*betterping*", value="It's a better version of ping. Use it if you wanna know more in-depth things. You may also use `bpg` instead of the default command.")
        emb.add_field(name="*git*", value="Sends my GitHub repository link for this bot. You may also use `g` or `github` instead of the default command.")
        if sWhisper == "w" or sWhisper == "dm":
            await ctx.author.send(embed=emb)
        elif whisper == None:
            await ctx.send(embed=emb)
        else:
            await ctx.send(embed=discord.Embed(description="That's not a valid argument!", color=discord.Colour.red()))


"""Defining this extension"""
def setup(bot):
    bot.add_cog(help(bot))
