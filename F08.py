import Global
from B01 import lcg

def banyak_type_jin(obj : any, type : str):
    ans = 0
    for i in range(obj.Neff):
        if obj.idx[i].role == type:
            ans += 1
    return ans

def cari_banyak_candi(obj : any) -> int:
    res = 0
    for i in range(obj.Neff):
        if obj.idx[i].pasir != 0 and obj.idx[i].batu != 0 and obj.idx[i].air != 0:
            res += 1
    return res

def batchkumpul() -> None:
    banyak_pengumpul = banyak_type_jin(Global.user, "jin_pengumpul")
    if banyak_pengumpul > 0:
        pasir = batu = air = 0
        for i in range(banyak_pengumpul):
            pasir += lcg(0,5)
            batu += lcg(0,5)
            air += lcg(0,5)
        Global.bahan_bangunan.pasir += pasir
        Global.bahan_bangunan.batu += batu
        Global.bahan_bangunan.air += air
        print(f"Mengerahkan {banyak_pengumpul} untuk mengumpulkan bahan.")
        print(f"Jin menemukan {pasir} pasir, {batu} batu, dan {air} air.")
    else:
        print("Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.")

def batchbangun() -> None:
    banyak_pembangun = banyak_type_jin(Global.user, "jin_pembangun")
    if banyak_pembangun > 0:
        pasir = batu = air = 0
        bahan_candi = [[0 for i in range(3)] for j in range(banyak_pembangun)]
        for i in range(banyak_pembangun):
            bahan_candi[i][0] = lcg(1,5)
            bahan_candi[i][1] = lcg(1,5)
            bahan_candi[i][2] = lcg(1,5)
            pasir += bahan_candi[i][0]
            batu += bahan_candi[i][1]
            air += bahan_candi[i][2]
        print(f"Mengerahkan {banyak_pembangun} untuk membangun candi dengan total bahan {pasir} pasir, {batu} batu, {air} air.")
        if Global.bahan_bangunan.pasir >= pasir and Global.bahan_bangunan.batu >= batu and Global.bahan_bangunan.air >= air:
            print(f"Jin berhasil membangun total {banyak_pembangun} candi.")
            banyak_candi = cari_banyak_candi(Global.candi)
            Global.bahan_bangunan.pasir -= pasir
            Global.bahan_bangunan.batu -= batu
            Global.bahan_bangunan.air -= air
            j = id = 0
            list_of_pembangun = [0 for i in range(banyak_pembangun)]
            for i in range(Global.user.Neff):
                if Global.user.idx[i].role == "jin_pembangun":
                    list_of_pembangun[j] = Global.user.idx[i].username
                    j += 1
            j = 0
            while id < 1000 and j < banyak_pembangun:
                if banyak_candi == 100:
                    break
                elif Global.candi.idx[id].pasir == 0 and Global.candi.idx[id].batu == 0 and Global.candi.idx[id].air == 0:
                    Global.candi.idx[id].id = id + 1
                    Global.candi.idx[id].username = list_of_pembangun[j]
                    Global.candi.idx[id].pasir = bahan_candi[j][0]
                    Global.candi.idx[id].batu = bahan_candi[j][1]
                    Global.candi.idx[id].air = bahan_candi[j][2]
                    if id == Global.candi.Neff:
                        Global.candi.Neff += 1
                    j += 1
                id += 1
        else:
            print(f"Bangun gagal. Kurang {max(pasir - Global.bahan_bangunan.pasir, 0)} pasir, {max(batu - Global.bahan_bangunan.batu, 0)} batu, dan {max(air - Global.bahan_bangunan.air, 0)} air.")
    else:
        print("Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.")