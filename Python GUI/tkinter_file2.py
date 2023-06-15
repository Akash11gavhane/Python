
from tkinter import *
from PIL import Image
from PIL import ImageTk
from tkinter import messagebox

# here tkinter is pre downloaded library and '*' means import all the libraries

#----------------------------------

def handle_login():
    email = email_input.get()
    password = password_input.get()

    if email == "akash1106gavhane@gmail.com" and password == "1106":
        messagebox.showinfo("Login Successful...!!!")
    else :
        messagebox.showerror("Error, Login Failed..!!")
    print(email , password , sep = "\n")



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
    background='#0096DC'
)

# how to add image
img = Image.open('image1.jpeg')
resized_img = img.resize((70 , 70))
img = ImageTk.PhotoImage(resized_img)


img_label = Label(root , image=img)
img_label.pack(pady = (10 , 10))

text_label = Label(root , text = "Flipkart" , fg = 'white' , bg = '#0096DC')
text_label.pack()
text_label.config(font = ('verdana' , 16))

email_label = Label(root , text = 'Enter Email' , fg = 'white' , bg = '#0096DC')
email_label.pack(pady = (20 , 5))
email_label.config(font = ('verdana' , 12))

email_input = Entry(root , width = 50)
email_input.pack(ipady = 6 , pady = (1 , 15))

password_label = Label(root , text = 'Enter Password' , fg = 'white' , bg = '#0096DC')
password_label.pack(pady = (20 , 5))
password_label.config(font = ('verdana' , 12))

password_input = Entry(root , width = 50)
password_input.pack(ipady = 6 , pady = (1 , 15))


login_btn = Button(root , text = 'Login Here' , bg = 'white' , fg = 'black' , width = 20 , height = 2 , command = handle_login)
login_btn.pack(pady = (10 , 20))
login_btn.pack(pady = (10 , 20))
login_btn.config(font = ('verdana' , 10))



# root.mainloop() what mainloop does
# it consistently keep our gui on the screen

root.mainloop()


