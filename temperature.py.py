import pyowm
import tkinter
from tkinter import *
class get_weather:
    
    def __init__(self):
        def get_temperature():
            try:
                owm = pyowm.OWM('d8303ab80e84f15ab671bc8e07c87371')
                mgr = owm.weather_manager()
                c=self.city.get()
                
                obs = mgr.weather_at_place(c)
                w = obs.weather
                t = w.temperature("celsius")
                t1 = t['temp']
                main_temp =  f"В городе <{self.city.get()}> сейчас {format(t1, '.1f')} С° "
                self.textbox.delete('1.0', END)
                self.textbox.insert('1.0',main_temp)
            except Exception as e:
                self.textbox.delete('1.0',END)
                self.textbox.insert('1.0',f"город <{self.city.get()}> не найден или его не существует")
                print(e,"(формулировка ошибки)")
        self.tk = Tk()
        self.tk.geometry('400x150')
        self.frame = Frame(master=self.tk,bg='light yellow')
        self.frame.pack(fill=BOTH)
        self.tk['bg'] = 'light yellow'
        self.label = Label(master=self.frame,text="Город")
        self.label.pack(fill=BOTH)
        self.city = StringVar()
        self.et = Entry(master=self.frame,textvariable=self.city)
        self.et.pack(fill=BOTH)
        self.button = Button(master=self.frame,text="Узнать температуру",command=get_temperature)
        self.button.pack(fill=BOTH)
        self.textbox = Text(master=self.frame,width=29,height=4)
        self.textbox.pack(fill=BOTH)
        self.tk.mainloop()    
if(__name__ == '__main__'):
    a=get_weather()

#идеи:    
#история запросов
#рекомендуемые города(города поблизости)
#создание веб-интерфейса
