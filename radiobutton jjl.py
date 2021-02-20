import tkinter
from tkinter import *

username = 'admin'
password = 'admin'

class LoginFrame(tkinter.Frame):

    def __init__(self, master=None):
        # memanggil kontruktor kelas induk (tkinter.Frame)
        tkinter.Frame.__init__(self, master)
        self.grid()
        self.utama()
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(1, weight=1)


    def utama(self) :

        # self['background'] = "#4a3933"
        
# jenis kelamin
        self.JK = tkinter.Label(self, text="Jenis Kelamin      :")

        

        # self.JK['fg'] = '#faf3e0'
        # self.JK['bg'] = '#4a3933'
        self.JK['font'] = 'Helvetica 12 bold'
        self.JK.grid(row=0, column=0, sticky=W)
        self.jkl = Radiobutton(self, highlightcolor='#161d6f')
        self.jkl['text'] = 'Laki-Laki'
        self.jkl.grid(row=0, column=1,sticky=tkinter.W )

def main():
# membuat kelas demo frame
    app = LoginFrame()
    app.master.title("Login Frame")
    app.master.grid_rowconfigure(0, weight=1)
    # app.master['background'] = "#4a3933"
    app.master.grid_columnconfigure(0, weight=1)
    app.mainloop()
# memanggil fungsi
if __name__ == "__main__":
    main()