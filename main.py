import requests, json, emoji, os, discord
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

url = requests.get("https://nfs.faireconomy.media/ff_calendar_thisweek.json")
text = url.text
# print(type(text))
data = json.loads(text)
# print(type(data))



@client.event
async def on_ready():
    print(f'Se ha logeado como: {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    mensaje = ""
    for noticia in data:
        fecha = noticia["date"].split('T')[0]
        hora = noticia["date"].split('T')[1].split('-')[0]
        manana = datetime.strftime(datetime.now() + timedelta(1), "%Y-%m-%d")
        #impacto = emoji.emojize(":fire:")
        impacto = "\N{fire}"
        if noticia["impact"] == "Medium":
            impacto *= 2
        else: 
            if noticia["impact"] == "High":
                impacto *= 3
        if fecha == manana :
            mensaje += noticia["country"]+", "+noticia["title"]+", Impacto: "+impacto+" "+noticia["impact"]+", fecha: "+manana+", hora: "+hora+"\n"

    if message.content.startswith('$noticias'):
        await message.channel.send(mensaje)  

client.run(TOKEN)
