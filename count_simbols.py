try:
	from tkinter import *
	from tkinter.messagebox import showinfo as show, askquestion as ask
	import sys
	import keyboard
	# from bs4 import BeautifulSoup
	from math import trunc
	from threading import Thread
	from functools import partial 
	import time
	import os
	# import random
	# import requests
	module = True
except ModuleNotFoundError:
	try:
		show("ошибка","Не найдена одна или несколько необходимых библиотек")
	except:
		print("Не найдена одна или несколько необходимых библиотек")
	module = False
global i,speed,text1,text2,text3
speed,i = 0,1
text1="""По небу бежали весёлые тучки. Они присели у леса. Полил тёплый грибной дождь.
Дождик закончился. Облака плыли дальше. Это были уже белые лошадки. Они цокали копытами. \nГривы у лошадей белые и кудрявые.
 Под ногами лошадей белое море. \nГребни волн прыгали, и лошади плыли по небу."""
text2="""Яркими цветами у дома пылал куст. Это был шиповник. Его посадили бабушка Настя и внук Антон.
Хороши на шиповнике белые и розовые цветы. \nШипы тоже хороши и колки. Наша кошка Пушинка тронула лапкой ветку. Стало больно. Кошка протянула мне лапку. Я вытащил занозу. Кошка лизала ранку."""
text3="""Лиля и Владик гнали корову Василиску на луг. На лугу летом хорошо!
За селом они прошли чудесную рощу. Лучи солнышка дарили земле свет и тепло. \nЛуговая трава была высокая. Бабочка перелетала с цветка на цветок. На васильках грозно гудел шмель. Кого он пугал? Корову Василиску?"""
stoprun = True
class App:
	def __init__(self,text_num):
		self.tk = Tk()
		self.tk['bg'] = 'white'
		# self.main_frame = Frame(self.tk)
		self.get_text_label = StringVar()
		try:
			match(text_num):
				case 1:
					Label(self.tk,text=text1).pack()
				case 2:
					Label(self.tk,text=text2).pack()
				case 3:
					Label(self.tk,text=text3).pack()
		except:
			print("Ошибка в инструкции 'match/case'\nобновите python что бы исправить")
		self.get_text = StringVar()
		self.text = Text(self.tk)
		self.text.pack()
		keyboard.add_hotkey('Ctrl + W', self.start_process)
		keyboard.add_hotkey('Ctrl + Q', self.info)
		# self.main_frame.pack()
		self.tk.mainloop()
	def start_process(self):
		# if(event.keycode == 87):
		new_process = Thread(target=self.processing)
		new_process.start()
	def info(self):
		# if(event.keycode == 81):
		global run
		run = False
		show("Скорость набора",f"{trunc(speed)} символов в сек\n{trunc(speed*60)} символов в мин ")	
		try:
			self.tk.destroy()
		except:	pass
	def processing(self):
		os.system('cls')
		# self.text.delete('1.0',END) 
		global i,speed
		i,speed= 1,0
		run = True
		while run:
		
			time.sleep(1)
			print(speed)
			try:
				speed = trunc(len(self.text.get("1.0",END))) / i
				i += 1
			except:	print(speed)
			
			#break	
			return 1
class Menu:
	def __init__(self):
		self.tk1 = Tk()
		self.tk1['bg'] = 'black'
		Button(text="Текст 1",font=('Blod',15),bg='black',fg='white',width=40,height=10,command=partial(App,1)).grid(row=1,column=1)
		Button(text="Текст 2",font=('Blod',15),bg='black',fg='white',width=40,height=10,command=partial(App,2)).grid(row=2,column=1)
		Button(text="Текст 3",font=('Blod',15),bg='black',fg='white',width=40,height=10,command=partial(App,3)).grid(row=3,column=1)
		Button(text="Правила",font=('areial',15),width=50,height=10,bg='black',fg='white',command=partial(show,"правила","Заходишь в нужный текст,\nпо готовности нажимаешь сочетание Control-w. Когда дописал,\nнажимаешь сочетание Control-q")).grid(row=1,column=2)
		Label(text="Если что ,\nнад интерфейсом не заморачивался",font=("areial",20),bg='black',fg='white').grid(row=2,column=2)
		Button(text="Выход",font=('areial',15),width=50,height=10,bg='black',fg='white',command=sys.exit).grid(row=3,column=2)
		self.tk1.mainloop()
if __name__ == '__main__':
	if(module):
		if(sys.version_info<(3,10,)):
			if  (ask("предупреждение",f"Приложение написано на версии 3.10.4, \nвозможны проблемы.\nПродолжить?") == "yes"):	Menu()
		else:	Menu()
