from F01 import login
from F02 import logout
from F03 import summonjin
from F04 import hapusjin
from F05 import ubahjin
from F06 import bangun
from F07 import kumpul
from F08 import batchbangun, batchkumpul
from F09 import laporanjin
from F10 import laporancandi
from F11 import hancurkancandi
from F12 import ayamberkokok
from F13 import load
from F14 import save
from F16 import exit
import Global

# MAIN PROGRAM
# load main program and files
load()

# run commands
while True:
    masukan = input(">>> ")
    if masukan == "login":
        login()
    elif masukan == "logout":
        logout()
    elif masukan == "summonjin" and Global.ID != -1 and Global.user.idx[Global.ID].role == "bandung_bondowoso":
        summonjin()
    elif masukan == "hapusjin" and Global.ID != -1 and Global.user.idx[Global.ID].role == "bandung_bondowoso":
        hapusjin()
    elif masukan == "ubahjin" and Global.ID != -1 and Global.user.idx[Global.ID].role == "bandung_bondowoso":
        ubahjin()
    elif masukan == "bangun" and Global.ID != -1 and Global.user.idx[Global.ID].role == "jin_pembangun":
        bangun(Global.user.idx[Global.ID].username)
    elif masukan == "kumpul" and Global.ID != -1 and Global.user.idx[Global.ID].role == "jin_pengumpul":
        kumpul()
    elif masukan == "batchkumpul" and Global.ID != -1 and Global.user.idx[Global.ID].role == "bandung_bondowoso":
        batchkumpul()
    elif masukan == "batchbangun" and Global.ID != -1 and Global.user.idx[Global.ID].role == "bandung_bondowoso":
        batchbangun()
    elif masukan == "laporanjin" and Global.ID != -1 and Global.user.idx[Global.ID].role == "bandung_bondowoso":   
        laporanjin(Global.user, Global.bahan_bangunan, Global.candi)
    elif masukan == "laporancandi" and Global.ID != -1 and Global.user.idx[Global.ID].role == "bandung_bondowoso":
        laporancandi(Global.candi, Global.bahan_bangunan)
    elif masukan == "hancurkancandi" and Global.ID != -1 and Global.user.idx[Global.ID].role == "roro_jonggrang":
        hancurkancandi(Global.candi)
    elif masukan == "ayamberkokok" and Global.ID != -1 and Global.user.idx[Global.ID].role == "roro_jonggrang":
        ayamberkokok(Global.candi)
    elif masukan == "save":
        save(Global.user, Global.candi, Global.bahan_bangunan)
    elif masukan == "help":
        pass
    elif masukan == "exit":
        exit()