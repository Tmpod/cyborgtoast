"""Imports"""
import hypixel as hype
import discord
from discord import utils
from discord.ext import commands
from discord.utils import get
from discord.utils import find
import random
import asyncio
import reprlib


"""Snuggle's Hypixel API Wrapper Setup"""
with open("./CYBORGHYPEKEY.txt") as fp:
    API_KEYS = fp.read().strip()
hype.setKeys(API_KEYS)


"""Bot inicialization"""
with open('./CYBORGTOKEN.txt') as fp:
    TOKEN = fp.read().strip()
prefix = "-" #I define the prefix before hand so that I can use it anywhere else easily.
bot = commands.Bot(description="This is party manager bot and it has some Hypixel related commands as well as random querks. [InDev]", command_prefix=prefix)


"""Removing the default help command"""
bot.remove_command('help')


"""Boot-up"""
@bot.event
async def on_ready():
    print('\n==================')
    print("I'm ready!")
    print('Logged in as')
    print(bot.user.name)
    print("ID: " + str(bot.user.id))
    print(f"Current prefix: {prefix}")
    print('==================\n')
    async def change_activities():
        options = ('Minesweeper', 'Pong', 'Tic-tac toe', 'with the Discord API', 'with the Hypixel API')
        timeout = 60
        watch = discord.Activity(type=discord.ActivityType.watching, name=f"for {prefix}help")
        stream = discord.Streaming(url="https://www.twitch.tv/tmpod", name="bits of information")
        listen = discord.Activity(type=discord.ActivityType.listening, name="to beeps and bops")
        while True:
            game = discord.Game(name=random.choice(options))
            possb = random.choice([watch, stream, game, listen])
            await bot.change_presence(activity=possb)
            await asyncio.sleep(timeout)

    # To fire up the worker in the background:
    bot.loop.create_task(change_activities())


"""Custom help command"""
@bot.group(aliases=['h'])
async def help(ctx):
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
async def whisper(ctx):
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
async def hypixelhelp(ctx, whisper=None):
    a = ctx.message.author
    sWhisper = str(whisper)
    emb = discord.Embed(title="__**CyborgToast Help**__", colour=discord.Colour(11756839), description=f"Here are the Hypixel related commands. These are subcommands from the main `{prefix}hypixel` command (which can also be `{prefix}hy`). Here's an example of how to use these commands: `{prefix}hypixel rankinfo BonjourCroquette`. Don't forget to use `{prefix}` before your commands!")
    emb.set_thumbnail(url="https://discordemoji.com/assets/emoji/ThinkingInverted.png")
    emb.set_footer(text="CyborgToast Bot help page | For more info DM me @Tmpod#0836", icon_url="https://cdn.discordapp.com/attachments/421358461473783819/437591960874778645/cyborgtoast.png")
    emb.add_field(name="*rankinfo <IGN>*", value="This command tells you what Hypixel rank the player you typed in has. You may also use `rinfo` or `ri` instead of the default command.")
    emb.add_field(name="*getrank <IGN>*", value="This command will assign the Hypixel rank as a role on this Discord server, if the Hypixel profile name you provided has your Discord account linked. You may also use `gr` instead of the default command.")
    emb.add_field(name="*getbedwarslevel <IGN>*", value="This command will assign the Bedwars level as a role on this Discord server, if the Hypixel profile name you provided has your Discord account linked. You may also use `getbwlevel`, `getbwlvl`, `gbwl` or `bw` instead of the default command.")
    emb.add_field(name="*link*", value="This will teach you how to link a Discord account to a Hypixel profile!")
    if sWhisper == "w" or sWhisper == "dm" or sWhisper == "priv" or sWhisper == "private":
        await ctx.author.send(embed=emb)
    elif whisper == None:
        await ctx.send(embed=emb)
    else:
        await ctx.send("That's not a valid argument!")
    await ctx.message.delete()


@help.command(aliases=['p'])
async def party(ctx, whisper=None):
    a = ctx.message.author
    sWhisper = str(whisper)
    emb = discord.Embed(title="__**CyborgToast Help**__", colour=discord.Colour(11756839), description=f"Here are the Hypixel related commands. These are subcommands from the main `{prefix}hypixel` command (which can also be `{prefix}hy`). Here's an example of how to use these commands: `{prefix}hypixel rankinfo BonjourCroquette`. Don't forget to use `{prefix}` before your commands!")
    emb.set_thumbnail(url="https://discordemoji.com/assets/emoji/ThinkingInverted.png")
    emb.set_footer(text="CyborgToast Bot help page | For more info DM me @Tmpod#0836", icon_url="https://cdn.discordapp.com/attachments/421358461473783819/437591960874778645/cyborgtoast.png")
    emb.add_field(name="*create <party name>*", value="Create a party with the given name. If no name is given the party will be called <THEPARTYMASTERNICK>'s Part")
    emb.add_field(name="*remove <party name>*", value="TODO.")
    emb.add_field(name="*disband*", value="Kinda done.")
    if sWhisper == "w" or sWhisper == "dm" or sWhisper == "priv" or sWhisper == "private":
        await ctx.author.send(embed=emb)
    elif whisper == None:
        await ctx.send(embed=emb)
    else:
        await ctx.send("That's not a valid argument!")
    await ctx.message.delete()


"""Command Groups"""
@bot.group(aliases=['hy', 'hypixel'])
async def hypixelcmd(ctx=None):
    """Hypixel related commands"""
    if ctx.invoked_subcommand is None:
        a = ctx.message.author
        await ctx.send(f"You haven't specified which command to execute! Try `{prefix}help` to see which commands are available. " + a.mention)


@bot.group(aliases=['p'])
async def party(ctx=None):
    """Party managment commands"""
    if ctx.invoked_subcommand is None:
        a = ctx.message.author
        await ctx.send(f"You haven't specified which command to execute! Try `{prefix}help` to see which commands are available. " + a.mention)


"""The actual commands""" #TODO: Separate things into cogs
@hypixelcmd.command(aliases=['gr'])
async def getrank(ctx, *, something=None):
    """This command will assign the Hypixel rank as a role on this Discord server, if the Hypixel profile name you provided has your Discord account linked."""
    a = ctx.message.author
    if something is None:
        await ctx.send("You haven't provided any name! " + a.mention)
    else:
        try:
            player = hype.Player(something)
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
        except hype.PlayerNotFoundException:
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
            async with ctx.typing():
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
            player = hype.Player(something)
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
        except hype.PlayerNotFoundException:
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
async def lenny(ctx):
    """Sends Lenny. Why having this?  ( ͡° ͜ʖ ͡° ) """
    await ctx.send(" ( ͡° ͜ʖ ͡° ) ")
    await ctx.message.delete()


@party.command(aliases=['c'])
async def create(ctx, *, smth=None):
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


@party.command(aliases=['d'])
async def disband(ctx):
    cat = ctx.channel.category
    if cat in ("Staff Team", "Textin'", "Music 🎧", "Looking to play", "Important Stuff Here", None, "test 💾"):
        await ctx.send(f"You cannot execute that command here! {ctx.author.mention}")
    else:
        for i in cat.channels:
            await i.delete()
        await cat.delete()


@party.command(aliases=['a'])
async def add(ctx, *, smth):
    cat = ctx.channel.category
    overwrites = cat.overwrites
    user = utils.find(lambda m: m.name == smth, ctx.guild.members)
    userN = utils.find(lambda m: m.nick == smth, ctx.guild.members)
    if user != None:
        await cat.set_permissions(user, read_messages=True, send_messages=True)
    elif userN != None:
        await cat.set_permissions(userN, read_messages=True, send_messages=True)
    else:
        await ctx.send(f"There's no user with that name or nick! {ctx.author.mention}")


@bot.command()
async def ping(ctx):
    ping = str(bot.latency * 1000)[:3]
    await ctx.send(f"Pong! :ping_pong: \nThe ping is **{ping}**ms!")


@bot.command(aliases=['i'])
async def invite(ctx, *, smth=None):
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
        await ctx.message.delete()
    else:
        await ctx.send(f"The server you specified is not valid or supported. {auth.mention}")


@bot.command(aliases=['d'])
async def dice(ctx):
    d = ['1', '2', '3', '4', '5', '6']
    choice = random.choice(d)
    fm = await ctx.send("Rolling the dice...")
    await asyncio.sleep(2)
    await ctx.send(f"You rolled **{choice}**!")
    await fm.delete()


@bot.command(aliases=['m8b'])
async def magic8ball(ctx, *, smth=None):
    answers = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes definitely', 'You may rely on it', 'You can count on it', 'As I see it, yes', 'Most likely', 'Outlook good', 'Yes', 'Signs point to yes', 'Absolutely', 'Reply hazy try again', 'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again', "Don't count on it", 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful', "Chances aren't good"]
    if smth == None:
        await ctx.send(f"You haven't asked anything! {ctx.author.mention}")
    else:
        await ctx.send(choice(answers))





"""Execution"""
bot.run(TOKEN)
