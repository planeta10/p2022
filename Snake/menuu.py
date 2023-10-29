from tkinter import *
from tkinter.messagebox import showinfo,askyesno
from tkinter.colorchooser import askcolor
import Snake_release,os

class main:
    def __init__(self):
        # root window

        self.root = Tk()
        self.root.focus_force()
        #self.root.resizable(False, False)
        # self.root.geometry('100x200')

        self.root.title('Menu')

        # create frames

        self.main_frame = Frame(self.root)
        

        self.main_frame.pack()

        #create main buttons

        self.play = Button(self.main_frame, text="play", font=("arear", 15), fg="black", command=self.go_app)
        self.settings =Button(self.main_frame, text="Settings", font=("arear", 15), fg="black",command=self.Settings)
        self.acheve = Button(self.main_frame, text="acheve", font=("arear", 15), fg="black",command=self.Loock_acheve)
        self.exit = Button(self.main_frame, text="exit", font=("arear", 15),command=lambda : exit(0))

        #create settings objects
        
        self.scale = Scale(self.root,from_ = 600, to=1500, length=300,resolution=20,showvalue=1,orient=HORIZONTAL,tickinterval=200)
        self.label_speed = Label(text="Изменение скорости (чем меньше значение , тем больше скорость)",font=("arear", 15))
        self.label_geometry_root = Label(text="Изменение размера окна",font=('arear',15))
        self.speed = IntVar()
        self.entry_speed= Entry(textvariable=self.speed)
        self.button_check_speed = Button(text="Применить",command=self.check_settings)
        self.check_add_speed = StringVar()
        self.checkbt = Checkbutton(text="Увеличивать скорость при поедании",variable=self.check_add_speed)
        self.exit_speed_button = Button(text="Exit",command=self.go_menue_from_settings)
        

        self.play.pack()
        self.settings.pack()
        self.acheve.pack()
        self.exit.pack()

        # add frames to notebook



        self.root.mainloop()


    def go_app(self):
        self.root.destroy()
        Snake_release.app()


    def Settings(self):
        self.main_frame.pack_forget()
        self.label_speed.pack()
        
        self.entry_speed.pack()
        self.label_geometry_root.pack()
        self.scale.pack()
        self.checkbt.pack()
        self.button_check_speed.pack()
        self.exit_speed_button.pack()
        self.entry_speed.delete(0,END)
        self.entry_speed.insert(0,60)

    def Loock_acheve(self):
        self.main_frame.pack_forget()
        self.exit_from_aheve = Button(text="exit",command=self.go_menue_from_aheve)

        try:

            with open("data.txt",'r') as data:
                self.label=Label(text=f"Your record is {data.read()} score",font=("arear", 15))
                self.label.pack()
        except Excetion as e:
            showinfo("",e)
           # self.label = Label(text=f"You dont play", font=("arear", 15))
            #self.label.pack()
        #finally:    showinfo("", "Error")
        self.exit_from_aheve.pack()


    def go_menue_from_aheve(self):
        self.label.forget()
        self.exit_from_aheve.forget()
        self.main_frame.pack()


    def go_menue_from_settings(self):
        self.label_speed.forget()
        self.exit_speed_button.forget()
        self.entry_speed.forget()
        self.button_check_speed.forget()
        self.scale.forget()
        self.label_geometry_root.forget()
        self.checkbt.forget()
        self.main_frame.pack()
    def check_settings(self):
        try:
            if self.speed.get() == "":  showinfo("","Введите значение")
        except: showinfo("","Некорректный ввод")
        else: 
            if not isinstance(self.speed.get(),int): showinfo("","Некорректный ввод")
            else:
                if int(self.speed.get())<40:
                    if askyesno("Внимение", "Не рекомендуется ставить значение скорости менее 40 \n Продолжить?"):
                        showinfo("","Применено")
                        os.remove("option.txt")
                        with open("option.txt",'w+') as file:
                            file.write(str(self.speed.get()))
                else:
                    showinfo("","Применено")
                    os.remove("option.txt")
                    with open("option.txt",'w+') as file:
                        file.write(str(self.speed.get()))
        try:    os.remove("window_config.txt")
        except Exception as e:   showinfo("",e)
     #   else:   showinfo("", "Произошла ошибка")
        with open("window_config.txt",'w+') as file:
            file.write(str(self.scale.get()))
        try:    os.remove("speed_app.txt")
        except FileNotFoundError: pass
        with open("speed_add.txt", 'w+') as file:
            file.write(str(self.check_add_speed.get()))



if __name__ =="__main__":
    main()