import tkinter as tk
from tkinter import *
import os
import tempfile
import shutil
import winshell
class app():
    def __init__(self, master):
        self.master = master
        master.title("Hızlan")
        master.config(background="white")
        master.geometry("215x30")
        self.createButtons()
        self.userTemp = tempfile.gettempdir()
        self.sysTemp = r"\Windows\Temp"

    def createButtons(self):
        cleanBtn = Button(self.master, text="Temizle", command=self.clean)
        cleanBtn.pack()
        cleanBtn.focus_set()
    
    def cleanUserTemp(self):
        os.chdir(self.userTemp)
        print(os.getcwd())
        everythink = os.listdir()
        silinenklasör, silinendosya = 0, 0
        silinemeyenklasör, silinemeyendosya = 0, 0
        for think in everythink:
            if os.path.isdir(think):
                try:
                    shutil.rmtree(think)
                    print("klasör silindi: " + think)
                    silinenklasör += 1
                except PermissionError:
                    print("bir izin sorunu var: " + think)
                    silinemeyenklasör += 1
            elif os.path.isfile(think):
                try:
                    os.remove(think)
                    print("dosya silindi: " + think)
                    silinendosya += 1
                except PermissionError:
                    print("bir izin sorunu var: "+ think)
                    silinemeyendosya += 1
        if silinenklasör > 0:
            print(str(silinenklasör) + " tane klasör silindi")
        if silinendosya > 0:
            print(str(silinendosya) + " tane dosya silindi")
        if silinemeyenklasör > 0:
            print(str(silinemeyenklasör) + " tane klasör silinemedi")
        if silinemeyendosya > 0:
            print(str(silinemeyendosya) + " tane dosya silinemedi")
        print("UserTemp is cleaned", end='\n')

    def cleanSysTemp(self):
        os.chdir(self.sysTemp)
        print(os.getcwd())
        everythink = os.listdir()
        silinenklasör, silinendosya = 0, 0
        silinemeyenklasör, silinemeyendosya = 0, 0
        for think in everythink:
            if os.path.isdir(think):
                try:
                    shutil.rmtree(think)
                    print("klasör silindi: " + think)
                    silinenklasör += 1
                except PermissionError:
                    print("bir izin sorunu var: " + think)
                    silinemeyenklasör += 1
            elif os.path.isfile(think):
                try:
                    os.remove(think)
                    print("dosya silindi: " + think)
                    silinendosya += 1
                except PermissionError:
                    print("bir izin sorunu var: "+ think)
                    silinemeyendosya += 1
        if silinenklasör > 0:
            print(str(silinenklasör) + " tane klasör silindi")
        if silinendosya > 0:
            print(str(silinendosya) + " tane dosya silindi")
        if silinemeyenklasör > 0:
            print(str(silinemeyenklasör) + " tane klasör silinemedi")
        if silinemeyendosya > 0:
            print(str(silinemeyendosya) + " tane dosya silinemedi")
        print("SysTemp is cleaned", end='\n')
            
    def cleanRecycleBin(self):
        if list(winshell.recycle_bin()):
            winshell.recycle_bin().empty(confirm=False, show_progress=True, sound=False)
            print("Geri Dönüşüm Kutusu temizlendi", end='\n')
        else:
            print("Geri Dönüşüm Kutusu zaten temiz", end='\n')
        

    def clean(self):

        self.cleanUserTemp()
        self.cleanSysTemp()
        self.cleanRecycleBin()

pncr = tk.Tk()
app = app(pncr)
pncr.mainloop()
