import discord
from discord.ext import commands
import random

class Chat(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.command()
    async def suma(self, ctx, *, ns:int):
        if self.check_server(ctx) == 2 or self.check_server(ctx) == 3:
            return
        else:
            number = 0
            for n in ns:
                number = number+n
            await ctx.send(number)
            print('Suma')

    @commands.command()
    async def ping(self, ctx):
        if self.check_server(ctx) == 2 or self.check_server(ctx) == 3:
            return
        else:
            await ctx.send("Pong!")
            print('Ping')

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
            print('di '+output)

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
            print('reverse '+output)

        @commands.command()
        async def hello(self, ctx):
            await ctx.send("world!")

        @commands.command()
        async def repite(self, ctx, veces:int, *args):
            output = ' '
            for word in args:
                output += word
                output += ' '

            embed1 = discord.Embed(
            title = "**Appu's Bot**",
            description = 'Repite "{}" {} veces'.format(output, veces),
            colour = 0xf29fc5
            )

            a = 1

            if veces <= 10:
                for i in range(veces):
                    embed1.add_field(name=output, value=f'Repetición {a} de {veces}', inline=False)
                    a = a+1
            else:
                await ctx.send('Me da bastante pereza tantas veces, es muy repetitivo. Me empiezo a cansar a partir de 10')

            await ctx.send(embed=embed1)
            print(ctx.message.content)

    @commands.command()
    async def dado(self, ctx, n):
        if self.check_server(ctx) == 2 or self.check_server(ctx) == 3:
            return
        else:
            number = random.randint(1,int(n))
            await ctx.send(number)

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

    def check_server(self,ctx):
        if ctx.guild.id == 532203232114769921: #Fans
            return 1
        elif ctx.guild.id == 509297767752138752: #Oficial
            return 2
        elif ctx.guild.id == 541718509084868623: #Entrevistas
            return 3
        elif ctx.guild.id == 605857306634354689: #PKN Oficial
            return 4
        else:
            return 5

def setup(client):
    client.add_cog(Chat(client))
