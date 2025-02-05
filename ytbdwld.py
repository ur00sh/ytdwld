import tkinter as tk
from tkinter import *
from pytube import YouTube
from tkinter import messagebox, filedialog

#funkcija za kreiranje vidzeta
def Widgets():
    
    headLabel = Label(root, text="YouTube Video Downloader",
                       padx = 15,
                       pady = 15,
                       font="SegoeUI, 14",
                       bg = "palegreen1",
                       fg = "red")
    headLabel.grid(row = 1,
                    column = 1,
                    pady = 10,
                    padx = 5,
                    columnspan = 3)
    linkLabel = Label(root,
                       text = "YouTube link: ",
                       bg = "salmon",
                       padx = 5,
                       pady = 5)
    linkLabel.grid(row = 2,
                    column = 0,
                    padx = 5,
                    pady = 5)
    root.linkText = Entry(root,
                          width = 35,
                          textvariable = video_Link,
                          font = "Arial 14")
    root.linkText.grid(row = 2,
                       column = 1,
                       padx = 5,
                       pady = 5,
                       columnspan = 2)
    destinationLabel = Label(root,
                              text = "Destination: ",
                              bg = "Salmon",
                              padx = 5,
                              pady = 9)
    destinationLabel.grid(row = 3,
                           column = 0,
                           padx = 5,
                           pady = 5)
    root.destinationText = Entry (root,
                                 width = 27,
                                 textvariable = downloadPath,
                                 font = "Arial 14")
    root.destinationText.grid(row = 3,
                              column = 1,
                              padx = 5,
                              pady = 5)
    browseButton = Button (root,
                       text = "Browse",
                       command = Browse,
                       width = 10,
                       bg = "bisque",
                       relief =  GROOVE)
    browseButton.grid(row = 3,
                  column = 2,
                  padx = 1,
                  pady = 1)
    downloadButton = Button (root,
                             text = "Download Video",
                             command = Download,
                             width = 20,
                             bg = "thistle1",
                             padx = 15,
                             pady = 10,
                             relief = GROOVE,
                             font = "Georgia 13")
    downloadButton.grid(row = 4,
                        column = 1,
                        padx = 20,
                        pady = 20)
    
#definisanje pretrazivacke funkcije
def Browse():
    #pop-up prozorce
    downloadDirectory = filedialog.askdirectory (initialdir = "Your directory path", title = "Save Video")
    #prikaz adrese foldera
    downloadPath.set(downloadDirectory)
    
#defnisanje funcije skidanja videa
def Download():
    YouTube_link = video_Link.get()
    downloadFolder = downloadPath.get()
    getVideo = YouTube(YouTube_link)
    videoStream = getVideo.streams.first()
    videoStream.download(downloadFolder)
    messagebox.showinfo("Success!!", "Downloaded and saved in\n" + downloadFolder)
    
#kreiranje objekta klase
root = tk.Tk()
root.geometry("520x280")
root.resizable(False, False)
root.title("YouTube Video Downloader")
root.config(background = "PaleGreen1")

video_Link = StringVar()
downloadPath = StringVar()

Widgets()

root.mainloop()