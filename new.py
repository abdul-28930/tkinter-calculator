import tkinter as tk
#from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    m_input = entry_int.get()
    km_output = m_input/1000
    output_string.set(km_output)

#main window
window = ttk.Window(themename= 'darkly')
window.title('m to km Calculator')
window.geometry('300x150')

#title
title_label = ttk.Label(master = window, 
                        text = 'Metre to kilometre', 
                        font='Calibri 24 bold')
title_label.pack()

#input field
input_frame = ttk.Frame(master = window)
entry_int = tk.IntVar()
entry = ttk.Entry(master = input_frame, 
                  textvariable= entry_int)
button = ttk.Button(master= input_frame, 
                    text= 'Convert', 
                    command= convert)
entry.pack(side="left", padx= 10)
button.pack(side="left")
input_frame.pack(pady= 10)

#output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, 
                         text="Output", 
                         font='Calibri 24', 
                         textvariable= output_string)
output_label.pack(pady= 5)



#run
window.mainloop()