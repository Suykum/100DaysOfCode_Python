from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=10, pady=10)

entry = Entry(width=20)
entry.insert(END, string="0")
entry.grid(column=1, row=0)

mile_label = Label(text="Miles")
mile_label.grid(column=2, row=0)
is_equal_to_lable = Label(text="is equal to")
is_equal_to_lable.grid(column=0, row=1)
value_lable = Label(text="0")
value_lable.grid(column=1, row=1)
km_lable=Label(text="Km")
km_lable.grid(column=2, row=1)


def calculate():
    mile = float(entry.get())
    km = round(mile * 1.609344)
    value_lable.config(text=km)


calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(column=1, row=2)
window.mainloop()


