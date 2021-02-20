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
        
        # # bind to focus events
    #     self.bind('<FocusIn>', self._on_focus)
    #     self.bind('<FocusOut>', self._on_lose_focus)

    # def _on_focus(self, event):
    #     self.configure(bg=self.namaSelect['highlightcolor'])

    # def _on_lose_focus(self, event):
    #     self.configure(bg=self._bg)


    def utama(self) :

        self['background'] = "#ccf2f4"
        # membuat label
        self.Nama = tkinter.Label(self, text="Username              :")
        self.Nama['bg'] = '#ccf2f4'
        self.Nama['fg'] = '#0a043c'
        self.Nama['font'] = 'Helvetica 12 bold'
        self.Nama.grid(row=0, column=0, sticky=W)

        
        # membuat entry nama
        self.nama = Entry(self)
        # merubah bg
        self.xScroll = tkinter.Scrollbar(self, orient=HORIZONTAL)
        self.xScroll.grid(row=1, column=1, sticky=EW)
        self.nama['bg'] = '#a4ebf3'
        # merubah ukuran border
        self.nama['bd'] = '2px'
        # hover
        self.nama['cursor'] = 'spider' 

        # slef.nama['exportselection'] = 

        
        # merubah warna fg atau text
        self.nama['fg'] = '#0a043c' 
        # merubah font
        self.nama['font'] = 'Helvetica' 
        # slef.nama['highlightbackground'] = 
        # slef.nama['highlightcolor'] = 
        # slef.nama['highlightthickness'] = 
        # slef.nama['insertbackground'] = 
        # slef.nama['insertborderwidth'] = 
        # slef.nama['insertofftime'] = 
        # slef.nama['insertontime'] = 
        # slef.nama['insertwidth'] = 
        self.nama['justify'] = 'left'
        self.nama['relief'] = 'ridge'
        # merubah warna saat di select
        self.nama['selectbackground'] = '#e40017'
        # merubah warna text saat di select
        self.nama['selectforeground'] = '#ff75a0'
        # merubah width saat di select
        self.nama['selectborderwidth'] = '2px'
        self.nama['show'] = ''
        # set nama variable
        self.nama['textvariable'] = 'idNama' 
        # merubah width
        self.nama['width'] = '30'
        self.nama['xscrollcommand'] = self.xScroll.set
        # membuat grid
        self.nama.grid(row=0, column=1, sticky=NSEW)
        
        self.xScroll['command'] = self.nama.xview


# password

        self.Password = tkinter.Label(self, text="Password              :")
        self.Password['fg'] = '#0a043c'
        self.Password['bg'] = '#ccf2f4'
        self.Password['font'] = 'Helvetica 12 bold'
        self.Password.grid(row=2, column=0, sticky=W)
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
        self.password.grid(row=2, column=1, sticky=W)

# select_range


        self.namaSelect = Button(self, 
            command=lambda:self.nama.select_range(1, END)
        )
        self.namaSelect['text'] = 'Select'
        # merubah bg
        self.namaSelect['bg'] = '#16c79a'
        # merubah ukuran border
        self.namaSelect['bd'] = '3px'
        # merubah warna fg atau text
        self.namaSelect['fg'] = '#91091e' 
        # merubah font
        self.namaSelect['font'] = 'Helvetica' 
        # merubah font
        self.namaSelect['justify'] = 'left'
        # merubah width
        self.namaSelect['width'] = '43'
        # merubah width
        self.namaSelect['height'] = '2'
        # set nama variable
        self.namaSelect['relief'] = 'raised' 
        # membuat button berbeda saat di tekan
        self.namaSelect['activebackground'] = '#d3e0ea' 
        # membuat button berbeda saat di tekan
        self.namaSelect['highlightcolor'] = '#e40017' 
        # membuat teks berbeda saat di tekan
        self.namaSelect['activeforeground'] = '#ef4f4f'
        # membuat grid
        self.namaSelect.grid(row=3, column=0, columnspan=2)

# Clear

        self.namaClick = Button(self, command=lambda:self.nama.select_clear())
        self.namaClick['text'] = 'Clear'
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
        self.namaClick['width'] = '43'
        # set nama variable
        self.namaClick['relief'] = 'raised' 
        # membuat button berbeda saat di tekan
        self.namaClick['activebackground'] = '#d3e0ea' 
        # membuat teks berbeda saat di tekan
        self.namaClick['activeforeground'] = '#ef4f4f'
        # membuat grid
        self.namaClick.grid(row=4, column=0, columnspan=2)

# select_adjust(index)

        self.namaClick = Button(self, command=lambda:self.nama.select_adjust(5))
        self.namaClick['text'] = 'adjust'
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
        self.namaClick['width'] = '43'
        # set nama variable
        self.namaClick['relief'] = 'raised' 
        # membuat button berbeda saat di tekan
        self.namaClick['activebackground'] = '#d3e0ea' 
        # membuat teks berbeda saat di tekan
        self.namaClick['activeforeground'] = '#ef4f4f'
        # membuat grid
        self.namaClick.grid(row=5, column=0, columnspan=2)


# select_form(index)

        self.namaClick = Button(self, command=lambda:self.nama.select_from(3))
        self.namaClick['text'] = 'from'
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
        self.namaClick['width'] = '43'
        # set nama variable
        self.namaClick['relief'] = 'raised' 
        # membuat button berbeda saat di tekan
        self.namaClick['activebackground'] = '#d3e0ea' 
        # membuat teks berbeda saat di tekan
        self.namaClick['activeforeground'] = '#ef4f4f'
        # membuat grid
        self.namaClick.grid(row=6, column=0, columnspan=2)

# select_present

        self.namaClick = Button(self, command=lambda:self.nama.select_present)
        self.namaClick['text'] = 'present'
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
        self.namaClick['width'] = '43'
        # set nama variable
        self.namaClick['relief'] = 'raised' 
        # membuat button berbeda saat di tekan
        self.namaClick['activebackground'] = '#d3e0ea' 
        # membuat teks berbeda saat di tekan
        self.namaClick['activeforeground'] = '#ef4f4f'
        # membuat grid
        self.namaClick.grid(row=7, column=0, columnspan=2)

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