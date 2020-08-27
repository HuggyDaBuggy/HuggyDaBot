import discord
import random
import asyncio
import os
from discord.ext import commands

client = commands.Bot(command_prefix = '/')

@client.event
async def on_ready():
    print('bruh')
    await client.change_presence(activity=discord.Game('Huggy the bot'))

@client.event
async def on_member_join(member):
    print(f'{member} hi or somehting')

@client.event
async def on_member_remove(member):
    print(f'{member} bye')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command()
async def huggy(ctx):
    response = ['bruh, lmao', 'literraly me after i breathe', 'insane', 'literraly me after i breathe insane', 'haha ban go brrr', 'bruh moment', 'walter', 'walter moment', 'hmmmoment', 'hmmmmmmmm']
    await ctx.send(f'huggy: {random.choice(response)}')

@client.command()
async def say(ctx, *, message):
    await ctx.send(f'{message}')

@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount + 1)
    await ctx.send(f'I have deleted {amount} messages')
    await asyncio.sleep(1)
    await ctx.channel.purge(limit=1)

@client.command()
async def kick(ctx, member : discord.Member, *,reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'Kicked {member.mention}')

@client.command()
async def ban(ctx, member : discord.Member, *,reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention}')

@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')
    for ban_entry in banned_users:
        user = ban_entry.user
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('Token')