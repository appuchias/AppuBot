import discord
from discord.ext import commands, tasks
import asyncio
import os
from itertools import cycle
from keep_alive import keep_alive
import json

copyright = "**Appu's Official Bot**\n*By Appúchia*"

def get_prefix(client, msg):
    if not msg.guild:   #If you are in DM channel
        return commands.when_mentioned_or("*")(client, msg)

    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

    if str(msg.guild.id) not in prefixes:   #If the guild has not got a custom prefix
        return commands.when_mentioned_or("*")(client, msg)

    prefix = prefixes[str(msg.guild.id)]
    return commands.when_mentioned_or(prefix)(client, msg)

client = commands.Bot(command_prefix=get_prefix)
client.remove_command('help')

async def owner(ctx):
    return ctx.author.id == 455321214525767680

@client.event
async def on_ready():
    print('Connected as:')
    print('{}: {}'.format(client.user.name, client.user.id))
    print('Prefix: *')
    print('--------------')
    change_status.start()
    game=discord.Game(name="*help | Appu's Official Bot | By Appu")
    await client.change_presence(activity=game)

@client.command(hidden=True)
async def emload(ctx, extension): #Emergency load
    client.load_extension(f'Cogs.{extension}')
    await ctx.send(f'Extensión {extension} cargada!')
    await log(ctx, f'Extension {extension} loaded!')

@client.command()
@commands.check(owner)
async def prefix(ctx, *, pref):
    with open("prefixes.json", "r") as f:
        prefixes =json.load(f)

    prefixes[str(ctx.guild.id)] = pref
    await ctx.send(f"El nuevo prefijo es {pref}")

    with open("prefixes.json", "w") as f:
        json.dump(prefixes, f, indent=4)

@client.command()
async def help(ctx):
    embed=discord.Embed(title='Help Command', description="Appu's", color=0x7289DA)
    embed.set_thumbnail(url=client.user.avatar_url)
    embed.set_footer(text=f'(By: {ctx.author}) |/| <> - Requerido, [] - Opcional |/| Todos los comandos se añaden a log', icon_url=ctx.author.avatar_url)

    if ctx.author.id == 455321214525767680:
        embed.add_field(name='`~General~`', value='**Comandos generales**', inline=False)
        embed.add_field(name='*help', value='Muestra este comando', inline=False)
        embed.add_field(name='*prefix <prefijo>', value="Cambia el prefijo del bot [Solo Propietario]", inline=False)
        embed.add_field(name='`~Mod~`', value='**Comandos de moderación** [Solo Mods]', inline=False)
        embed.add_field(name='*clear <n>', value='Elimina hasta 20 mensajes', inline=False)
        embed.add_field(name='*kick <@member> [motivo]', value='Echa a alguien', inline=False)
        embed.add_field(name='*ban <@member> [motivo]', value='Banea a alguien', inline=False)
        embed.add_field(name='*unban <nombre del miembro>', value='Elimina el ban al miembro especificado', inline=False)
        embed.add_field(name='*warn <@member> [motivo]', value="Avisa a alguien. Especifica motivo por favor", inline=False)
        embed.add_field(name='*mute <@member>', value="Mutea a alguien", inline=False)
        embed.add_field(name='*tmute <@member> <tiempo(minutos)>', value="Mutea a alguien durante el tiempo que le digas", inline=False)
        embed.add_field(name='`~Basic~`', value='**Comandos básicos**', inline=False)
        embed.add_field(name="*load <Extensión>", value="Carga la extensión que le digas [Only Mods]", inline=False)
        embed.add_field(name="*unload <Extensión>", value="Descarga la extensión que le digas [Only Mods]", inline=False)
        embed.add_field(name="*reload <Extensión>", value="Recarga la extensión que le digas [Only Mods]", inline=False)
        embed.add_field(name='`~Chat~`', value='**Comandos con respuestas en el chat directas**', inline=False)
        embed.add_field(name='*ping', value='Responde Pong! Útil para verificar la conexión', inline=False)
        embed.add_field(name='*di <msg>', value='Dice lo que pongas.', inline=False)
        embed.add_field(name='*reverse <msg>', value='Dice al revés lo que pone.', inline=False)
        embed.add_field(name='*repite <veces> <msg>', value='Repite lo que quieras hasta 10 veces.', inline=False)
        embed.add_field(name='*suma <n1> <n2> <n3>', value='Suma hasta 3 números.', inline=False)
        embed.add_field(name='*dado <n de caras>', value='Tira un dado de cualquier número de caras.', inline=False)
        embed.add_field(name='*moneda', value='Lanza una moneda.', inline=False)
        await ctx.send(embed=embed)
        return

    else:
        embed.add_field(name='`~General~`', value='**Comandos generales**', inline=False)
        embed.add_field(name='*help', value='Muestra este comando', inline=False)
        embed.add_field(name='*prefix <prefijo>', value="Cambia el prefijo del bot [Solo Propietario]", inline=False)
        embed.add_field(name='`~Mod~`', value='**Comandos de moderación** [Solo Mods]', inline=False)
        embed.add_field(name='*clear <n>', value='Elimina hasta 20 mensajes', inline=False)
        embed.add_field(name='*kick <@member> [motivo]', value='Echa a alguien', inline=False)
        embed.add_field(name='*ban <@member> [motivo]', value='Banea a alguien', inline=False)
        embed.add_field(name='*unban <nombre del miembro>', value='Elimina el ban al miembro especificado', inline=False)
        embed.add_field(name='*warn <@member> [motivo]', value="Avisa a alguien. Especifica motivo por favor", inline=False)
        embed.add_field(name='*mute <@member>', value="Mutea a alguien", inline=False)
        embed.add_field(name='*tmute <@member> <tiempo(minutos)>', value="Mutea a alguien durante el tiempo que le digas", inline=False)
        embed.add_field(name='`~Basic~`', value='**Comandos básicos**', inline=False)
        embed.add_field(name="*load <Extensión>", value="Carga la extensión que le digas [Only Mods]", inline=False)
        embed.add_field(name="*unload <Extensión>", value="Descarga la extensión que le digas [Only Mods]", inline=False)
        embed.add_field(name="*reload <Extensión>", value="Recarga la extensión que le digas [Only Mods]", inline=False)
        embed.add_field(name='`~Chat~`', value='**Comandos con respuestas en el chat directas**', inline=False)
        embed.add_field(name='*ping', value='Responde Pong! Útil para verificar la conexión', inline=False)
        embed.add_field(name='*di <msg>', value='Dice lo que pongas.', inline=False)
        embed.add_field(name='*reverse <msg>', value='Dice al revés lo que pone.', inline=False)
        embed.add_field(name='*repite <veces> <msg>', value='Repite lo que quieras hasta 10 veces.', inline=False)
        embed.add_field(name='*suma <n1> <n2> <n3>', value='Suma hasta 3 números.', inline=False)
        embed.add_field(name='*dado <n de caras>', value='Tira un dado de cualquier número de caras.', inline=False)
        embed.add_field(name='*moneda', value='Lanza una moneda.', inline=False)
    #embed.add_field(name=f'*', value=None, inline=False)
    await ctx.send(embed=embed)

async def log(ctx, msg):
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

#Blinking current statuses
activities = cycle([f"*help | Appu's Bot | Trabajando duramente para crear un mundo mejor :D", f"*help | Appu's Bot"])
statuses = cycle([discord.Status.idle, discord.Status.online])

@client.command(hidden=True)
@commands.check(commands.is_owner())
async def logout(ctx):
    await ctx.message.delete()
    msg = await ctx.send('Desconectando...')
    await asyncio.sleep(2)
    await msg.delete()
    await client.logout()

#Load all extensions
extensions = []
for filename in os.listdir('./Cogs'):
    if str(filename).endswith('.py'):
        client.load_extension(f'Cogs.{filename[:-3]}')
        extensions.append(filename[:-3])
print(f'{extensions} loaded!')


#Tasks
keep_alive()
#Status
@tasks.loop(seconds=5)
async def change_status():
    await client.change_presence(status=next(statuses), activity=discord.Game(next(activities)))

client.run(os.environ.get("Token_Bot"))
