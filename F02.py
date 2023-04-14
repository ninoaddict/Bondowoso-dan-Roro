import Global

# TODO : 
def logout() -> None:
    if Global.ID == -1:
        print("Logout gagal!")
        print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")
    else:
        Global.ID = -1
        print()