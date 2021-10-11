import random
def toranpu_():
    
    torannpu = []
    suuti = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    ma_ku = ["♡","♤","♧","♢"]
    for i in suuti:
        for j in ma_ku:
            torannpu.append(i+j)
    return torannpu

def Bakara_1(torannpu):
    fs = []
    for i in range(2):
            fs_0 = random.choice(torannpu)
            fs.append(fs_0)
            torannpu.remove(fs_0)
    for i in fs:
        fs_deta = 0
        fs_1 = i[0]
        if fs_1 == "J" or fs_1 == "Q" or fs_1 == "K" or fs_1 == "1":
            fs_deta += 0
        elif fs_1 == "A":
            fs_deta += 1
        else:
            fs_deta += int(fs_1)

    if fs_deta >= 10:
        sc_deta = fs_deta-10
    else:
        sc_deta = fs_deta
    return  sc_deta

    # elif pl_2 <= 5 and bn_2 == 7:
    #     pl_3 = random.choice(torannpu)
    #     pl.append(pl_3)
    #     torannpu.remove(pl_3)
    #     pl_4 = pl_3[0]
    #     if pl_4 == "J" or pl_4== "Q" or pl_4 == "K" or pl_4 == "1":
    #         pl_2 += 0
    #     elif pl_4 == "A":
    #         pl_2 += 1
    #     else:
    #         pl_2 += int(pl_4)

    # elif pl_2 >= 6 and bn_2 <= 5:
    #         bn_3 = random.choice(torannpu)
    #         bn.append(bn_3)
    #         torannpu.remove(bn_3)
    #         bn_4 = bn_3[0]
    #         if bn_4 == "J" or bn_4 == "Q" or bn_4 == "K" or bn_4 == "1":
    #             bn_2 += 0
    #         elif bn_4 == "A":
    #             bn_2 += 1
    #         else:
    #             bn_2 += int(bn_4)

    # elif pl_2 <= 5 and bn_2 <= 2:
    #     pl_3 = random.choice(torannpu)
    #     pl.append(pl_3)
    #     torannpu.remove(pl_3)
    #     pl_4 = pl_3[0]
    #     if pl_4 == "J" or pl_4 == "Q" or pl_4 == "K" or pl_4 == "1":
    #         pl_2 += 0
    #     elif pl_4 == "A":
    #         pl_2+= 1
    #     else:
    #         pl_2 += int(pl_4)
    #     bn_3 = random.choice(torannpu)
    #     torannpu.remove(bn_3)
    #     bn.append(bn_3)
    #     bn_4 = bn_3[0]
    #     if bn_4 == "J" or bn_4 == "Q" or bn_4 == "K" or bn_4 == "1":
    #         bn_2 += 0
    #     elif bn_4 == "A":
    #         bn_2 += 1
    #     else:
    #         bn_2 += int(bn_4)

    # elif pl_2 <= 5:
    #     pl_3  = random.choice(torannpu)
    #     pl.append(pl_3)
    #     torannpu.remove(pl_3)
    #     pl_4 = pl_3[0]
    #     if pl_4 == "J" or pl_4 == "Q" or pl_4 == "K" or pl_4 == "1":
    #         pl_2 += 0
    #     elif pl_4 == "A":
    #         pl_2 += 1
    #     else:
    #         pl_2 += int(pl_4)

    #     if pl_2 >= 8:
    #         pass

    #     elif (pl_2 >= 0 and pl_2 < 8 and bn_2 == 3) or (pl_2 >= 2 and pl_2 <= 7 and bn_2 == 4) or (pl_2 >= 4 and pl_2 <= 7 and bn_2 == 5) or (pl_2 == 6 or pl_2 == 7 and bn_2 == 6):
    #         bn_3 = random.choice(torannpu)
    #         bn.append(bn_3)
    #         torannpu.remove(bn_3)
    #         bn_4 = bn_3[0]
    #         if bn_4 == "J" or bn_4 == "Q" or bn_4 == "K" or bn_4 == "1":
    #             bn_2 += 0
    #         elif bn_4 == "A":
    #             bn_2 += 1
    #         else:
    #             bn_2 += int(bn_4)
    # if pl_2 >= 10:
    #     pl_rst = pl_2-10
    # else:
    #     pl_rst = pl_2

    # if bn_2 >= 10:
    #     bn_rst = bn_2 -10
    # else:
    #     bn_rst = bn_2
    # if bn_rst > pl_rst:
    #     Rst = ("バンカー")
    #     ban = 1
    #     if ban == bet:
    #         print("賞金" + str((int(mny) * 195) // 100))
    #     else:
    #         print("賞金なし")
    # elif bn_rst < pl_rst:
    #     Rst = ("プレイヤー")
    #     ban = 2
    #     if ban == bet :
    #         print("賞金" + str(int(mny) * 2))
    #     else:
    #         print("賞金なし")
    # else:
    #     Rst = ("引き分け")
    #     ban = 3
    #     if ban == bet:
    #         print("賞金" + str(int(mny) * 9))
    #     else:
    #         print("賞金なし")
    # print(Rst)
    # print(pl)
    # print(bn)

# mny = int(input("賭け金を >"))
# bet =int(input("対象を バンカー:1 プレイヤー:2　タイ:3 >"))
torannpu = toranpu_()
pl = Bakara_1(torannpu)
bn = Bakara_1(torannpu)
print(pl)
print(bn)