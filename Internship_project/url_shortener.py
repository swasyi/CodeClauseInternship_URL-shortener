from tkinter import*
import pyshorteners
win=Tk()
win.title("URL Shortener")
win.geometry("900x500")

def myUrl():
    url_entry=url.get()
    result=pyshorteners.Shortener().tinyurl.short(url_entry)
    urlEntry.insert(END,result)



Label(win,text="Url Shortener",font=("Georgia 20 bold"),fg="white",bg="black").pack(pady=10)
frame=Frame(win)
Label(frame,text="Enter Your URL Here",font=("Georgia 20 bold"),fg="white",bg="black").pack(side=LEFT)
url=Entry(frame,width=40,font=("Georgia 20"))
url.pack()
frame.pack(pady=10)

Button(win,text="Generate Link",font=("Georgia 20 bold"),command=myUrl).pack(pady=10)

frame2=Frame(win)
Label(frame2,text="Copy Your URL",font=("Georgia 15 bold"),fg="white",bg="black").pack(side=LEFT)
urlEntry=Entry(frame2,width="25",fg="blue",font="Georgia 15 bold")
urlEntry.pack()
frame2.pack(pady=10)

win.mainloop()