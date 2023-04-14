import Global

# TODO : login into an user
def login() -> None:
    if Global.ID != - 1:
        print("Login gagal!")
        print(f"Anda telah login dengan username {Global.user.idx[Global.ID].username}, silahkan lakukan “logout” sebelum melakukan login kembali.")
    else:
        username = input("Username: ")
        password = input("Password: ")
        for i in range(Global.user.Neff):
            if Global.user.idx[i].username == username:
                if Global.user.idx[i].password == password:
                    print(f"\nSelamat datang, {username}!")
                    print("Masukkan command “help” untuk daftar command yang dapat kamu panggil.")
                    Global.ID = i
                else:
                    print("\nPassword salah!")
                    Global.ID = -1
                return
        print("\nUsername tidak terdaftar!")