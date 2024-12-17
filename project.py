from tkinter import *
from yt_dlp import YoutubeDL
from tkinter import messagebox


def high_quality():
    try:
        abdo = entry.get() 
        quality = {
            'format': 'best', 
            'outtmpl': 'downloads/%(title)s.%(ext)s'  
        }
        with YoutubeDL(quality) as ydl:
            ydl.download([abdo]) 
        messagebox.showinfo("success", "Downloaded in High Resolution")  
    except Exception as e:
        messagebox.showerror( f"Erorr: {str(e)}")  


def low_quality():
    try:
        abdo = entry.get()
        quality = {
            'format': 'worst',  
            'outtmpl': 'downloads/%(title)s.%(ext)s'
        }
        with YoutubeDL(quality) as ydl:
            ydl.download([abdo])  
        messagebox.showinfo("success", "The video was downloaded in low quality!") 
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while loading the video: {str(e)}")  


def audio_only():
    try:
        abdo = entry.get()  
        quality = {
            'format': 'bestaudio',  
            'outtmpl': 'downloads/%(title)s.%(ext)s' 
        }
        with YoutubeDL(quality) as ydl:
            ydl.download([abdo])
        messagebox.showinfo("success", "The audio has been downloaded successfully!") 
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while downloading audio: {str(e)}") 



window = Tk()
window.title("downloaded by youtube")
window.geometry("800x400")
window.configure(bg="#999999") 


Label(window, text="Enter your  link video", font="bold").place(x=320, y=30)

entry = Entry(window, width=50)
entry.place(x=255, y=80)

Button(window, text="high_quality", command=high_quality, font="bold").place(x=160, y=200)
Button(window, text="low_quality", command=low_quality, font="bold").place(x=340, y=200)
Button(window, text="audio_only", command=audio_only, font="bold").place(x=530, y=200)


window.mainloop()