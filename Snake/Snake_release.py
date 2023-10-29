
from tkinter import *
from random import randrange,randint as ri
from random import randint
from functools import partial
from tkinter.messagebox import showinfo
from threading import Thread
import menuu
import sys,os
#from sums import summ

class app:
    def __init__(self):
        """

        :rtype: object

        """
        self.snake_list = []
        self.apple_list = {}
        self.coords = []
        

        #получает скорость 
        try:
            with open("option.txt",'r+') as file:
                reading = file.read()
                if reading == "":
                    file.write("50")
                    speed = 50
                else:   speed = reading
        except FileNotFoundError:
            with open("option.txt",'w+') as file:
                file.write("50")
                speed = 50

        #получаем размер окна
        with open("window_config.txt") as file:
            self.size = file.read()
        self.FPS = speed
        self.FPS = int(self.FPS)

        global  transform,is_upgrade,one_item,step
        self.super_apple = False # если True то надо создать яблако
        self.is_apple=False #имеется ли яблоко на холсте
        self.i = 0#счетаем время для исчездновения яблока
        self.rand_time = 0#рандомный период отрисовки
        step = 20 #шаг
        is_upgrade = False #надо ли увеличивать
        transform = 1 # направление
        one_item = True # один или несколько элементов
        self.a = False#для шара
        
        self.tk = Tk()
        self.tk.geometry("{}x{}".format(self.size,self.size))#("1200x650")
        self.tk['bg'] = "black"
        self.tk.resizable(False, False)
        self.tk.title("Snake game")
        self.tk.wm_attributes("-topmost",1)
        self.tk.focus_force()

        #смотрим какой рекорд

        try:
            with open("data.txt",'r') as file:
                self.record = int(file.read())
        except FileNotFoundError:
            with open("data.txt", 'w+') as file:
                file.write("0")
                self.record = 0
        #смотрим надо ли увеличивать скорость
        with open("speed_add.txt") as file:
            self.check_speed_add = file.read()

        self.canvas = Canvas(self.tk, width=self.size, height=self.size, background="black")
        self.canvas.pack()
        
        temp_place = ri(0,int(self.size)-40)
        self.oval = self.canvas.create_oval(temp_place,temp_place,temp_place+30,temp_place+30,fill="white")
        self.head = self.canvas.create_rectangle(200, 200, 220, 220, fill="red")
        self.snake_list.append(self.head)
        
       # self.label = Label(self.tk,text="Score: 0",font = ('areal', 20),bg="black",fg='Yellow')#,anchor=NE)
       # self.label.place(x=int(self.size)-200,y=10)
        #self.label.lift()
        
        
        self.create_apple()

        self.tk.bind("w", self.in_up)  # 1-вверх 2-вниз 3-влево 4-вправо
        self.tk.bind("s", self.in_down)
        self.tk.bind("a", self.in_left)
        self.tk.bind("d", self.in_right)
      #  Thread(target=self.ball)
        self.moving()
        self.ball()
        # self.main()


        self.tk.mainloop()
       
    def ball(self):
	
        x0, y0, x1, y1 = self.canvas.coords(self.head)
                                    
        check = self.canvas.find_overlapping(x0, y0, x1, y1)
     #   if len(check)>1:
          #  showinfo("",self.head)
        #print(check)
        try:
            if 1 in check and 2 in check:#self.head in check[1:]:# or 4 in check:
                if len(self.snake_list) == 1:
                    self.FPS=1000
                
                    showinfo("","Game over")
                    self.tk.destroy()
                    menuu.main()
               #     self.tk.destroy()
                    return None
                
                

                self.canvas.delete(self.snake_list[len(self.snake_list)-1])
                del self.snake_list[len(self.snake_list)-1]
        except IndexError:   pass
            
        if self.canvas.coords(self.oval)[0] <= 0.0:
            self.xb*=-1
            #self.yb *=1
            self.a = True
            #print(self.canvas.coords(self.oval))
            #self.canvas.coords(self.oval)[0]
        elif self.canvas.coords(self.oval)[1] <= 0:
            #self.xb*=1
            #print(self.canvas.coords(self.oval))
            self.yb *=-1#-2,0
            self.a = True
            
        elif self.canvas.coords(self.oval)[2] >= int(self.size):
            self.xb*=-1
            #self.yb*=1
            #print(self.canvas.coords(self.oval))
            self.a = True
        if self.canvas.coords(self.oval)[3] > int(self.size):
            #self.xb*=1
            #print(self.canvas.coords(self.oval))
            self.yb*=-1
            self.a = True

        #если не двигали    
        if not self.a:
            print('HOP RAZVAROT')
            self.xb=1#*0.25
            self.yb=-1#*0.25
        self.canvas.move(self.oval,self.xb,self.yb)
        self.tk.update()
      #  showinfo()
        self.tk.after(1,self.ball)
    def in_up(self,event):
        global transform;
        if(len(self.snake_list)>1):
            if(transform!=2): transform = 1
        else:   transform = 1
    def in_down(self,event):
        global transform;
        if (len(self.snake_list) > 1):
            if(transform!=1): transform = 2
        else:   transform = 2
    def in_left(self,event):
        global transform
        if (len(self.snake_list) > 1):
            if(transform!=4):   transform = 3
        else:   transform = 3
    def in_right(self,event):
        global transform;
        if (len(self.snake_list) > 1):
            if(transform!=3):   transform = 4
        else:   transform = 4
    
    def create_apple(self):
        
        if not self.is_apple:   self.i = 0
       
        if not self.is_apple:
            rand = randint(1,3) #шанс
            if rand == 2:
                self.rand_time = randint(30,60) #рандомный период отрисовки
                self.super_apple = True
            print(rand)
        self.x, self.y = randrange(0, int(self.size)-200, step), randrange(0, int(self.size)-100,step)
       
        for cord in self.coords:

            while [self.x,self.y,self.x+step,self.y+step] == cord:
                self.x, self.y = randrange(0, 370, step), randrange(0, 370, step)
            continue

        try:

            self.canvas.delete(self.apple_list["default"])
            

            #self.apple_list = {}

            self.apple_list["default"] = self.canvas.create_oval(self.x, self.x+step,self.y, self.x + step, self.y + step, fill="red")
            if self.super_apple:
                
                self.x, self.y = randrange(0, int(self.size)-200, step), randrange(0, int(self.size)-100,step)
                self.apple_list["super"] = self.canvas.create_oval(self.x, self.y, self.x + step, self.y + step, fill="blue")
                
                self.is_apple = True
        except Exception as e:

           # self.apple_list = {}
            self.apple_list["default"] = self.canvas.create_oval(self.x, self.y, self.x + step, self.y + step, fill="red")
            if self.super_apple and not self.is_apple:
                self.x, self.y = randrange(0, int(self.size)-200, step), randrange(0, int(self.size)-100,step)
                self.apple_list["super"] = self.canvas.create_oval(self.x, self.y, self.x + step, self.y + step, fill="blue")
                self.is_apple = True

               #выводим на название окна счет
            if(len(self.snake_list) > 1):
                self.tk.title(f"Score: {len(self.snake_list)-1}")#self.label.configure(text=f"Score: {len(self.snake_list)-1}")
        
        self.tk.update()


    def moving(self):
        global is_upgrade,one_item
        

        if self.is_apple:
            
            self.i += 1
            self.tk.title(f"{self.i}/{self.rand_time}")
        else:
            i=0
        #else:
         #   self.i = 0
        try:
            if self.i == self.rand_time:
                #del self.apple_list["super"]
                self.canvas.delete(self.apple_list["super"])
                self.is_apple = False
                self.super_apple = False
                self.tk.title(f"Score: {len(self.snake_list)-1}")
        except KeyError:    pass
        
        if one_item:
            try:
                if(transform==1):
                    try:
                            if [self.canvas.coords(self.head)[0], self.canvas.coords(self.head)[1] - step, self.canvas.coords(self.head)[2],
                                self.canvas.coords(self.head)[3] - step] == self.canvas.coords(self.apple_list["default"]):
                                self.snake_upgreater()
                            elif [self.canvas.coords(self.head)[0], self.canvas.coords(self.head)[1] - step, self.canvas.coords(self.head)[2],
                                self.canvas.coords(self.head)[3] - step] == self.canvas.coords(self.apple_list["super"]):
                                self.super_apple = True
                    except KeyError:    pass
                elif (transform == 2):
                    try:
                        if [self.canvas.coords(self.head)[0], self.canvas.coords(self.head)[1] + step, self.canvas.coords(self.head)[2],
                            self.canvas.coords(self.head)[3] + step] == self.canvas.coords(self.apple_list["default"]):
                            self.snake_upgreater()
                        elif[self.canvas.coords(self.head)[0], self.canvas.coords(self.head)[1] + step, self.canvas.coords(self.head)[2],
                            self.canvas.coords(self.head)[3] + step] == self.canvas.coords(self.apple_list["super"]):
                           self.super_apple = True
                    except KeyError:    pass
                            
                elif (transform == 3):
                    try:
                        if [self.canvas.coords(self.head)[0] - step, self.canvas.coords(self.head)[1], self.canvas.coords(self.head)[2] - step,
                            self.canvas.coords(self.head)[3]] == self.canvas.coords(self.apple_list["default"]):
                            self.snake_upgreater()
                        elif[self.canvas.coords(self.head)[0] - step, self.canvas.coords(self.head)[1], self.canvas.coords(self.head)[2] - step,
                            self.canvas.coords(self.head)[3]] == self.canvas.coords(self.apple_list["super"]):
                            self.super_apple = True
                    except KeyError:    pass
                elif (transform == 4):
                    try:
                        if [self.canvas.coords(self.head)[0] + step, self.canvas.coords(self.head)[1], self.canvas.coords(self.head)[2] + step,
                            self.canvas.coords(self.head)[3]] == self.canvas.coords(self.apple_list["default"]):
                            self.snake_upgreater()
                        elif [self.canvas.coords(self.head)[0] + step, self.canvas.coords(self.head)[1], self.canvas.coords(self.head)[2] + step,
                            self.canvas.coords(self.head)[3]] == self.canvas.coords(self.apple_list["super"]):
                            self.super_apple = True
                    except KeyError:    pass
                is_upgrade = False
                
            except IndexError:
                pass

        self.check_coords()
        if is_upgrade:
            #is_upgrade = False
            self.snake_upgreater()

        if len(self.snake_list) > 1:
            if one_item:
                one_item = False

            for i in range(len(self.snake_list) - 1, 0, -1):
                self.canvas.coords(self.snake_list[i], self.canvas.coords(self.snake_list[i - 1]))
        
        for i in range(len(self.snake_list)):
            self.coords.append(self.canvas.coords(self.snake_list[i]))
        
        if transform == 1:
           # if len(self.snake_list) > 1:
            self.Snakex , self.Snakey= 0,-step
            self.canvas.move(self.head, 0, -step)
            print(self.Snakex, self.Snakey,self.FPS)
        elif transform == 2:
            self.Snakex, self.Snakey = 0, step
            self.canvas.move(self.head, self.Snakex, self.Snakey)
            print(self.Snakex, self.Snakey,self.FPS)
        elif transform == 3:
            self.Snakex, self.Snakey = -step, 0
            self.canvas.move(self.head, self.Snakex, self.Snakey)
            print(self.Snakex, self.Snakey,self.FPS)
        elif transform == 4:
            self.Snakex, self.Snakey = step, 0
            self.canvas.move(self.head,self.Snakex, self.Snakey)
            print(self.Snakex, self.Snakey,self.FPS)


        self.tk.update()
  
        self.canvas.after(int(self.FPS), lambda: self.moving())

    def check_coords(self):
        # print(self.coords)
        if self.canvas.coords(self.head)[2] > int(self.size) or self.canvas.coords(self.head)[0] < 0 or self.canvas.coords(self.head)[1] < 0 or self.canvas.coords(self.head)[3] > int(self.size):
            self.tk.wm_attributes("-topmost",0)	
            if len(self.snake_list)-1 > self.record:
                os.remove("data.txt")

                with open("data.txt", 'w+') as file:


                        file.write(str(len(self.snake_list)-1))
                        self.tk.wm_attributes("-topmost",0)
                        showinfo("Ура!", f"Вы побили предыдущий рекорд на {(len(self.snake_list)-1)-self.record} очка(ов)")

            showinfo(""," Змейка выползла \n за границы окна")
            self.tk.destroy()
            menuu.main()
            return None
        for i in range(len(self.snake_list)-1):
            if i > 1 and len(self.snake_list) > 3:
                if self.canvas.coords(self.snake_list[0]) == self.canvas.coords(self.snake_list[i]):
                        
                    if len(self.snake_list)-1 > self.record:
                            os.remove("data.txt")

                            with open("data.txt", 'w+') as file:
                                file.write(str(len(self.snake_list)-1))
                                self.tk.wm_attributes("-topmost",0)
                                showinfo("Ура!",
                                         f"Вы побили предыдущий рекорд на {(len(self.snake_list)-1) - self.record} очка(ов)")
                    self.tk.wm_attributes("-topmost",0)
                    showinfo("","Змейка самоубилась")
                    self.tk.destroy()
                    menuu.main()
                    return None
        global is_upgrade
       # try:
        if self.is_apple: #and not self.super_apple:
            
            if (self.canvas.coords(self.head) == self.canvas.coords(self.apple_list["super"])):
                self.super_apple = False
                self.canvas.delete(self.apple_list["super"])
                self.is_apple = False
                self.FPS /=0.8
                self.tk.title(f"Score: {len(self.snake_list)-1}")
       # except KeyError:    showinfo("","weef")
                
                
        if(self.canvas.coords(self.head) == self.canvas.coords(self.apple_list["default"])):
            #global is_upgrade

            if (not one_item ):
                is_upgrade = True
            
        self.tk.update()

    def snake_upgreater(self):
        global one_item,is_upgrade
        one_item = False
        self.snake_list.append(self.canvas.create_rectangle(self.coords[len(self.snake_list) - 1][0],
                                                            self.coords[len(self.snake_list) - 1][1],
                                                            self.coords[len(self.snake_list) - 1][2],
                                                            self.coords[len(self.snake_list) - 1][3], fill='green'))
        is_upgrade = False
        if self.check_speed_add == "1":
            self.FPS *=0.97
        else:   print(self.check_speed_add)
        self.create_apple()
        self.tk.update()

if __name__ == '__main__':
    print(app())
