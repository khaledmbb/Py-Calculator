from tkinter import *

root = Tk()
root.title("Calculator")
e = Entry(root, borderwidth=5, width=45)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=5)

math = ""


def click(num):
    e.config(bg="white", fg="black")
    e.delete(0, END)
    e.insert(END, num)


def addition():
    global f_num, math
    math = "addition"
    f_num = e.get()
    e.delete(0, END)


def subtraction():
    global f_num, math
    math = "subtraction"
    f_num = e.get()
    e.delete(0, END)


def multiplication():
    global f_num, math
    math = "multiplication"
    f_num = e.get()
    e.delete(0, END)


def division():
    global f_num, math
    math = "division"
    f_num = e.get()
    e.delete(0, END)


def calc():
    try:
        s_num = int(e.get())
        e.delete(0, END)
        if math == "addition":
            e.insert(0, str(int(f_num) + s_num))
        elif math == "subtraction":
            e.insert(0, str(int(f_num) - s_num))
        elif math == "multiplication":
            e.insert(0, str(int(f_num) * s_num))
        elif math == "division":
            e.insert(0, str(round(int(f_num) / s_num, None)))
    except ValueError:
        e.insert(0, "Please type the second number")
        e.config(bg="red", fg="white")


def clear():
    e.delete(0, END)


def del_one():
    curr_num = e.get()
    e.delete(0, END)
    e.insert(0, curr_num[:-1])


for i in range(1, 10):
    btn = Button(root, text=i, padx=38, pady=20)
    btn.grid(
        row=3 if i <= 3 else 2 if i <= 6 else 1,
        column=0 if i in (1, 4, 7) else 1 if i in (2, 5, 8) else 2,
    )
    btn.configure(command=lambda text=btn["text"]: click(text))

zero_btn = Button(root, text="0", padx=38, pady=20, command=lambda: click(0)).grid(
    row=4, column=0
)
add = Button(root, text="+", padx=37, pady=20, command=addition).grid(row=4, column=1)
sub = Button(root, text="-", padx=39, pady=20, command=subtraction).grid(
    row=4, column=2
)
mult = Button(root, text="*", padx=38, pady=20, command=multiplication).grid(
    row=5, column=0
)
div = Button(root, text="/", padx=39, pady=20, command=division).grid(row=5, column=1)
delete = Button(root, text="X", padx=38, pady=20, command=del_one).grid(row=5, column=2)
equal = Button(root, text="=", padx=25, pady=20, width=19, command=calc).grid(
    row=6, column=0, columnspan=2
)
del_all = Button(root, text="C", padx=38, pady=20, command=clear).grid(row=6, column=2)


root.mainloop()
