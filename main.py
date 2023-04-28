from tkinter import *
import pyshorteners

root = Tk()
root.title('URL Shortener')
root.geometry('600x350')

def shorten():
    if e2.get():
        e2.delete(0,END)

    if e1.get():
        #Convert to tinyurl
        url= pyshorteners.Shortener().tinyurl.short(e1.get()) 
        e2.insert(END, url)

label1 = Label(root, text="Enter Link to Shorten:", font=("Courier",20), fg="Blue")
label1.pack(pady= 10)

e1 = Entry(root, font=("Courier",20), justify= CENTER, width= 30, fg= "blue")
e1.pack(pady= 10)

e1.focus_set()

btn1 = Button(root, text="Shorten Link", fg= "blue", font= "Courier", command= shorten)
btn1.pack(pady= 20)

label2 = Label(root, text= "Shortened Link", font= ("Courier", 20))
label2.pack()

e2 = Entry(root, font=("Courier", 20), justify = CENTER, width= 30, bd=1)
e2.pack()



root.mainloop()