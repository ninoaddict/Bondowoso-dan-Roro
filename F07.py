from Global import Bahan_Bangunan
from B01 import lcg

# TODO : 
def kumpul(bahan_bangunan : Bahan_Bangunan) -> None:
    pasir = lcg(0,5)
    batu = lcg(0,5)
    air = lcg(0,5)
    bahan_bangunan.pasir += pasir
    bahan_bangunan.batu += batu
    bahan_bangunan.air += air
    print(f"Jin menemukan {pasir} pasir, {batu} batu, dan {air} air.")