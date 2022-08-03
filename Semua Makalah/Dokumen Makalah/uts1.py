# aplikasi sederhana berbasis python
class Toko:
    def muhlis():
        # untuk menampilkan ket toko martabak muhlis
        Toko_muhlis = ('Toko muhlis', 'pilih menu:',
                       '1. Martabak = Rp.10000', 'Beli 3 Dapat Diskon 20%')
        for i in Toko_muhlis:
            print(i)
        opsi = input('Pilih Menunya :')
        if opsi == '1':
            jumlah = int(input('jumlah :'))
            uang_kamu = int(input('uang kamu :'))
            harga = 10000
            diskon = 20/100
        if jumlah == 1:
            print('Kamu Akan Membeli Martabak Berjumlah :',
                  jumlah, 'Dengan Harga :', harga)
        elif jumlah == 3:
            print('Kamu Membeli Martabak Berjumlah :', jumlah,
                  'Dengan Harga :', harga, 'Dan mendapatkan diskon sebesar 20%')
            print('Total Diskon :', harga*jumlah*20/100)


x = Toko
x.muhlis()
