from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import os
from mutagen.mp3 import MP3
from tkinter.messagebox import showerror 
from threading import Thread
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1' # To pygame dont write "Hello from the pygame community."

from pygame import mixer
mixer.init()

class App():

  def __init__(self):

    self.button_play_status = False #if False: button_play text=➮ elif True: button_play text = ||
    self.music_info = False #if False music dont play ; if True: music play
    self.colse_to_thread = False #if True: we most colse the window

    self.tk = Tk()
    self.tk.protocol("WM_DELETE_WINDOW", self._on_close_TK)
    self.button_play = Button(text="➮",command=self.play,width=7,height=3)
    self.button_stop = Button(text="▉",command=self.stop,width=7,height=3)

    val = IntVar()

    self.volume_regular = Scale(orient=VERTICAL, length=100, from_=100, to=1,command=self.volume_control)

    self.time_var = IntVar()

    self.time_progress = ttk.Progressbar(orient="horizontal",length=150,variable=self.time_var,mode="determinate")
  

    self.time_progress.grid(row=2,column=2)
    self.button_play.grid(row=1,column=1) 
    self.button_stop.grid(row=1,column=2)
    self.volume_regular.grid(row=1,column=3)

    self.tk.mainloop()

  def stop(self):

    if self.music_info:
    
      mixer.music.stop()
      self.button_play.configure(text='➮')
      self.music_info = False
      self.button_play_status = False

  def play(self):

    if not self.button_play_status:

      self.button_play_status = True

      if not self.music_info:     

        self.path_sound = filedialog.askopenfilename()

      

        if self.path_sound != "": 

            if os.path.exists(self.path_sound):

            
              if os.path.splitext(self.path_sound)[1] != '.mp3':

                showerror("FormatError","File most have got the format: '.mp3'")

                self.button_play_status = False
                self.music_info = False

              else:

                mixer.music.load(self.path_sound)
                sound = MP3(self.path_sound)
                self.sound_length = sound.info.length
                
                
                self.time_progress['maximum']=round(self.sound_length)
                mixer.music.set_volume(self.volume_regular.get()/100)
                mixer.music.play()
                self.time_progress.start(1000)
                self.music_info = True
                Thread(target=self.thread_Progressbar).start()

                


            else:   
                   
              showerror("Error","File is not found!")

              self.button_play_status = False

            if self.music_info:

              self.button_play.configure(text="||")

      else:

        mixer.music.unpause()
        self.time_progress.start(1000)
        self.button_play.configure(text="||")
        mixer.music.set_volume(self.volume_regular.get()/100)

    else:

      self.button_play_status = False
      self.music_info=False
      mixer.music.pause()
      self.time_progress.stop()
      self.time_var.set(0)
      self.button_play.configure(text='➮')

  def volume_control(self,val):

    if self.music_info:

      mixer.music.set_volume(self.volume_regular.get()/100)


  def time_control(self):
    ...
  def thread_Progressbar(self):
    while True:
      print(f"Bar:{self.time_progress['value']},  Time:{self.sound_length};{round(self.sound_length)}")
      if self.time_progress['value'] == round(self.sound_length)-1 or not self.music_info:
        self.time_progress.stop()
        self.time_var.set(0)
        
        self.button_play.configure(text='➮')
        self.music_info=False
        self.button_play_status = False

        break

      if self.colse_to_thread:
        break
    
    exit()
  def _on_close_TK(self):
    if self.music_info:
      mixer.music.stop()
    self.colse_to_thread = True
    self.tk.destroy()
if __name__ == '__main__':
  App()
  
  
