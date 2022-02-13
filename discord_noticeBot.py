import discord
from discord.activity import Streaming
from discord.ext import commands
import datetime


from web_scrap import precioInicial
from web_scrap import precioDeseado

bot = commands.Bot(command_prefix=">", description="Soy el bot dis_noticeBot")

@bot.command()
async def ready(ctx):
    await ctx.send('Ignorame solo soy un bot')

@bot.command()
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="asdas dfgdf", 
    timestamp=datetime.datetime.utcnow(), color=discord.Color.blurple())
    embed.add_field(name="Servidor creador el", value=f"{ctx.guild.User.created_at}")
    embed.add_field(name="Server Dueño", value=f"{ctx.guild.owner}")
    await ctx.send(embed=embed)

@bot.command()
async def steamDiscount(ctx):
    if precioInicial < precioDeseado:
        test = (f"ATENCION Hay oferta, bajo el precio! Esta en: S/.{precioInicial} en el Enlace: https://store.steampowered.com/app/728880")
        await ctx.send(test)
    else:
        test = ("No hay oferta")
        await ctx.send(test)

# Eventos
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="Tu bot favorito", url="https://www.twitch.tv/rubius"))
    print('Bot Ready')

bot.run('<your_discord_code>')
