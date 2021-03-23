import urllib.request
# import git
import pandas as pd
import datetime
import http.client, urllib.request, urllib.parse, urllib.error, base64
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import tweepy
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
import requests
import json  
import codecs
import numpy as np
import wget
import http.client, urllib.request, urllib.parse, urllib.error, base64

def update():
    print("Comenzó...")
    try:
        # datasetFinalTweet()
        # Comentarla para no cargar el API.
        print("Los tweet se cargaron correctamente...")
    except:
        print("Error al cargar los Tweet")
    try:
        bingNews()
        print("Las noticias se cargaron correctamente...")
    except:
        print("Error al cargar los Noticias")
    try:
        guardarDataCovid()
        print("Los datos de datacovid se cargaron correctamente...")
    except:
        print("Error al cargar los archivos del la organizacion")
    # guardarRepositorio()

    return

def guardarDataCovid():
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
    urllib.request.urlretrieve(covid, "datacovidhn/Covid HN.xlsx")
    urllib.request.urlretrieve(localiza, "datacovidhn/LOCALIZA HN.xlsx")
    urllib.request.urlretrieve(salud, "datacovidhn/SALUD_HN.xlsx")
    urllib.request.urlretrieve(farmacias, "datacovidhn/FARMACIAS_HN.xlsx")
    urllib.request.urlretrieve(datos_rrss, "datacovidhn/DATOS RRSS HN.xlsx")
    urllib.request.urlretrieve(pacientes, "datacovidhn/Condición_Pacientes_HN.xlsx")
    urllib.request.urlretrieve(alimentacion, "datacovidhn/ALIMENTACION_HN.xlsx")
    urllib.request.urlretrieve(cuarentena, "datacovidhn/00 DATACOVID_HN_CUARENTENA.xlsx")
    urllib.request.urlretrieve(trabajo, "datacovidhn/00 DATACOVID Trabajo_HN.xlsx")
    urllib.request.urlretrieve(economicos, "datacovidhn/Indicadores_Economicos.xlsx")

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


def definirDatasetPorCuenta(cuenta):

    lista = get_tweetConFecha(cuenta)
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
    # data.to_excel("final.xlsx", index=False)

    return data

def datasetFinalTweet():
    cuentas = [
                "saludhn",
                "opsoms"
                ]
    salida = []
    for i in cuentas:
        salida.append(definirDatasetPorCuenta(i))
    data = pd.concat(salida)
    data = data.sort_values(by=['FechaAux'])
    del data["FechaAux"]
    # data.to_csv("../Datos_Honduras/tweeter/tweeter.csv", index=False)
    data.to_csv("tweeter/tweeter.csv", index=False)
    return data

def fechaCorrecta(i):
    año = i[0:4]
    mes = i[5:7]
    dia = i[8:10]
    hora = i[11:13]
    minuto = i[14:16]
    return dia + "-" + mes + "-" + año + " " + hora + ":" + minuto

def reemplazarFinal(i):
    return i.replace("&pid=News","")

def bingNews(pais = "Honduras"):
    #pais = "Chile"
    headers = {
        # Request headers
        #'Ocp-Apim-Subscription-Key': 'b091fbaeb9f94255b542befc3ecff8b8',
        'Ocp-Apim-Subscription-Key': 'a9b5b1527a7b43929d7e15a383b1583a',
    }

    params = urllib.parse.urlencode({
        # Request parameters
        'q':  'covid-19 coronavirus ' + pais + ' loc:hn FORM=HDRSC4',
        'count': '40',
        'offset': '0',
        'mkt': 'es-US',
        'safeSearch': 'Moderate',
        "sortBy": "Date"
    })

    #conn = http.client.HTTPSConnection('api.cognitive.microsoft.com')
    conn = http.client.HTTPSConnection('dataintelligence.cognitiveservices.azure.com')
    conn.request("GET", "/bing/v7.0/news/search?%s" % params, "{body}", headers)
    response = conn.getresponse()
    #data = response.read()

    decoded_data=codecs.decode(response.read(), 'utf-8-sig')
    d = json.loads(decoded_data)
    conn.close()
    aux =  d['value']
    salida = []
    for i in aux:
        try:
            i["imagen"] = i["image"]["thumbnail"]["contentUrl"]
            i["pais"] = "Chile"
            try:
                i["Fuente"] = i['provider'][0]["name"]
            except:
                pass
            salida.append(i.copy())
        except:
            pass
    data = pd.DataFrame(salida)[["name","url","description","datePublished","imagen","pais","Fuente"]]
    data["datePublished"] = data["datePublished"].apply(fechaCorrecta)
    data["imagen"] = data["imagen"].apply(reemplazarFinal)
    data[::-1].to_csv("Bing/News/Honduras.csv",index=False)
    return


if __name__ == '__main__':
    print('Empezando proceso de descarga.')
    update()
    print('El roceso de descarga ha finalizado.')