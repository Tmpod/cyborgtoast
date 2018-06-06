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
#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
import discord
from discord.ext import commands
from discord import utils
import reprlib
import json
import sys
import asyncio


with open('CYBORGBASEDATA.json') as json_data:
    database = json.load(json_data)
extensions = database['extensions']
prefix = database['prefixes']


class debugcog:
    def __init__(self, bot):
        self.bot = bot


    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.NotOwner):
            em = discord.Embed(description=f":octagonal_sign: You are not my creator! Cya!", color=discord.Colour.red())
            msg = await ctx.send(embed=em)
            await asyncio.sleep(3)
            await ctx.message.delete()
            await msg.delete()
        else:
            print(error)


    @commands.is_owner()
    @commands.group(aliases=['dg'])
    async def debug(self, ctx=None):
        """Debug/Bot Dev commands"""
        if ctx.invoked_subcommand is None:
            await ctx.send(embed=discord.Embed(description=f":octagonal_sign: You haven't specified which command to execute! Try `{prefix}help` to see which commands are available. {ctx.author.mention}" , color=discord.Colour.red()))


    @commands.is_owner()
    @commands.group(aliases=['db'])
    async def database(sefl, ctx=None):
        """Database commands"""
        if ctx.invoked_subcommand is None:
            await ctx.send(embed=discord.Embed(description=f":octagonal_sign: You haven't specified which command to execute! Try `{prefix}help` to see which commands are available. {ctx.author.mention}" , color=discord.Colour.red()))


    @debug.command()
    async def test(self, ctx):
        """Just retrieves a bunch of useful data"""
        auth = ctx.author
        guild = ctx.guild
        cat = ctx.channel.category
        chan = ctx.channel

        output = f"```{auth}\n\n{auth.nick}\n\n{auth.roles}\n\n{guild.name}\n\n{cat.name}\n\n{cat.channels}\n\n{chan.name}\n\n{self.bot.guilds}\n\n{self.bot.latency}```"
        await ctx.send(output)
        await ctx.send(reprlib.repr(cat.name))
        print(reprlib.repr(cat.name))
        print(self.bot.guilds[1:])
        # else:
        #     await ctx.send(":octagonal_sign: You are not my creator! Cya!")
        # await ctx.message.delete()


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


    @debug.command()
    async def test6(self, ctx):
        await ctx.send(f"```{ctx.author.roles}```")


    @debug.command()
    async def test7(self, ctx, smth):
        user = utils.find(lambda m: m.name == smth, ctx.guild.members)
        await ctx.send(f"```{ctx.message.channel}\n{user}\n{user.nick}```")


    @debug.command(aliases=['r'])
    async def reload(self, ctx, *, smth=None):
        if smth == None:
            em = discord.Embed(description=":question: You haven't specified which cog to reload!", color=discord.Colour.red())
            await ctx.send(embed=em)
        elif str(smth) in extensions:
            try:
                self.bot.unload_extension(smth)
                self.bot.load_extension(smth)
                em = discord.Embed(description=f":white_check_mark: Successfuly reloaded **{smth}** !", color=discord.Colour.green())
                await ctx.send(embed=em)
                print(f"\nSuccessfuly reloaded {smth}")
            except:
                em = discord.Embed(description=":octagonal_sign: An error occured during this process. Please refer to the shell.", color=discord.Colour.red())
                await ctx.send(embed=em)
        else:
            em = discord.Embed(description=":octagonal_sign: That cog name is not valid!", color=discord.Colour.red())
            await ctx.send(embed=em)


    @debug.command(aliases=['u'])
    async def unload(self, ctx, *, smth=None):
        if smth == None:
            em = discord.Embed(description=":question: You haven't specified which cog to unload!", color=discord.Colour.red())
            await ctx.send(embed=em)
        elif str(smth) in extensions:
            try:
                self.bot.unload_extension(smth)
                em = discord.Embed(description=f":white_check_mark: Successfuly unloaded **{smth}** !", color=discord.Colour.green())
                await ctx.send(embed=em)
                print(f"\nSuccessfuly unloaded {smth}")
            except:
                em = discord.Embed(description=":octagonal_sign: An error occured during this process. Please refer to the shell.", color=discord.Colour.red())
                await ctx.send(embed=em)
        else:
            em = discord.Embed(description=":octagonal_sign: That cog name is not valid!", color=discord.Colour.red())
            await ctx.send(embed=em)


    @debug.command(aliases=['l'])
    async def load(self, ctx, *, smth=None):
        if smth == None:
            em = discord.Embed(description=":question: You haven't specified which cog to load!", color=discord.Colour.red())
            await ctx.send(embed=em)
        elif str(smth) in extensions:
            try:
                self.bot.load_extension(smth)
                em = discord.Embed(description=f":white_check_mark: Successfuly loaded **{smth}** !", color=discord.Colour.green())
                await ctx.send(embed=em)
                print(f"\nSuccessfuly loaded {smth}")
            except:
                em = discord.Embed(description=":octagonal_sign: An error occured during this process. Please refer to the shell.", color=discord.Colour.red())
                await ctx.send(embed=em)
        else:
            em = discord.Embed(description=":octagonal_sign: That cog name is not valid!", color=discord.Colour.red())
            await ctx.send(embed=em)


    @debug.command(aliases=['cl', 'cogls'])
    async def coglist(self, ctx):
        prettycogs = '\n'.join(extensions)
        await ctx.send(embed=discord.Embed(title="Here's the full list of all the cogs!",description=f"```{prettycogs}```"))


    @debug.command(aliases=['gach'])
    async def getallchannels(self, ctx):
        guild = ctx.guild
        print(f"\n```Channels:\n{guild.channels}```")
        await ctx.send(f"```TextChannels: {guild.text_channels}```")
        await ctx.send(f"```VoiceChannels: {guild.voice_channels}```")
        await ctx.send(f"```Categories: {guild.categories}```")


    @debug.command(aliases=['gm'])
    async def getmention(self, ctx, smth):
        user = utils.find(lambda m: m.name == smth, ctx.guild.members)
        await ctx.send(f"```{user.mention}```")


    @debug.command(aliases=['exit', 'e', 'sd'])
    async def shutdown(self, ctx):
        em = discord.Embed(description=":bomb: Sutting down in 5 seconds...", color=discord.Colour.dark_red())
        await ctx.send(embed=em)
        await asyncio.sleep(5)
        channel = self.bot.get_channel(451776576237993984)
        em = discord.Embed(description=f":bomb: **{self.bot.user.name} successfuly shut down**", color=discord.Colour.dark_red())
        await channel.send(embed=em)
        sys.exit(1)


    @database.command(aliases=['gp', 'getprefix'])
    async def getprefixes(self, ctx, smth=None):
        await ctx.send(embed=discord.Embed(description=f"```{database['prefixes']}```", color=discord.Colour.greyple()))

    @database.command(aliases=['gb', 'getbot'])
    async def getbots(self, ctx, smth=None):
        if smth == None:
            result = database['guilds'][ctx.guild.name]['bots']
            await ctx.send(f"```{result}```")
        else:
            try:
                result = database['guilds'][smth]['bots']
                await ctx.send(f"```{result}```")
            except KeyError:
                em = discord.Embed(description=":octagonal_sign: That guild isn't supported yet!", color=discord.Colour.red())
                await ctx.send(embed=em)



    """Now the exec function. Courtesy of Espy#6820 (find it here: https://github.com/neko404notfound/nekosquared/blob/master/neko2/cogs/basics.py#L981-L1018). All credit for code from here to the marker "EXEC CODE END" goes to Espy, I do not wish to claim credit for this neat piece of code. I invite you to go send some love to him as he did a awesome job with Neko²."""
    @debug.command(hidden=True)
    async def exec(self, ctx, *, command):
        self.logger.warning(
            f'{ctx.author} executed {command!r} in {ctx.channel}')
        binder = bookbinding.StringBookBinder(ctx, max_lines=50, prefix='```python', suffix='```')

        try:
            binder.add_line('# Output:')
            if command.count('\n') == 0:
                with async_timeout.timeout(10):
                    if command.startswith('await '):
                        command = command[6:]
                    result = eval(command)
                    if inspect.isawaitable(result):
                        binder.add_line(
                            f'# automatically awaiting result {result}')
                        result = await result
                    binder.add(str(result))
            else:
                with async_timeout.timeout(60):
                    with io.StringIO() as output_stream:
                        with contextlib.redirect_stdout(output_stream):
                            with contextlib.redirect_stderr(output_stream):
                                wrapped_command = (
                                        'async def _aexec(ctx):\n' +
                                        '\n'.join(f'    {line}'
                                                  for line
                                                  in command.split('\n')) +
                                        '\n')
                                exec(wrapped_command)
                                result = await (locals()['_aexec'](ctx))
                        binder.add(output_stream.getvalue())
                        binder.add('# Returned ' + str(result))
        except:
            binder.add(traceback.format_exc())
        finally:
            binder.start()
#This is not wroking atm ^


"""Defining this extension"""
def setup(bot):
    bot.add_cog(debugcog(bot))

