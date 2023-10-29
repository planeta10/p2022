# -*- coding: utf-8 -*-

from tkinter import *
from tkinter.messagebox import showerror as error,showinfo as info
import json,os
import main



def main():
    global str_name,str_address,str_number,name,number,address,tk1,in_return
    tk1 = Tk()
    tk1.title('Добавить контакт')
    tk1.focus_force()

    in_return = False #для вызвращения в main file

    Label(tk1,text='Имя').grid(row=1,column=0)
    Label(tk1,text='Номер').grid(row=2, column=0)
    Label(tk1,text='Адрес(не обязательно)').grid(row=3, column=0)

    button = Button(tk1,text="Сохранить и закрыть",command=check_entry)

    str_name = StringVar()
    str_number = StringVar()
    str_address = StringVar()

    name = Entry(tk1,textvariable=str_name)
    name.insert(0,1234)

    number = Entry(tk1,textvariable=str_number)
    number.insert(0,1234)

    address = Entry(tk1,textvariable=str_address)
    address.insert(0,1234)

    name.grid(row=1,column=1)
    number.grid(row=2, column=1)
    address.grid(row=3, column=1)
    button.grid(row=4,column=2)

    tk1.mainloop()

def check_entry():
    global in_return
    if name.get() == "" and number.get() == "":

        error(f"{str_name.get()} and {str_number.get()}", "Обязательные поля для ввода должны быть заполнены!")

    else:
        b = save_in_json()
        tk1.quit()
        tk1.destroy()
        in_return = True


def save_in_json():

    #Запись в json файл

    # забираем данные из файла
    try:
        with open("data/contacts.json",'r+') as file:

            text_from_file = json.load(file)
            text_from_file["main_user"].append(
                {"name": name.get(), "number": number.get(), "address": address.get()})
           # error("",text_from_file)

        # удаляем файл

        os.remove("data/contacts.json")

        #перезаписываем с добавленым словарем (контактом)

        with open("data/contacts.json",'w+') as file:

            json.dump(text_from_file,file)

    #обработка исключения если нету файла
    except FileNotFoundError:

        #записываем в файл пустой json
        with open("data/contacts.json","w+") as file:

            st = """{"main_user":[]}"""
            json_st = json.loads(st)

            json.dump(json_st,file)
            info("","Попробуйте еще раз, должно сработать!")
    except Exception as e: error("",e)
    else:
        #отображение в TextBox
        pass


if __name__ == '__main__':
    main()