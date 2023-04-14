import Global

# TODO : return jin index
def check_username(obj : any, username : str) -> int:
    for i in range(obj.Neff):
        if obj.idx[i].username == username:
            return i
    return -1

# TODO : delete jin
def hapusjin() -> None:
    username = input("Masukkan username jin: ")
    id = check_username(Global.user, username)
    if id == -1:
        print("\nTidak ada jin dengan username tersebut.")
    else:
        konfirmasi = input("Apakah anda yakin ingin menghapus jin dengan username Jin1 (Y/N)? ")
        if konfirmasi == "Y":
            # hapus candi yang dibangun username
            for i in range(Global.candi.Neff):
                if Global.candi.idx[i].username == username:
                    Global.candi.idx[i].username = 0
                    Global.candi.idx[i].pasir = 0
                    Global.candi.idx[i].batu = 0
                    Global.candi.idx[i].air = 0
            # hapus user dari list of user
            switch = False
            for i in range(Global.user.Neff):
                if i == id:
                    switch = True
                elif switch:
                    Global.user.idx[i-1] = Global.user.idx[i]
            Global.user[Global.user.Neff-1].username = 0
            Global.user[Global.user.Neff-1].password = 0
            Global.user[Global.user.Neff-1].role = 0
            Global.user.Neff -= 1