from customtkinter import *
import Mathing_main,pymysql
class App:
    def __init__(self):
        self.tk = CTk()
        self.tk.geometry("400x400")
        self.tk.resizable(0,0)
        self.main_frame = CTkFrame(self.tk,width=400,height=400)
        self.login_frame = CTkFrame(self.tk)
        self.name_str = StringVar()
        self.name = CTkEntry(self.login_frame,textvariable=self.name_str)
        self.passw_str = StringVar()
        self.passw = CTkEntry(self.login_frame,textvariable=self.passw_str)
        self.login_open_button = CTkButton(self.main_frame,text="Войти",command=self.__login_open_in)
        self.login_in_button = CTkButton(self.login_frame,text="Войти",command=lambda:self.login_in(self.name_str.get(),self.passw_str.get()))
        self.Singleplayer = CTkButton(self.main_frame,text="Singleplayer",font=("Bold",35),command=lambda: self.__play(mode="Single"))     
        self.Multiplayer = CTkButton(self.main_frame,text="Multiplayer",font=("Bold",35),command=lambda: self.__play(mode="Multiple"))     
        self.login_open_button.pack()
        self.Singleplayer.pack()
        self.Multiplayer.pack()
        self.name.pack()
        self.passw.pack()
        self.login_in_button.pack()
        self.main_frame.pack()
        self.tk.mainloop()
    def __play(self,mode):    Mathing_main.Main(mode=mode)
    def __login_open_in(self):  self.main_frame.forget();self.login_frame.pack()
    def __conn_db(self):
        self.connection = pymysql.connect(host='localhost',
                             user='root',
                             password='Root',
                             database='Mathing_mind',
                             cursorclass=pymysql.cursors.DictCursor)

    def login_in(self,name,passw):
       self.__conn_db()
       sql = f"SELECT * from users where name='{name}';"
       with self.connection.cursor() as cursor:

           cursor.execute(sql)
           result = cursor.fetchone()
       print(result)
        


if __name__ == '__main__':
        App()

