import discord
from discord.ext import commands, tasks
import random
import asyncio
import os

prefix = '*'

class Extensions(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.client.log = self.log

    #Commands
    #Load an extension
    @commands.command()
    async def load(self, ctx, extension):
        self.client.load_extension(f'Cogs.{extension}')
        await ctx.send(f'Extensión {extension} cargada!')
        await self.log(ctx, f'Extension {extension} loaded!')

    #Unload an extension
    @commands.command()
    async def unload(self, ctx, extension):
        self.client.unload_extension(f'Cogs.{extension}')
        await ctx.send(f'Extensión {extension} descargada!')
        await self.log(ctx, f'Extension {extension} unloaded!')

    #Reload an extension
    @commands.command()
    async def reload(self, ctx, extension):
        self.client.unload_extension(f'Cogs.{extension}')
        await ctx.send(f'Extension {extension} descargada!')
        await ctx.send('Recargando en breve...')
        await asyncio.sleep(2)
        self.client.load_extension(f'Cogs.{extension}')
        await ctx.send(f'Extensión {extension} recragada!')
        await self.log(ctx, f'Extension {extension} reloaded!')

    #Logging function
    async def log(self, ctx, msg):
        channel = discord.utils.get(ctx.guild.channels, name='log')
        guild = ctx.guild
        if channel in guild.channels:
            await channel.send(msg)
            print(msg)
        else:
            await guild.create_text_channel(name='log', topic="The bot's log", reason='Needed to work')
            channel = discord.utils.get(ctx.guild.channels, name='log')
            overwrite = discord.PermissionOverwrite()
            overwrite.send_messages=False
            overwrite.read_messages=False
            await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)

            top_two = guild.roles[-2:]
            for role in top_two:
                await channel.set_permissions(role, read_messages=True, send_messages=True)
            await channel.send(msg)
            print(msg)
        f = open("modlog.txt", "a")
        f.write(f"{msg}\n")
        f.close()

def setup(client):
    client.add_cog(Extensions(client))
