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
        # membuat label
        self.Nama = tkinter.Label(self, text="Username              :")
        self.Nama['fg'] = '#0a043c'
        self.Nama['bg'] = '#ccf2f4'
        self.Nama['font'] = 'Helvetica 12 bold'
        self.Nama.grid(row=0, column=0, sticky=W)
        # membuat entry nama
        self.nama = Entry(self)
        # merubah bg
        self.nama['bg'] = '#a4ebf3'
        # merubah ukuran border
        self.nama['bd'] = '2px'
        # hover
        self.nama['cursor'] = 'spider' 
        # merubah warna saat di select
        self.nama['selectbackground'] = '#e40017'
        # merubah warna text saat di select
        self.nama['selectforeground'] = '#ff75a0'
        # merubah width saat di select
        self.nama['selectborderwidth'] = '2px'
        # merubah warna fg atau text
        self.nama['fg'] = '#0a043c' 
        # merubah font
        self.nama['font'] = 'Helvetica' 
        # merubah width
        self.nama['width'] = '30'
        # set nama variable
        self.nama['textvariable'] = 'idNama' 
        # membuat grid
        self.nama.grid(row=0, column=1, sticky=W)

# password

        self.Password = tkinter.Label(self, text="Password              :")
        self.Password['fg'] = '#0a043c'
        self.Password['bg'] = '#ccf2f4'
        self.Password['font'] = 'Helvetica 12 bold'
        self.Password.grid(row=1, column=0, sticky=W)
        # membuat entry nama
        self.password = Entry(self)
        # merubah bg
        self.password['bg'] = '#a4ebf3'
        # merubah ukuran border
        self.password['bd'] = '2px'
        # hover
        self.password['cursor'] = 'heart' 
        # merubah warna fg atau text
        self.password['fg'] = '#0a043c' 
        # merubah font
        self.password['font'] = 'Helvetica' 
        # merubah tampilan inputan
        self.password['show'] = '*'
        # merubah width
        self.password['width'] = '30'
        # set nama variable
        self.password['textvariable'] = 'idPass' 
        # membuat grid
        self.password.grid(row=1, column=1, sticky=W)
        
# Checkbutton

        self.cek = StringVar() 
        
        def text():
            self.text = Label(self)
            self.text['text']=self.cek.get()
            self.text.grid(row=3, column=1)
        self.show = Checkbutton(self,
            activebackground='#91091e',
            activeforeground='#94ebcd'
        )
        # membuat grid
        self.show['bg'] = '#ccf2f4'
        self.show['bd'] = '10'
        # self.show['highlightcolor']
        # self.show['disableforeground'] = 'disable'
        self.show['font'] = 'Helvetica 12 bold'
        self.show['fg'] = '#0a043c'
        self.show['height'] = '1'
        self.show['justify'] = 'left'
        self.show['offvalue']="Off"
        self.show['onvalue']="On"
        self.show['padx'] = '20'
        self.show['pady'] = '20'
        self.show['relief'] = 'sunken'
        self.show['selectcolor'] = 'green'
        self.show['wraplength'] = 100
        self.show['cursor'] = 'heart' 
        self.show['text'] = 'Tampilkan Password'
        self.show['underline'] = '0'
        self.show['variable'] = self.cek
        self.show['width'] = '10'
        self.show.grid(row=3, column=0, sticky=W)

        
        def text():
            self.text = Label(self)
            self.text['text']=self.cek.get()
            self.text.grid(row=3, column=1)

        self.show['command'] = text

# gambar
        self.gambar = Checkbutton(self)
        # deklarasi foto
        self.photos = PhotoImage(file = "logo.png") 
        #mengatur ukuran button
        self.photoimages = self.photos.subsample(20, 20) 
        self.gambar['image'] = self.photoimages
        self.gambar['state'] = 'disable'
        self.gambar.grid(row=4, column=0, sticky=W)
# gambar
        self.gambarbt = Checkbutton(self)
        self.gambarbt['bitmap'] = 'error'
        self.gambarbt['state'] = 'disable'
        self.gambarbt.grid(row=4, column=1, sticky=W)

# button
        self.namaSelect = Button(self, command=self.show.select)
        self.namaSelect['text'] = 'Select'
        # membuat grid
        self.namaSelect.grid(row=0, column=2, sticky=W)
# button
        self.namaSelect = Button(self, command=self.show.deselect)
        self.namaSelect['text'] = 'deSelect'
        # membuat grid
        self.namaSelect.grid(row=1, column=2, sticky=W)
# button
        self.namaSelect = Button(self, command=self.show.flash)
        self.namaSelect['text'] = 'flash'
        # membuat grid
        self.namaSelect.grid(row=2, column=2, sticky=W)
# button
        self.namaSelect = Button(self, command=self.show.invoke)
        self.namaSelect['text'] = 'invoke'
        # membuat grid
        self.namaSelect.grid(row=3, column=2, sticky=W)
# button
        self.namaSelect = Button(self, command=self.show.toggle)
        self.namaSelect['text'] = 'toogle'
        # membuat grid
        self.namaSelect.grid(row=4, column=2, sticky=W)
        



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