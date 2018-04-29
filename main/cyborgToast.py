#Imports
import hypixel
import discord
from discord import utils
from discord.ext import commands
from discord.utils import get
import random
import asyncio


#Snuggle's Hypixel API Wrapper Setup
API_KEYS = ['8bffd101-c891-4c18-8eec-9283c7e95a23']
hypixel.setKeys(API_KEYS)


#Bot inicialization
TOKEN = 'NDM2NjE3ODE3MDQzNzYzMjAw.DbqIDw.5uaoqimdpwKJz6N6rNfeTdo_U68'
prefix = "-" #I define the prefix before hand so that I can use it anywhere else easily.
bot = commands.Bot(description="This bot detects your Hypixel rank and assigns a corresponding role", command_prefix=prefix)


#Removing the default help command
bot.remove_command('help')


#Boot-up
@bot.event
async def on_ready():
    print('==================')
    print("I'm ready!")
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('==================')
    async def change_activities():
        options = ('Minesweeper', 'Pong', 'Tic-tac toe')
        timeout = 60
        watch = discord.Activity(type=discord.ActivityType.watching, name=f"for {prefix}help")
        stream = discord.Streaming(url="https://www.twitch.tv/tmpod", name="bits of information")
        listen = discord.Activity(type=discord.ActivityType.listening, name="to beeps and boops")
        while True:
            game = discord.Game(name=random.choice(options))
            possb = random.choice([watch, stream, game, listen])
            await bot.change_presence(activity=possb)
            await asyncio.sleep(timeout)

    # To fire up the worker in the background:
    bot.loop.create_task(change_activities())


#Custom help command
@bot.group(aliases=['h'])
async def help(ctx):
    if ctx.invoked_subcommand is None:
        a = ctx.message.author
        emb = discord.Embed(title="__**CyborgToast Help**__", colour=discord.Colour(11756839), description=f"Here is the normal-user available command list. The prefix for this bot is currently `{prefix}` . You have to **always** put it right before the key command words without any spaces. _Example:_ `{prefix}help w`")
        emb.set_thumbnail(url="https://discordemoji.com/assets/emoji/ThinkingInverted.png")
        emb.set_footer(text="CyborgToast Bot help page | For more info DM me at Tmpod#0836", icon_url="https://cdn.discordapp.com/attachments/421358461473783819/437591960874778645/cyborgtoast.png")
        emb.add_field(name="*hypixel <subcommand>*", value=f"This category contains some Hypixel related commands. Do `{prefix}help hypixel` to check all the Hypixel related commands! You may also use `hy` instead of the default command.")
        emb.add_field(name="*party <subcommand>*", value=f"This category contains the party management commands. Do `{prefix}help party` to check all the Hypixel related commands! You may also use `p` instead of the default command.")
        emb.add_field(name="*shrug*", value="Sends a shrug. Why having this? ¯\\_(ツ)_/¯")
        emb.add_field(name="*help*", value="Shows this message. You can use `help w` to get this message in a DM to you! You may also use `h` instead of the default command")
        await ctx.send(embed=emb)
        await ctx.message.delete()


@help.command(aliases=['w', 'dm', 'priv', 'private'])
async def whisper(ctx):
    a = ctx.message.author
    emb = discord.Embed(title="__**CyborgToast Help**__", colour=discord.Colour(11756839), description=f"Here is the normal-user available command list. The prefix for this bot is currently `{prefix}` . You have to **always** put it right before the key command words without any spaces. _Example:_ `{prefix}help w`")
    emb.set_thumbnail(url="https://discordemoji.com/assets/emoji/ThinkingInverted.png")
    emb.set_footer(text="CyborgToast Bot help page | For more info DM me at Tmpod#0836", icon_url="https://cdn.discordapp.com/attachments/421358461473783819/437591960874778645/cyborgtoast.png")
    emb.add_field(name="*hypixel <subcommand>*", value=f"This category contains some Hypixel related commands. Do `{prefix}help hypixel` to check all the Hypixel related commands! You may also use `hy` instead of the default command.")
    emb.add_field(name="*shrug*", value="Sends a shrug. Why having this? ¯\\_(ツ)_/¯")
    emb.add_field(name="*help*", value="Shows this message. You can use `help w` to get this message in a DM to you! You may also use `h` instead of the default command")
    await ctx.author.send(embed=emb)
    await ctx.message.delete()


@help.command(aliases=['hy', 'hypixel'])
async def hypixelhelp(ctx, whisper=None):
    a = ctx.message.author
    sWhisper = str(whisper)
    emb = discord.Embed(title="__**CyborgToast Help**__", colour=discord.Colour(11756839), description=f"Here are the Hypixel related commands. These are subcommands from the main `{prefix}hypixel` command (which can also be `{prefix}hy`). Here's an example of how to use these commands: `{prefix}hypixel rankinfo BonjourCroquette`. Don't forget to use `{prefix}` before your commands!")
    emb.set_thumbnail(url="https://discordemoji.com/assets/emoji/ThinkingInverted.png")
    emb.set_footer(text="CyborgToast Bot help page | For more info DM me at Tmpod#0836", icon_url="https://cdn.discordapp.com/attachments/421358461473783819/437591960874778645/cyborgtoast.png")
    emb.add_field(name="*rankinfo <IGN>*", value="This command tells you what Hypixel rank the player you typed in has. You may also use `rinfo` or `ri` instead of the default command.")
    emb.add_field(name="*getrank <IGN>*", value="This command will assign the Hypixel rank as a role on this Discord server, if the Hypixel profile name you provided has your Discord account linked. You may also use `gr` instead of the default command.")
    emb.add_field(name="*link*", value="This will teach you how to link a Discord account to a Hypixel profile!")
    if sWhisper == "w" or sWhisper == "dm" or sWhisper == "priv" or sWhisper == "private":
        await ctx.author.send(embed=emb)
    else:
        await ctx.send(embed=emb)
    await ctx.message.delete()


@help.command(aliases=['p'])
async def party(ctx, whisper=None):
    a = ctx.message.author
    sWhisper = str(whisper)
    emb = discord.Embed(title="__**CyborgToast Help**__", colour=discord.Colour(11756839), description=f"Here are the Hypixel related commands. These are subcommands from the main `{prefix}hypixel` command (which can also be `{prefix}hy`). Here's an example of how to use these commands: `{prefix}hypixel rankinfo BonjourCroquette`. Don't forget to use `{prefix}` before your commands!")
    emb.set_thumbnail(url="https://discordemoji.com/assets/emoji/ThinkingInverted.png")
    emb.set_footer(text="CyborgToast Bot help page | For more info DM me at Tmpod#0836", icon_url="https://cdn.discordapp.com/attachments/421358461473783819/437591960874778645/cyborgtoast.png")
    emb.add_field(name="*create <party name>*", value="Create a party with the given name.")
    emb.add_field(name="*remove <party name>*", value="TODO.")
    emb.add_field(name="*disband*", value="TODO")
    if sWhisper == "w" or sWhisper == "dm" or sWhisper == "priv" or sWhisper == "private":
        await ctx.author.send(embed=emb)
    else:
        await ctx.send(embed=emb)
    await ctx.message.delete()


#Groups
@bot.group(aliases=['hy', 'hypixel'])
async def hypixelcmd(ctx=None):
    if ctx.invoked_subcommand is None:
        a = ctx.message.author
        await ctx.send(f"You haven't specified which command to execute! Try `{prefix}help` to see which commands are available. " + a.mention)


@bot.group(aliases=['p'])
async def party(ctx=None):
    if ctx.invoked_subcommand is None:
        a = ctx.message.author
        await ctx.send(f"You haven't specified which command to execute! Try `{prefix}help` to see which commands are available. " + a.mention)


#The actual commands
@hypixelcmd.command(aliases=['gr'])
async def getrank(ctx, *, something=None):
    """This command will assign the Hypixel rank as a role on this Discord server, if the Hypixel profile name you provided has your Discord account linked."""
    a = ctx.message.author
    if something is None:
        await ctx.send("You haven't provided any name! " + a.mention)
    else:
        try:
            player = hypixel.Player(something)
            pRank = str(player.getRank()['rank'])
            success = f"{pRank} rank successfuly assigned! " + a.mention
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
                        await ctx.send(a.mention + "You don't have a rank on the Hypixel Network.")
                else:
                    await ctx.send(a.mention + "You are not the owner of that account or you haven't linked your Discord account to your Hypixel profile. To do so use `!hypixelverify`!")
            except KeyError:
                await ctx.send(f"This user doesn't have a Discord account linked. Use `{prefix}hypixel link` and follow the steps given!")
        except hypixel.PlayerNotFoundException:
            await ctx.send("Player not found!")
    await ctx.message.delete()


@hypixelcmd.command(aliases=['ri', 'rinfo'])
async def rankinfo(ctx, something=None):
    """This commad tells you what Hypixel rank the player you typed in has."""
    a = ctx.message.author
    if something is None:
        await ctx.send("You haven't provided any name! " + a.mention)
    else:    
        try:
            player = hypixel.Player(something)
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
        except hypixel.PlayerNotFoundException:
            await ctx.send("Player not found!")
    await ctx.message.delete()


@hypixelcmd.command(aliases=['getbwlevel', 'getbwlvl', 'gbwl', 'bw'])
async def getbedwarslevel(ctx, something=None):
    """This command will assign the Bedwars level as a role on this Discord server, if the Hypixel profile name you provided has your Discord account linked. """
    a = ctx.message.author
    if something is None:
        await ctx.send("You haven't provided any name! " + a.mention)
    else:
        try:
            player = hypixel.Player(something)
            bwLvl = int(player.getBWLvL())
            success = f"Bedwars level {prefix} successfuly assigned! " + a.mention
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
                        await ctx.send(a.mention + "You don't have enough stars... How did you even get here? :emote3:")
                else:
                    await ctx.send(a.mention + "You are not the owner of that account or you haven't linked your Discord account to your Hypixel profile. To do so use `!hypixelverify`!")
            except KeyError:
                await ctx.send(f"This user doesn't have a Discord account linked. Use `{prefix}hypixel link` and follow the steps given!")
        except hypixel.PlayerNotFoundException:
            await ctx.send("Player not found!")
    await ctx.message.delete()


@hypixelcmd.command()
async def link(ctx):
    """This will teach you how to link a Discord account to a Hypixel profile!"""
    em = discord.Embed(title="__**How to link your Discord account with your Hypixel profile**__", description="This will teach you how to link your Discord account with your Hypixel profile so that you can use some commands provided by me :smile:", url="https://www.wikihow.com/Link-a-Discord-Account-with-a-Hypixel-Profile", colour=discord.Colour(2895667))
    em.set_thumbnail(url="https://cdn.discordapp.com/attachments/421358461473783819/435450006749708288/serveimage.jpeg")
    em.set_footer(text="How to link Discord with Hypixel page | For more info click the Hypixel icon.", icon_url="https://cdn.discordapp.com/attachments/421358461473783819/437591960874778645/cyborgtoast.png")
    em.add_field(name=":one:", value="First login into the Hypixel Network with your Minecraft account.")
    em.add_field(name=":two:", value="After successfuly logging in, right-click your player head.")
    em.add_field(name=":three:", value="Click on Social Media.")
    em.add_field(name=":four:", value="Left-click on Discord.", inline=False)
    em.add_field(name=":five:", value="Paste your Discord tag in chat (don't worry no one will see it). And now you are all done!")
    await ctx.message.delete()
    await ctx.send(embed=em)


@bot.command()
async def shrug(ctx):
    """Send a shrug. Why having this? ¯\_(ツ)_/¯"""
    await ctx.message.delete()
    await ctx.send("¯\_(ツ)_/¯")



@party.command()
async def create(ctx, *, smth=None):
    guild = ctx.guild
    # illum = utils.get(ctx.guild.roles, id=437701360151035915)
    if smth is None:
        overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False),
        guild.me: discord.PermissionOverwrite(read_messages=True),
        # illum: discord.PermissionOverwrite(read_messages=True)
    }
        cat = await guild.create_category_channel(ctx.message.author, overwrites = overwrites)
    else:
        await ctx.send("placeholder")





















#Execution
bot.run(TOKEN)

