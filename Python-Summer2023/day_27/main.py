import tkinter

def get_clicked():
    km_lab.config(text= round(int(ent_miles.get()) * 1.609,2))
window = tkinter.Tk()

km = 0
window.minsize(width= 300, height= 300)
window.title("Mile to km Converter")
window.config(padx= 50,pady= 20)

ent_miles = tkinter.Entry(width= 10)
ent_miles.grid(column= 1,row= 0)
label_miles = tkinter.Label(text= "Miles")
label_miles.config(padx= 10)
label_miles.grid(column= 2, row= 0)
equal_lab = tkinter.Label(text= "is equal to")
equal_lab.grid(column= 0,row= 1)
km_lab = tkinter.Label(text= km)
km_lab.grid(column= 1, row= 1)
km_text_lab = tkinter.Label(text= "Km")
km_text_lab.grid(column= 2, row= 1)
but = tkinter.Button(text= "Calculate",command=get_clicked)
but.grid(column= 1, row= 2)

















window.mainloop()

