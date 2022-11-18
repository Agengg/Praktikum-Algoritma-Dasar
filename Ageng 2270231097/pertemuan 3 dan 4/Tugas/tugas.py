print("============Resto Makan Kenyang============")
pembeli = input("Nama Pembeli : ")
alamat = input("Alamat : ")
no_telp = int(input("Nomor Telp : "))  
tanggal = input("Tanggal : ")


def makanan():
    global totalmakanan
    global porsi
    global makan
    print("\n===============MENU MAKANAN===============")
    print(" 1  |Gulai Kepala Ikan Kakap   | 70000,00")
    print(" 2  |Chicken Mozarela          | 40000,00")
    print(" 3  |Nasi Ayam Tariyaki        | 30000,00")
    print(" 4  |Spagheti Bolognaise       | 23000,00")
    print(" 5  |Nasi Goreng Seafood       | 350000,00")
    nomor = int(input("Masukkan Pilihan 1/2/3/4/5 : "))
    porsi = int(input("Berapa Porsi : "))

    if nomor == 1:
        totalmakanan = porsi * 70000
        print(porsi,"Gulai Kepala Ikan Kakap = Rp.",totalmakanan)
        makan=("Gulai Kepala Ikan Kakap")
    elif nomor == 2:
        totalmakanan = porsi * 40000
        print(porsi,"Chicken Mozarela = Rp.",totalmakanan)
        makan=("Chicken Mozarela")
    elif nomor == 3:
        totalmakanan = porsi * 30000
        print(porsi,"Nasi Ayam Tariyaki = Rp.",totalmakanan)
        makan=("Nasi Ayam Tariyaki")
    elif nomor == 4:
        totalmakanan = porsi * 23000
        print(porsi,"Spagheti Bolognaise  = Rp.",totalmakanan)
        makan=("Spagheti Bolognaise ")
    elif nomor == 5:
        totalmakanan = porsi * 35000
        print(porsi,"Nasi Goreng Seafood = Rp.",totalmakanan)
        makan=("Nasi Goreng Seafood")
    else:
        print("Pilihan tidak ada di daftar menu\nSilahkan pilih kembali !!!")
        makanan()

def minuman():
    global totalminuman
    global gelas
    global minum
    print("\n===============MENU MINUMAN===============")
    print("1. Es Teh - Rp.3000,00")
    print("2. Teh Hangat - Rp.4000,00")
    print("3. Es Jeruk - Rp.5000,00")
    print("4. Aneka Juice - Rp.12000,00")
    nomor = int(input("Masukkan Pilihan 1/2/3/4 : "))
    gelas = int(input("Berapa Gelas : "))

    if nomor == 1:
        totalminuman = gelas * 3000
        print(gelas,"Es teh = Rp.",totalminuman)
        minum=("Es Teh")
    elif nomor == 2:
        totalminuman = porsi * 4000
        print(gelas,"Teh Hangat = Rp.",totalminuman)
        minum=("Teh Hangat")
    elif nomor == 3:
        totalminuman = gelas * 5000
        print(gelas,"Es Jeruk = Rp.",totalminuman)
        minum=("Es Jeruk")
    elif nomor == 4:
        totalminuman = gelas * 12000
        print(gelas,"Aneka Juice = Rp.",totalminuman)
        minum=("Aneka Juice")
    else:
        print("Pilihan tidak ada di daftar menu\nSilahkan pilih kembali !!!")
        minuman()

makanan()
minuman()
total_semua = totalmakanan + totalminuman

print("\nTotal yang harus di bayar :",total_semua)
uang = int(input("Uang Tunai Pembeli : Rp."))
kembalian = int(uang - total_semua)
print("Kembalian :", kembalian)

print("\n===============S T R U K===============")
print("Nama\t\t:",pembeli)
print("Alamat\t\t:",alamat)
print("Nomor\t\t:",no_telp)
print("Tanggal\t\t:",tanggal)
print("Beli\t\t:",porsi,makan,"(Rp.",totalmakanan,")")
print("Beli\t\t:",gelas,minum,"(Rp.",totalminuman,")")
print("Tagihan\t\t: Rp.",total_semua)
print("Dibayar\t\t: Rp.",uang)
print("Kembalian\t: Rp.",kembalian)

print("======================================")
print("======================================")