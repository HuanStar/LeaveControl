import os
import tkinter as tk
from tkinter.messagebox import *
 
root = tk.Tk()
root.title('脱离控制 1.0')
root.geometry('240x70')
def tuokong():
    os.system('taskkill /f /im StudentMain.exe')
    tk.messagebox.showinfo( "提示", "脱控成功")

def lianjie():
    os.startfile(r'C:\Program Files (x86)\Mythware\极域电子教室软件 v4.0 2015 豪华版\StudentMain.exe')
    tk.messagebox.showinfo( "提示", "连接成功")
 
B = tk.Button(root, text ="一键脱控", command = tuokong)

A = tk.Button(root, text ="一键连接", command = lianjie)

B.pack()
A.pack()
root.mainloop()
#os.startfile(r'C:\Program Files (x86)\Mythware\极域电子教室软件 v4.0 2015 豪华版\StudentMain.exe')

