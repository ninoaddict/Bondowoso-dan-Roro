import Global

# TODO : return jin index
def check_username(obj : any, username : str) -> int:
    for i in range(obj.Neff):
        if obj.idx[i].username == username:
            return i
    return -1

# TODO : change jin type
def ubahjin() -> None:
    username = input("Masukkan username jin : ")
    id = check_username(Global.user, username)
    if id == -1:
        print("\nTidak ada jin dengan tipe tersebut.")
    else:
        type = Global.user.idx[id].role
        if type == "jin_pembangun":
            jin_type = "Pembangun"
            jin_type_change = "Pengumpul"
            change = "jin_pengumpul"
        else:
            jin_type = "Pengumpul"
            jin_type_change = "Pembangun"
            change = "jin_pembangun"
        konfirmasi = input(f"Jin ini bertipe “{jin_type}”. Yakin ingin mengubah ke tipe “{jin_type_change}”? ")
        if konfirmasi == "Y":
            print("\nJin telah berhasil diubah.")
            Global.user.idx[id].role = change