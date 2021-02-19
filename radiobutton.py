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
        
# jenis kelamin

        self.JK = tkinter.Label(self, text="Jenis Kelamin      :")
        
        self.JK['fg'] = '#0a043c'
        self.JK['bg'] = '#ccf2f4'
        self.JK['font'] = 'Helvetica 12 bold'
        self.JK.grid(row=0, column=0, sticky=W)
        self.jkl = Radiobutton(self, command=lambda:self.JK.destroy)
        # merubah ketika di klik
        self.jkl['activebackground'] = '#f1d1d0'
        self.jkl['activeforeground'] = '#16c79a'
        self.jkl['anchor'] = E
        self.jkl['bg'] = '#ccf2f4'
        self.jkl['borderwidth'] = '10px'
        self.jkl['cursor'] = 'plus'
        self.jkl['font'] = 'Helvetica' 
        self.jkl['fg'] = '#0a043c'
        self.jkl['height'] = '2'
        # self.jkl['justify'] = 'left'
        self.jkl['padx'] = 50
        self.jkl['pady'] = 10
        self.jkl['relief'] = 'groove'
        self.jkl['text'] = 'Laki-Laki'
        self.jkl['textvariable'] = 'jkl'
        self.jkl['variable'] = 'Laki-Laki'
        # merubah font
        self.jkl.grid(row=0, column=1,sticky=tkinter.W )

        self.jkw = Radiobutton(self)
        self.jkw['text'] = 'Wanita'
        self.jkw['fg'] = '#0a043c'
        self.jkw['bg'] = '#ccf2f4'
        self.jkw['textvariable'] = 'jkw'
        self.jkw['variable'] = 'Wanita'
        # merubah font
        self.jkw['font'] = 'Helvetica' 
        # merubah ketika di klik
        self.jkw['activebackground'] = '#f1d1d0'
        self.jkw['activeforeground'] = '#16c79a'
        self.jkw.grid(row=1, column=1,sticky=tkinter.W )

        self.JK = tkinter.Label(self, text="Jenis Kelamin      :")
        
# bitmap
        
        self.jkb = Radiobutton(self)
        # merubah ketika di klik
        self.jkb['activebackground'] = '#f1d1d0'
        self.jkb['activeforeground'] = '#16c79a'
        self.jkb['anchor'] = E
        self.jkb['bg'] = '#ccf2f4'
        self.jkb['bitmap'] = 'error'
        self.jkb['text'] = 'Laki-Laki'
        self.jkb['fg'] = '#0a043c'
        self.jkb['textvariable'] = 'jkl'
        self.jkb['variable'] = 'Laki-Laki'
        # merubah font
        self.jkb['font'] = 'Helvetica' 
        self.jkb.grid(row=3, column=1,sticky=tkinter.W )

       
# image
        
        # deklarasi foto
        self.photos = PhotoImage(file = "logo.png") 
        #mengatur ukuran button
        self.photoimages = self.photos.subsample(20, 20) 
        self.jki = Radiobutton(self)
        # merubah ketika di klik
        self.jki['activebackground'] = '#f1d1d0'
        self.jki['activeforeground'] = '#16c79a'
        self.jki['anchor'] = E
        
        self.jki['image'] = self.photoimages
        self.jki['bg'] = '#ccf2f4'
        self.jki['text'] = 'Laki-Laki'
        self.jki['fg'] = '#0a043c'
        self.jki['textvariable'] = 'jkl'
        self.jki['variable'] = 'Laki-Laki'
        # merubah font
        self.jki['font'] = 'Helvetica' 
        self.jki.grid(row=4, column=1,sticky=tkinter.W )

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
        self.submit['width'] = '43'
        # set nama variable
        self.submit['relief'] = 'raised' 
        # membuat button berbeda saat di tekan
        self.submit['activebackground'] = '#d3e0ea' 
        # membuat teks berbeda saat di tekan
        self.submit['activeforeground'] = '#ef4f4f'
        # membuat grid
        self.submit.grid(row=8, column=0, columnspan=2)



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