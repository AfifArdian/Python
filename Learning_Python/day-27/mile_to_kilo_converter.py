from tkinter import *

def miles_to_km():
    num_miles = float(miles_input.get())
    km = round(num_miles * 1.609)
    kilometer_result_label.config(text=f"{km}")

window = Tk()
window.title("Mile to KM Converter")
window.minsize(width=300, height=200)
window.config(padx=150, pady=20) # Optional

label = Label(text="is equal to")
label.grid(column=0, row=1)

miles_input = Entry(width=5)
print(miles_input.get())
miles_input.grid(column=1, row=0)

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row=1)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

kilometer_label = Label(text="Km")
kilometer_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)




window.mainloop()