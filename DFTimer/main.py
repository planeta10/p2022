
﻿# Python defult Timer
from tkinter import *
from tkinter.messagebox import showerror
import plyer, sys

global  tk,a,m

def stop():

    global is_stop
    is_stop=1


def _in_pause():

    global in_pause
    in_pause = True


def _from_pause():
    global in_pause
    in_pause = False
    bt_proceed.grid_forget()
    bt_pause.grid(row=4, column=3)

def play():

    global a,m,s,out_s,bt_s,is_stop,data,in_pause,bt_pause,bt_proceed #slv

    if in_pause:
        bt_pause.grid_forget()
        bt_proceed.grid(row=4,column=2)
    else:
        bt_proceed.forget()
    if a:

        m = min_check.get()

        s,out_s =sec_check.get(),sec_check.get()

        if int(m) >= 60 or int(s) >= 60:  showerror("Внимание!", "Значение секунд и минут не может быть более 59!");return False

        a = False

        label_time.config(text="{}:{}".format(m, s))

        bt_s = Button(text="Stop", bg="black",fg="red",relief="flat",font=("bold", 15),activebackground="black",command=stop)
        bt_s.grid(row=4, column=1)

        bt_pause.grid(row=4,column=3)

        bt.grid_forget()
    else:

        if m == 0 and s == 0:
            plyer.notification.notify(app_name="Windows timer", title="Время прошло",
                                      message="Установленное время истекло!")
            a=True
            in_pause = False
            bt_s.destroy()
            bt_pause.grid_forget()
            label_time.config(text="00:00")
            bt.grid(row=4, column=2)
            return True

        try:

            if is_stop == 1:

                a=True
                in_pause = False
                is_stop=0
                label_time.config(text="00:00")
                bt_s.destroy()
                bt_pause.grid_forget()
                bt_proceed.grid_forget()
                bt.grid(row=4, column=2)
                return "Stop"

        except NameError:   pass

        if not in_pause:

            if s == 0 and m != 0:
                s,out_s = 59,59
                m -= 1

            else:

                s -= 1
                if type(out_s) == int:  out_s -=1
                if s < 10:  out_s = f"0{s}"

    # для красоты вывода чисел менее 10
    if not in_pause:

        try:

            if s < 10:
                out_s = f"0{s}"

            elif s == 0:
                out_s = "00"

        except NameError:   pass

        label_time.config(text="{}:{}".format(m, out_s))

    slv = tk.after(1000, play)

tk = Tk()

tk["bg"] = "black"
tk.resizable(False,False)

label_time = Label(text="00:00", bg="black", fg="white", font=('bold', 23))
label_time.grid(row=1, column=2)

Label(text="Количество минут", bg="black", fg="white").grid(row=2, column=1)
Label(text="Количество секунд", bg="black", fg="white").grid(row=3, column=1)

min_check = IntVar()
sec_check = IntVar()

minutes = Entry(fg="white", bg="black", font=("areal", 9), textvariable=min_check)
minutes.grid(row=2, column=2)

sec = Entry(fg="white", bg="black", font=("areal", 9), textvariable=sec_check)
sec.grid(row=3, column=2)

bt = Button(text="play", command=play,bg="black",fg="green",font=("bold", 15),activebackground="black",relief="flat")
bt.grid(row=4, column=2)

bt_pause = Button(text="Pause", command=_in_pause,bg="black",fg="orange",font=("bold", 15),activebackground="black",relief="flat")

bt_proceed = Button(text="Countinue", command=_from_pause,bg="black",fg="green",font=("bold", 15),activebackground="black",relief="flat")



a = True  # если true то еще не начинали
in_pause = False #если true то мы в паузе

slv = ""

tk.mainloop()
