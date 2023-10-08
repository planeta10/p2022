# -*- coding -*-: utf-8 -*-
from customtkinter import *
from tkinter import ttk
from tkinter import *
from tkinter import messagebox as mb
from random import randint,choice
import math
from threading import Thread
import time,Rank,os,SaveDb




class Main:
    
    def __init__(self,mode):

        self.tk = CTk()
        self.tk.title("Mathing")
        #self.tk.resizable(0,0)
        self.tk.resizable(height = None, width = None)
        
        self.WIDTH = 500
        self.HEIGHT = 500
        self.mode = mode #Single or Multipl
        self.step = 0
        self.sleep_time = 0.7 #seconds
        self.is_start_timer = False # True if we must start timer
        self.is_run_timer = False
        self.hard_cft = 0
        self.all_results = {}
        self.true_or_false = []
        self.num_examples = 2
        self.theme = "dark"
        self.ask_results = True
        
        set_appearance_mode("Dark")

        
        """ Create Multi Tabs """
        self.notebook = ttk.Notebook(self.tk)
        # self.notebook.pack()

        
        self.frame_play = CTkFrame(self.notebook, width=self.WIDTH, height=self.HEIGHT)
        self.frame_settings = CTkFrame(self.notebook, width=self.WIDTH, height=self.HEIGHT)
        self.frame_rank = CTkFrame(self.notebook, width=self.WIDTH, height=self.HEIGHT)
        self.frame_game = CTkFrame(self.notebook, width=self.WIDTH, height=self.HEIGHT)
        self.frame_child_play=CTkFrame(self.frame_play, width=self.WIDTH, height=self.HEIGHT)
        self.frame_child_game = CTkFrame(self.frame_play, width=self.WIDTH, height=self.HEIGHT)

        self.frame_settings.pack_propagate(0)
        
        
        
        self.frame_play.pack(fill='both', expand=True)
        self.frame_child_play.pack(fill='both',expand=True)

        self.notebook.add(self.frame_play, text='Играть')
        self.notebook.add(self.frame_rank, text='Звание')
        self.notebook.add(self.frame_settings, text='Настройки')

        
        """ Set window on screen cetner """
 
        sw = self.tk.winfo_screenwidth()
        sh = self.tk.winfo_screenheight()
 
        x = (sw - self.WIDTH) / 2
        y = (sh - self.HEIGHT) / 2
        self.tk.geometry('%dx%d+%d+%d' % (self.WIDTH, self.HEIGHT, x, y))

        """ Add interphace"""
        CTkLabel(self.frame_child_play,text="Возраст",font=("Arial",30)).pack()

        self.text_age = StringVar()

        self.age = CTkEntry(self.frame_child_play,font=("Calibry",25),justify=CENTER,textvariable=self.text_age)
        self.age.focus()
        self.label_hard_cft = CTkLabel(self.frame_child_game,font=("Arial",25))
        self.button_start = CTkButton(self.frame_child_play,text="Начать",command=self.check_age)
        self.math_example = CTkLabel(self.frame_child_game,font = ("Bold",100))
        self.label_check_rank = Label(self.frame_rank,text = self.__get_rank_file(),font=("Bold",30),bg="white",fg="black")
        #self.label_check_rank = Label(self.frame_rank,text = "Text",font=("Bold",30),bg="white",fg="black")   
        #self.theme = CTkCheckBox(self.frame_settings,text="Темная тема", variable=self.var_theme)#, command=checkbutton_changed)
        self.var_theme = IntVar()
        self.cb_theme = CTkCheckBox(self.frame_settings,command=self.change_theme,variable=self.var_theme,text="Темная тема",font=("Bold",30))#, variable=self.var_theme)
        self.cb_theme.select()
        def ask_results_func():
            self.ask_results=False if self.ask_results else True
        self.ask_results_button = CTkCheckBox(self.frame_settings,command=ask_results_func,text="Отображение результата",font=("Bold",30))
        self.ask_results_button.select()

        
                 
        self.text_result=StringVar()
        
        self.entry_result = CTkEntry(self.frame_child_game,font=("Calibry",25),justify=CENTER,textvariable = self.text_result)
        self.button_save_result=CTkButton(self.frame_child_game,text="Дальше",command=self.next)        
        self.label_time = CTkLabel(self.frame_child_game,text="0.0",font = ("Areal",60))

        self.label_time.place(anchor=CENTER,relx=0.5,rely=0.2)
        self.label_hard_cft.place(anchor=CENTER,relx=0.38,rely=0.9)
        self.button_save_result.place(relx=0.7,rely=0.9)
        self.math_example.place(x=self.WIDTH/2,y=self.HEIGHT/2,anchor=CENTER)
        self.entry_result.place(anchor=CENTER,x=self.WIDTH/2,y=self.HEIGHT/2+100)
        
        self.entry_result.focus()
        
                
        #self.theme.pack(anchor="ce")  """ Not working :/""" 
        
        
        self.label_check_rank.pack(anchor=CENTER)
        self.age.pack()
        self.button_start.pack(anchor=SE,side=BOTTOM,fill='both')
        self.cb_theme.pack(anchor=NW)
        self.ask_results_button.pack(anchor=NW)
        

        self.tk.bind('<Return>',self.next_ent)

        self.notebook.pack()

        
        self.tk.mainloop()

               
    
    def change_theme(self):
        if self.var_theme.get():
            set_appearance_mode("dark")
            self.theme = "dark"
        else:
            set_appearance_mode("light")
            self.theme = "light"
    def next_ent(self,event):
            if self.step !=0:
                self.is_start_timer = True
                self.next()
            elif self.text_age != "":
                self.check_age()

    def check_age(self):
    
        self.age_user = self.text_age.get()

        if self.age_user.isdigit():

            self.age_user=int(self.age_user)

            if self.age_user >=0:
              
              self.start()

            else:
            	mb.showerror("","Возраст делжен быть положительным числом!")

    def start(self):

      self.frame_child_play.forget()
      self.frame_child_game.pack()
      self.step = 0
      self.is_start_timer = True
      Thread(target=self.print_timer1()).run()
      self.start_time = time.time()# Start timer
      
      
      self.next()
     
    
    def print_timer1(self):
        if self.is_start_timer:
            
            if not self.is_run_timer:            
               self.is_run_timer = True
               self.time_now = time.time()
               
            self.label_time.configure(text=f"{round(time.time()-self.time_now,1)}")
            
            if 0 <= round(time.time()-self.time_now,1) < 1+self.hard_cft+0.6:
                self.label_time.configure(text_color="light blue")

            elif 1+self.hard_cft+0.6 <= round(time.time()-self.time_now,1) < 2+self.hard_cft*3:
                self.label_time.configure(text_color="green")
            elif 2+self.hard_cft*3 <=round(time.time()-self.time_now,1) < 3+self.hard_cft*3:
                self.label_time.configure(text_color="yellow")
            elif 3+self.hard_cft*3<=round(time.time()-self.time_now,1) < 4+self.hard_cft*3:
                self.label_time.configure(text_color="orange")
            else:
                self.label_time.configure(text_color="red")


            self.tk.after(10,self.print_timer1)
            
        else:
           
           return None
    def number_generate(self,a,b,hard):
        
       
                    if hard == 0:                  
                        num1 = randint(a,b)*10
                        num2 = num1 + randint(1,9)*10
                    elif hard == 1:                       
                        num1 = randint(a,b)*10
                        num2 =randint(a,b)*10+randint(1,9)
                    else: 
                        num1,num2 = 0,0
                        while num1 == num2 and (num1%10==0 or num2%10==0): 
                            if randint(0,1):
                                x = (randint(a,b)+b)*10+randint(6,9)
                                num1 =randint(a,b)*10+randint(1,5)
                            else:
                                x = (randint(a,b)+b)*10+randint(1,5)
                                num1 =randint(a,b)*10+randint(6,9)
                            num2 = x-num1
                    #if num1 == num2 or num1>=1000 or num2>=1000:
                    #    ...#mb.showinfo("from generator", "")
                    #if num2<0:
                    #    num2 = num2
                    #if num1 == num2:
                    #    num2 = num2          
                    #if num2<0:
                    #    num2 = num2
                    #print(num1,num2,num2 <=0)
                    return [int(num1),int(num2)]
    def char_generate(self,n1,n2):
        char_t = choice(["+","-"])
        example = ""
        if self.age_user >=13:
            if  char_t == "-" and n1<n2:
                if int(str(n2)[1:]) < int(str(n1)[1:]): self.hard_cft = 2
                example = str(n2)+char_t+str(n1)
            elif char_t == "-" and n1>n2:
                if int(str(n1)[1:]) > int(str(n2)[1:]): self.hard_cft = 2
                example = str(n1)+char_t+str(n2)
            elif char_t == "+":
                example = str(n1)+char_t+str(n2)
        else:
            if  char_t == "-" and n1<n2:
                if n2< n1: self.hard_cft = 2
                example = str(n2)+char_t+str(n1)
            elif char_t == "-" and n1>n2:
                if n1 > n2: self.hard_cft = 2
                example = str(n1)+char_t+str(n2)
            elif char_t == "+":
                example = str(n1)+char_t+str(n2)
            else:
                raise Exception("CharGeneratorError ----> name example is not defined")
        
        return example
    def show_results(self):
        
        self.window = CTkToplevel()
        self.window.configure(bg="white")
        self.window.title("Результат")
        for i in self.all_results:
            print(self.all_results)
            CTkLabel(self.window,text=f"{self.all_results[i][0]}. {i} ваш ответ: {self.all_results[i][1]}; Правильный ответ: {self.all_results[i][2]}",text_color="green" if self.all_results[i][3] else "red",font=("Bold",20)).pack()
    def next(self):
        global all_results
        self.entry_result.focus()
        if self.text_result.get().isdigit():
            self.is_run_timer = False

        if 0 < self.step < self.num_examples and self.text_result.get().isdigit(): #We must save answer and show new math example
           # mb.showinfo("if",self.text_result.get().isdigit())
            self.is_start_timer = False
            
            if self.text_result.get().isdigit() and int(self.text_result.get())==self.result:
                self.entry_result.configure(fg_color="green")
            else:
                self.entry_result.configure(fg_color="red")
            self.entry_result.update()
            time.sleep(self.sleep_time)
            self.entry_result.configure(fg_color="white") if self.theme == "light" else self.entry_result.configure(fg_color="gray")
            self.true_or_false.append(int(self.text_result.get())==self.result if self.text_result.get().isdigit() else False)
            print(self.true_or_false)
            self.is_start_timer = True
            self.print_timer1()
            self.all_results[self.example] =[self.step,
                                             self.text_result.get(),
                                             self.result,
                                             int(self.text_result.get())==self.result] #step ; answer ; real result; True or False answer
            
            self.step += 1
            
            self.tk.title(self.step)
                        
            if self.age_user <=9:
                while self.now == self.example:
                    
                    n1 = randint(1,9)
                    n2 =randint(1,9)
                    char = choice(["+","-"])
                    if  char == "-" and n1<n2:
                        self.example = str(n2)+char+str(n1)
                    else:
                        self.example = str(n1)+char+str(n2)
                        
            elif 10 <= self.age_user <= 13:
                while self.now == self.example:
                    self.hard_cft = randint(0,2)
                    n1,n2=self.number_generate(30/10,90/10,hard=self.hard_cft)
                    self.example = self.char_generate(n1,n2)
            else:#elif self.step==0:
                while self.now == self.example:
                    self.hard_cft=randint(0,2)
                    n1,n2=self.number_generate(100/10,990/10,hard=self.hard_cft)
                    self.example = self.char_generate(n1,n2)

            self.now = self.example               
            self.math_example.configure(text=self.example)
            self.result = eval(self.example)
            self.entry_result.delete(0,END)
            self.label_hard_cft.configure(text=f"Сложность: {self.hard_cft+1}/3")
                
        elif self.step >= self.num_examples: # We must save last answer
            #mb.showinfo("elif1",self.text_result.get().isdigit())
            
            self.is_start_timer,self.is_run_timer = False,False
            if self.text_result.get().isdigit() and int(self.text_result.get())==self.result:
                self.entry_result.configure(fg_color="green")
            else:
                self.entry_result.configure(fg_color="red")
            self.entry_result.update()
            time.sleep(self.sleep_time)
            self.entry_result.configure(fg_color="white") if self.theme == "light" else self.entry_result.configure(fg_color="gray")
            self.all_results[self.example] =[self.step,
                                             self.text_result.get(),
                                             self.result,
                                             int(self.text_result.get())==self.result]
            self.entry_result.delete(0,END)
            self.true_or_false.append(int(self.text_result.get())==self.result) if self.text_result.get().isdigit() else self.true_or_false.append(False)
            
            self.end_time = time.time() # Stop timer
            
            
            self.frame_child_game.forget()
            self.frame_child_play.pack(fill='both',expand=True)
            self.age.delete(0,END)
            if self.ask_results:
                self.show_results()
                self.rank = Rank.start(self.num_examples,round(self.end_time-self.start_time-self.num_examples*self.sleep_time,1),self.true_or_false)
                self.window.destroy()
            self.__save_rank_to_file()
            
            self.true_or_false = []
            self.all_results = {}
            
            self.tk.title("Mathing")
            self.age.focus()
            self.step=0
        elif self.step == 0: # We mustn't save answer because this is the fisrt example
         #   mb.showinfo("elif2",self.text_result.get().isdigit())
            self.step += 1
            self.tk.title(self.step)
            
            if self.age_user <=9:
                    n1 = randint(1,9)
                    n2 =randint(1,9)                                       
                    self.example = self.char_generate(n1,n2)
            elif self.age_user <= 13:                   
                    self.hard_cft = randint(0,2)                    
                    n1,n2=self.number_generate(30/10,90/10,hard=self.hard_cft)                    
                    self.example = self.char_generate(n1,n2)
            else:                   
                    char = choice(["+","-"])                    
                    self.hard_cft = randint(0,2)                   
                    n1,n2=self.number_generate(100/10,990/10,self.hard_cft)        
                    self.example = self.char_generate(n1,n2)                   
            
            self.now = self.example       
            self.math_example.configure(text=self.example)
            self.result = eval(self.example)
            self.label_hard_cft.configure(text=f"Сложность: {self.hard_cft+1}/3")

    def __get_rank_file(self):
        try:
           with open("data/rank.txt", 'r') as file:
              read = file.read()
              return read if read != "" else "Сыргайте один раунд \nчтобы получить звание!"
        except:
              if not os.path.isdir("data"):
                 try:
                    os.mkdir("data")
                 except:
                    print("Unable to create dir")  
              try:
                 with open("data/rank.txt", 'w+') as file:
                      return "Сыргайте одну игру \nчто бы получить звание!"  
              except:
                      print("Unable to create rank file")                 
        
    def __save_rank_to_file(self):
        try:
            
            with open("data/rank.txt",'r+') as file:
                file.truncate()
                file.write(self.rank)
                self.label_check_rank.configure(text=self.rank)

        except FileNotFoundError:   mb.showerror("Ошибка","Необходимый файл rank не найден")
        
    
if __name__ == '__main__':
    Main("Single")
