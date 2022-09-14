import numpy as np
def f1(wD:list,index,line,pl,d1,d2):
    inter = G.intP(line,pl)
    d = np.linalg.norm(np.array(wD[index].intP)-inter)
    #原来的
    if d>=(d2/2-d1/2):ic = True
    else:ic = False
    return ic,inter

def f2(wD:list, d1, d2):
    Data = []
    index = len(wD) - 1
    dl = G.f3(wD[index].P, wD[index].P)
    state = ''
    while index>=0:
        dp = G.f3(
            T.dV(wD[index].id, wD[index].id),
            wD[index].iP)
        ic,ints = f1(wD, index, dl, dp, d1, d2)
        ct = C()
        if ic:
            np = G.intP(
                np.array(wD[index].ip),
                ints,
                0.001,
                d2 - d1)
            dl = G.f3(list(np), list(np))
            ct.sC(ic,np)
            Data.ins(0,ct)
        else:
            ct.stC(ic,np.array([0,0,0]))
            Data.ins(0,ct)
        index += -1
    return Data
