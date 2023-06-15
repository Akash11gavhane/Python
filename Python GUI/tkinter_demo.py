
from tkinter import *
from PIL import Image
from PIL import ImageTk

# here tkinter is pre downloaded library and '*' means import all the libraries

#----------------------------------

# 1st create a variable for the Tk() class

root = Tk()

# root is for accessing all the methods from the tkinter class

# .titel() function is used to change the title on the window
# before using that tk was there after
# ---> Login form will be there
root.title("Login Form")


# how to change the fevicon ?
# .iconbitmap function is used to change the fevicon image or image icon that diplay on the left corner of the window


# root.iconbitmap(add the path of the fevicon file )


# minsize() function helps us to change the default size of the window
# using minsize we can set the minimum size for the window
# we cant make it more smaller than the given size to the window
root.minsize(300 , 300)

# maxsize is same like the minsize using maxsize we can give the default maxiuma size of the window
# we cant make more big window than the given size
root.maxsize(1000 , 1000)


# what if we want there will be a perticular size window
# then there is geometry() function is there

root.geometry("500x600")

# background color for the window
root.configure(
    background='blue'
)

# how to add image

img = ImageTk.PhotoImage(Image.open('image1.jpeg'))

img_lable = Label(root , image=img)

# root.mainloop() what mainloop does
# it consistently keep our gui on the screen

root.mainloop()


