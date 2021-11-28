import os
import psutil
import tkinter as tk # 导入tkinter库
from tkinter import messagebox
from tkinter import filedialog

file = open("./bin/Path.txt", "r", encoding='UTF-8')

Path = file.readline()

file.close()


def findprocess(processname):
    pl = psutil.pids()
    for pid in pl:
        if psutil.Process(pid).name() == processname:
            return True
    else:
        return False


def outofcontrol():
    if (findprocess('StudentMain.exe')):
        os.system('taskkill /f /im StudentMain.exe')
        messagebox.showinfo("提示", "脱控成功")
    else:
        messagebox.showwarning(title='错误', message='当前未运行极域电子教室程序！')

def connect():
    try:
        os.startfile(Path)
        # r'C:\Program Files (x86)\Mythware\极域电子教室软件 v4.0 2015 豪华版\StudentMain.exe'
        # print(Path)
        messagebox.showinfo("提示", "连接成功")
    except:
        messagebox.showwarning(title='错误', message='未在指定文件夹找到极域电子教室主程序！')
        # print(Path)


def path():
    global Path
    # wd_path = tk.Tk()
    wd_path = tk.Toplevel()
    wd_path.title("设置路径")
    wd_path.geometry('300x100')
    wd_path.iconbitmap('./img/favicon_new.ico')
    lab = tk.Label(wd_path, text='请选择极域电子教室的路径:', font=('Arial', 10))
    lab.place(x=0, y=0)
    var = tk.StringVar()
    ent = tk.Label(wd_path, bg="white", height="2", width="29", font=('Arial', 10), textvariable=var)
    ent.place(x=0, y=25)
    btu1 = tk.Button(wd_path, text=" 取消 ", command=wd_path.destroy)

    def path_get():
        global Path
        Path = str(var.get())
        # print(Path)
        wd_path.destroy()

    def findfile():
        window = tk.Toplevel()
        window.withdraw()
        # Folderpath = filedialog.askdirectory()
        filepath = filedialog.askopenfilename()
        # print('Folderpath:', Folderpath)
        # print('Filepath:', Filepath)
        lists = list(filepath)
        for i in range(len(filepath)):
            if lists[i] == '/':
                lists[i] = "\\"
        list2 = [str(i) for i in lists]
        filepaths = ''.join(list2)
        var.set(filepaths)
        file = open("./bin/Path.txt", "w")
        file.write(filepaths)

    btu = tk.Button(wd_path, text="选择路径", command=findfile)
    btu.place(x=240, y=28)
    btu2 = tk.Button(wd_path, text=" 确定 ", command=path_get)

    btu1.place(x=50, y=70)
    btu2.place(x=205, y=70)
    var.set(Path)
    wd_path.mainloop()


root = tk.Tk()

root.title('Leave Control V1.1')

root.geometry('300x160')

root.iconbitmap('./img/favicon_new.ico')

menubar = tk.Menu(root)

settingmenu = tk.Menu(menubar, tearoff=0)

menubar.add_cascade(label='设置', menu=settingmenu)

settingmenu.add_command(label='路径', command=path)
submenu = tk.Menu(settingmenu, tearoff=0)
settingmenu.add_cascade(label='语言', menu=submenu, underline=0)
submenu.add_command(label='中文')
# settingmenu.add_command(label='语言')
settingmenu.add_command(label='个性化')
settingmenu.add_separator()  # 添加一条分隔线
settingmenu.add_command(label='退出', command=root.quit)  # 用tkinter里面自带的quit()函数

helpmenu = tk.Menu(menubar, tearoff=0)

menubar.add_cascade(label='帮助', menu=helpmenu)

helpmenu.add_command(label='指南')
helpmenu.add_command(label='检查更新')
helpmenu.add_separator()
helpmenu.add_command(label='关于')

root.config(menu=menubar)

btu1 = tk.Button(root, text="一键脱控", command=outofcontrol)

btu2 = tk.Button(root, text="一键连接", command=connect)

btu1.place(x=80, y=50)
btu2.place(x=170, y=50)

root.mainloop()