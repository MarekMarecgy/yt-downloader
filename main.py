from art import asciiart
from multiple import multidownloader
from pytube import YouTube
from pydub import AudioSegment
import os
import glob

print(asciiart)

if os.path.isdir('./Downloaded') == False:
    os.mkdir('./Downloaded')
if os.path.isdir('./Processing') == False:
    os.mkdir('./Processing')

def downloader():
    adr = input(str("wklej adres url filmiku który Cię interesuje -> "))
    yt = YouTube(adr)

    print(f"Zostanie pobrany następujący tytuł : {yt.title}")
    title = str(yt.title)
    whattype = (yt.streams.filter(only_audio=True))

    # for x in whattype:
    #     print(x)

    stream = whattype.last()

    x = stream.download('./Processing')

    AudioSegment.from_file(x).export(f"./Downloaded/{title}.mp3", format="mp3")

    files = glob.glob('./Processing/*')
    for f in files:
        os.remove(f)

    print("\n\n Pobieranie Ukończone ||| Pliki mp3 znajdziesz w folderze Downloaded")


print("Chcesz pobrać jeden(1) czy więcej utworów(2) ? ")
answ1 = input("Wybierz 1 lub 2 ---->>>: ")

if answ1 == "1":
    downloader()
elif answ1 == "2":
    multidownloader()