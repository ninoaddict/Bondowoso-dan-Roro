from Global import Candi, Bahan_Bangunan, User
from B01 import lcg

# TODO : 
def bangun(pembangun : str, candi : Candi, bahan_bangunan : Bahan_Bangunan) -> None:
    pasir = lcg(1,5)
    batu = lcg(1,5)
    air = lcg(1,5)
    if bahan_bangunan.pasir >= pasir and bahan_bangunan.batu >= batu and bahan_bangunan.air >= air:
        bahan_bangunan.pasir -= pasir
        bahan_bangunan.batu -= batu
        bahan_bangunan.air -= air
        byk = cari_banyak_candi(candi)
        if byk == 100:
            print("Candi berhasil dibangun.")
            print("Sisa candi yang perlu dibangun: 0")
        else:
            id = lowest_idx(candi)
            candi.idx[id].id = id+1
            candi.idx[id].username = pembangun
            candi.idx[id].pasir = pasir
            candi.idx[id].batu = batu
            candi.idx[id].air = air
            if id == candi.Neff:
                candi.Neff += 1
            print("Candi berhasil dibangun.")
            print(f"Sisa candi yang perlu dibangun: {100 - (byk + 1)}")
    else:
        pass
# TODO : 
def cari_banyak_candi(obj : Candi) -> int:
    res = 0
    for i in range(obj.Neff):
        if obj.idx[i].pasir != 0 and obj.idx[i].batu != 0 and obj.idx[i].air != 0:
            res += 1
    return res

# TODO : 
def lowest_idx(obj : Candi) -> int:
    for i in range(obj.Neff):
        if obj.idx[i].pasir == 0 and obj.idx[i].batu == 0 and obj.idx[i].air == 0:
            return i
    return obj.Neff
