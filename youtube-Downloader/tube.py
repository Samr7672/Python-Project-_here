import tkinter as tk
from tkinter import StringVar
# If this import fails, run: pip install pytubefix
#from pytube import YouTube
from pytubefix import YouTube 

root = tk.Tk()
root.geometry("500x300")
root.resizable(False, False)
root.title("Youtube-video-downloader")

link = StringVar()

tk.Label(root, text="Paste Link Here:", font='arial 12 bold').place(x=160, y=60)

link_enter = tk.Entry(root, width=50, textvariable=link)
link_enter.place(x=90, y=100)

def downloader():
    try:
        url_text = link.get()
        yt = YouTube(url_text)
        video = yt.streams.get_highest_resolution()
        video.download()
        tk.Label(root, text="DOWNLOADED! ✅", font='arial 15', fg="green").place(x=160, y=210)
    except Exception as e:
        tk.Label(root, text="ERROR!", font='arial 15', fg="red").place(x=200, y=210)
        print(e)

tk.Button(root, text="DOWNLOAD", font='arial 15 bold', bg='pale violet red', padx=2, command=downloader).place(x=180, y=150)

root.mainloop()