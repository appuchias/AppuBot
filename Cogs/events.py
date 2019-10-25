import discord
from discord.ext import commands, tasks
import asyncio

#Bot prefix
prefix = '*'

class Events(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.client.log = self.log

    #Events
    #When a reaction is added to a message
    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        if user == self.client.user:
            return
        else:
            await reaction.message.add_reaction(reaction)
            await self.log(reaction.message.channel, f'(#{reaction.message.channel}): Reacción {str(reaction)} añadida al mensaje "{reaction.message.content}" por {user}')

    #When a reaction is removed from a message
    @commands.Cog.listener()
    async def on_reaction_remove(self, reaction, user):
        if user == self.client.user:
            return
        else:
            await reaction.message.remove_reaction(reaction, self.client.user)
            await self.log(reaction.message.channel, f'(#{reaction.message.channel}): Reacción {str(reaction)} eliminada del mensaje "{reaction.message.content}" por {user}')

    @commands.Cog.listener()
    async def on_member_join(member):
        new = discord.utils.get(member.guild.roles, name="Readme")
        await member.add_roles(new)
        await member.send("Bienvenido!")
        channel = discord.utils.get(member.guild.channels, name="usuarios")
        await channel.send(f"@everyone:\n{member.mention} se acaba de unir! :tada:")

    @commands.Cog.listener()
    async def on_member_remove(member):
        channel = discord.utils.get(member.guild.channels, name="usuarios")
        await channel.send(f"{user} se acaba de ir, parece que no lo pasaba bien D:")

    @commands.command()
    async def login(self, ctx):
        user = ctx.author
        readme = discord.utils.get(ctx.guild.roles, name="Readme")
        todos = discord.utils.get(ctx.guild.roles, name="Todos")
        await user.remove_roles(readme)
        await user.add_roles(todos)
        await user.send("Bienvenido al server! Pásalo bien! Para consultar las normas ve a ")

    #Logging function
    async def log(self, ctx, msg):
        channel = discord.utils.get(ctx.guild.channels, name='log')
        if channel in ctx.guild.channels:
            pass
        else:
            await guild.create_text_channel(name='log', topic="El log del bot. Silénciame si no quieres morir por notificaciones :)", reason='Log necesario...')
            channel = discord.utils.get(ctx.guild.channels, name='log')
            overwrites = {guild.default_role: discord.PermissionOverwrite(read_messages=False, send_messages=False)}

            top_two = guild.roles[-2:]
            for role in top_two:
                overwrite[role] = discord.PermissionOverwrite(read_messages=True, send_messages=True)
            await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
        await channel.send(msg)
        print(f"Log: {msg}")

        with open("modlog.txt", "a") as f:
            f.write(f"Log: {msg}")

def setup(client):
    client.add_cog(Events(client))
