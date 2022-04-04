from prettytable import PrettyTable
from pytube import YouTube
from pydub import AudioSegment
import os
import glob


def multidownloader():
    tabela = PrettyTable()
    tabela.field_names = ["Songs Name's"]
    ytlist = []
    przelacznik = True

    adr = input(str("wklej adres url filmiku który Cię interesuje -> "))
    yt = YouTube(adr)
    ytlist.append(yt)

    while przelacznik:
        adr = input(str("wklej kolejny adres lub zakończ wpisujac END -> :"))
        if adr != "END":
            yt = YouTube(adr)
            ytlist.append(yt)
        else:
            przelacznik = False
            print("ROZPOCZYNAM POBIERANIE")

    for adress in ytlist:
        tabela.add_row([str(adress.title)])
        # print(adress.title)
        title = str(adress.title)
        whattype = (adress.streams.filter(only_audio=True))
        stream = whattype.last()
        x = stream.download('./Processing')
        AudioSegment.from_file(x).export(f"./Downloaded/{title}.mp3", format="mp3")

        files = glob.glob('./Processing/*')
        for f in files:
            os.remove(f)
    print(tabela)
    print("Pobieranie Ukończone ||| Pliki mp3 znajdziesz w folderze Downloaded")