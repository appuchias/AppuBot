import discord
from discord.ext import commands

class PinkPills(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.command(alias="pkn")
    async def pinkpills(self,ctx, player: str=None):
        """Obtén información de uno de los jugadores del club."""
        # await ctx.send('Bajo construcción... Estará cuanto antes')
        # return
        if player == None:
            await ctx.send('Es obligatorio el campo de un jugador o miembro del club.\nEn caso de que creas que los estás poniendo bien y no te aparezca lo esperado, por favor contáctame (@PINK PILLS | Appu | CEO) o prueba con otros nicks que puedan funcionar.\nEl bot no es sensible a mayúsculas')
            return
        jugador = player.lower().replace("é", "e")
        if jugador == 'rigar' or jugador == 'rigar98':
            await ctx.send('Rigar98 **(CEO)**...\nRigar es el creador de este club. Es principalmemte el que hace que todo funcione.\nÉl es Javier Rivera, CEO y fundador del club, tiene 20 años y es de la Mallorca; estuvo en el 2º Equipo de CSGO.')
        elif jugador == 'appu' or jugador == 'appuchia':
            await ctx.send('Appuchia **(CEO)**...\nAppu es el gestor de Discord de Pink Pills desde enero de 2019. Ahora mismo estoy programando varios bots a la vez y voy aprendiendo según me hace falta. (Utilizo Python para los bots)\nSi tienes cualquier duda de algo de Discord, cuenta conmigo. Te responderé lo antes que pueda :upside_down:')
        elif jugador == 'leafff' or jugador == 'leaf' or jugador == 'leaff':
            await ctx.send('LeaFff **(CEO)**...\nLeaFff es AWP en Counter-Strike, de 15 años, que vive en Vigo y su nombre real es Pablo G.B. y es fan de G2. Su instagram es @leafff.cs.gg')
        elif jugador == 'skadi':
            await ctx.send('Skadi **(CEO)**...\nSkadi tiene 17 años (es del 2002), estudia un bachillerato de ciencias de la tecnología y aspira a ser ingeniero. En Pink Pills se encarga de streamear y ayudar en cualquier aspecto. Es de Galicia, España y se pasa su tiempo libre viendo animes y jugando.')
        elif jugador == 'h4lp3r':
            await ctx.send('H4lp3R **(CEO)**...\nH4lp3R es jugador de R6 en Pink Pills.\nHabla de su historia aquí: ||https://cdn.discordapp.com/attachments/523151601993646090/610993776323723265/TXT_H4lp3R.png||')
        elif jugador == 'acex':
            await ctx.send('AceX...\nAceX es jugador de CS:GO, posición de entry-fragger, tiene 16 años y 3 de ellos jugando CS.')
        elif jugador == 'predator' or jugador == 'pepote':
            await ctx.send('Predator...\nPredator es jugador de CSGO en Pink Pills, tiene 17 años, le gusta jugar con sus amigos y entrenar con el equipo.\nSe considera una persona callada y seria.')
        elif jugador == 'emybet' or jugador == 'jose':
            await ctx.send('Emybet...\nJosé es Lurker en el 2º equipo de CS:GO en Pink Pills. Él es de Córdoba.')
        elif jugador == 'mx4':
            await ctx.send('MX4...\nMX4 literalmente me ha dicho:\n\tHola, soy el Manager de el equipo de R6 de Pink Pills. Trabajo como desarrollador, tanto de software como web, especializado en ese último. Pertenezco al equipo de desarrollo del juego DeathGarden BloodHarvest. Como hobbie, jugar a videojuegos y dedicarle tiempo al club y a mi equipo de R6.')
        elif jugador == 'streapz':
            await ctx.send('StreapZ...\nStreapZ es jugador de LoL, en posición de support y Platino/Diamante\nSu twitch es: https://www.twitch.tv/streapzz')
        elif jugador == 'braindead':
            await ctx.send('Braindead...\nBraindead es jugador del equipo de LoL para PINK PILLS en la posición de jungla y es de Albacete')
        elif jugador == 'genaker':
            await ctx.send('Genaker...\nGenaker es el IGL del 1º equipo de CSGO en Pink Pills, muy buen jugador y repetable:\n*Hasta se metió en una jaula con un león, un tigre y un oso y acabo invicto* **!!**')
        elif jugador == 'jnk':
            await ctx.send('JnK...\nJnK es entry fragger del 1º equipo de CS:GO en Pink Pills.')

        elif jugador == 'bot':
            await ctx.send('Yo...\nYo no soy jugador de Pink Pills... Me banearon por aimhack y ahora me he quedado como ayudante.\n|| **NO ES BROMA** ||')
        elif jugador == '.':
            await ctx.send('...\n es ')

        else:
            await ctx.send('No hay un jugador con ese nombre o lo has escrito mal... :upside_down:')
            print('Pinkpills: Fail')
        print('Pinkpills: '+jugador)

def setup(client):
    client.add_cog(PinkPills(client))

# elif jugador == 'adrian':
#     await ctx.send('Adrian...\nAdrián es jugador de Rocket League de 17 años.')
# elif jugador == 'kimmys':
#     await ctx.send('KimmyS...\nKimmyS es jugador del 2° equipo de CSGO de Pink Pills, jugando como entry-fragger, tiene 16 años y es del País Vasco. Su nombre real es Kimetz Etxabe')
# elif jugador == 'adristo':
#     await ctx.send('Adristo...\nAdristo es jugador de Fortnite, sus amigos lo llaman "constructor"')
# elif jugador == 'joker':
#     await ctx.send('$ℰÑϴℛ  JOḰℰℜ...\n$ℰÑϴℛ  JOḰℰℜ es jugador competitivo de Clash Royale en Pink Pills, es un jugador español de 17 años residente en Francia.')
# elif jugador == 'jovi04':
#     await ctx.send('Jovi04...\nJovi is on fire, your team is terrified')
# elif jugador == 'rojiblanco':
#     await ctx.send('Rojiblanco...\nRojiblanco se llama Jesús Yeray es de las Islas Canarias, tiene 17 años, su cumpleaños es el 6 de Abril, juega para Pink Pills en el equipo de R6, es divertido y muy hablador y aparte de los videojuegos le encantan los animales y hacer senderos por la isla.')
# elif jugador == 'jagger':
#     await ctx.send('Jagger...\nJagger es jugador de CS:GO')
# elif jugador == 'nachoGamess':
#     await ctx.send('NachoGameSs.PKS...\nNachoGameS es jugador del primer equipo de Fortnite de Pink Pills Su nombre de verdad es Nacho vive en Zaragoza, Aragón')
# elif jugador == 'fuszahviing':
#     await ctx.send('FusZahViing...\nFusZahViing es jugador de Pink Pills')
# elif jugador == 'dank':
#     await ctx.send('DankMoney...\nDank es entrenador del 2º equipo de CS:GO y exjugador de Pink Pills')
# elif jugador == 'hel0s':
#     await ctx.send('Hэl0s✪...\nHэl0s✪ es jugador y capitán del 2° equipo de CS:GO en Pink Pills eSports.\nNo sabemos demasiado sobre él. Bueno, nadie sabe demasiado sobre él, pero hemos escuchado que tiene tanto aim que mató a un jugador que estaba en NBK de Cache desde conector de Train, con una sola bala!! :upside_down:')
# elif jugador == 'tete':
#     await ctx.send('tEtE...\ntEtE es un jugador de la R6 Academy de Pink Pills')
# elif jugador == 'napibula':
#     await ctx.send('NOOTpíbula...\nNOOTpíbula es, literalmente, "Best support mi casa".')
# elif jugador == 'boomer':
#     await ctx.send('Boomer.PKS...\nBoomer es jugador del 1º euipo de Fortnite en Pink Pills repartiendo ostias como panes 24/7.')
# elif jugador == 'woti':
#     await ctx.send('Woti...\nWoti es jugador de Pink Pills')
# elif jugador == 'alrube':
#     await ctx.send('Alrube...\nAlrube es jugador de Pink Pills')
# elif jugador == 'aron1t0':
#     await ctx.send('4aron1tO...\n4aron1tO es jugador de Pink Pills')
# elif jugador == 'tarik':
#     await ctx.send('TARIK...\nTARIK es jugador de Pink Pills')
# elif jugador == 'guti':
#     await ctx.send('Guti98...\nGuti98 es jugador de Pink Pills')
# elif jugador == 'gasmask':
#     await ctx.send('gasMask...\ngasMask es jugador de Pink Pills')
# elif jugador == 'espartanluc':
#     await ctx.send('EspartanLuc...\nEspartanLuc es jugador de Pink Pills')
# elif jugador == 'b3t4x':
#     await ctx.send('B3T4X...\nB3T4X es jugador de Pink Pills')
# elif jugador == 'alvaro':
#     await ctx.send('Alvaro...\nAlvaro es jugador de Pink Pills')
# elif jugador == 'ivanjesusrc':
#     await ctx.send('ivanjesusrc...\nivanjesusrc es jugador de Pink Pills')
# elif jugador == 'dragster':
#     await ctx.send('DragsteR...\nDragsteR es jugador de Pink Pills')
# elif jugador == 'alesito':
#     await ctx.send('alesito...\nalesito es jugador de Pink Pills')
# elif jugador == 'lex':
#     await ctx.send('LEX...\nLEX es jugador de Pink Pills')
# elif jugador == 'josejuan':
#     await ctx.send('joseJuan...\njoseJuan es jugador de Pink Pills')
# elif jugador == 'ivanbma':
#     await ctx.send('ivanBMA...\nivanBMA es jugador de Pink Pills')
# elif jugador == 'gt':
#     await ctx.send('GT...\nGT es jugador de Pink Pills')
# elif jugador == 'miguel':
#     await ctx.send('MIGUEL...\nMIGUEL es jugador de Pink Pills')
