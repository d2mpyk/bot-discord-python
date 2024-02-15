import requests, json, emoji, os, discord
from datetime import datetime, timedelta
from dotenv import load_dotenv


url = requests.get("https://nfs.faireconomy.media/ff_calendar_thisweek.json")
text = url.text
# print(type(text))
data = json.loads(text)
# print(type(data))

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
        print(noticia["country"]+", "+noticia["title"]+", Impacto: "+impacto+" "+noticia["impact"]+", fecha: "+manana+", hora: "+hora)

