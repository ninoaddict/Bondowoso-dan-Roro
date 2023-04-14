from Global import Candi
def cari_banyak_candi(candi : Candi) -> int:
    res = 0
    for i in range(candi.Neff):
        if candi.idx[i].pasir != 0 and candi.idx[i].batu != 0 and candi.idx[i].air != 0:
            res += 1
    return res

def ayamberkokok(candi : Candi) -> None:
    banyak_candi = cari_banyak_candi(candi)
    print("Kukuruyuk.. Kukuruyuk..")
    print(f'\nJumlah Candi: {banyak_candi}')
    if banyak_candi >= 100:
        print('\nYah, Bandung Bondowoso memenangkan permainan!')
    else:
        print("*Bandung Bondowoso angry noise*")
        print("Roro Jonggrang dikutuk menjadi candi.")
    exit()
