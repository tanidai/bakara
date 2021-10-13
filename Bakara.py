import random
def toranpu_():
    torannpu = []
    suuti = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    ma_ku = ["♡","♤","♧","♢"]
    for i in suuti:
        for j in ma_ku:
            torannpu.append(i+j)
    return torannpu

def haihu_(torannpu,fs_list=list()):
    fs_deta = 0
    fs = random.choice(torannpu)
    fs_list.append(fs)
    torannpu.remove(fs)
    if fs[0] == "J" or fs[0] == "Q" or fs[0] == "K" or fs[0] == "1":
        fs_deta = 0
    elif fs[0] == "A":
        fs_deta = 1
    else:
        fs_deta = int(fs[0])
    return  fs_deta,fs_list

def haihu_2():
    sc_1,sc_list = haihu_(torannpu)
    sc_2,sc_list = haihu_(torannpu,sc_list)
    sc_deta = int(sc_1) + int(sc_2)
    if int(sc_deta) >= 10:
        sc_deta = sc_deta - 10
    else:
        sc_deta = sc_deta
    return sc_deta,sc_list

# def hanntei_(pl,bn,pl_list,bn_list):
#     if pl >= 8 or bn >= 8:
#         if bn > pl:
#             cs = 5
#         elif bn < pl:
#             cs = 4
#         else:
#             cs = 3
#     elif pl <= 5 and bn == 7:
#         pl_3,pl_list= haihu_(torannpu,pl_list)
#         pl += int(pl_3)

#     elif pl == 6 or pl == 7 and bn <= 5:
#         bn_3,bn_list= haihu_(torannpu,bn_list)
#         bn += int(bn_3)

#     elif pl <= 5 and bn <= 2:
#         pl_3,pl_list= haihu_(torannpu,pl_list)
#         pl += int(pl_3)

#         bn_3,bn_list= haihu_(torannpu,bn_list)
#         bn += int(bn_3)

#     elif pl <= 5:
#         pl_3,pl_list= haihu_(torannpu)
#         pl += int(pl_3)

#         if pl >= 8:
#             pass
#         elif (pl >= 0 and pl < 8 and bn == 3) or (pl >= 2 and pl <= 7 and bn == 4) or (pl >= 4 and pl <= 7 and bn == 5) or (pl == 6 or pl == 7 and bn == 6):
#             bn_3,bn_list= haihu_(torannpu)
#             bn += int(bn_3)

#     if pl >= 10:
#         pl_rst = pl-10
#     else:
#         pl_rst = pl

#     if bn >= 10:
#         bn_rst = bn -10
#     else:
#         bn_rst = bn

#     if bn_rst > pl_rst:
#         cs = 1
#     elif bn_rst < pl_rst:
#         cs = 2
#     else:
#         cs = 3
#     return cs,pl_rst,bn_rst,pl_list,bn_list
     
# def hanntei_2(mny,bet,cs):
#     if mny > 0:

#         if cs == 1 and bet == 1:
#             print("賞金" + str(int(mny * 195 / 100 )))
#         elif cs == 2 and bet == 2:
#             print("賞金" + str(mny * 2))
#         elif cs == 3 and bet == 3:
#             print("賞金" + str(mny * 9))
#         elif cs == 4 and bet == 2:
#             print("賞金" + str(mny * 2))
#             print("プレイヤーのナチュラルウィン")
#         elif cs == 5 and bet == 1:
#             print("賞金" + str(int(mny * 195 / 100 )))
#             print("バンカーのナチュラルウィン")
#     else:
#         print("賞金なし")
#     print(cs)

mny = int(input("賭け金を >"))
bet =int(input("対象を バンカー:1 プレイヤー:2　タイ:3 >"))
pl_deta =[]
bn_deta = []
torannpu = toranpu_()
pl,pl_list = haihu_2()
bn,bn_list = haihu_2()
# cs,pl,bn,pl_list,bn_list = hanntei_(pl,bn,pl_list,bn_list)
# hanntei_2(mny,bet,cs)
print(torannpu)
print("プレイヤー" + str(pl))
print("バンカー" + str(bn))
print(pl_list)
print(bn_list)