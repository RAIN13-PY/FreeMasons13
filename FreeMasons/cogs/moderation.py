import discord
from discord.ext import commands
import asyncio
import datetime
import json
import time
from datetime import datetime
class ModerationCog(commands.Cog, name='Moderation'):

    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def purge(self, ctx, *, number:int=None):
        if ctx.author.guild_permissions.manage_messages:
            try:
                if number is None:
                    await ctx.send('You must put a number')
                else:
                    delete = await ctx.message.channel.purge(limit=number)
                    await ctx.send(f'Messages purged by {ctx.message.author.mention}: there were `{len(delete)}` messages purged')
            except:
                await ctx.send(f'Im having trouble purging `{len(delete)}` messages maybe try a lower number?')
        else:
                await ctx.send('You do not have premission to purge messages')

    @commands.command()
    async def kick(self, ctx, user:discord.Member, *, reason=None):
        if user.guild_permissions.manage_messages:
            await ctx.send(f'{ctx.message.author.mention} this user cannot be kicked ')
        elif ctx.message.author.guild_permissions.kick_members:
            if reason is None:
                await user.send(f"You have been kicked from `{user.guild}` by `{ctx.message.author}` because of `{reason}`")
                await ctx.guild.kick(user=user, reason='There was no reason given for your kick')
                await ctx.send(f'{user} has been kicked by {ctx.message.author.mention}')
            else:
                await user.send(f"You have been kicked from `{user.guild}` by `{ctx.message.author}` because of `{reason}`")
                await ctx.guild.kick(user=user, reason=reason)
                await ctx.send(f'{user} has been kicked by {ctx.message.author.mention} for {reason}')
        else:
            await ctx.send(f'{ctx.message.author.mention} you do not have perms to kick')

    @commands.command()
    async def ban(self, ctx, user:discord.Member=None, *, reason=None):
        if user is None:
            await ctx.send("Enter a user to ban")
            return
        if user.guild_permissions.manage_messages:
            await ctx.send(f'{ctx.message.author.mention} this user cannot be banned ')
        elif ctx.message.author.guild_permissions.ban_members:
            if reason is None:
                await user.send(f"You have been banned from `{user.guild}` by `{ctx.message.author}` because of `{reason}`")
                await ctx.guild.ban(user=user, reason='There was no reason given for your kick')
                await ctx.send(f'{user} has been banned by {ctx.message.author.mention}')
            else:
                await user.send(f"You have been banned from `{user.guild}` by `{ctx.message.author}` because of `{reason}`")
                await ctx.guild.ban(user=user, reason=reason)
                await ctx.send(f'{user} has been banned by {ctx.message.author.mention}')
        else:
            await ctx.send(f'{ctx.message.author.mention} you do not have perms to ban')
    

    @commands.command()
    async def warn(self, ctx, user:discord.Member, *, reason=None):
        if ctx.message.author.guild_permissions.kick_members:
            await user.send(f"You have been warned on {user.guild} by {ctx.message.author} because of `{reason}`")
        else:
            await ctx.send('You do not have perms to warn')


    @commands.command()
    async def mute(self, ctx, member:discord.Member):
        if ctx.message.author.guild_permissions.kick_members:
            role = discord.utils.get(ctx.guild.roles, name="muted")
            await member.add_roles(role)
            await ctx.send(f'{member} has been muted')
        else:
            await ctx.send(f'{ctx.message.author.mention} You do not have perms to mute')
    @commands.command()
    @commands.has_role("Admins")
    async def AddBlackListedWord(self, ctx,word=None):
        if word is None:
            await ctx.send("Please enter a word to blacklist")
            return
        with open("/Users/14028/Desktop/FreeMasons/cogs/BlackList.json", 'r') as b:
            data = json.load(b)
        if ctx.author.id != 702958589731668030:
            return
        for x in data['BlackListWords']:
            if(int(x['ID']) == 123):
                x['Words'].append(word)
                await ctx.send(f"{word} blacklisted")
        with open("/Users/14028/Desktop/FreeMasons/cogs/BlackList.json", 'w') as b:
            json.dump(data, b, indent=2)

    @commands.command()
    async def FacBeef(self, ctx, Playerone=None, Playertwo=None):
        if Playerone is None:
            await ctx.send("Please enter 2 users (dont use @'s)")
            return
        if Playertwo is None:
            await ctx.send("Please enter 2 users (dont use @'s)")
            return
        embed=discord.Embed(title="Faction Beef", color=0x0062ff)
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/803331991692902420/20e96d21ef3e29fc8fabd8e5573a0073.png?size=128")
        embed.add_field(name=f"{Playerone}", value="Member 1", inline=False)
        embed.add_field(name=f"{Playertwo}", value="Member 2", inline=True)
        embed.set_footer(text="Settle The BEEF")
        message = await ctx.send(embed=embed)
        await message.add_reaction('U+0030')
    @commands.command()
    async def ClaimCollector(self, ctx):
        with open("/Users/14028/Desktop/FreeMasons/cogs/Collecter.json", 'r') as b:
            data = json.load(b)
        for x in data['Collecter']:
            if x['ID'] == 123:
                if x['Person'] == 'None':
                    x['Person'] = str(ctx.author.name)
                    x['Time'] = str(datetime.now())
                    embed=discord.Embed(title="Chunk Collecter Claim", description="Use this to tell people that you are currently using chunk Collector")
                    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/803331991692902420/20e96d21ef3e29fc8fabd8e5573a0073.png?size=128")
                    embed.add_field(name=f"{ctx.author.name} has Claimed the Collecter at {x['Time']}", value="FreeMasons", inline=False)
                    embed.set_footer(text="do /CollectorCheck to see who currently is using collecter do /unclaimCollector to unclaim it")
                    await ctx.send(embed=embed)
                else:
                    await ctx.send("Someone has claimed the collector")
        with open("/Users/14028/Desktop/FreeMasons/cogs/Collecter.json", 'w') as b:
            json.dump(data, b, indent=2)
    @commands.command()
    async def CollectorCheck(self, ctx):
        with open("/Users/14028/Desktop/FreeMasons/cogs/Collecter.json", 'r') as b:
            data = json.load(b)
        for x in data['Collecter']:
            if x['ID'] == 123:
                if x['Person'] == 'None':
                    embed=discord.Embed(title="Collector Check", description="This command tells who is on the collector")
                    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/803331991692902420/20e96d21ef3e29fc8fabd8e5573a0073.png?size=128")
                    embed.add_field(name="No one has claimed the Collecter", value="FreeMasons", inline=False)
                    embed.set_footer(text="use /claimCollecter to claim it")
                    await ctx.send(embed=embed)
                    return
                else:
                    embed=discord.Embed(title="Collector Check", description="This command tells who is on the collector")
                    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/803331991692902420/20e96d21ef3e29fc8fabd8e5573a0073.png?size=128")
                    embed.add_field(name=f"{x['Person']} has the Collector claimed since {x['Time']}", value="FreeMasons", inline=False)
                    embed.set_footer(text="Do not use collector if someone has claimed it to unclaim use /unclaimCollector")
                    await ctx.send(embed=embed)
    @commands.command()
    async def unclaimCollector(self, ctx):
        with open("/Users/14028/Desktop/FreeMasons/cogs/Collecter.json", 'r') as b:
            data = json.load(b)
        for x in data['Collecter']:
            if x['ID'] == 123:
                if x['Person'] == ctx.author.name:
                    x['Person'] = 'None'
                    embed=discord.Embed(title="UnclaimCollecter", description="Unclaimed")
                    embed.set_author(name="FreeMasonBot")
                    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/803331991692902420/20e96d21ef3e29fc8fabd8e5573a0073.png?size=128")
                    embed.add_field(name="Succesfully unclaimed collecter", value="FreeMasons", inline=False)
                    embed.set_footer(text="use /claimCollector to claim it")
                    await ctx.send(embed=embed)
                else:
                    await ctx.send("You cant unclaim someone elses collector")
        with open("/Users/14028/Desktop/FreeMasons/cogs/Collecter.json", 'w') as b:
            json.dump(data, b, indent=2)

    

def setup(bot):
    bot.add_cog(ModerationCog(bot))
    print('Moderation loaded')