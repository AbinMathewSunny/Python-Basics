from tkinter import *

def milestokm():
    miles = float(miles_input.get())
    km=miles*1.609
    kilo_label.config(text=f"{km:.2f}")


window = Tk()
window.title("converter")
window.config(padx=20,pady=20)
miles_input=Entry(width=7)
miles_input.grid(column=1, row=0)

label1=Label(text="Miles")
label1.grid(column=2, row=0)


equal=Label(text="Is equal to")
equal.grid(column=0, row=1)


result_label=Label(text="0")
result_label.grid(column=1, row=1)


kilo_label = Label(text="km")
kilo_label.grid(column=2, row=1)


calculate_butt=Button(text="calculate",width="20",command=milestokm)
calculate_butt.grid(column=1, row=2)







window.mainloop()
