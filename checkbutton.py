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
# Checkbutton

        self.cek = StringVar() 
        
        self.show = Checkbutton(self, 
        # set bg saat di click
                activebackground='#91091e',
        # set fg saat di click 
                activeforeground='#94ebcd'
        )
        # set bg
        self.show['bg'] = '#ccf2f4'
        # set ukuran border
        self.show['bd'] = '10'
        # merubah bentuk cursor
        self.show['cursor'] = 'heart' 
        # merubah font
        self.show['font'] = 'Helvetica 12 bold'
        # merubah warna fg
        self.show['fg'] = '#0a043c'
        # merubah tinggi
        self.show['height'] = '1'

        # self.show['highlightcolor']

        # merubah rata
        self.show['justify'] = 'left'
        # set value saat tidak di pilih
        self.show['offvalue']="Off"
        # set value saat di pilih
        self.show['onvalue']="On"
        # set padding horizontal
        self.show['padx'] = '20'
        # set padding vertical
        self.show['pady'] = '20'
        # merubah bentuk dari border
        self.show['relief'] = 'sunken'
        # merubah warna kotak check
        self.show['selectcolor'] = 'blue'
        # memberi huruf pada huruf
        self.show['underline'] = '0'
        # mendeklarasikan jenis variable
        self.show['variable'] = self.cek
        # mengatur panjang checkbutton
        self.show['width'] = '10'
        # mengatur panjang huruf
        self.show['wraplength'] = 100
        # mengatur text
        self.show['text'] = 'Tampilkan Password'
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
        # mengatur ukuran button
        self.photoimages = self.photos.subsample(20, 20) 
        # mengatur image pada Checkbutton
        self.gambar['image'] = self.photoimages
        # mengatur apakah aktif atau tidak
        self.gambar['state'] = 'disable'
        self.gambar.grid(row=4, column=0, sticky=W)
# bitmap
        self.gambarbt = Checkbutton(self)
        # mengatur gambar bitmap
        self.gambarbt['bitmap'] = 'error'
        # mengatur apakah aktif atau tidak
        self.gambarbt['state'] = 'disable'
        self.gambarbt.grid(row=4, column=1, sticky=W)
# bitmap
        self.gambardf = Checkbutton(self)
        # mengatur apakah aktif atau tidak
        self.gambardf['state'] = 'disable'
        # mengatur text
        self.gambardf['text'] = 'disable'
        # mengatur warna saat checkbutton di disable
        self.gambardf['disabledforeground'] = 'red'
        self.gambardf.grid(row=5, column=1, sticky=W)

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