from Global import Candi

def hancurkancandi(candi : Candi):
    masukan = int(input("Masukkan ID candi: "))
    if candi.idx[masukan-1].pasir == 0:
        print("\nTidak ada candi dengan ID tersebut.")
    else:
        konfirmasi = input(f"Apakah anda yakin ingin menghancurkan candi ID: {masukan} (Y/N)? ")
        if konfirmasi == 'Y':
            print("\nCandi telah berhasil dihancurkan.")
            candi.idx[masukan-1].username = 0
            candi.idx[masukan-1].pasir = 0
            candi.idx[masukan-1].batu = 0
            candi.idx[masukan-1].air = 0