from Global import User, Candi

# TODO : return jin index
def check_username(user : User, username : str) -> int:
    for i in range(user.Neff):
        if user.idx[i].username == username:
            return i
    return -1

# TODO : delete jin
def hapusjin(user : User, candi : Candi) -> None:
    username = input("Masukkan username jin: ")
    id = check_username(user, username)
    if id == -1:
        print("\nTidak ada jin dengan username tersebut.")
    else:
        konfirmasi = input("Apakah anda yakin ingin menghapus jin dengan username Jin1 (Y/N)? ")
        if konfirmasi == "Y":
            # hapus candi yang dibangun username
            for i in range(candi.Neff):
                if candi.idx[i].username == username:
                    candi.idx[i].username = 0
                    candi.idx[i].pasir = 0
                    candi.idx[i].batu = 0
                    candi.idx[i].air = 0
            # hapus user dari list of user
            switch = False
            for i in range(user.Neff + 1):
                if i == id:
                    switch = True
                elif switch:
                    user.idx[i-1] = user.idx[i]
            user.Neff -= 1