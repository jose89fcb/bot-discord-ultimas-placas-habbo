import discord
from discord.ext import commands
import requests
import json



 
 
 
bot = commands.Bot(command_prefix='!', description="ayuda bot") #Comando
bot.remove_command("help") # Borra el comando por defecto !help
 
 
@bot.command()
async def ultimasplacas(ctx):
    response = requests.get(f"https://www.habbotravel.com/tools/getBadgesBox.php?page=1")
    codigo1 = response.json()['data'][0]['name']
    codigo2 = response.json()['data'][1]['name']
    codigo3 = response.json()['data'][2]['name']
    codigo4 = response.json()['data'][3]['name']
    codigo5 = response.json()['data'][4]['name']
  


    
    
    #PLACA 1
    embed = discord.Embed(title=f"Código: {codigo1}", description="1")
    embed.set_thumbnail(url="https://images.habbo.com/c_images/album1584/" + f"{codigo1}.png")
    await ctx.channel.send(embed=embed)


    #PLACA 2
    embed = discord.Embed(title=f"Código: {codigo2}", description="2")
    embed.set_thumbnail(url="https://images.habbo.com/c_images/album1584/" + f"{codigo2}.png")
    await ctx.channel.send(embed=embed)

    #PLACA 3
    embed = discord.Embed(title=f"Código: {codigo3}", description="3")
    embed.set_thumbnail(url="https://images.habbo.com/c_images/album1584/" + f"{codigo3}.png")
    await ctx.channel.send(embed=embed)

    #PLACA 4
    embed = discord.Embed(title=f"Código: {codigo4}", description="4")
    embed.set_thumbnail(url="https://images.habbo.com/c_images/album1584/" + f"{codigo4}.png")
    await ctx.channel.send(embed=embed)

    #PLACA 5
    embed = discord.Embed(title=f"Código: {codigo5}", description="5")
    embed.set_thumbnail(url="https://images.habbo.com/c_images/album1584/" + f"{codigo5}.png")
    await ctx.channel.send(embed=embed)
   
 
 
 
@bot.event
async def on_ready():
    print("BOT listo!")
    
 
    
bot.run('') 
