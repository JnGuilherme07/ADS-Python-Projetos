from yt_dlp import YoutubeDL

url = input('URL do video: ')

salvar = {        #Coloque o caminho do seu diretorio
    'outtmpl' : r'C:\Users\jonegui\Downloads\%(title)s.%(ext)s'
}

with YoutubeDL(salvar) as ydl:
    ydl.download([url])