import Global
from B01 import lcg

# TODO : 
def bangun(pembangun : str) -> None:
    pasir = lcg(1,5)
    batu = lcg(1,5)
    air = lcg(1,5)
    if Global.bahan_bangunan.pasir >= pasir and Global.bahan_bangunan.batu >= batu and Global.bahan_bangunan.air >= air:
        Global.bahan_bangunan.pasir -= pasir
        Global.bahan_bangunan.batu -= batu
        Global.bahan_bangunan.air -= air
        byk = cari_banyak_candi(Global.candi)
        if byk == 100:
            print("Candi berhasil dibangun.")
            print("Sisa candi yang perlu dibangun: 0")
        else:
            id = lowest_idx(Global.candi)
            Global.candi.idx[id].id = id+1
            Global.candi.idx[id].username = pembangun
            Global.candi.idx[id].pasir = pasir
            Global.candi.idx[id].batu = batu
            Global.candi.idx[id].air = air
            print(id)
            if id == Global.candi.Neff:
                Global.candi.Neff += 1
            print("Candi berhasil dibangun.")
            print(f"Sisa candi yang perlu dibangun: {100 - (byk + 1)}")
    else:
        pass
# TODO : 
def cari_banyak_candi(obj : any) -> int:
    res = 0
    for i in range(obj.Neff):
        if obj.idx[i].pasir != 0 and obj.idx[i].batu != 0 and obj.idx[i].air != 0:
            res += 1
    return res

# TODO : 
def lowest_idx(obj : any) -> int:
    for i in range(obj.Neff):
        if obj.idx[i].pasir == 0 and obj.idx[i].batu == 0 and obj.idx[i].air == 0:
            return i
    return obj.Neff
