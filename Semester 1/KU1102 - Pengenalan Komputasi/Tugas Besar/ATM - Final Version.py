############################### Inisiasi ###############################
# Karena hanya 2 bahasa dan tidak dirancang untuk penambahan fitur, maka kami
# menggunakan 2 prosedur bahasa dibandingkan membuat file bahasa dan mengaksesnya.
# Kedua fungsi memiliki algoritma yang sama, hanya bahasa print yang beda.
# External Library
from pandas import *
import openpyxl
import xlsxwriter
from hashlib import *

# Inisiasi variabel
acctoowner, ibalance, pin = {}, [], 0   # acctoowner adalah map / dictionary untuk no rek-username, ibalance adalah saldo user dalam variabel global
account, pindb, owner = [], [], []      # list menyimpan informasi database pada memori pada saat program berjalan
idx, accnum, cash = -1, 0, []                    # idx digunakan untuk simpan indeks no rekening pada main, accnum adalah no rek user.

# Inisiasi file
# Membuka file db.xlsx dengan pandas, dengan data type str untuk pin dan rek.
dbase = read_excel("EncryptedDbase.xlsx", sheet_name = "Sheet1",converters={'NO REK':str,'PIN':str})
for i in range (10):                    # Membaca 10 baris pertama data nasabah.
    acctoowner[dbase.loc[i, "NO REK"]] = dbase.loc[i, "PEMILIK"]
    ibalance.append(dbase.loc[i, "SALDO"])
    account.append(dbase.loc[i, "NO REK"])
    pindb.append(dbase.loc[i, "PIN"])
    owner.append(dbase.loc[i, "PEMILIK"])
cash.append(int(dbase.loc[0, "ISI MESIN"]))


#########################################################################

############################ Prosedur Input ############################
# Prosedur input dengan exception handler dan exit, secara rekursif memanggil
# xcpinput(BHS) ketika input bukan integer dan exit() ketika batal atau cancel.
# xcpinput() support return type string untuk mengatasi integer 001 akan
# menjadi 1, jika digunakan integer, maka untuk pin atau rekening bank
# diharuskan menggunakan xcpinput(BHS,1) agar return adalah string.
def xcpinput(BHS,strings=0):
    s = input(">> ")
    print();print()                                 # Print newline.
    if (s == "CANCEL") or (s == "BATAL"):           # Jika "tombol" cancel atau
        if BHS == "INDO":                           # batal ditekan.
            print("TRANSAKSI DIBATALKAN")
            print("SILAHKAN AMBIL KARTU ANDA")
        elif BHS == "ENGLISH":
            print("TRANSACTION CANCELED")
            print("PLEASE TAKE YOUR CARD")
        exit()
    try:                                            # Blok exception handler.
        check = int(s)
        if strings == 1:                            # Jika return yang diminta string.
            return str(s)
        else:
            return int(s)
    except ValueError:                              # Jika konversi gagal terjadi.
        if BHS == "INDO":
            print("MASUKKAN TIDAK DIKETAHUI")
        elif BHS == "ENGLISH":
            print("UNKNOWN INPUT")
        else:                                       # Jika BHS tidak terinisiasi
            print("MASUKKAN TIDAK DIKETAHUI")       # dengan bahasa yang ada.
            print("UNKNOWN INPUT")
        return xcpinput(BHS,strings)

#########################################################################

##################### Prosedur memperbarui database #####################
def updatedatabase():
    # Inisiasi format writing.
    book = xlsxwriter.Workbook('EncryptedDbase.xlsx')              # Membuka db.xlsx.
    sheet = book.add_worksheet("Sheet1")               # Membuka sheet1.
    sheet.set_column(0, 4, 25)                         # Mengganti ukuran kolom indeks 0 hingga 4, menjadi 25.
    form = book.add_format({'align': 'center'})        # Format dasar untuk write.
    # Menulis baris paling atas dengan PIN SALDO NO REK dan PEMILIK, dengan format text form
    sheet.write(0, 0, "PIN", form)
    sheet.write(0, 1, "SALDO", form)
    sheet.write(0, 2, "NO REK", form)
    sheet.write(0, 3, "PEMILIK", form)
    sheet.write(0, 4, "ISI MESIN", form)
    # Menulis ulang data yang telah disimpan oleh program pada memori
    for i in range (10):
        sheet.write(i + 1, 0, pindb[i], form)          # Semua write dalam strings
        sheet.write(i + 1, 1, ibalance[i], form)
        sheet.write(i + 1, 2, account[i], form)
        sheet.write(i + 1, 3, owner[i])
    sheet.write(1, 4, cash[0], form)
    book.close()                                       # Tutup db.xlsx dan keluar
    return
#########################################################################

########################## Prosedur print quit ##########################
def qut(BHS,ty):                        # Karena mengetik print
    if BHS == "INDO":                   # satu-satu membosankan.
        print("SILAHKAN AMBIL KARTU ANDA")
        if ty == 1:
            print("TERIMA KASIH TELAH MENGGUNAKAN ATM BANK BANG")
    elif BHS == "ENGLISH":
        print("PLEASE TAKE YOUR CARD")
        if ty == 1:
            print("THANK YOU FOR USING BANK BANG ATM")
#########################################################################

########################## Prosedur print uang ##########################
# Pengeprintan uang dengan style x,xxx,xxx,xxx
def prtmn(bal):
    ln = len(str(bal))
    st = '{:' + str(ln) + ',.0f}'
    pr = str(st.format(bal))
    return pr
#########################################################################




####################### Prosedur Bahasa Indonesia #######################
def indo():
    BHS = "INDO"                # Inisiasi bahasa yang digunakan.
    balance = ibalance[idx]     # Inisiasi saldo akun.
    internalacc = accnum        # Inisiasi rek user
    while True:                 # Meskipun True, semua jalur memiliki return atau continue.
##### Blok Pengecekan PIN #####
        correct = False
        print("MASUKKAN PIN ATM ANDA")
        inp = sha512(xcpinput(BHS,1).encode('utf-8')).hexdigest()
        pin = pindb[idx]
        if pin == inp:             # Pengecekan pin salah atau benar.
            correct = True
        cnt = 0
        while(correct == False):    # Jika pin yang dimasukkan salah.
            print("PIN SALAH")
            cnt += 1
            if(cnt == 3):
                print("ANDA TELAH MEMASUKKAN PIN YANG SALAH SEBANYAK 3 KALI.")
                qut(BHS,0)
                return
            print("ANDA MEMILIKI", 3 - cnt, "KESEMPATAN LAGI UNTUK MEMASUKKAN PIN ANDA")
            print("MASUKKAN PIN ATM ANDA")
            inp = sha512(xcpinput(BHS,1).encode('utf-8')).hexdigest()
            if(pin == inp):
                correct = True
#####***************************************************************#####
        print("PILIH JENIS TRANSAKSI")      # Print menu transaksi.
        print("TEKAN BATAL UNTUK MEMBATALKAN TRANSAKSI")
        print("1. TRANSFER")
        print("2. PENARIKAN TUNAI")
        print("3. INFO SALDO")
        print("4. UBAH PIN")
        trans = xcpinput(BHS)               # Input menu yang diinginkan user.
# Jika user memilih menu transfer uang.
        if(trans == 1):
            while True:                     # Dilakukan permintaan no. rek terus menerus.
                print("MASUKKAN NO. REKENING YANG DITUJU")
                dacc = xcpinput(BHS,1)
                eacc = sha512(dacc.encode('utf-8')).hexdigest()
                print("APAKAH NO. REKENING PENERIMA SUDAH BENAR")
                print("1. BENAR")
                print("2. ULANGI")
                temp = xcpinput(BHS)
                if temp == 2:
                    continue                # Jika user masih ingin input rek lagi.
                elif eacc == accnum:
                    print("NO. REKENING TIDAK VALID")
                    continue                # Jika no rek user adalah milik sendiri.
                elif temp == 1:
                    try:
                        acctoowner[eacc]     # Handler ketika no. rek nasabah penerima tidak ada
                    except KeyError:
                        print("NO. REKENING TIDAK DITEMUKAN")
                        continue
                    break                   # Melanjutkan prosedur transfer uang.
            print("MASUKKAN JUMLAH UANG YANG AKAN DITRANSFER")
            money = xcpinput(BHS)           # Input jumlah transfer user.
            if(money > balance):
                print("MAAF, SALDO ANDA TIDAK MENCUKUPI UNTUK TRANSAKSI INI")
                qut(BHS,0)                  # Jika saldo user tidak mencukupi,
                return                      # batalkan transfer dan keluar.
            else:
                print("ANDA AKAN MENTRANSFER UANG SEBESAR RP" + prtmn(money), "PADA REKENING BERIKUT:")
                print("NO REK :", dacc)
                print("NAMA :", acctoowner[eacc])
                print("APAKAH ANDA YAKIN UNTUK MELAKUKAN TRANSAKSI INI?")
                print("1. YA")
                print("2. TIDAK")
                respon = xcpinput(BHS)      # Konfirmasi transfer.
                if(respon == 1):
                    balance -= money
                    for i in range (10):    # Mencari akun penerima dan pengirim.
                        if(account[i] == eacc):
                            ibalance[i] += money    # Mengganti saldo penerima & pengirim.
                            ibalance[idx] = balance
                    updatedatabase()        # Pembaruan database
                    print("TRANSAKSI BERHASIL")
                    print("SALDO ANDA")
                    print("RP" + prtmn(balance),"\n")
                    qut(BHS,1)              # Print keluar.
                else:
                    print("TRANSAKSI DIBATALKAN")
                    qut(BHS,0)              # Print keluar tanpa ty.
                return                      # Keluar dari bank.
# Jika user memilih penarikan uang.
        elif(trans == 2):
            while True:                 # Terus menerus meminta input penarikan yang valid.
                print("MASUKKAN JUMLAH PENARIKAN TUNAI YANG ANDA AKAN INGINKAN")
                print("(DALAM KELIPATAN RP50,000)")
                print("MAKSIMAL RP1,500,000")
                money = xcpinput(BHS)   # Input uang yang akan ditransfer.
                if cash[0] < money:
                    print("MAAF, UANG DALAM MESIN TIDAK MENCUKUPI UNTUK PENARIKAN SEJUMLAH INI")
                    qut(BHS, 0)
                if(money % 50000 == 0 and money <= 1500000):
                    if(money <= balance):
                        break           # Uang cukup, dan dilanjutkan proses penarikan.
                    elif(money > balance):
                        print("MAAF, SALDO ANDA TIDAK MENCUKUPI UNTUK PENARIKAN SEJUMLAH INI")
                        qut(BHS,0)
                        return          # Uang tidak cukup, keluar.
                else:
                    print("JUMLAH TIDAK VALID\n\n")
            balance -= money            # Pengurangan uang milik rekening user.
            ibalance[idx] = balance
            cash[0] -= money
            updatedatabase()            # Perbarui database dengan data yang baru.
            print("SILAKAN AMBIL UANG ANDA")
            qut(BHS,1)                  # Print pesan keluar dan keluar.
            return
# Jika user memilih cek saldo.
        elif(trans == 3):
            print("SALDO REKENING ANDA")
            print("RP" + prtmn(balance))    # Print uang dengan style angka uang.
            print("\n")
            print("TRANSAKSI LAGI?")
            print("1. YA")
            print("2. TIDAK")
            ans = xcpinput(BHS)             # Input user untuk transaksi lain.
            if(ans == 1):
                continue                    # Jika masih ingin transaksi, kembalikan pada atas, while True.
            else:
                qut(BHS,1)
                return                      # Print keluar dan keluar.
# Jika user memilih mengganti pin.
        elif(trans == 4):
            while True:
                print("MASUKKAN PIN BARU UNTUK REKENING ANDA")
                print("(PIN TERDIRI DARI 6 ANGKA)")     # Print batasan ganti pin.
                inpnew1 = xcpinput(BHS,1)
                newpin = sha512(inpnew1.encode('utf-8')).hexdigest()
                if len(inpnew1) != 6:                    # Jika panjang pin tidak 6 digit.
                    print("PIN TIDAK VALID")
                    print("\n")
                    continue                            # Kembalikan lagi pada while dalam transaksi 4.
                else:                                   # Jika pin sudah memenuhi kriteria.
                    print("KONFIRMASI PIN BARU ANDA")
                    inpnew2 = xcpinput(BHS,1)
                    cfmpin = sha512(inpnew2.encode('utf-8')).hexdigest()
                    if cfmpin == newpin:                # Konfirmasi pin.
                        break                           # Jika sudah benar lanjutkan prosedur penggantian.
                    else:
                        print("PIN TIDAK COCOK")        # Jika pin tidak cocok dengan pin baru,
                        continue                        # kembalikan pada loop transaksi 4.
            pindb[idx] = newpin                         # Penggantian pin user dengan yang baru.
            updatedatabase()                            # Pembaruan database.
            print("PIN ANDA BERHASIL DIUBAH")           # Print transaksi lain.
            print("TRANSAKSI LAGI?")
            print("1. YA")
            print("2. TIDAK")
            ans = xcpinput(BHS)                         # Input transaksi lain.
            if(ans == 1):
                continue                                # Kembalikan pada awal loop while.
            else:
                qut(BHS,1)                              # Print keluar dan keluar.
                return
#########################################################################

######################## Prosedur Bahasa Inggris ########################
def english():
    cash = dbase.loc[0, "ISI MESIN"]
    BHS = "ENGLISH"             # Kode bahasa Inggris dan Indonesia sama
    balance = ibalance[idx]     # Inisiasi saldo akun.
    internalacc = accnum
    while True:
##### Blok Pengecekan PIN #####
        correct = False
        print("INSERT YOUR ATM PIN")
        inp = sha512(xcpinput(BHS,1).encode('utf-8')).hexdigest()
        pin = pindb[idx]
        if(inp == pin):
            correct = True
        cnt = 0
        while(correct == False):
            print("INVALID PIN")
            cnt += 1
            if(cnt == 3):
                print("YOU HAVE INSERTED INVALID PIN 3 TIMES")
                qut(BHS,0)
                return
            print("YOU HAVE", 3 - cnt, "CHANCES LEFT TO INSERT YOUR PIN")
            print("INSERT YOUR PIN")
            inp = sha512(xcpinput(BHS,1).encode('utf-8')).hexdigest()
            if(inp == pin):
                correct = True
#####***************************************************************#####
        print("PICK TRANSACTION MENU")
        print("PRESS CANCEL TO ABORT TRANSACTION")
        print("1. TRANSFER")
        print("2. WITHDRAW CASH")
        print("3. BALANCE INFO")
        print("4. CHANGE PIN")
        trans = xcpinput(BHS)
# Jika user memilih transfer uang
        if(trans == 1):
            while True:
                print("INSERT ACCOUNT NUMBER FOR TRANSFER")
                dacc = xcpinput(BHS,1)
                eacc = sha512(dacc.encode('utf-8')).hexdigest()
                print("IS RECIPIENT ACCOUNT NUMBER RIGHT")
                print("1. PROCEED")
                print("2. OTHER ACCOUNT")
                temp = xcpinput(BHS)
                if temp == 2:
                    continue                # Jika user masih ingin input rek lagi.
                elif eacc == accnum:
                    print("INVALID ACCOUNT NUMBER")
                    continue                # Jika no rek user adalah milik sendiri.
                elif temp == 1:
                    try:
                        acctoowner[eacc]     # Handler ketika no. rek nasabah penerima tidak ada
                    except KeyError:
                        print("ACCOUNT NOT FOUND")
                        continue
                    break                   # Melanjutkan prosedur transfer uang.
            print("INSERT BALANCE TO BE TRANSFERED")
            money = xcpinput(BHS)
            if(money > balance):
                print("YOUR BALANCE IS INSUFFICIENT FOR THIS TRANSACTION")
                qut(BHS,0)
                return
            else:
                print("YOU WILL TRANSFER RP" + prtmn(money), "BALANCE TO THIS ACCOUNT:")
                print("ACCOUNT NUMBER :", dacc)
                print("NAME :", acctoowner[eacc])
                print("ARE YOU SURE FOR THIS TRANSACTION?")
                print("1. YES")
                print("2. NO")
                respon = xcpinput(BHS)
                if(respon == 1):
                    balance -= money
                    for i in range (10):
                        if(account[i] == eacc):
                            ibalance[i] += money
                            ibalance[idx] = balance
                    updatedatabase()
                    print("TRANSACTION SUCCEED")
                    print("YOUR BALANCE")
                    print("RP" + prtmn(balance),"\n")
                    qut(BHS,1)
                else:
                    print("TRANSACTION CANCELED")
                    qut(BHS,0)
                return
# Jika user memilih ambil uang
        elif(trans == 2):
            while True:
                print("INSERT WITHDRAW BALANCE")
                print("(IN MULTIPLE OF RP50,000)")
                print("MAXIMUM RP1,500,000")
                money = xcpinput(BHS)
                if cash[0] < money:
                    print("SORRY, WE HAVE INSUFFICIENT BALANCE FOR THIS TRANSACTION")
                    qut(BHS, 0)
                if(money % 50000 == 0 and money <= 1500000):
                    if(money <= balance):
                        break           # Uang cukup, dan dilanjutkan proses penarikan.
                    elif(money > balance):
                        print("INSUFFICIENT BALANCE FOR THIS TRANSACTION")
                        qut(BHS,0)
                        return          # Uang tidak cukup, keluar.
                else:
                    print("INVALID AMOUNT OF MONEY\n\n")
            balance -= money
            ibalance[idx] = balance
            cash[0] -= money
            updatedatabase()
            print("PLEASE TAKE YOUR MONEY")
            qut(BHS,1)
            return
# Jika user memilih cek saldo
        elif(trans == 3):
            print("YOUR ACCOUNT BALANCE")
            print("RP" + prtmn(balance))
            print("\n")
            print("DO OTHER TRANSACTION?")
            print("1. YES")
            print("2. NO")
            ans = xcpinput(BHS)
            if(ans == 1):
                continue
            else:
                qut(BHS,1)
                return
# Jika user memilih ganti pin
        elif(trans == 4):
            while True:
                print("INSERT YOUR NEW PIN")
                print("(YOUR NEW PIN MUST CONTAIN 6 DIGIT)")
                inpnew1 = xcpinput(BHS,1)
                newpin = sha512(inpnew1.encode('utf-8')).hexdigest()
                if len(inpnew1) != 6:
                    print("INVALID PIN")
                    print()
                    continue
                else:
                    print("CONFIRM YOUR NEW PIN")
                    inpnew2 = xcpinput(BHS,1)
                    cfmpin = sha512(inpnew2.encode('utf-8')).hexdigest()
                    if cfmpin == newpin:
                        break
                    else:
                        print("PIN DOESNT MATCH")
                        continue
            pindb[idx] = newpin
            updatedatabase()
            print("YOUR PIN HAS BEEN CHANGED")
            print("DO OTHER TRANSACTION?")
            print("1. YES")
            print("2. NO")
            ans = xcpinput(BHS)
            if(ans == 1):
                continue
            else:
                qut(BHS,1)
                return
#########################################################################

############################# Main function #############################
print("SELAMAT DATANG DI ATM BANK BANG")
print("WELCOME TO BANK BANG ATM")
print();print();print();
print("MASUKKAN KARTU ATM ANDA")
print("INSERT YOUR ATM CARD")
accnum = sha512(str(xcpinput(0,1)).encode('utf-8')).hexdigest()
for i in range (10):                # Pengecekan apakah no rekening ada.
    if(accnum == account[i]):
        idx = i
if(idx == -1):                      # Jika no rekening tidak ada yang cocok,
    exit()                          # Maka idx akan tetap -1 seperti pada inisiasi.
for i in range (25):                # Python tidak ada clear screen.
    print("\n")
# Loop utama
while True:
    print("PILIH BAHASA")
    print("LANGUAGE PREFERENCE")
    print("1. INDONESIA")
    print("2. ENGLISH")
    l = xcpinput(0)                 # Karena bahasa belum ditentukan, maka digunakan 0.
    if(l == 1):
        indo()
        break
    elif(l == 2):
        english()
        break
    else:
        print("PILIHANNYA CUMA 2 GAN")
#########################################################################
