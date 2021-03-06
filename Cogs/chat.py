import discord
from discord.ext import commands
import random

class Chat(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.command()
    async def suma(self, ctx, *, args):
        output=0
        for n in args.split(" "):
            output+=int(n)
            print(output)
        await ctx.send(output)
        await self.log(ctx, output)

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"Pong! ||({round(self.client.latency*1000)}ms)||")
        await self.log(ctx, f"Pong! ||({round(self.client.latency*1000)}ms)||")

    @commands.command()
    async def di(self, ctx, *, args):
        if self.check_server(ctx) == 2 or self.check_server(ctx) == 3:
            return
        else:
            output = ' '
            for word in args.split(" "):
                output += word
                output += ' '
            await ctx.send(output)
            await self.log(ctx, output)

    @commands.command()
    async def reverse(self, ctx, *, args):
        if self.check_server(ctx) == 2 or self.check_server(ctx) == 3:
            return
        else:
            output = ' '
            for word in args.split(" "):
                output += word
                output += ' '
            output = output[::-1]
            await ctx.send(output)
            await self.log(ctx, f"Reverse: {output}")

        @commands.command()
        async def hello(self, ctx):
            await ctx.send("world!")

        @commands.command()
        async def repite(self, ctx, veces:int, *args):
            output = ' '
            for word in args:
                output += word
                output += ' '

            embed = discord.Embed(
            title = "**Appu's Bot**",
            description = 'Repite "{}" {} veces'.format(output, veces),
            colour = 0xf29fc5
            )

            a = 1

            if veces <= 10:
                for i in range(veces):
                    embed.add_field(name=output, value=f'Repetición {a} de {veces}', inline=False)
                    a = a+1
            else:
                await ctx.send('Me da bastante pereza tantas veces, es muy repetitivo. Me empiezo a cansar a partir de 10')

            await ctx.send(embed=embed)

    @commands.command()
    async def dado(self, ctx, n):
        number = random.randint(1,int(n))
        await ctx.send(number)
        await self.log(ctx, f"Dado: {number}")

    @commands.command()
    async def moneda(self, ctx):
        if self.check_server(ctx) == 2 or self.check_server(ctx) == 3:
            return
        else:
            numero = random.randint(0,2)
            if numero == 1:
                await ctx.send('Ha salido CARA!')
            elif numero == 2:
                await ctx.send('Ha salido CRUZ')
            elif numero == 0:
                number = random.randint(0,2)
                if number == 1:
                    await ctx.send('Ha salido CARA!')
                elif number == 2:
                    await ctx.send('Ha salido CRUZ')
                elif number == 0:
                    n = random.randint(0,2)
                    if n == 1:
                        await ctx.send('Ha salido CARA!')
                    elif n == 2:
                        await ctx.send('Ha salido CRUZ')
                    elif n == 0:
                        await ctx.send('***CANTO!!!***:tada::tada:')
        await self.log(ctx, f"Moneda: {numero}")

    async def log(self, ctx, msg):
        channel = discord.utils.get(ctx.guild.channels, name='log')
        if channel in ctx.guild.channels:
            pass
        else:
            await ctx.guild.create_text_channel(name='log', topic="El log del bot. Silénciame si no quieres morir por notificaciones :)", reason='Log necesario...')
            channel = discord.utils.get(ctx.guild.channels, name='log')
            overwrites = {ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False, send_messages=False)}

            top_two = ctx.guild.roles[-2:]
            for role in top_two:
                overwrites[role] = discord.PermissionOverwrite(read_messages=True, send_messages=True)
            await channel.set_permissions(ctx.guild.default_role, overwrite=overwrites)
        await channel.send(msg)
        print(f"Log: {msg}")

        with open("modlog.txt", "a") as f:
            f.write(f"Log: {msg}\n")

def setup(client):
    client.add_cog(Chat(client))
