from tkinter import  *
from pytube import YouTube


window=Tk()
window.geometry("600x700")
window.config(bg='green')
window.title("Yotube-video-downloader")

window_logo=PhotoImage(file="logo.png")
window.iconphoto(False,window_logo)
Label(window, text="Video Downloader", font=(" Arial 30 bold"),bg="red").pack(padx=5,pady=100)
video_link=StringVar()
Label(window,text="Enter the link",font=("Arial",25,"bold")).place(x=170,y=161)
Entry_link=Entry(window,width=50,font=35,textvariable=video_link,bd=4).place(x=35,y=250)



def video_download():
    from pytube import YouTube

    video_url=YouTube(str(video_link.get()))

    my_video=video_url.streams.first()
    my_video.download()
    Label(window,text="Download has been completed !",font=("Arial",45,"bold"),bg="Lightpink",fg="Black").place(x=120,y=350)
    Label(window,text="Video has been downloaded in the app folder!",font=("Arial",45,"bold"),bg="Lightpink",fg="Black").place(x=20,y=400)


Button(window,text="DOWNLOAD",font=("Arial",25,"bold"),bg="Lightblue",command=video_download).place(x=180,y=300)

window.mainloop()

