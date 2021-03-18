import pandas as pd
import datetime
import urllib.request

def update():
    descargarDatos()
    getKeys()
    
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
    f = open('C://key.json','r')
    keys = f.read()
    jkeys = json.loads(keys)
    return jkeys

if __name__ == '__main__':
    print('Empezando proceso de descarga.')
    update()
    print('El roceso de descarga ha finalizado.')
    