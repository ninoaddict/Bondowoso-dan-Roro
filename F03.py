from Global import User
# TODO : return username idx
def username_idx(user : User, username : str) -> None:
    for i in range(user.Neff):
        if user.idx[i].username == username:
            return i
    return -1

# TODO : summonjin
def summonjin(user : User) -> None:
    if user.Neff < 103:
        print("Jenis jin yang dapat dipanggil:")
        print(f" (1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
        print(f" (2) Pembangun - Bertugas membangun candi \n")

        # input validation
        masukan = int(input("Masukan nomor jenis jin yang ingin dipanggil: "))
        while masukan != 1 and masukan != 2:
            print(f"\nTidak ada jenis jin bernomor “{masukan}”!\n")
            masukan = int(input("Masukkan nomor jenis jin yang ingin dipanggil: "))

        # username validation
        username = input("Masukkan username jin: ")
        while username_idx(user, username) != -1:
            print(f"\nUsername “{username} sudah diambil!”\n")
            username = input("Masukkan username jin: ")
        
        # password validation
        password = input("Masukkan password jin: ")
        while len(password) < 5 or len(password) > 25:
            print("\nPassword panjangnya harus 5-25 karakter!\n")
            password = input("Masukkan password jin: ")
        print("\nMengumpulkan sesajen...")
        print("Menyerahkan sesajen...")
        print("Membacakan mantra...\n")
        print(f"Jin {username} berhasil dipanggil!")

        # add jin to user 
        N = user.Neff
        if masukan == 1:
            type_jin = "jin_pengumpul"
        else:
            type_jin = "jin_pembangun"
        user.idx[N].username = username
        user.idx[N].password = password
        user.idx[N].role = type_jin
        user.Neff += 1