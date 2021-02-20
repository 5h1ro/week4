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

        self['background'] = "#ccf2f4"
        
# lulusan
        # membuat horizontal scroll
        self.xScroll = tkinter.Scrollbar(self, orient=HORIZONTAL)
        # mengatur letak croll
        self.xScroll.grid(row=1, column=1, sticky=EW)
        # membuat vertikal scroll
        self.yScroll = tkinter.Scrollbar(self, orient=VERTICAL)
        # mengatur letak croll
        self.yScroll.grid(row=0, column=2, sticky=NS)

        
        self.Lulusan = tkinter.Label(self, text="Lulusan                  :")
        self.Lulusan['fg'] = '#0a043c'
        self.Lulusan['bg'] = '#ccf2f4'
        self.Lulusan['font'] = 'Helvetica 12 bold'
        self.Lulusan.grid(row=0, column=0, sticky=W)
        self.lulusan = Listbox(self)
        # merubah bg
        self.lulusan['bg'] = '#a4ebf3'
        # merubah ukuran border
        self.lulusan['bd'] = '2px' 
        # cursor
        self.lulusan['cursor'] = 'plus'
        # merubah font
        self.lulusan['font'] = 'Helvetica' 
        # merubah warna fg atau text
        self.lulusan['fg'] = '#0a043c' 
        # merubah height
        # set nama relief
        self.lulusan['relief'] = 'sunken' 
        self.lulusan['height'] = '2'
        # merubah selectbackground color
        self.lulusan['selectbackground'] = '#16c79a'
        # selectmode
        self.lulusan['selectmode'] = 'single'
        # merubah width
        self.lulusan['width'] = '7'
        # set seeder  
        self.lulusan.insert(1, "Sekolah Dasar")  
        self.lulusan.insert(2, "Sekolah Menengah Pertama")  
        self.lulusan.insert(3, "Sekolah Menengah Atas")  
        self.lulusan.insert(4, "Diploma 3")  
        self.lulusan.insert(5, "Strata 1")
        # membuat grid
        self.lulusan['justify'] = 'left'

        
        self.lulusan['xscrollcommand'] = self.xScroll.set
        self.lulusan['yscrollcommand'] = self.yScroll.set

        self.lulusan.grid(row=0, column=1, sticky=W)

        self.xScroll['command'] = self.lulusan.xview
        self.yScroll['command'] = self.lulusan.yview


# submit


        self.submit = Button(self)
        self.submit['text'] = 'Submit'
        # merubah bg
        self.submit['bg'] = '#16c79a'
        # merubah ukuran border
        self.submit['bd'] = '3px'
        # merubah warna fg atau text
        self.submit['fg'] = '#91091e' 
        # merubah font
        self.submit['font'] = 'Helvetica' 
        # merubah font
        self.submit['justify'] = 'right'
        # merubah width
        self.submit['width'] = '20'
        # set nama variable
        self.submit['relief'] = 'raised' 
        # membuat button berbeda saat di tekan
        self.submit['activebackground'] = '#d3e0ea' 
        # membuat teks berbeda saat di tekan
        self.submit['activeforeground'] = '#ef4f4f'
        # membuat grid
        self.submit.grid(row=2, column=0, columnspan=2)


def main():
# membuat kelas demo frame
    app = LoginFrame()
    app.master.title("Login Frame")
    app.master.grid_rowconfigure(0, weight=1)
    app.master['background'] = "#ccf2f4"
    app.master.grid_columnconfigure(0, weight=1)
    app.mainloop()
# memanggil fungsi
if __name__ == "__main__":
    main()