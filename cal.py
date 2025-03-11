import tkinter as tk

def on_click(button_text):
    if button_text == "=":
        try:
            result = eval(entry_var.get())
            entry_var.set(result)
        except Exception as e:
            entry_var.set("Error")
    elif button_text == "C":
        entry_var.set("")
    else:
        entry_var.set(entry_var.get() + button_text)

root = tk.Tk()
root.title("Calculator")

entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 20), bd=10, relief=tk.GROOVE, justify="right")
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('C', '0', '=', '+')
]

for r, row in enumerate(buttons):
    for c, text in enumerate(row):
        btn = tk.Button(root, text=text, font=("Arial", 20), padx=20, pady=20, command=lambda t=text: on_click(t))
        btn.grid(row=r+1, column=c, sticky="nsew")


root.mainloop()
