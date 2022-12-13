# import modul 
from tkinter import * # type:ignore
import tkinter.ttk as ttk
import tkinter.messagebox as tkmsg
from random import randint, choice

class Menu:
    def __init__(self, kode_menu, nama_menu, harga):
        self.kode_menu = kode_menu
        self.nama_menu = nama_menu
        self.jumlah = 0
        self.harga = int(harga)
    
    def __str__(self):
        return (self.kode_menu + ' ' + self.nama_menu)

    def get_kode(self):
        return self.kode_menu
    def get_nama(self):
        return self.nama_menu
    def get_harga(self):
        return self.harga

class Meals(Menu):
    def __init__(self, kode_menu, nama_menu, harga, tingkat_kegurihan):
        super().__init__(kode_menu, nama_menu, harga)
        self.tingkat_kegurihan = tingkat_kegurihan

    def get_ext(self):
        return self.tingkat_kegurihan

class Drinks(Menu):
    def __init__(self, kode_menu, nama_menu, harga, tingkat_kemanisan):
        super().__init__(kode_menu, nama_menu, harga)
        self.tingkat_kemanisan = tingkat_kemanisan

    def get_ext(self):
        return self.tingkat_kemanisan

class Sides(Menu):
    def __init__(self, kode_menu, nama_menu, harga, tingkat_keviralan):
        super().__init__(kode_menu, nama_menu, harga)
        self.tingkat_keviralan = tingkat_keviralan

    def get_ext(self):
        return self.tingkat_keviralan

class Meja:
    
    def __init__(self):
        self.state = False
        self.nama = ''
        self.total = 0
        self.pesanan = [list(), list(), list()] 
        

class Main(Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.master.geometry("400x200")  # type:ignore
        self.pack()
        master.title("Kafe Daun-Daun Pacilkom v2.0 🌿") # type:ignore

        button1 = Button(self, text="Buat Pesanan", width=30, command=self.buat_pesanan, bg="#4472C4", fg="white")
        button2 = Button(self, text="Selesai Gunakan Meja", width=30, command=self.selesai_gunakan_meja, bg="#4472C4", fg="white")
        button1.grid(row=0, column=0, padx=10, pady=45)
        button2.grid(row=1, column=0)
        
    def buat_pesanan(self):
        BuatPesanan(self.master)

    def selesai_gunakan_meja(self):
        pass
        # SelesaiGunakanMeja(self.master)

class BuatPesanan(object):
    def __init__(self, master = None):        
        self.master = Toplevel()
        self.master.geometry("370x200")
        self.master.title("Kafe s-Daun Pacilkom v2.0 🌿")

        self.lbl_nama = Label(self.master, text="Siapa nama Anda?")
        self.entry = Entry(self.master)
        self.button1 = Button(self.master, text="Kembali", width=20, command=self.master.destroy, bg="#4472C4", fg="white")
        self.button2 = Button(self.master, text="Lanjut", width=20, command=self.pressed, bg="#4472C4", fg="white")

        self.lbl_nama.grid(row=0, column=0, padx=30)
        self.entry.grid(row=0, column=1, padx=30, pady=40)
        self.button1.grid(row=1, column=0, padx=20, pady=45)
        self.button2.grid(row=1, column=1)

        self.master.mainloop()

    def pressed(self):
        if self.entry.get() == '':
            tkmsg.showerror('Nama kosong', 'Anda belum memasukkan nama, mohon isi nama anda')
        else:
            self.generate_table(self.entry.get())

    def generate_table(self, nama):
        self.master.destroy()
        self.total_columns = 4
        self.meja = self.newMeja()
        self.newWindow = Toplevel()

        if(self.meja == -1):
            tkmsg.showerror('Meja penuh', 'Tidak ada meja tersedia\nMohon coba lagi nanti')
            self.newWindow.destroy()

        self.width = 680 
        self.height = 14*20 + 20*(len(list_menu[0]) + len(list_menu[1]) + len(list_menu[2])) + 10
        self.newWindow.geometry(f'{self.width}x{self.height}') #type:ignore

        extra = ['Kode', 'Nama', 'Harga', 'Kegurihan', 'Jumlah']
        roww = 0

        self.labelNama = Label(self.newWindow, text= f'Nama pemesan : {nama}')
        self.labelNama.grid(row=roww, column=1, pady=(10, 20), columnspan=2)

        self.labelMeja = Label(self.newWindow, text= f'No meja : {self.meja}')
        self.labelMeja.grid(row=roww, column=4, pady=(10, 20), sticky='e')

        self.buttonUbah = Button(self.newWindow, text="Ubah", command=lambda :self.ganti_meja(self.labelMeja), bg="#4472C4", fg="white")
        self.buttonUbah.grid(row=roww, column=5, pady=(10, 20), sticky='w')

        roww += 1

        harga = 0
        self.cmbbx = [list(), list(), list()]

        for a in range (3):
            to_print = list_menu[a]
            tot_row = len(to_print)

            if a == 0:
                lbl = Label(self.newWindow, text='MEALS')
            elif(a == 1):
                lbl = Label(self.newWindow, text='DRINKS')
            else:
                lbl = Label(self.newWindow, text='SIDES')

            lbl.grid(row=roww, column=1, sticky='nesw')
            roww += 1

            firstRow = Entry(self.newWindow, width = 20, fg = 'blue')
            firstRow.grid(row = roww, column = 0 + 1, padx=(30,0))
            firstRow.insert(END, extra[0])
            firstRow['state'] = 'readonly'

            for j in range(self.total_columns):
                entry = Entry(self.newWindow, width = 20, fg = 'blue')
                entry.grid(row = roww, column = j + 2)
                entry.insert(END, extra[j+1])
                entry['state'] = 'readonly'

            roww += 1
            for menu in to_print:

                entry_label = Entry(self.newWindow, width = 20, fg = 'blue')
                entry_nama = Entry(self.newWindow, width = 20, fg = 'blue')
                entry_harga = Entry(self.newWindow, width = 20, fg = 'blue')
                entry_ext = Entry(self.newWindow, width = 20, fg = 'blue')
                
                entry_label.grid(row = roww, column = 1, padx=(30,0))
                entry_nama.grid(row = roww, column = 2)
                entry_harga.grid(row = roww, column = 3)
                entry_ext.grid(row = roww, column = 4)
                
                entry_label.insert(END, menu.get_kode())
                entry_nama.insert(END, menu.get_nama())
                entry_harga.insert(END, format_angka(menu.get_harga()))
                entry_ext.insert(END, menu.get_ext())

                entry_label['state'] = 'readonly'
                entry_nama['state'] = 'readonly'
                entry_harga['state'] = 'readonly'
                entry_ext['state'] = 'readonly'

                self.val = tuple([str(k) for k in range(10)])
                opsi_jumlah = ttk.Combobox(self.newWindow, values = self.val , width=17, state='readonly') 
                opsi_jumlah.set('0')
                opsi_jumlah.grid(row = roww, column = self.total_columns + 1)
                opsi_jumlah.bind("<<ComboboxSelected>>", self.update_total)
                
                roww += 1

                self.cmbbx[a].append(opsi_jumlah)

            extra[3] = 'Kemanisan' if a == 0 else 'Keviralan'
        
        self.total = Label(self.newWindow, text= f'Total harga: {format_angka(self.get_total())}')
        self.total.grid(row= roww, column= 5)
        roww += 1

        btn1 = Button(self.newWindow, text="Kembali", width=15, command=self.newWindow.destroy, bg="#4472C4", fg="white")
        btn2 = Button(self.newWindow, text="Ok", width=15, command=self.newWindow.destroy, bg="#4472C4", fg="white")

        btn1.grid(row= roww, column= 2, pady= 40, columnspan=2)
        btn2.grid(row= roww, column= 3, columnspan=2)

    def update_total(self, things):
        self.total['text'] = f'Total harga: {format_angka(self.get_total())}'

    def get_total(self):
        total = 0
        for a in range(3):
            for i, cbx in enumerate (self.cmbbx[a]):
                total += int(cbx.get())*int(list_menu[a][i].get_harga())

        return total

    def newMeja(self):
        avail = list()
        for num, meja in enumerate (list_meja):
            if(not meja.state):
                avail.append(num)

        if(len(avail) == 0):
            return -1
        else:
            return choice(avail) 
    
    def ganti_meja(self, labelMeja):
        TabelMeja('ubah', self.meja, labelMeja)
        self.meja = self.labelMeja


class TabelMeja(object):
    def __init__(self, jenis = '', noMeja = -1, labelMeja = Label()):        
        self.master = Toplevel()
        prevLabel = labelMeja
        currentMeja = noMeja
        self.master.geometry('300x300')
        # self.labelMeja['text'] = (f'No meja : {self.meja}')
        roww = 0
        lbl_greet = Label(self.master, text= f'Silakan klik meja kosong yang di inginkan:')
        lbl_greet.grid(row= roww, column= 0, padx=(40), pady=(0, 20), columnspan=4)

        for i in range(10):
            padding = (3,6) if i//5 == 0 else (6,3)
            button = Button(self.master, text=f'{i}', width = 10, bg='#808A87', fg='white')
            button.grid(row=i%5+1, column=i//5+1, pady=10, padx=padding)

       

    
# class SelesaiGunakanMeja(object):
#     def __init__(self, master = None):
#         super().__init__(master)
#         self.master.geometry("400x200")
#         self.title("Kafe Daun-Daun Pacilkom v2.0 🌿")

#         self.lbl_command = Label(self, text="Silakan klik meja yang selesai digunakan:")
#         self.lbl_command.grid(column=0, row=0)

#         #TODO

#         self.mainloop()

list_menu = [list(), list(), list()]
template_menu = [list(), list(), list()]
list_meja = list()

def format_angka(angka):    
    angka = str(angka)
    return 'Rp' + ('.'.join(angka[::-1][i:i+3] for i in range(0, len(angka[::-1]), 3)))[::-1]

def cek_menu():
    isiFile = open('menu.txt', 'r')
    kode, nama, is_not_whole, a = list(), list(), False, -1

    for line in isiFile:
        line = line.strip()

        if(line[:3] != '==='):
            baris = line.split(';')
            kode.append(baris[0])
            nama.append(baris[1])

            if(int(baris[2]) < 0 or isinstance(baris[2], float)): 
                is_not_whole = True
                break
            
            if a == 0:
                baris = Meals(baris[0], baris[1], baris[2], baris[3])
            elif(a == 1):        
                baris = Drinks(baris[0], baris[1], baris[2], baris[3])
            else:
                baris = Sides(baris[0], baris[1], baris[2], baris[3])
                
            list_menu[a].append(baris)
            template_menu[a].append(0)
            
        else:
            a += 1

    for i in range(10):
        a = Meja()
        a.pesanan = template_menu
        list_meja.append(a)

    if  len(nama) != len(set(nama)) or len(kode) != len(set(kode)) or is_not_whole:
        print('Daftar menu tidak valid, cek kembali menu.txt!') 
        exit()

if __name__ == '__main__':
    
    cek_menu()
    window = Tk()
    cafe = Main(window)
    window.mainloop()
