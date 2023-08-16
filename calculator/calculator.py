import customtkinter as ctk
import re
# import numpy as np


ctk.set_appearance_mode("system")  # light, dark, system

# light colors
light_text_color_1 = "#000000"
light_color_1 = "#cbd2d5"
light_color_2 = "#3a8dcf"
light_color_3 = "#35709e"
light_hover_color_1 = "#3a8dcf"
light_hover_color_3 = "#3a8dcf"
light_hover_color_4 = "#b35e5e"

# dark colors
dark_text_color_1 = "#ffffff"
dark_color_1 = "#303134"
dark_color_2 = "#3b5160"
dark_color_3 = "#144870"
dark_hover_color_1 = "#3b5160"
dark_hover_color_3 = "#3b5160"
dark_hover_color_4 = "#663636"


# functions
def calculate():
    global result
    global equation
    global recent_calc
    global history, history_index
    if equation == "":
        equation = result
    try:
        result = eval(formatter(equation))
        if (result > 0) and ((result <= 0.0001) or (result >= 10000)):
            result = str("{:.3e}".format(result))
        elif (result < 0) and ((result >= -0.0001) or (result <= -10000)):
            result = str("{:.3e}".format(result))
        elif "." in str(result):
            temp_result = str(result).split(".")[-1]
            if result % 1 == 0:
                result = int(result)
            elif len(temp_result) < 5:
                result = str(result)
            else:
                result = "{:.5f}".format(result)
        print(f"= {result}")
        output_var_1.set(equation)
        output_var_2.set(result)
        result = str(result)
        history.append(equation)
        equation = ""
        recent_calc = True
        history_index = 0

    except ZeroDivisionError:
        output_var_1.set("Can't devide by zero")

    except SyntaxError:
        output_var_1.set("Syntax Error")

    except OverflowError:
        output_var_1.set("Overflow")


def formatter(text):
    global equation
    text = text.replace("×", "*")
    text = text.replace("÷", "/")
    text = re.sub(r"(\d)\(", r"\1*(", text)
    text = re.sub(r"\)\(", r")*(", text)
    text = text.replace("^", "**")
    print(text)
    return text


def adder(x):
    global result
    global equation
    global recent_calc
    if (x in "+-×÷^") and recent_calc:
        equation = result
    recent_calc = False
    result = ""
    output_var_1.set(result)
    if len(equation) > 0:
        if x in "+-×÷^":
            if equation[-1] in "+-×÷^":
                if (x == "-") and (equation[-1] != "-"):
                    equation += x
                    output_var_2.set(equation)
                else:
                    pass
            else:
                equation += x
                output_var_2.set(equation)
        else:
            equation += x
            output_var_2.set(equation)
    elif x not in "+×÷^":
        equation += x
        output_var_2.set(equation)


def remover():
    global result
    global equation
    result = ""
    output_var_1.set(result)
    equation = equation[:-1]
    output_var_2.set(equation)


def clearer():
    global result
    global equation
    global history_index
    history_index = 0
    result = ""
    output_var_1.set(result)
    equation = ""
    output_var_2.set(equation)


def history_func(value: str):
    global equation
    global hisory, history_index
    if value == "up":
        output_var_1.set("")
        history_index += 1
        try:
            equation = history[-history_index]
            output_var_2.set(equation)
        except IndexError:
            history_index -= 1
    elif value == "down":
        output_var_1.set("")
        history_index -= 1
        try:
            equation = history[len(history) - history_index]
            output_var_2.set(equation)
        except IndexError:
            history_index += 1


def info():
    output_var_1.set("Calculator by Mahdi Hasan")


app = ctk.CTk()
app.title("Calculator")
app.geometry("400x500")
app.rowconfigure(0, weight=1)
app.rowconfigure(1, weight=2)
app.columnconfigure(0, weight=1)

# variables
output_var_1 = ctk.StringVar()
output_var_2 = ctk.StringVar()
result = ""
equation = ""
history = []
history_index = 0
recent_calc = False

result_frame = ctk.CTkFrame(
    app,
    fg_color=(light_color_1, dark_color_1),
)
result_frame.grid(
    row=0,
    column=0,
    padx=10,
    pady=(10, 0),
    sticky="nsew",
)
result_frame.rowconfigure((0, 1), weight=1)
result_frame.columnconfigure(0, weight=1)

btn_frame = ctk.CTkFrame(app, fg_color="transparent")
btn_frame.grid(
    row=1,
    column=0,
    sticky="nsew",
)
btn_frame.rowconfigure((0, 1, 2, 3, 4, 5), weight=1)
btn_frame.columnconfigure((0, 1, 2, 3), weight=1)

result_label_1 = ctk.CTkLabel(
    result_frame,
    textvariable=output_var_1,
    text_color=(light_text_color_1, dark_text_color_1),
    font=("Roboto", 16),
)
result_label_1.grid(
    row=0,
    column=0,
    padx=10,
    pady=(10, 0),
    sticky="e",
)

result_label_2 = ctk.CTkLabel(
    result_frame,
    textvariable=output_var_2,
    text_color=(light_text_color_1, dark_text_color_1),
    font=("Roboto", 36),
)
result_label_2.grid(
    row=1,
    column=0,
    padx=10,
    pady=(0, 10),
    sticky="e",
)

# row 0
btn_h1 = ctk.CTkButton(
    btn_frame,
    text="⬅️",
    fg_color=(light_color_1, dark_color_1),
    hover_color=(light_hover_color_1, dark_hover_color_1),
    font=("Roboto", 20),
    text_color=(light_text_color_1, dark_text_color_1),
    command=lambda: history_func("up"),
)
btn_h1.grid(
    row=0,
    column=0,
    padx=(10, 0),
    pady=(10, 0),
    sticky="nsew",
)

btn_h2 = ctk.CTkButton(
    btn_frame,
    text="➡️",
    fg_color=(light_color_1, dark_color_1),
    hover_color=(light_hover_color_1, dark_hover_color_1),
    font=("Roboto", 20),
    text_color=(light_text_color_1, dark_text_color_1),
    command=lambda: history_func("down"),
)
btn_h2.grid(
    row=0,
    column=1,
    padx=(10, 0),
    pady=(10, 0),
    sticky="nsew",
)

btn_del = ctk.CTkButton(
    btn_frame,
    text="DEL",
    fg_color=(light_color_1, dark_color_1),
    hover_color=(light_hover_color_1, dark_hover_color_1),
    font=("Roboto", 20),
    text_color=(light_text_color_1, dark_text_color_1),
    command=lambda: remover(),
)
btn_del.grid(
    row=0,
    column=2,
    padx=(10, 0),
    pady=(10, 0),
    sticky="nsew",
)

btn_ac = ctk.CTkButton(
    btn_frame,
    text="AC",
    fg_color=(light_color_1, dark_color_1),
    hover_color=(light_hover_color_4, dark_hover_color_4),
    font=("Roboto", 20),
    text_color=(light_text_color_1, dark_text_color_1),
    command=lambda: clearer(),
)
btn_ac.grid(
    row=0,
    column=3,
    padx=(10, 10),
    pady=(10, 0),
    sticky="nsew",
)

# row 1
btn_info = ctk.CTkButton(
    btn_frame,
    text="i",
    fg_color=(light_color_1, dark_color_1),
    hover_color=(light_hover_color_1, dark_hover_color_1),
    font=("Roboto", 20),
    text_color=(light_text_color_1, dark_text_color_1),
    command=lambda: info(),
)
btn_info.grid(
    row=1,
    column=0,
    padx=(10, 0),
    pady=(10, 0),
    sticky="nsew",
)

btn_br_start = ctk.CTkButton(
    btn_frame,
    text="(",
    fg_color=(light_color_1, dark_color_1),
    hover_color=(light_hover_color_1, dark_hover_color_1),
    font=("Roboto", 20),
    text_color=(light_text_color_1, dark_text_color_1),
    command=lambda: adder("("),
)
btn_br_start.grid(
    row=1,
    column=1,
    padx=(10, 0),
    pady=(10, 0),
    sticky="nsew",
)

btn_br_end = ctk.CTkButton(
    btn_frame,
    text=")",
    fg_color=(light_color_1, dark_color_1),
    hover_color=(light_hover_color_1, dark_hover_color_1),
    font=("Roboto", 20),
    text_color=(light_text_color_1, dark_text_color_1),
    command=lambda: adder(")"),
)
btn_br_end.grid(
    row=1,
    column=2,
    padx=(10, 0),
    pady=(10, 0),
    sticky="nsew",
)

btn_div = ctk.CTkButton(
    btn_frame,
    text="^",
    fg_color=(light_color_1, dark_color_1),
    hover_color=(light_hover_color_1, dark_hover_color_1),
    font=("Roboto", 20),
    text_color=(light_text_color_1, dark_text_color_1),
    command=lambda: adder("^"),
)
btn_div.grid(
    row=1,
    column=3,
    padx=(10, 10),
    pady=(10, 0),
    sticky="nsew",
)

# row 2
btn_7 = ctk.CTkButton(
    btn_frame,
    text="7",
    fg_color=(light_color_2, dark_color_2),
    font=("Roboto", 20),
    text_color=(light_text_color_1, dark_text_color_1),
    command=lambda: adder("7"),
)
btn_7.grid(
    row=2,
    column=0,
    padx=(10, 0),
    pady=(10, 0),
    sticky="nsew",
)

btn_8 = ctk.CTkButton(
    btn_frame,
    text="8",
    fg_color=(light_color_2, dark_color_2),
    font=("Roboto", 20),
    text_color=(light_text_color_1, dark_text_color_1),
    command=lambda: adder("8"),
)
btn_8.grid(
    row=2,
    column=1,
    padx=(10, 0),
    pady=(10, 0),
    sticky="nsew",
)

btn_9 = ctk.CTkButton(
    btn_frame,
    text="9",
    fg_color=(light_color_2, dark_color_2),
    font=("Roboto", 20),
    text_color=(light_text_color_1, dark_text_color_1),
    command=lambda: adder("9"),
)
btn_9.grid(
    row=2,
    column=2,
    padx=(10, 0),
    pady=(10, 0),
    sticky="nsew",
)

btn_div = ctk.CTkButton(
    btn_frame,
    text="÷",
    fg_color=(light_color_1, dark_color_1),
    hover_color=(light_hover_color_1, dark_hover_color_1),
    font=("Roboto", 20),
    text_color=(light_text_color_1, dark_text_color_1),
    command=lambda: adder("÷"),
)
btn_div.grid(
    row=2,
    column=3,
    padx=(10, 10),
    pady=(10, 0),
    sticky="nsew",
)

# row 3
btn_4 = ctk.CTkButton(
    btn_frame,
    text="4",
    fg_color=(light_color_2, dark_color_2),
    font=("Roboto", 20),
    text_color=(light_text_color_1, dark_text_color_1),
    command=lambda: adder("4"),
)
btn_4.grid(
    row=3,
    column=0,
    padx=(10, 0),
    pady=(10, 0),
    sticky="nsew",
)

btn_5 = ctk.CTkButton(
    btn_frame,
    text="5",
    fg_color=(light_color_2, dark_color_2),
    font=("Roboto", 20),
    text_color=(light_text_color_1, dark_text_color_1),
    command=lambda: adder("5"),
)
btn_5.grid(
    row=3,
    column=1,
    padx=(10, 0),
    pady=(10, 0),
    sticky="nsew",
)

btn_6 = ctk.CTkButton(
    btn_frame,
    text="6",
    fg_color=(light_color_2, dark_color_2),
    font=("Roboto", 20),
    text_color=(light_text_color_1, dark_text_color_1),
    command=lambda: adder("6"),
)
btn_6.grid(
    row=3,
    column=2,
    padx=(10, 0),
    pady=(10, 0),
    sticky="nsew",
)

btn_multi = ctk.CTkButton(
    btn_frame,
    text="×",
    fg_color=(light_color_1, dark_color_1),
    hover_color=(light_hover_color_1, dark_hover_color_1),
    font=("Roboto", 20),
    text_color=(light_text_color_1, dark_text_color_1),
    command=lambda: adder("×"),
)
btn_multi.grid(
    row=3,
    column=3,
    padx=(10, 10),
    pady=(10, 0),
    sticky="nsew",
)

# row 4
btn_1 = ctk.CTkButton(
    btn_frame,
    text="1",
    fg_color=(light_color_2, dark_color_2),
    font=("Roboto", 20),
    text_color=(light_text_color_1, dark_text_color_1),
    command=lambda: adder("1"),
)
btn_1.grid(
    row=4,
    column=0,
    padx=(10, 0),
    pady=(10, 0),
    sticky="nsew",
)

btn_2 = ctk.CTkButton(
    btn_frame,
    text="2",
    fg_color=(light_color_2, dark_color_2),
    font=("Roboto", 20),
    text_color=(light_text_color_1, dark_text_color_1),
    command=lambda: adder("2"),
)
btn_2.grid(
    row=4,
    column=1,
    padx=(10, 0),
    pady=(10, 0),
    sticky="nsew",
)

btn_3 = ctk.CTkButton(
    btn_frame,
    text="3",
    fg_color=(light_color_2, dark_color_2),
    font=("Roboto", 20),
    text_color=(light_text_color_1, dark_text_color_1),
    command=lambda: adder("3"),
)
btn_3.grid(
    row=4,
    column=2,
    padx=(10, 0),
    pady=(10, 0),
    sticky="nsew",
)

btn_minus = ctk.CTkButton(
    btn_frame,
    text="-",
    fg_color=(light_color_1, dark_color_1),
    hover_color=(light_hover_color_1, dark_hover_color_1),
    font=("Roboto", 20),
    text_color=(light_text_color_1, dark_text_color_1),
    command=lambda: adder("-"),
)
btn_minus.grid(
    row=4,
    column=3,
    padx=(10, 10),
    pady=(10, 0),
    sticky="nsew",
)

# row 5
btn_0 = ctk.CTkButton(
    btn_frame,
    text="0",
    fg_color=(light_color_2, dark_color_2),
    font=("Roboto", 20),
    text_color=(light_text_color_1, dark_text_color_1),
    command=lambda: adder("0"),
)
btn_0.grid(
    row=5,
    column=0,
    padx=(10, 0),
    pady=(10, 10),
    sticky="nsew",
)

btn_dot = ctk.CTkButton(
    btn_frame,
    text=".",
    fg_color=(light_color_2, dark_color_2),
    font=("Roboto", 20),
    text_color=(light_text_color_1, dark_text_color_1),
    command=lambda: adder("."),
)
btn_dot.grid(
    row=5,
    column=1,
    padx=(10, 0),
    pady=(10, 10),
    sticky="nsew",
)

btn_calc = ctk.CTkButton(
    btn_frame,
    text="=",
    fg_color=(light_color_3, dark_color_3),
    hover_color=(light_hover_color_3, dark_hover_color_3),
    font=("Roboto", 20),
    text_color=(light_text_color_1, dark_text_color_1),
    command=lambda: calculate(),
)
btn_calc.grid(
    row=5,
    column=2,
    padx=(10, 0),
    pady=(10, 10),
    sticky="nsew",
)

btn_plus = ctk.CTkButton(
    btn_frame,
    text="+",
    fg_color=(light_color_1, dark_color_1),
    hover_color=(light_hover_color_1, dark_hover_color_1),
    font=("Roboto", 20),
    text_color=(light_text_color_1, dark_text_color_1),
    command=lambda: adder("+"),
)
btn_plus.grid(
    row=5,
    column=3,
    padx=(10, 10),
    pady=(10, 10),
    sticky="nsew",
)

app.bind("<KeyPress-1>", lambda event: adder("1"))
app.bind("<KeyPress-2>", lambda event: adder("2"))
app.bind("<KeyPress-3>", lambda event: adder("3"))
app.bind("<KeyPress-4>", lambda event: adder("4"))
app.bind("<KeyPress-5>", lambda event: adder("5"))
app.bind("<KeyPress-6>", lambda event: adder("6"))
app.bind("<KeyPress-7>", lambda event: adder("7"))
app.bind("<KeyPress-8>", lambda event: adder("8"))
app.bind("<KeyPress-9>", lambda event: adder("9"))
app.bind("<KeyPress-0>", lambda event: adder("0"))
app.bind("<KeyPress-plus>", lambda event: adder("+"))
app.bind("<KeyPress-minus>", lambda event: adder("-"))
app.bind("<KeyPress-asterisk>", lambda event: adder("×"))
app.bind("<KeyPress-slash>", lambda event: adder("÷"))
app.bind("<KeyPress-asciicircum>", lambda event: adder("^"))
app.bind("<KeyPress-period>", lambda event: adder("."))
app.bind("<KeyPress-parenleft>", lambda event: adder("("))
app.bind("<KeyPress-parenright>", lambda event: adder(")"))
app.bind("<KeyPress-period>", lambda event: adder("."))
app.bind("<KeyPress-BackSpace>", lambda event: remover())
app.bind("<KeyPress-Escape>", lambda event: clearer())
app.bind("<KeyPress-Return>", lambda event: calculate())
app.bind("<KeyPress-Left>", lambda event: history_func("up"))
app.bind("<KeyPress-Right>", lambda event: history_func("down"))

app.mainloop()
