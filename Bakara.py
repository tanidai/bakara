import random
def Bakara_(mny,bet):
    bn_deta= 0
    pl_deta= 0
    pl = []
    bn = []
    torannpu = []
    suuti = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    ma_ku = ["♡","♤","♧","♢"]
    for i in suuti:
        for j in ma_ku:
            torannpu.append(i+j)

    for i in range(2):
            pl_0 = random.choice(torannpu)
            pl.append(pl_0)
            torannpu.remove(pl_0)        
            bn_0 = random.choice(torannpu)
            bn.append(bn_0)
            torannpu.remove(bn_0)

        
    for i in pl:
        pl_1 = i[0]
        if pl_1 == "J" or pl_1 == "Q" or pl_1 == "K" or pl_1 == "1":
            pl_deta += 0
        elif pl_1 == "A":
            pl_deta += 1
        else:
            pl_deta += int(pl_1)

    for i in bn:
        bn_1 = i[0]
        if bn_1 == "J" or bn_1 == "Q" or bn_1 == "K" or bn_1 == "1":
            bn_deta += 0
        elif bn_1 == "A":
            bn_deta += 1
        else:
            bn_deta += int(bn_1)

    if pl_deta >= 10:
        pl_2 = pl_deta-10
    else:
        pl_2 = pl_deta

    if bn_deta >= 10:
        bn_2 = bn_deta-10
    else:
        bn_2 = bn_deta



    if pl_2 >=8 or bn_2 >= 8:
        pl_rst = pl_2
        bn_rst = bn_2

    elif pl_2 == bn_2 and pl_2 >= 6:
        pl_rst = pl_2
        bn_rst = bn_2

    elif pl_2 <= 5 and bn_2 == 7:
        pl_3 = random.choice(torannpu)
        pl.append(pl_3)
        torannpu.remove(pl_3)
        pl_4 = pl_3[0]
        if pl_4 == "J" or pl_4== "Q" or pl_4 == "K" or pl_4 == "1":
            pl_2 += 0
        elif pl_4 == "A":
            pl_2 += 1
        else:
            pl_2 += int(pl_4)

    elif pl_2 >= 6 and bn_2 <= 5:
            bn_3 = random.choice(torannpu)
            bn.append(bn_3)
            torannpu.remove(bn_3)
            bn_4 = bn_3[0]
            if bn_4 == "J" or bn_4 == "Q" or bn_4 == "K" or bn_4 == "1":
                bn_2 += 0
            elif bn_4 == "A":
                bn_2 += 1
            else:
                bn_2 += int(bn_4)

    elif pl_2 <= 5 and bn_2 <= 2:
        pl_3 = random.choice(torannpu)
        pl.append(pl_3)
        torannpu.remove(pl_3)
        pl_4 = pl_3[0]
        if pl_4 == "J" or pl_4 == "Q" or pl_4 == "K" or pl_4 == "1":
            pl_2 += 0
        elif pl_4 == "A":
            pl_2+= 1
        else:
            pl_2 += int(pl_4)
        bn_3 = random.choice(torannpu)
        torannpu.remove(bn_3)
        bn.append(bn_3)
        bn_4 = bn_3[0]
        if bn_4 == "J" or bn_4 == "Q" or bn_4 == "K" or bn_4 == "1":
            bn_2 += 0
        elif bn_4 == "A":
            bn_2 += 1
        else:
            bn_2 += int(bn_4)


    elif pl_2 <= 5:
        pl_3  = random.choice(torannpu)
        pl.append(pl_3)
        torannpu.remove(pl_3)
        pl_4 = pl_3[0]
        if pl_4 == "J" or pl_4 == "Q" or pl_4 == "K" or pl_4 == "1":
            pl_2 += 0
        elif pl_4 == "A":
            pl_2 += 1
        else:
            pl_2 += int(pl_4)

        if pl_2 >= 8:
            pass

        elif (pl_2 >= 0 and pl_2 <= 8 and bn_2 == 3) or (pl_2 >= 2 and pl_2 <= 7 and bn_2 == 4) or (pl_2 >= 4 and pl_2 <= 7 and bn_2 == 5) or (pl_2 == 6 and pl_2 == 7 and bn_2 == 6):
            bn_3 = random.choice(torannpu)
            bn.append(bn_3)
            torannpu.remove(bn_3)
            bn_4 = bn_3[0]
            if bn_4 == "J" or bn_4 == "Q" or bn_4 == "K" or bn_4 == "1":
                bn_2 += 0
            elif bn_4 == "A":
                bn_2 += 1
            else:
                bn_2 += int(bn_4)
    if pl_2 >= 10:
        pl_rst = pl_2-10
    else:
        pl_rst = pl_2

    if bn_2 >= 10:
        bn_rst = bn_2 -10
    else:
        bn_rst = bn_2
    if bn_rst > pl_rst:
        Rst = ("バンカー")
        ban = 1
        if ban == bet:
            print("賞金" + str((int(mny) * 195) // 100))
        else:
            print("賞金なし")
    elif bn_rst < pl_rst:
        Rst = ("プレイヤー")
        ban = 2
        if ban == bet :
            print("賞金" + str(int(mny) * 2))
        else:
            print("賞金なし")
    else:
        Rst = ("引き分け")
        ban = 3
        if ban == bet:
            print("賞金" + str(int(mny) * 9))
        else:
            print("賞金なし")
    print(Rst)
    print(pl)
    print(bn)

mny = int(input("賭け金を >"))
bet =int(input("対象を バンカー:1 プレイヤー:2　タイ:3 >"))
Bakara_(mny,bet)