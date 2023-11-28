import tkinter as tk
import math

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    expression = entry.get()
    try:
        if "^" in expression:
            base, exponent = expression.split("^")
            result = float(base) ** float(exponent)
        elif "sin" in expression:
            angle = expression.replace("sin", "")
            result = math.sin(float(angle))
        elif "cos" in expression:
            angle = expression.replace("cos", "")
            result = math.cos(float(angle))
        else:
            result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

root = tk.Tk()
root.title("Калькулятор")

entry = tk.Entry(root, width=70, borderwidth=1)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    (1, 2, 3, "+"),
    (4, 5, 6, "-"),
    (7, 8, 9, "*"),
    (0, ".", "^", "/"),
    ( "","","sin", "cos")
]

for i, row in enumerate(buttons, start=1):
    for j, symbol in enumerate(row):
        button = tk.Button(root, text=str(symbol), padx=40, pady=20, command=lambda symbol=symbol: button_click(symbol))
        button.grid(row=i, column=j, padx=5, pady=5)

button_clear = tk.Button(root, text="C", padx=40, pady=20, command=button_clear)
button_clear.grid(row=5, column=0, padx=5, pady=5)

button_equal = tk.Button(root, text="=", padx=40, pady=20, command=button_equal)
button_equal.grid(row=5, column=1, padx=5, pady=5)

root.mainloop()