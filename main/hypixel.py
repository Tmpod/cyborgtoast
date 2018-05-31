#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
import discord
from discord.ext import commands
import hypixelapi as hype
import json

with open('CYBORGBASEDATA.json') as json_data:
    basedata = json.load(json_data)
    prefix = basedata['prefix']
#     hypixelKey = str(basedata['hypixelKey'])
# hype.setKeys(hypixelKey)


class hypixel:
    def __init__(self, bot):
        self.bot = bot

    @commands.group(aliases=['hy', 'hypixel'])
    async def hypixelcmd(self, ctx):
        """Hypixel related commands"""
        if ctx.invoked_subcommand is None:
            a = ctx.message.author
            await ctx.send(f":octagonal_sign: You haven't specified which command to execute! Try `{prefix}help` to see which commands are available. " + a.mention)   


    @hypixelcmd.command(aliases=['gr'])
    async def getrank(self, ctx, *, something=None):
        """This command will assign the Hypixel rank as a role on this Discord server, if the Hypixel profile name you provided has your Discord account linked."""
        a = ctx.message.author
        if something is None:
            await ctx.send(":octagonal_sign: You haven't provided any name! " + a.mention)
        else:
            try:
                player = hype.Player(something)
                pRank = str(player.getRank()['rank'])
                success = f":white_check_mark: {pRank} rank successfuly assigned! " + a.mention
                try:
                    socialMedias = player.JSON['socialMedia']['links']
                    if str(socialMedias['DISCORD']) == str(ctx.message.author):
                        if pRank == "MVP++":
                            await ctx.author.add_roles(get(a.guild.roles, name="MVP++"))
                            await ctx.send(success)
                        elif pRank == "MVP+":
                            await ctx.author.add_roles(get(a.guild.roles, name="MVP+"))
                            await ctx.send(success)
                        elif pRank == "MVP":
                            await ctx.author.add_roles(get(a.guild.roles, name="MVP"))
                            await ctx.send(success)
                        elif pRank == "VIP+":
                            await ctx.author.add_roles(get(a.guild.roles, name="VIP+"))
                            await ctx.send(success)
                        elif pRank == "VIP":
                            await ctx.author.add_roles(get(a.guild.roles, name="VIP"))
                            await ctx.send(success)
                        else:
                            await ctx.send(":octagonal_sign: You don't have a rank on the Hypixel Network." + a.mention)
                    else:
                        await ctx.send(f":octagonal_sign: You are not the owner of that account or you haven't linked your Discord account to your Hypixel profile. To do so use `{prefix}link`!" + a.mention)
                except KeyError:
                    await ctx.send(f":octagonal_sign: This user doesn't have a Discord account linked. Use `{prefix}hypixel link` and follow the steps given!")
            except hype.PlayerNotFoundException:
                await ctx.send(":octagonal_sign: Player not found!")


    @hypixelcmd.command(aliases=['ri', 'rinfo'])
    async def rankinfo(self, ctx, something=None):
        """This commad tells you what Hypixel rank the player you typed in has."""
        a = ctx.message.author
        if something is None:
            await ctx.send(":octagonal_sign: You haven't provided any name! " + a.mention)
        else:    
            try:
                await ctx.trigger_typing()
                player = hype.Player(something)
                pRank = str(player.getRank()['rank'])
                pName = str(player.getName())
                if pRank == "MVP++":
                    emR = discord.Embed(description = player.getRank()['rank'],colour=discord.Colour.dark_gold())
                    emR.set_author(name=pName + " Hypixel Rank:", icon_url="https://cdn.discordapp.com/attachments/415126611239895050/415128299862491139/rank-mvpplusplus.png")
                elif pName == "hypixel":
                    emR = discord.Embed(description = "Owner" ,colour=discord.Colour.dark_red())    
                    emR.set_author(name=pName + " Hypixel Rank:", icon_url="https://cdn.discordapp.com/attachments/421358461473783819/435450006749708288/serveimage.jpeg")
                elif pRank == "MVP+":
                    emR = discord.Embed(description = player.getRank()['rank'],colour=discord.Colour.teal())
                    emR.set_author(name=pName + " Hypixel Rank:", icon_url="https://cdn.discordapp.com/attachments/415126611239895050/415127788866240522/b7d8e5a027280c3bb378859d02dbe582cdb9c743.png")
                elif pRank == "MVP":
                    emR = discord.Embed(description = player.getRank()['rank'],colour=discord.Colour.teal())
                    emR.set_author(name=pName + " Hypixel Rank:", icon_url="https://cdn.discordapp.com/attachments/415126611239895050/415127446514302976/a0be666f173157b0c42cba984cbb97239485a382.png")
                elif pRank == "VIP+":
                    emR = discord.Embed(description = player.getRank()['rank'],colour=discord.Colour.green())
                    emR.set_author(name=pName + " Hypixel Rank:", icon_url="https://cdn.discordapp.com/attachments/415126611239895050/415126912034275328/ec6e32c36cd8881bac4df63b17ba1ebd88f94819.png")
                elif pRank == "VIP":
                    emR = discord.Embed(description = player.getRank()['rank'],colour=discord.Colour.green())
                    emR.set_author(name=pName + " Hypixel Rank:", icon_url="https://cdn.discordapp.com/attachments/415126611239895050/415126625416380416/e6d6709c969b73397cd84cf77c96fa3619284d85.png")
                elif pRank == "Admin":
                    emR = discord.Embed(description = player.getRank()['rank'],colour=discord.Colour.red())
                    emR.set_author(name=pName + " Hypixel Rank:", icon_url="https://cdn.discordapp.com/attachments/421358461473783819/435450006749708288/serveimage.jpeg")
                elif pRank == "Moderator":
                    emR = discord.Embed(description = player.getRank()['rank'],colour=discord.Colour.green())
                    emR.set_author(name=pName + " Hypixel Rank:", icon_url="https://cdn.discordapp.com/attachments/421358461473783819/435450006749708288/serveimage.jpeg")
                elif pRank == "Helper":
                    emR = discord.Embed(description = player.getRank()['rank'],colour=discord.Colour.blue())
                    emR.set_author(name=pName + " Hypixel Rank:", icon_url="https://cdn.discordapp.com/attachments/421358461473783819/435450006749708288/serveimage.jpeg")
                elif pRank == "YouTube":
                    emR = discord.Embed(description = player.getRank()['rank'],colour=discord.Colour.red())
                    emR.set_author(name=pName + " Hypixel Rank:", icon_url="https://cdn.discordapp.com/attachments/421358461473783819/435446947680223232/youtube_social_icon_white.png")
                else:
                    emR = discord.Embed(title=pName + " Hypixel Rank:", description = player.getRank()['rank'],colour=discord.Colour.light_grey())
                await ctx.send(embed=emR)            
            except hype.PlayerNotFoundException:
                await ctx.send(":octagonal_sign: Player not found!")


    @hypixelcmd.command(aliases=['getbwlevel', 'getbwlvl', 'gbwl', 'bw'])
    async def getbedwarslevel(self, ctx, something=None):
        """This command will assign the Bedwars level as a role on this Discord server, if the Hypixel profile name you provided has your Discord account linked. """
        a = ctx.message.author
        if something is None:
            await ctx.send(":octagonal_sign: You haven't provided any name! " + a.mention)
        else:
            try:
                player = hype.Player(something)
                bwLvl = int(player.getBWLvL())
                success = f":white_check_mark: Bedwars level {prefix} successfuly assigned! " + a.mention
                try:
                    socialMedias = player.JSON['socialMedia']['links']
                    if str(socialMedias['DISCORD']) == str(ctx.message.author):
                        if 40 > bwLvl >= 30 :
                            await ctx.author.add_roles(get(a.guild.roles, name="BW 30⭐"))
                            await ctx.send(success)
                        elif 50 > bwLvl >= 40:
                            await ctx.author.add_roles(get(a.guild.roles, name="BW 40⭐"))
                            await ctx.send(success)
                        elif 60 > bwLvl >= 50:
                            await ctx.author.add_roles(get(a.guild.roles, name="BW 50⭐"))
                            await ctx.send(success)
                        elif 70 > bwLvl >= 60:
                            await ctx.author.add_roles(get(a.guild.roles, name="BW 60⭐"))
                            await ctx.send(success)
                        elif 80 > bwLvl >= 70:
                            await ctx.author.add_roles(get(a.guild.roles, name="BW 70⭐"))
                            await ctx.send(success)
                        elif 90 > bwLvl >= 80:
                            await ctx.author.add_roles(get(a.guild.roles, name="BW 80⭐"))
                            await ctx.send(success)
                        elif 100 > bwLvl >=90:
                            await ctx.author.add_roles(get(a.guild.roles, name="BW 90⭐"))
                            await ctx.send(success)
                        elif 200 > bwLvl >=100:
                            await ctx.author.add_roles(get(a.guild.roles, name="BW 100⭐"))
                            await ctx.send(success)
                        elif bwLvl >= 200:
                            await ctx.author.add_roles(get(a.guild.roles, name="BW 200⭐"))
                            await ctx.send(success)                                                                                                                        
                        else:
                            await ctx.send(":octagonal_sign: You don't have enough stars... How did you even get here? :thinking:" + a.mention)
                    else:
                        await ctx.send(f":octagonal_sign: You are not the owner of that account or you haven't linked your Discord account to your Hypixel profile. To do so use `{prefix}link!" + a.mention)
                except KeyError:
                    await ctx.send(f":octagonal_sign: This user doesn't have a Discord account linked. Use `{prefix}hypixel link` and follow the steps given!")
            except hype.PlayerNotFoundException:
                await ctx.send(":octagonal_sign: Player not found!")


    @hypixelcmd.command()
    async def link(self, ctx):
        """This will teach you how to link a Discord account to a Hypixel profile!"""
        em = discord.Embed(title="__**How to link your Discord account with your Hypixel profile**__", description="This will teach you how to link your Discord account with your Hypixel profile so that you can use some commands provided by me :smile:", url="https://www.wikihow.com/Link-a-Discord-Account-with-a-Hypixel-Profile", colour=discord.Colour(2895667))
        em.set_thumbnail(url="https://cdn.discordapp.com/attachments/421358461473783819/435450006749708288/serveimage.jpeg")
        em.set_footer(text="How to link Discord with Hypixel page | For more info click the Hypixel icon.", icon_url="https://cdn.discordapp.com/attachments/421358461473783819/437591960874778645/cyborgtoast.png")
        em.add_field(name=":one:", value="First login into the Hypixel Network with your Minecraft account.")
        em.add_field(name=":two:", value="After successfuly logging in, right-click your player head.")
        em.add_field(name=":three:", value="Click on Social Media.")
        em.add_field(name=":four:", value="Left-click on Discord.", inline=False)
        em.add_field(name=":five:", value="Paste your Discord tag in chat (don't worry no one will see it). And now you are all done!")
        await ctx.send(embed=em)



"""Defining this extension"""
def setup(bot):
    bot.add_cog(hypixel(bot))