import discord
import random
#TOKEN
#LINK DO BICHO = https://discord.com/oauth2/authorize?client_id=1428832511785570364&permissions=8&integration_type=0&scope=bot

# A variável intents armazena as permissões do bot
intents = discord.Intents.default()
# Ativar a permissão para ler o conteúdo das mensagens
intents.message_content = True
# Criar um bot e passar as permissões
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Fizemos login como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hello!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith('gira'):
        a = random.choice(['cara', 'coroa'])
        await message.channel.send(a)

    elif message.content.startswith('se apresente'):
        await message.channel.send("Meu nome é *Yoshikage Kira.* Tenho 33 anos. Minha casa fica na parte nordeste de Morioh, onde todas as moradias são, e eu não sou casado. Eu trabalho como funcionário das lojas de departamento Kame Yu, e chego em casa todos os dias às oito da noite, no máximo. Eu não fumo, mas ocasionalmente bebo. Estou na cama às 23h e me certifico de ter oito horas de sono, não importa o que aconteça. Depois de tomar um copo de leite morno e fazer cerca de vinte minutos de alongamentos antes de ir para a cama, geralmente não tenho problemas para dormir até de manhã. Assim como um bebê, eu acordo sem qualquer fadiga ou estresse pela manhã. Foi-me dito que não houve problemas no meu último check-up. Estou tentando explicar que sou uma pessoa que deseja viver uma vida muito tranquila. Eu cuido para não me incomodar com quaisquer inimigos, como ganhar e perder, que me faria perder o sono à noite. É assim que eu lido com a sociedade e sei que é isso que me traz felicidade. Embora, se eu fosse lutar, não perderia para ninguém.")
    else:
        await message.channel.send(message.content)
    
client.run("seu tolken")
        break
    else:
        print('não tem essa palavra no dicionário :(')
