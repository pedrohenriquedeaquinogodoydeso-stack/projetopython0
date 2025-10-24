import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Estamos logados como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Olá! eu sou um bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def gira(ctx):
    a = random.choice(['cara', 'coroa'])
    await ctx.send(a)

        
@bot.command()
async def apresente(ctx):
    await ctx.send("Meu nome é *Yoshikage Kira.* Tenho 33 anos. Minha casa fica na parte nordeste de Morioh, onde todas as moradias são, e eu não sou casado. Eu trabalho como funcionário das lojas de departamento Kame Yu, e chego em casa todos os dias às oito da noite, no máximo. Eu não fumo, mas ocasionalmente bebo. Estou na cama às 23h e me certifico de ter oito horas de sono, não importa o que aconteça. Depois de tomar um copo de leite morno e fazer cerca de vinte minutos de alongamentos antes de ir para a cama, geralmente não tenho problemas para dormir até de manhã. Assim como um bebê, eu acordo sem qualquer fadiga ou estresse pela manhã. Foi-me dito que não houve problemas no meu último check-up. Estou tentando explicar que sou uma pessoa que deseja viver uma vida muito tranquila. Eu cuido para não me incomodar com quaisquer inimigos, como ganhar e perder, que me faria perder o sono à noite. É assim que eu lido com a sociedade e sei que é isso que me traz felicidade. Embora, se eu fosse lutar, não perderia para ninguém.")
#Meu nome é *Yoshikage Kira.* Tenho 33 anos. Minha casa fica na parte nordeste de Morioh, onde todas as moradias são, e eu não sou casado. Eu trabalho como funcionário das lojas de departamento Kame Yu, e chego em casa todos os dias às oito da noite, no máximo. Eu não fumo, mas ocasionalmente bebo. Estou na cama às 23h e me certifico de ter oito horas de sono, não importa o que aconteça. Depois de tomar um copo de leite morno e fazer cerca de vinte minutos de alongamentos antes de ir para a cama, geralmente não tenho problemas para dormir até de manhã. Assim como um bebê, eu acordo sem qualquer fadiga ou estresse pela manhã. Foi-me dito que não houve problemas no meu último check-up. Estou tentando explicar que sou uma pessoa que deseja viver uma vida muito tranquila. Eu cuido para não me incomodar com quaisquer inimigos, como ganhar e perder, que me faria perder o sono à noite. É assim que eu lido com a sociedade e sei que é isso que me traz felicidade. Embora, se eu fosse lutar, não perderia para ninguém.


@bot.command()
async def rap(ctx):
    await ctx.send('vou recomendar um rap muito bom:')
    await ctx.send('https://www.youtube.com/watch?v=nPotQAV0mMU')
    
@bot.command()
async def quiz(ctx):
    async def resposta_botao(interact:discord.Interaction):
        await interact.response.send_message('Bom gosto')
    async def resposta_botao2(interact:discord.Interaction):
        await interact.response.send_message('Bom gosto, mas não é melhor que o Josuke.')

    await ctx.send('Escolha um jojo:')
    view = discord.ui.View()
    botao = discord.ui.Button(label='Josuke', style=discord.ButtonStyle.green)
    botao.callback = resposta_botao
    botao2 = discord.ui.Button(label='Joseph', style=discord.ButtonStyle.green)
    botao2.callback = resposta_botao2

    view.add_item(botao2)
    view.add_item(botao)
    await ctx.reply(view=view)



bot.run("seu tolken")
