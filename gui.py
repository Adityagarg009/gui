import tkinter as tk
from tkinter import ttk

def on_radio_select():
    selected_value.set(f"Radio {radio_var.get()} is selected.")

def on_dropdown_select(event):
    selected_value.set(f"Selected item: {dropdown_var.get()}")

def on_button_click():
    selected_value.set("Button is clicked!")

root = tk.Tk()
root.title("Sample Windows 11-style UI")
root.geometry("400x300")

tab_control = ttk.Notebook(root)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Tab 1')
tab_control.add(tab2, text='Tab 2')
tab_control.pack(expand=1, fill='both')

radio_var = tk.StringVar()
radio_var.set("Off")
radio_frame = ttk.LabelFrame(tab1, text="Radio Buttons")
radio_frame.pack(padx=20, pady=20)

radio_off = ttk.Radiobutton(radio_frame, text="Off", variable=radio_var, value="Off", command=on_radio_select)
radio_off.pack(padx=5, pady=5, anchor="w")

radio_on = ttk.Radiobutton(radio_frame, text="On", variable=radio_var, value="On", command=on_radio_select)
radio_on.pack(padx=5, pady=5, anchor="w")

options = ["Vanguard", "hello", "you", "hi"]
dropdown_var = tk.StringVar()
dropdown_var.set(options[0])

dropdown_frame = ttk.LabelFrame(tab2, text="Drop-down Menu")
dropdown_frame.pack(padx=20, pady=20)

dropdown = ttk.Combobox(dropdown_frame, values=options, textvariable=dropdown_var)
dropdown.pack(padx=5, pady=5)
dropdown.bind("<<ComboboxSelected>>", on_dropdown_select)

button_frame = ttk.Frame(root)
button_frame.pack(pady=10)

action_button = ttk.Button(button_frame, text="Click Me for item to be seletected", command=on_button_click)
action_button.pack(padx=20, pady=10)

selected_value = tk.StringVar()
selected_label = ttk.Label(root, textvariable=selected_value, font=("Segoe UI", 12, "bold"))
selected_label.pack(pady=10)

root.mainloop()

