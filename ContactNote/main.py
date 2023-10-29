from tkinter import *
from tkinter.messagebox import showinfo as info
from dataclasses import dataclass
import json,os
import contact_adder


class main_app:
    def __init__(self):

        self.tk = Tk()
        self.tk.title("Записная книжка")
        self.tk.resizable(0,0)
        #self.tk.geometry('500x500')

        self.menu = Menu(self.tk)
        self.tk.config(menu=self.menu)

        filemenu = Menu(self.menu, tearoff=0)
        filemenu.add_command(label="Добавить",command=self.add_contact)
        filemenu.add_command(label="Редактировать...")
        filemenu.add_command(label="Удалить...")

        helpmenu = Menu(self.menu, tearoff=0)
        helpmenu.add_command(label="Помощь")
        helpmenu.add_command(label="О программе")

        self.menu.add_cascade(label="Контакты",
                             menu=filemenu)
        self.menu.add_cascade(label="Справка",
                             menu=helpmenu)

        self.tk.config(menu=self.menu)
        self.main_frame = Frame(self.tk)

        self.label = Label(self.tk, text="Поиск контактов")
        self.label.pack()

        """self.add = Button(text="Добавить контакт",command=self.add_contact)
        self.add.pack(side=RIGHT)"""


        self.entry = Entry(width=117)
        self.entry.pack()

        self.scroll = Scrollbar(self.tk, orient='vertical')
        self.textbox = Text(self.main_frame, width=70,font=("Bold",20),yscrollcommand=self.scroll.set)
        self.textbox.pack()

        self.scroll.config(command=self.textbox.yview)
        self.scroll.pack(side=RIGHT,fill="y")

        self.main_frame.pack()

        #отображаем все контакты
        self.viev_contact()

        self.tk.mainloop()

    def add_contact(self):
        var = contact_adder.main()

        self.viev_contact()


    def viev_contact(self):
        if os.path.exists(r"C:\Users\ОЛЬГА\Desktop\need\coding\python\ContactBook\data\contacts.json"):
            with open(r"C:\Users\ОЛЬГА\Desktop\need\coding\python\ContactBook\data\contacts.json", 'r') as file:
                #читаем содержимое файла(все контакты)
                text_from_file = json.load(file)

                #Вывод контактов в TextBox
                if len(text_from_file["main_user"]) != 0:
                    self.textbox.delete(1.0,END)
                    for i in enumerate(text_from_file["main_user"]):
                        string = f'Name: {i[1]["name"]} Num: {i[1]["number"]} Address: {i[1]["address"]} \n'
                        print(string)
                        self.textbox.insert(END,string)#f'{i[0]}.0',string)
                        self.textbox.update()

        else: info("","File is not defined")

    def contact_find(self):
        ...


if __name__ == '__main__':
    main_app()