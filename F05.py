from Global import User

# TODO : return jin index
def check_username(user : User, username : str) -> int:
    for i in range(user.Neff):
        if user.idx[i].username == username:
            return i
    return -1

# TODO : change jin type
def ubahjin(user : User) -> None:
    username = input("Masukkan username jin : ")
    id = check_username(user, username)
    if id == -1:
        print("\nTidak ada jin dengan tipe tersebut.")
    else:
        type = user.idx[id].role
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
            user.idx[id].role = change