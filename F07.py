import Global
from B01 import lcg

# TODO : 
def kumpul() -> None:
    pasir = lcg(0,5)
    batu = lcg(0,5)
    air = lcg(0,5)
    Global.bahan_bangunan.pasir += pasir
    Global.bahan_bangunan.batu += batu
    Global.bahan_bangunan.air += air
    print(f"Jin menemukan {pasir} pasir, {batu} batu, dan {air} air.")