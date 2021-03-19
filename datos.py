import pandas as pd
import datetime
import urllib.request
import json
import tweepy

def update():
    descargarDatos()

    return

def descargarDatos():
    # Filename: Covid HN
    covid = "https://onedrive.live.com/download.aspx?cid=9f999e057ad8c646&page=view&resid=9F999E057AD8C646!92347&parId=9F999E057AD8C646!62371&authkey=!AkePW7UW1KXQkMM&app=Excel"
    
    # Filename: LOCALIZA HN
    localiza = "https://onedrive.live.com/download?cid=9f999e057ad8c646&page=view&resid=9F999E057AD8C646!62378&parId=9F999E057AD8C646!62371&authkey=!AkePW7UW1KXQkMM&app=Excel"

    # Filename: SALUD_HN.xlsx
    salud = "https://onedrive.live.com/download?cid=9f999e057ad8c646&page=view&resid=9F999E057AD8C646!62384&parId=9F999E057AD8C646!62371&authkey=!AkePW7UW1KXQkMM&app=Excel"

    # Filename: FARMACIAS_HN.xlsx
    farmacias = "https://onedrive.live.com/download?cid=9f999e057ad8c646&page=view&resid=9F999E057AD8C646!62386&parId=9F999E057AD8C646!62371&authkey=!AkePW7UW1KXQkMM&app=Excel"

    # Filename: DATOS RRSS HN.xlsx
    datos_rrss = "https://onedrive.live.com/download?cid=9f999e057ad8c646&page=view&resid=9F999E057AD8C646!62469&parId=9F999E057AD8C646!62371&authkey=!AkePW7UW1KXQkMM&app=Excel"

    # Filename: Condición_Pacientes_HN.xlsx
    pacientes = "https://onedrive.live.com/download?cid=9f999e057ad8c646&page=view&resid=9F999E057AD8C646!62448&parId=9F999E057AD8C646!62371&authkey=!AkePW7UW1KXQkMM&app=Excel"

    # Filename: ALIMENTACION_HN.xlsx
    alimentacion = "https://onedrive.live.com/download?cid=9f999e057ad8c646&page=view&resid=9F999E057AD8C646!62388&parId=9F999E057AD8C646!62371&authkey=!AkePW7UW1KXQkMM&app=Excel"

    # Filename: 00 DATACOVID_HN_CUARENTENA.xlsx
    cuarentena = "https://onedrive.live.com/download?cid=9f999e057ad8c646&page=view&resid=9F999E057AD8C646!62380&parId=9F999E057AD8C646!62371&authkey=!AkePW7UW1KXQkMM&app=Excel"

    # Filename: 00 DATACOVID Trabajo_HN.xlsx
    trabajo = "https://onedrive.live.com/download?cid=9f999e057ad8c646&page=view&resid=9F999E057AD8C646!62377&parId=9F999E057AD8C646!62371&authkey=!AkePW7UW1KXQkMM&app=Excel"

    # Filename: Indicadores_Economicos.xlsx
    economicos = "https://onedrive.live.com/download?cid=9f999e057ad8c646&page=view&resid=9F999E057AD8C646!62658&parId=9F999E057AD8C646!62371&authkey=!AkePW7UW1KXQkMM&app=Excel"

    # Downloading files
    urllib.request.urlretrieve(covid, "Covid HN.xlsx")
    urllib.request.urlretrieve(localiza, "LOCALIZA HN.xlsx")
    urllib.request.urlretrieve(salud, "SALUD_HN.xlsx")
    urllib.request.urlretrieve(farmacias, "FARMACIAS_HN.xlsx")
    urllib.request.urlretrieve(datos_rrss, "DATOS RRSS HN.xlsx")
    urllib.request.urlretrieve(pacientes, "Condición_Pacientes_HN.xlsx")
    urllib.request.urlretrieve(alimentacion, "ALIMENTACION_HN.xlsx")
    urllib.request.urlretrieve(cuarentena, "00 DATACOVID_HN_CUARENTENA.xlsx")
    urllib.request.urlretrieve(trabajo, "00 DATACOVID Trabajo_HN.xlsx")
    urllib.request.urlretrieve(economicos, "Indicadores_Economicos.xlsx")

    return

def getKeys():
    f = open('keys.json','r')
    keys = f.read()
    jkeys = json.loads(keys)
    return jkeys

def FechaTweeter(palabra):
    anio = int(palabra[-4:])
    meses = {
        "Jan":1,
        "Feb":2,
        "Mar":3,
        "Apr":4,
        "May":5,
        "Jun":6,
        "Jul":7,
        "Aug":8,
        "Sep":9,
        "Oct":10,
        "Nov":11,
        "Dec":12
    }

    mes = meses[palabra[4:7]]
    dia = int(palabra[8:10])
    hora = int(palabra[11:13]) 
    minuto = int(palabra[14:16])
    segundo = int(palabra[17:19])
    return datetime.datetime(anio,mes,dia,hora,minuto,segundo) - datetime.timedelta(hours = 6)

def depurarFuenteTweet(palabra):
    salida = palabra.replace('<a href="https://about.twitter.com/products/tweetdeck" rel="nofollow">','').replace("</a>","")
    salida = salida.replace('<a href="http://twitter.com/download/iphone" rel="nofollow">',"")
    salida = salida.replace('<a href="https://studio.twitter.com" rel="nofollow">',"")
    salida = salida.replace('<a href="https://mobile.twitter.com" rel="nofollow">',"")
    salida = salida.replace('<a href="http://twitter.com" rel="nofollow">',"")
    salida = salida.replace('<a href="http://twitter.com/download/android" rel="nofollow">',"")
    salida = salida.replace('<a href="https://www.hootsuite.com" rel="nofollow">',"")
    #salida = salida.replace('<a href=""http://twitter.com/download/android"" rel=""nofollow"">',"")
    return salida

def APITWEET():
    # Declaramos nuestras Twitter API Keys:
    keys = getKeys()
    #ACCESS_TOKEN = '1230251564616515586-2KqPsCG2mIJp3irRjENgHpCfQUxTUg'
    #ACCESS_TOKEN_SECRET = '6PJfMtYGY7w6csiIX9m1S5jFEKNZ3hE9PVkHKeN1S14iM'
    #CONSUMER_KEY = 'koO4XqTuWFr5ADGcE8kjIkVoU'
    #CONSUMER_SECRET = '3F4sk9qU8zbKBROuLPUUj1uvE2YuhseXPe0ahMQoivg4icN5bL'  
    ACCESS_TOKEN = keys['twitter']['token_acceso']
    ACCESS_TOKEN_SECRET = keys['twitter']['secreto_token_acceso']
    CONSUMER_KEY = keys['twitter']['clave_api']
    CONSUMER_SECRET = keys['twitter']['clave_secreta_api']
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    return api

def get_tweetConFecha(user, api = APITWEET()):
    return list(api.user_timeline(screen_name = user, count= 10))


if __name__ == '__main__':
    print('Empezando proceso de descarga.')
    update()
    print('El roceso de descarga ha finalizado.')

    lista = get_tweetConFecha("cristiano")
    salida = []
    for i in lista:  
        jsonObject = i._json.copy()
        datos = {
                    "Contenido" : jsonObject["text"], 
                    "IR" : "https://twitter.com/i/web/status/" + jsonObject["id_str"], 
                    "Fecha" : FechaTweeter(jsonObject["created_at"]).strftime("%d/%m/%Y %H:%M:%S"),
                    "Dispositivo" : depurarFuenteTweet(jsonObject["source"]),
                    "Likes" : jsonObject["favorite_count"],
                    "Retweets" : jsonObject["retweet_count"],
                    "Entidad" : jsonObject["user"]["name"],
                    "Hora" : FechaTweeter(jsonObject["created_at"]).strftime("%H:%M:%S"),
                    "Foto": jsonObject["user"]["profile_image_url"].replace("_normal.","."),
                    "FechaAux": FechaTweeter(jsonObject["created_at"])
                }
        salida.append(datos.copy())

    data = pd.DataFrame(salida)
    data.to_excel("final.xlsx", index=False)        