print('''
==================================
         TOKO MUHLIS JAYA
        MAKANAN DAN MINUMAN
==================================
             Menu
            Makanan 
----------------------------------
| KODE |    NAMA     |   HARGA   |
----------------------------------
| A1   | Nasi Goreng | Rp. 8.000  |
| A2   | Nasi Pecel  | Rp. 9.000  |
| A3   | Nasi Padang | Rp. 10.000 |

             Menu
            Minuman 
----------------------------------
| KODE |    NAMA     |   HARGA   |
----------------------------------
| B1   |    Es Teh   | Rp. 3.000  |
| B2   |  Teh Hangat | Rp. 2.000  |
| B3   |   Es Jeruk  | Rp. 4.000  |

----------Terima Kasih------------
''')

print('Silahkan Pilih Menu\n\nJika Menu Makanan Tekan 1\n\nJika Menu Minuman Tekan 2')
opsi = input('Tekan 1/2 : ')
if opsi == 1 :
        kode = input('\nKode Makanan : ')
        n = int(input('Jumlah beli : '))
        if kode == 'A1':
                 print(f'Nasi Goreng\nHarga Rp. 8.000\nJumlah : {n}\nTotal bayar : Rp. {n*8000},\n')
                 print('Terima Kasih')
        elif kode == 'A2':
                 print(f'Nasi Pecel\nHarga Rp. 9.000\nJumlah : {n}\nTotal bayar : Rp. {n*9000},\n')
                 print('Terima Kasih')
        elif kode == 'A3':
                 print(f'Nasi Padang\nHarga Rp. 10.000\nJumlah : {n}\nTotal bayar : Rp. {n*10000},\n')
                 print('Terima Kasih')
        else:
                 print('Kode Makanan Tidak Terdaftar')
elif opsi == 2:
        kode = input('\nKode Minuman : ')
        n = int(input('Jumlah beli : '))
        if kode == 'B1':
                 print(f'Es Teh\nHarga Rp. 3.000\nJumlah : {n}\nTotal bayar : Rp. {n*3000},\n')
                 print('Terima Kasih')
        elif kode == 'B2':
                 print(f'Teh Hangat\nHarga Rp. 2.000\nJumlah : {n}\nTotal bayar : Rp. {n*2000},\n')
                 print('Terima Kasih')
        elif kode == 'B3':
                 print(f'Es Jeruk\nHarga Rp. 4.000\nJumlah : {n}\nTotal bayar : Rp. {n*4000},\n')
                 print('Terima Kasih')
        else:
                 print('Kode Minuman Tidak Terdaftar')
