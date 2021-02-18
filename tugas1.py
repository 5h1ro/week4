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

# submit


        self.namaClick = Button(self, command=lambda:self.nama.select_clear())
        self.namaClick['text'] = 'Submit'
        # merubah bg
        self.namaClick['bg'] = '#16c79a'
        # merubah ukuran border
        self.namaClick['bd'] = '3px'
        # merubah warna fg atau text
        self.namaClick['fg'] = '#91091e' 
        # merubah font
        self.namaClick['font'] = 'Helvetica' 
        # merubah font
        self.namaClick['justify'] = 'right'
        # merubah width
        self.namaClick['width'] = '10'
        # set nama variable
        self.namaClick['relief'] = 'raised' 
        # membuat button berbeda saat di tekan
        self.namaClick['activebackground'] = '#d3e0ea' 
        # membuat teks berbeda saat di tekan
        self.namaClick['activeforeground'] = '#ef4f4f'
        # membuat grid
        self.namaClick.grid(row=0, column=2)

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

# NIP


        self.NIP = tkinter.Label(self, text="NIP                          :")
        self.NIP['fg'] = '#0a043c'
        self.NIP['bg'] = '#ccf2f4'
        self.NIP['font'] = 'Helvetica 12 bold'
        self.NIP.grid(row=2, column=0, sticky=W)
        # membuat entry nama
        self.nip = Entry(self)
        # merubah bg
        self.nip['bg'] = '#a4ebf3'
        # merubah ukuran border
        self.nip['bd'] = '2px'
        # hover
        self.nip['cursor'] = 'clock' 
        # merubah warna fg atau text
        self.nip['fg'] = '#0a043c' 
        # merubah copy
        self.nip['exportselection'] = 'false'
        # merubah font
        self.nip['font'] = 'Helvetica' 
        # merubah text alignment
        self.nip['justify'] = 'center'
        # merubah width
        self.nip['width'] = '30'
        # select range
        self.nip.select_range(1, tkinter.END)
        # set nama variable
        self.nip['textvariable'] = 'idNIP' 
        # membuat grid
        self.nip.grid(row=2, column=1, sticky=W)

# submit


        self.NIPClick = Button(self, command=lambda:
                    self.nip.select_range(6, 13))
        self.NIPClick['text'] = 'Submit'
        # merubah bg
        self.NIPClick['bg'] = '#16c79a'
        # merubah ukuran border
        self.NIPClick['bd'] = '3px'
        # merubah warna fg atau text
        self.NIPClick['fg'] = '#91091e' 
        # merubah font
        self.NIPClick['font'] = 'Helvetica' 
        # merubah font
        self.NIPClick['justify'] = 'right'
        # merubah width
        self.NIPClick['width'] = '10'
        # set nama variable
        self.NIPClick['relief'] = 'raised' 
        # membuat button berbeda saat di tekan
        self.NIPClick['activebackground'] = '#d3e0ea' 
        # membuat teks berbeda saat di tekan
        self.NIPClick['activeforeground'] = '#ef4f4f'
        # membuat grid
        self.NIPClick.grid(row=2, column=2)

# NIP


        self.TL = tkinter.Label(self, text="Tanggal Lahir                     :")
        self.TL['fg'] = '#0a043c'
        self.TL['bg'] = '#ccf2f4'
        self.TL['font'] = 'Helvetica 12 bold'
        self.TL.grid(row=2, column=4, sticky=W)
        # membuat entry nama
        self.tl = Entry(self)
        # merubah bg
        self.tl['bg'] = '#a4ebf3'
        # merubah ukuran border
        self.tl['bd'] = '2px'
        # hover
        self.tl['cursor'] = 'clock' 
        # merubah warna fg atau text
        self.tl['fg'] = '#0a043c' 
        # merubah font
        self.tl['font'] = 'Helvetica' 
        # merubah font
        self.tl['justify'] = 'left'
        # merubah width
        self.tl['width'] = '30'
        # select range
        self.tl.select_range(1, tkinter.END)
        # set nama variable
        self.tl['textvariable'] = 'idTL' 
        # membuat grid
        self.tl.grid(row=2, column=5, sticky=W)

# alamat

        self.Alamat = tkinter.Label(self, text="Alamat                    :")
        self.Alamat['fg'] = '#0a043c'
        self.Alamat['bg'] = '#ccf2f4'
        self.Alamat['font'] = 'Helvetica 12 bold'
        self.Alamat.grid(row=4, column=0, sticky=W)
        # membuat entry nama
        self.alamat = Entry(self)
        # merubah bg
        self.alamat['bg'] = '#a4ebf3'
        # merubah ukuran border
        self.alamat['bd'] = '2px'
        # hover
        self.alamat['cursor'] = 'clock' 
        # merubah warna fg atau text
        self.alamat['fg'] = '#0a043c' 
        # merubah font
        self.alamat['font'] = 'Helvetica' 
        # merubah font
        self.alamat['justify'] = 'left'
        # merubah width
        self.alamat['width'] = '30'
        # set nama variable
        self.alamat['textvariable'] = 'idAlamat' 
        # set nama relief
        self.alamat['relief'] = 'sunken' 
        # membuat grid
        self.alamat.grid(row=4, column=1, sticky=W)

# lulusan

        self.Lulusan = tkinter.Label(self, text="Lulusan                  :")
        self.Lulusan['fg'] = '#0a043c'
        self.Lulusan['bg'] = '#ccf2f4'
        self.Lulusan['font'] = 'Helvetica 12 bold'
        self.Lulusan.grid(row=5, column=0, sticky=W)
        self.lulusan = Listbox(self)
        # selectmode
        self.lulusan['selectmode'] = 'single'
        # merubah bg
        self.lulusan['bg'] = '#a4ebf3'
        # merubah selectbackground color
        self.lulusan['selectbackground'] = '#16c79a'
        # merubah ukuran border
        self.lulusan['bd'] = '2px' 
        # merubah warna fg atau text
        self.lulusan['fg'] = '#0a043c' 
        # merubah font
        self.lulusan['font'] = 'Helvetica' 
        # set nama relief
        self.alamat['relief'] = 'sunken' 
        # merubah width
        self.lulusan['width'] = '30'
        # merubah height
        self.lulusan['height'] = '5'
        # set seeder  
        self.lulusan.insert(1, "SD")  
        self.lulusan.insert(2, "SMP")  
        self.lulusan.insert(3, "SMA")  
        self.lulusan.insert(4, "D3")  
        self.lulusan.insert(5, "S1")
        # membuat grid
        self.lulusan['justify'] = 'center'
        self.lulusan.grid(row=5, column=1, sticky=W)

# jenis kelamin

        self.JK = tkinter.Label(self, text="Jenis Kelamin      :")
        self.JK['fg'] = '#0a043c'
        self.JK['bg'] = '#ccf2f4'
        self.JK['font'] = 'Helvetica 12 bold'
        self.JK.grid(row=6, column=0, columnspan=6, sticky=W)
        self.jkl = Radiobutton(self)
        self.jkl['text'] = 'Laki-Laki'
        self.jkl['fg'] = '#0a043c'
        self.jkl['bg'] = '#ccf2f4'
        self.jkl['textvariable'] = 'jkl'
        self.jkl['variable'] = 'Laki-Laki'
        # merubah font
        self.jkl['font'] = 'Helvetica' 
        # merubah ketika di klik
        self.jkl['activebackground'] = '#f1d1d0'
        self.jkl['activeforeground'] = '#16c79a'
        self.jkl.grid(row=6, column=1,sticky=tkinter.W )

        self.jkw = Radiobutton(self)
        self.jkw['text'] = 'Wanita'
        self.jkw['fg'] = '#0a043c'
        self.jkw['bg'] = '#ccf2f4'
        self.jkl['textvariable'] = 'jkw'
        self.jkw['variable'] = 'Wanita'
        # merubah font
        self.jkw['font'] = 'Helvetica' 
        # merubah ketika di klik
        self.jkw['activebackground'] = '#f1d1d0'
        self.jkw['activeforeground'] = '#16c79a'
        self.jkw.grid(row=7, column=1,sticky=tkinter.W )
        
        self.show = Checkbutton(self)
        # membuat grid
        self.show['text'] = 'Tampilkan Password'
        self.show['fg'] = '#0a043c'
        self.show['bg'] = '#ccf2f4'
        self.show['font'] = 'Helvetica 12 bold'
        self.show.grid(row=3, column=1, sticky=W)

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