import pandas as pd
import datetime

def update():
    descargarDatos()
    fechaActualizacion()

    return

def descargarDatos():
    df = pd.read_csv("https://raw.githubusercontent.com/Sud-Austral/MPG/main/Prueba/Geo2_NI_provinces_.csv")
    df.to_excel("new_file.xlsx")

    return

def numerar():
    for i in range(10):
        print(i)

def fechaActualizacion():
    f = open ('holamundo.txt','wb')
    f.write(bytes(datetime.datetime.now().strftime("La fecha de actualización es: %m/%d/%Y, %H:%M:%S"), 'utf-8'))
    f.close()

if __name__ == '__main__':
    print('Empezando proceso de descarga.')
    