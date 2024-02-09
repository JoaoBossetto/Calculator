import tkinter as tk

calculation = ""

def add_calculattion(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def evaluate_calculation():
    global calculation
    try:
        result = str(eval(calculation))
        calculation = ""
        text_result.delete(1.0, "end")
        text_result.insert(1.0, result)
    except:
        clear_field()
        text_result.insert(1.0, "Error")

def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")

root = tk.Tk()
root.title("Calculator")
root.geometry("300x275")

text_result = tk.Text(root, height=2, width=16, font=("Arial", 24))
text_result.grid(columnspan=5)

#1
btn_1 = tk.Button(root, text="1", command=lambda:add_calculattion(1), width = 5, font=("Arial", 14))
btn_1.grid(row=2, column=1)

#2
btn_2 = tk.Button(root, text="2", command=lambda:add_calculattion(2), width = 5, font=("Arial", 14))
btn_2.grid(row=2, column=2)

#3
btn_3 = tk.Button(root, text="3", command=lambda:add_calculattion(3), width = 5, font=("Arial", 14))
btn_3.grid(row=2, column=3)

#4
btn_4 = tk.Button(root, text="4", command=lambda:add_calculattion(4), width = 5, font=("Arial", 14))
btn_4.grid(row=3, column=1)

#5
btn_5 = tk.Button(root, text="5", command=lambda:add_calculattion(5), width = 5, font=("Arial", 14))
btn_5.grid(row=3, column=2)

#6
btn_6 = tk.Button(root, text="6", command=lambda:add_calculattion(6), width = 5, font=("Arial", 14))
btn_6.grid(row=3, column=3)

#7
btn_7 = tk.Button(root, text="7", command=lambda:add_calculattion(7), width = 5, font=("Arial", 14))
btn_7.grid(row=4, column=1)

#8
btn_8 = tk.Button(root, text="8", command=lambda:add_calculattion(8), width = 5, font=("Arial", 14))
btn_8.grid(row=4, column=2)

#9
btn_9 = tk.Button(root, text="9", command=lambda:add_calculattion(9), width = 5, font=("Arial", 14))
btn_9.grid(row=4, column=3)

#0
btn_0 = tk.Button(root, text="0", command=lambda:add_calculattion(0), width = 5, font=("Arial", 14))
btn_0.grid(row=5, column=2)

#addition
btn_plus = tk.Button(root, text="+", command=lambda:add_calculattion("+"), width = 5, font=("Arial", 14))
btn_plus.grid(row=2, column=4)

#subtraction
btn_minus = tk.Button(root, text="-", command=lambda:add_calculattion("-"), width = 5, font=("Arial", 14))
btn_minus.grid(row=3, column=4)

#mult
btn_multiplication = tk.Button(root, text="*", command=lambda:add_calculattion("*"), width = 5, font=("Arial", 14))
btn_multiplication.grid(row=4, column=4)

#div
btn_division = tk.Button(root, text="/", command=lambda:add_calculattion("/"), width = 5, font=("Arial", 14))
btn_division.grid(row=5, column=4)

#(
btn_paren = tk.Button(root, text="(", command=lambda:add_calculattion("("), width = 5, font=("Arial", 14))
btn_paren.grid(row=5, column=1)

#)
btn_paren = tk.Button(root, text=")", command=lambda:add_calculattion(")"), width = 5, font=("Arial", 14))
btn_paren.grid(row=5, column=3)

#=
btn_equal = tk.Button(root, text="=", command=evaluate_calculation, width = 11, font=("Arial", 14))
btn_equal.grid(row=6, column=3, columnspan=2)

#clear
btn_clear = tk.Button(root, text="c", command=clear_field, width = 11, font=("Arial", 14))
btn_clear.grid(row=6, column=1, columnspan=2)

root.mainloop()
