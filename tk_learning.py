import tkinter as tk
import ttkbootstrap as ttk
import math
def farenheit_convert():
    farenheit_input = entry_int.get()
    celsius_output = (farenheit_input - 32) * 5/9
    output_string.set(f"{celsius_output}°C ")
def celsius_convert():
    celsius_input = entry_int.get()
    farenheit_output = (celsius_input * 9/5) + 32
    output_string.set(f"{farenheit_output}°F")
def user_input():
    select_unit = input().lower()
    if select_unit == "f":
        farenheit_convert()
        return "f"
    elif select_unit == "c":
        celsius_convert()
        return "c"

    
#window
window = ttk.Window(themename = "darkly")
window.title(" Celsius to Farenheit converter")
window.geometry("600x200")
#title
title_label = ttk.Label(master = window, text = " Celsisus to Farenheit", font = "Calibri 18 bold" )
title_label.pack(side = "top")

input_frame = ttk.Frame(master = window)
entry_int = tk.IntVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)
button = ttk.Button(master = input_frame, text = "Convert",  command = celsius_convert)
entry.pack(side = "left", padx = 10)
button.pack(side = "right")
input_frame.pack(pady = 10)
#Input field decision

#output
output_string = tk.StringVar()
output_label  = ttk.Label(master = window,text = "Output", font = "Calibri 16", textvariable = output_string)
output_label.pack(pady = 5)

#run
window.mainloop()
