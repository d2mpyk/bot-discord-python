import requests, json, os, discord
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")

url = requests.get("https://nfs.faireconomy.media/ff_calendar_thisweek.json")
data = json.loads(url.text)

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'El Bot se ha logeado como: {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    mensaje = ""
    for noticia in data:
        fecha = noticia["date"].split('T')[0]
        hora = noticia["date"].split('T')[1].split('-')[0]
        manana = datetime.strftime(datetime.now() + timedelta(1), "%Y-%m-%d")
        impacto = "\N{fire}"
        if noticia["impact"] == "Medium":
            impacto *= 2
        else: 
            if noticia["impact"] == "High":
                impacto *= 3
        if fecha == manana :
            mensaje += "***"+noticia["country"]+"***, _"+noticia["title"]+"_, **Impacto**: "+impacto+" "+noticia["impact"]+", **fecha**: "+manana+", **hora**: "+hora+"\n"

    if message.content.startswith('/noticias'):
        try:
            await message.channel.send(mensaje)
        except:
            await message.channel.send("No hay noticias que mostrar")

        await message.channel.send('https://www.forexfactory.com/calendar')
        

client.run(os.getenv('TOKEN'))
