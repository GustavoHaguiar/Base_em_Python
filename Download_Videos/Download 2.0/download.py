from pytube import YouTube
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import tkinter

root = tkinter.Tk()
root.title('Download videos')
root.geometry("700x400")


def Download(directory):
    new_link = link.get()
    yt = YouTube(new_link)
    messagebox.showinfo("message","wait a moment...")
    yt.streams.filter(file_extension='mp4')
    print(yt.streams)
    stream = yt.streams.get_by_itag(18)
    print(stream)
    stream.download(output_path=directory)


def settings():
    directory = filedialog.askdirectory(master=root, title="Directory download")
    Download(directory)
    messagebox.showinfo("message","download complete")


label_download = ttk.Label(root, text="Download videos", font=30)
label_download.place(anchor="center", relx=0.5, rely=0.3)

label_link = ttk.Label(root, text="Link:", font=16)
label_link.place(anchor='center', relx=0.3, rely=0.5)

link = ttk.Entry(root)
link.place(anchor="center", relx=0.58, rely=0.5, relheight=0.07, relwidth=0.5)

button = ttk.Button(root, text="Download", command=settings)
button.place(anchor='center', relx=0.5, rely=0.7, relwidth=0.71, relheight=0.13)





root.mainloop()
