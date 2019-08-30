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
        new = discord.utils.get(member.guild.roles, name="Nuevos")
        await member.add_roles(new)
        await member.send("Bienvenido al servidor oficial de **Pink Pills**\n\tAhora será avisado el cocreador y el gestor de Discord para la asignación de roles y demás procedimientos. Gracias por unirte a PINK PILLS :blush:")
        channel = discord.utils.get(member.guild.channels, name="nuevos-notificación")
        await channel.send(f"@everyone:\n{member.mention} se acaba de unir! :tada:")

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
    client.add_cog(Events(client))
