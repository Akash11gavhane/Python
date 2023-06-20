from tkinter import *
from PIL import ImageTk , Image

import os


def rotate_image():

    global counter
    img_label.config(image=img_array[counter % len(img_array)])
    counter = counter + 1

def previous_Image():
    global counter
    counter = counter - 1
    img_label.config(image = img_array[counter])


counter = 1
root = Tk()

root.title("Wallpaper Viewer")

root.geometry('800x700')
root.configure(background='black')


files = os.listdir('wallpaper')


img_array = []
for file in files :
    img = Image.open(os.path.join('wallpaper' , file))
    resized_img = img.resize((500 , 500))
    img_array.append(ImageTk.PhotoImage(resized_img))



img_label = Label(root , image = img_array[0])
img_label.pack(pady = (15 , 10))
next_btn = Button(root , text = "Next" , bg = 'white' , fg = 'black' , width = 28 , height = 2 , command = rotate_image)
next_btn.pack()

previous_btn = Button(root , text = "Previous" , bg = 'white' , fg = 'black' , width = 28 , height = 2 , command = previous_Image)
previous_btn.pack(pady = (15 , 10))

root.mainloop()