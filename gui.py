import tkinter as tk

def convert_to_feet():
    try:
        value = float(centi_entry.get())
        result = value * 0.0328
        centi_result.set(f"{result:.2f} Feet")
    except ValueError:
        centi_result.set("Invalid input")

def convert_to_inches():
    try:
        value = float(feet_entry.get())
        result = value * 12
        feet_result.set(f"{result:.2f} Inches")
    except ValueError:
        feet_result.set("Invalid input")

def convert_to_sqmtrs():
    try:
        value = float(sqft_entry.get())
        result = value * 0.0929
        sqft_result.set(f"{result:.2f} Sqmtrs")
    except ValueError:
        sqft_result.set("Invalid input")

def convert_to_acres():
    try:
        value = float(sq_entry.get())
        result = value / 43560
        sq_result.set(f"{result:.6f} Acres")
    except ValueError:
        sq_result.set("Invalid input")

window = tk.Tk()
window.title("Unit Converter")
window.geometry("800x400")

window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=1)
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)

frame1 = tk.Frame(master=window, bg="black")
frame1.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

frame2 = tk.Frame(master=window, bg="black")
frame2.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

frame3 = tk.Frame(master=window, bg="black")
frame3.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

frame4 = tk.Frame(master=window, bg="black")
frame4.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

label_style = "Arial 12 bold"
entry_style = "Arial 12"

centi_label = tk.Label(frame1, text="Centimeter to Feet", font=label_style, fg="white", bg="black")
centi_entry = tk.Entry(frame1, width=20, font=entry_style, bg="white", fg="black")
centi_result = tk.StringVar()
centi_result.set("")
centi_output = tk.Label(frame1, textvariable=centi_result, font=label_style, fg="white", bg="black")

centi_button = tk.Button(frame1, text="Convert", command=convert_to_feet, font=label_style, bg="black", fg="white")

centi_label.grid(row=0, column=0, padx=5, pady=5)
centi_entry.grid(row=0, column=1, padx=5, pady=5)
centi_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
centi_output.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

feet_label = tk.Label(frame2, text="Feet to Inches", font=label_style, fg="white", bg="black")
feet_entry = tk.Entry(frame2, width=20, font=entry_style, bg="white", fg="black")
feet_result = tk.StringVar()
feet_result.set("")
feet_output = tk.Label(frame2, textvariable=feet_result, font=label_style, fg="white", bg="black")

feet_button = tk.Button(frame2, text="Convert", command=convert_to_inches, font=label_style, bg="black", fg="white")

feet_label.grid(row=0, column=0, padx=5, pady=5)
feet_entry.grid(row=0, column=1, padx=5, pady=5)
feet_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
feet_output.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

sqft_label = tk.Label(frame3, text="Sqft to Sqmtrs", font=label_style, fg="white", bg="black")
sqft_entry = tk.Entry(frame3, width=20, font=entry_style, bg="white", fg="black")
sqft_result = tk.StringVar()
sqft_result.set("")
sqft_output = tk.Label(frame3, textvariable=sqft_result, font=label_style, fg="white", bg="black")

sqft_button = tk.Button(frame3, text="Convert", command=convert_to_sqmtrs, font=label_style, bg="black", fg="white")

sqft_label.grid(row=0, column=0, padx=5, pady=5)
sqft_entry.grid(row=0, column=1, padx=5, pady=5)
sqft_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
sqft_output.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

sq_label = tk.Label(frame4, text="Sqft to Acres", font=label_style, fg="white", bg="black")
sq_entry = tk.Entry(frame4, width=20, font=entry_style, bg="white", fg="black")
sq_result = tk.StringVar()
sq_result.set("")
sq_output = tk.Label(frame4, textvariable=sq_result, font=label_style, fg="white", bg="black")

sq_button = tk.Button(frame4, text="Convert", command=convert_to_acres, font=label_style, bg="black", fg="white")

sq_label.grid(row=0, column=0, padx=5, pady=5)
sq_entry.grid(row=0, column=1, padx=5, pady=5)
sq_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
sq_output.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

window.mainloop()
