from tkinter import Image, Tk, Button
from tkinter import *
import moviepy.editor as mp
import os
import re
from tkinter.filedialog import askdirectory
from tkinter import messagebox
from tkinter import PhotoImage
from PIL import Image,ImageTk

root = Tk()
#p1=PhotoImage("C:\\Users\\Vijay Gupta\\Pictures\\Camera Roll\\favpng_movie-logo.png")
#root.iconphoto(False,p1)
root.title('Video Mp4 to Mp3 Audio converter')
image1=Image.open("C:\\Users\\Vijay Gupta\\Pictures\\Camera Roll\\wp4676621-4k-pc-wallpapers.jpg")
filename=ImageTk.PhotoImage(image1)
background_label = Label(root, image=filename)
background_label.image=filename
background_label.place(x=0, y=0)

root.minsize(width=500,height=200)
root.resizable(width=False,height=False)

def open_mp4_folder():
    global mp4_directory
    mp4_directory=askdirectory()
    print(mp4_directory)

def open_mp3_folder():
    global mp3_directory
    mp3_directory=askdirectory()
    print(mp3_directory)


def convert():
    for file in [n for n in os.listdir(mp4_directory) if re.search('.mp4',n)]:
        full_path = os.path.join(mp4_directory,file)
        output_path = os.path.join(mp3_directory, os.path.splitext(file)[0]+ '.mp3' )
        audioclip = mp.AudioFileClip(full_path)
        audioclip.write_audiofile(output_path)
        messagebox.showinfo("Complete", "Mp4 file converted to Mp3 Successfully")


mp4_btn = Button(root,text="Choose Mp4 Folder",width=25, command=open_mp4_folder,bg="blue",fg="white")
mp4_btn.grid(row=1,column=0,padx = 50, pady =50)

mp3_btn = Button(root,text="Choose Mp3 Folder",width=25, command=open_mp3_folder,bg="brown",fg="white")
mp3_btn.grid(row=1,column=1)

convert_btn = Button(root,text="Convert Mp4 to Mp3",width=25, command=convert,bg="yellow",fg="black")
convert_btn.grid(row=2,column=0)

exit_btn = Button(root,text="Exit Application",width=25, command=root.destroy,bg="purple",fg="white")
exit_btn.grid(row=2,column=1)




root.mainloop()
