import discord
from discord.ext import commands
import youtube_dl
import asyncio

players = {}
queues = {}

class Music:
    def __init__(self,client):
        self.client = client



    def check_queue(id):
        if queues[id] != []:
            player = queues[id].pop(0)
            players[id] = player
            player.start()

    @commands.command(pass_context=True)
    async def play(self, ctx, url):
        server = ctx.message.server
        channel = ctx.message.author.voice.voice_channel
        voice_client = self.client.voice_client_in(server)
        player = await voice_client.create_ytdl_player(url, after=lambda : check_queue(server.id))
        players[server.id] = player
        await ctx.send('Ahora está sonando "{}"'.format(url))
        print('Reproduciendo música en {}'.format(server))
        player.start()

    @commands.command(pass_context=True)
    async def join(self,ctx):
        server = ctx.message.server
        channel = ctx.message.author.voice.voice_channel
        await self.client.join_voice_channel(channel)
        await ctx.send('Unido al canal "{}"'.format(channel))
        print('Unido a un canal en {}'.format(server))

    @commands.command(pass_context=True)
    async def leave(self,ctx):
        server = ctx.message.server
        voice_client = self.client.voice_client_in(server)
        await voice_client.disconnect()
        await ctx.send('Me he ido de un canal en {}'.format(server))
        print('Me he ido de un canal en {}'.format(server))

    @commands.command(pass_context=True)
    async def queue(self,ctx, url):
        server = ctx.message.server
        voice_client = self.client.voice_client_in(server)
        player = await voice_client.create_ytdl_player(url)

        if server.id in queues:
            queues[server.id].append(player)
        else:
            queues[server.id] = [player]
        await ctx.send('Añadido "{}" a la cola!'.format(url))
        print('Añadido [{}:{} a la cola'.format(server,voice_client))

    @commands.command(pass_context=True)
    async def pause(self,ctx):
        id = ctx.message.server.id
        players[id].pause()
        await ctx.send('Pausado')
        print('Pausado')

    @commands.command(pass_context=True)
    async def stop(self,ctx):
        id = ctx.message.server.id
        players[id].stop()
        await ctx.send('Finalizado')
        print('Finalizado')

    @commands.command(pass_context=True)
    async def resume(self,ctx):
        id = ctx.message.server.id
        players[id].resume()
        await ctx.send('Continuado')
        print('Continuado')

def setup(client):
    client.add_cog(Music(client))
