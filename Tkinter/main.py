import tkinter

window = tkinter.Tk()
window.title("My first GUI")
window.minsize(width=500, height=300)


#label
label1=tkinter.Label(text="iLabel",font=("Arial", 24, "bold"))
label1.pack(side="left")




window.mainloop()