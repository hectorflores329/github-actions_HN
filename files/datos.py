import pandas as pd
import datetime

def update():
    descargarDatos()

    return

def descargarDatos():
    # Filename: Covid HN
    covid = "https://onedrive.live.com/download.aspx?cid=9f999e057ad8c646&page=view&resid=9F999E057AD8C646!92347&parId=9F999E057AD8C646!62371&authkey=!AkePW7UW1KXQkMM&app=Excel"
    
    # Filename: LOCALIZA HN
    localiza = "https://onedrive.live.com/download?cid=9f999e057ad8c646&page=view&resid=9F999E057AD8C646!62378&parId=9F999E057AD8C646!62371&authkey=!AkePW7UW1KXQkMM&app=Excel"

    df = pd.read_excel(covid)
    df.to_excel("Covid HN.xlsx")

    df = pd.read_excel(localiza)
    df.to_excel("LOCALIZA HN.xlsx")

    return


if __name__ == '__main__':
    print('Empezando proceso de descarga.')
    update()
    print('El roceso de descarga ha finalizado.')
    