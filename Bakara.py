import random
def toranpu_():
    torannpu = []
    suuti = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    ma_ku = ["♡","♤","♧","♢"]
    for i in suuti:
        for j in ma_ku:
            torannpu.append(i+j)
    return torannpu

def haihu_(torannpu):
    fs_deta = 0
    fs = random.choice(torannpu)
    torannpu.remove(fs)
    if fs[0] == "J" or fs[0] == "Q" or fs[0] == "K" or fs[0] == "1":
        fs_deta += 0
    elif fs[0] == "A":
        fs_deta += 1
    else:
        fs_deta += int(fs[0])
    return  fs_deta

def haihu_2():
    sc = 0
    for i in range(2):
        sc += haihu_(torannpu)
    if sc >= 10:
        sc_deta = sc - 10
    else:
        sc_deta = sc
    return sc_deta

def hanntei_(pl,bn):
    if pl >= 8 or bn >= 8:
        if bn > pl:
            cs = 1
        elif bn< pl:
            cs = 2
        else:
            cs = 3
    elif pl <= 5 and bn == 7:
        pl += haihu_(torannpu)
    
    elif pl >= 6 and bn <= 5:
        bn += haihu_(torannpu)

    elif pl <= 5 and bn <= 2:
        pl += haihu_(torannpu)
        bn += haihu_(torannpu)

    elif pl <= 5:
        pl += haihu_(torannpu)

        if pl >= 8:
            pass
        elif (pl >= 0 and pl < 8 and bn == 3) or (pl >= 2 and pl <= 7 and bn == 4) or (pl >= 4 and pl <= 7 and bn == 5) or (pl == 6 or pl == 7 and bn == 6):
            bn += haihu_(torannpu)
            
    if pl >= 10:
        pl_rst = pl-10
    else:
        pl_rst = pl

    if bn >= 10:
        bn_rst = bn -10
    else:
        bn_rst = bn

    if bn_rst > pl_rst:
        cs = 1
    elif bn_rst < pl_rst:
        cs = 2
    else:
        cs = 3
    return cs 
def hanntei_2(mny,bet,cs):
    if bet == cs:
        if cs == 1:
            print("賞金" + str(int(mny * 195 / 100 )))
        elif cs == 2:
            print("賞金" + str(mny * 2))
        else:
            print("賞金" + str(mny * 9))
    else:
        print("賞金なし")

mny = int(input("賭け金を >"))
bet =int(input("対象を バンカー:1 プレイヤー:2　タイ:3 >"))
torannpu = toranpu_()
pl = haihu_2()
bn = haihu_2()
print("プレイヤー" + str(pl))
print("バンカー" + str(bn))
cs = hanntei_(pl,bn)
hanntei_2(mny,bet,cs)
print(torannpu)