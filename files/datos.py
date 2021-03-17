import pandas as pd
import datetime

def update():
    descargarDatos()
    fechaActualizacion()

    return

def descargarDatos():
    df = pd.read_excel("https://onedrive.live.com/download.aspx?cid=9f999e057ad8c646&page=view&resid=9F999E057AD8C646!92347&parId=9F999E057AD8C646!62371&authkey=!AkePW7UW1KXQkMM&app=Excel")
    df.to_excel("file1.xlsx")

    return


if __name__ == '__main__':
    print('Empezando proceso de descarga.')
    update()
    print('El roceso de descarga ha finalizado.')
    