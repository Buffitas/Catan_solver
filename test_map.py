from elements import Hexagon
from elements import Corner
from elements import Edge


### TESTING ###

def create_test_map():
    hexagon_list = []

    ### CREATE HEXAGON ###

    hA = Hexagon('A', 5, 'rock')
    hexagon_list.append(hA)
    hB = Hexagon('B', 2, 'wood')
    hexagon_list.append(hB)
    hC = Hexagon('C', 6, 'wood')
    hexagon_list.append(hC)
    hD = Hexagon('D', 10, 'wool')
    hexagon_list.append(hD)
    hE = Hexagon('E', 9, 'brick')
    hexagon_list.append(hE)

    hE.thief = True
    
    corner_list = []

    ### CREATE CORNERS ###

    cA1 = Corner('A1', [hA])
    corner_list.append(cA1)
    cA2 = Corner('A2', [hA])
    corner_list.append(cA2)
    cAB = Corner('AB', [hA, hB])
    corner_list.append(cAB)
    cB1 = Corner('B1', [hB])
    corner_list.append(cB1)
    cB2 = Corner('B2', [hB])
    corner_list.append(cB2)

    cC1 = Corner('C1', [hA])
    corner_list.append(cC1)
    cAC = Corner('AC', [hA, hC])
    corner_list.append(cAC)
    cACD = Corner('ACD', [hA, hD, hC])
    corner_list.append(cACD)
    cABD = Corner('ABD', [hA, hB, hD])
    corner_list.append(cABD)
    cBDE = Corner('BDE', [hB, hE, hD])
    corner_list.append(cBDE)
    cBE = Corner('BE', [hB, hE])
    corner_list.append(cBE)
    cE1 = Corner('E1', [hE])
    corner_list.append(cE1)

    cC2 = Corner('C2', [hC])
    corner_list.append(cC2)
    cC3 = Corner('C3', [hC])
    corner_list.append(cC3)
    cCD = Corner('CD', [hD, hC])
    corner_list.append(cCD)
    cD1 = Corner('D1', [hD])
    corner_list.append(cD1)
    cDE = Corner('DE', [hE, hD])
    corner_list.append(cDE)
    cE2 = Corner('E2', [hE])
    corner_list.append(cE2)
    cE3 = Corner('E3', [hE])
    corner_list.append(cE3)

    edge_list = []

    ### CREATE EDGES ###

    e_A1_A2 = Edge('A1_A2', [cA1, cA2])
    edge_list.append(e_A1_A2)
    e_A2_AB = Edge('A2_AB', [cA2, cAB])
    edge_list.append(e_A2_AB)
    e_AB_B1 = Edge('AB_B1', [cAB, cB1])
    edge_list.append(e_AB_B1)
    e_B1_B2 = Edge('B1_B2', [cB1, cB2])
    edge_list.append(e_B1_B2)

    e_A1_AC = Edge('A1_AC', [cA1, cAC])
    edge_list.append(e_A1_AC)
    e_AB_ABD = Edge('AB_ABD', [cAB, cABD])
    edge_list.append(e_AB_ABD)
    e_B2_BE = Edge('B2_BE', [cB2, cBE])
    edge_list.append(e_B2_BE)

    e_C1_AC = Edge('C1_AC', [cC1, cAC])
    edge_list.append(e_C1_AC)
    e_AC_ACD = Edge('AC_ACD', [cAC, cACD])
    edge_list.append(e_AC_ACD)
    e_ACD_ABD = Edge('ACD_ABD', [cACD, cABD])
    edge_list.append(e_ACD_ABD)
    e_ABD_BDE = Edge('ABD_BDE', [cABD, cBDE])
    edge_list.append(e_ABD_BDE)
    e_BDE_BE = Edge('BDE_BE', [cBDE, cBE])
    edge_list.append(e_BDE_BE)
    e_BE_E1 = Edge('BE_E1', [cBE, cE1])
    edge_list.append(e_BE_E1)

    e_C1_C2 = Edge('C1_C2', [cC1, cC2])
    edge_list.append(e_C1_C2)
    e_ACD_CD = Edge('ACD_CD', [cACD, cCD])
    edge_list.append(e_ACD_CD)
    e_BDE_DE = Edge('BDE_DE', [cBDE, cDE])
    edge_list.append(e_BDE_DE)
    e_E1_E2 = Edge('E1_E2', [cE1, cE2])
    edge_list.append(e_E1_E2)

    e_C2_C3 = Edge('C2_C3', [cC2, cC3])
    edge_list.append(e_C2_C3)
    e_C3_CD = Edge('C3_CD', [cC3, cCD])
    edge_list.append(e_C3_CD)
    e_CD_D1 = Edge('CD_D1', [cCD, cD1])
    edge_list.append(e_CD_D1)
    e_D1_DE = Edge('D1_DE', [cD1, cDE])
    edge_list.append(e_D1_DE)
    e_DE_E2 = Edge('DE_E2', [cDE, cE2])
    edge_list.append(e_DE_E2)
    e_E2_E3 = Edge('E2_E3', [cE2, cE3])
    edge_list.append(e_E2_E3)

    return hexagon_list, corner_list, edge_list


    
    ### CREATE HEXAGONS ###

#     hA = Hexagon('A', 5, 'rock')
#     hexagon_list.append(hA)
#     hB = Hexagon('B', 2, 'wood')
#     hexagon_list.append(hB)
#     hC = Hexagon('C', 6, 'wood')
#     hexagon_list.append(hC)
#     hD = Hexagon('D', 10, 'wool')
#     hexagon_list.append(hD)
#     hE = Hexagon('E', 9, 'brick')
#     hexagon_list.append(hE)
#     hF = Hexagon('F', 4, 'hay')
#     hexagon_list.append(hF)
#     hG = Hexagon('G', 3, 'brick')
#     hexagon_list.append(hG)
#     hH = Hexagon('H', 8, 'hay')
#     hexagon_list.append(hH)
#     hI = Hexagon('I', 11, 'brick')
#     hexagon_list.append(hI)
#     hJ = Hexagon('J', 0, '-')
#     hexagon_list.append(hJ)
#     hK = Hexagon('K', 5, 'wool')
#     hexagon_list.append(hK)
#     hL = Hexagon('L', 8, 'wool')
#     hexagon_list.append(hL)
#     hM = Hexagon('M', 4, 'wood')
#     hexagon_list.append(hM)
#     hN = Hexagon('N', 3, 'rock')
#     hexagon_list.append(hN)
#     hO = Hexagon('O', 6, 'wood')
#     hexagon_list.append(hO)
#     hP = Hexagon('P', 10, 'rock')
#     hexagon_list.append(hP)
#     hQ = Hexagon('Q', 11, 'hay')
#     hexagon_list.append(hQ)
#     hR = Hexagon('R', 12, 'wool')
#     hexagon_list.append(hR)
#     hS = Hexagon('S', 9, 'hay')
#     hexagon_list.append(hS)

#     ### CREATE CORNERS ###

#     cA1 = Corner('A1', [hA])
#     corner_list.append(cA1)
#     cA2 = Corner('A2', [hA])
#     corner_list.append(cA2)
#     cAB = Corner('AB', [hA, hB])
#     corner_list.append(cAB)
#     cB1 = Corner('B1', [hB])
#     corner_list.append(cB1)
#     cBC = Corner('BC', [hB, hC])
#     corner_list.append(cBC)
#     cC1 = Corner('C1', [hC])
#     corner_list.append(cC1)
#     cC2 = Corner('C2', [hC])
#     corner_list.append(cC2)

#     cD1 = Corner('D1', [hD])
#     corner_list.append(cD1)
#     cAD = Corner('AD', [hD, hA])
#     corner_list.append(cAD)
#     cADE = Corner('ADE', [hA, hD, hE])
#     corner_list.append(cADE)
#     cABE = Corner('ABE', [hA, hB, hE])
#     corner_list.append(cABE)
#     cBEF = Corner('BEF', [hB, hE, hF])
#     corner_list.append(cBEF)
#     cBCF = Corner('BCF', [hC, hB, hF])
#     corner_list.append(cBCF)
#     cCFG = Corner('CFG', [hC, hG, hF])
#     corner_list.append(cCFG)
#     cCG = Corner('CG', [hC, hG])
#     corner_list.append(cCG)
#     cG1 = Corner('G1', [hG])
#     corner_list.append(cG1)

#     cH1 = Corner('cH1', [hH])
#     corner_list.append(cH1)
#     cHD = Corner('HD', [hH, hD])
#     corner_list.append(cHD)
#     cDHI = Corner('DHI', [hD, hH, hI])
#     corner_list.append(cDHI)
#     cDEI = Corner('DEI', [hD, hE, hI])
#     corner_list.append(cDEI)
#     cEIJ = Corner('EIJ', [hE, hI, hJ])
#     corner_list.append(cEIJ)
#     cEFJ = Corner('EFJ', [hE, hJ, hF])
#     corner_list.append(cEFJ)
#     cFJK = Corner('FJK', [hJ, hK, hF])
#     corner_list.append(cFJK)
#     cFGK = Corner('FGK', [hK, hG, hF])
#     corner_list.append(cFGK)
#     cGKL = Corner('GKL', [hL, hG, hK])
#     corner_list.append(cGKL)
#     cGL = Corner('GL', [hL, hG])
#     corner_list.append(cGL)
#     cL1 = Corner('L1', [hL])
#     corner_list.append(cL1)

#     cH2 = Corner('H2', [hH])
#     corner_list.append(cH2)
#     cHM = Corner('HM', [hH, hM])
#     corner_list.append(cHM)
#     cHIM = Corner('HIM', [hH, hI, hM])
#     corner_list.append(cHIM)
#     cIMN = Corner('IMN', [hI, hM, hN])
#     corner_list.append(cIMN)
#     cIJN = Corner('IJN', [hI, hJ, hN])
#     corner_list.append(cIJN)
#     cJNO = Corner('JNO', [hJ, hN, hO])
#     corner_list.append(cJNO)
#     cJKO = Corner('JKO', [hJ, hK, hO])
#     corner_list.append(cJKO)
#     cKOP = Corner('KOP', [hK, hO, hP])
#     corner_list.append(cKOP)
#     cKLP = Corner('KLP', [hK, hL, hP])
#     corner_list.append(cKLP)
#     cLF = Corner('LF', [hL, hF])
#     corner_list.append(cLF)
#     cL2 = Corner('L2', [hL])
#     corner_list.append(cL2)

#     cM1 = Corner('M1', [hM])
#     corner_list.append(cM1)
#     cMQ = Corner('MQ', [hM, hQ])
#     corner_list.append(cMQ)
#     cMNQ = Corner('MNQ', [hM, hN, hQ])
#     corner_list.append(cMNQ)
#     cNQR = Corner('NQR', [hN, hQ, hR])
#     corner_list.append(cNQR)
#     cNOR = Corner('NOR', [hN, hO, hR])
#     corner_list.append(cNOR)
#     cORS = Corner('ORS', [hO, hR, hS])
#     corner_list.append(cORS)
#     cOPS = Corner('OPS', [hP, hO, hS])
#     corner_list.append(cOPS)
#     cPS = Corner('PS', [hP, hS])
#     corner_list.append(cPS)
#     cP1 = Corner('P1', [hP])
#     corner_list.append(cP1)

#     cQ1 = Corner('Q1', [hQ])
#     corner_list.append(cQ1)
#     cQ2 = Corner('Q2', [hQ])
#     corner_list.append(cQ2)
#     cQR = Corner('QR', [hQ, hR])
#     corner_list.append(cQR)
#     cR1 = Corner('R1', [hR])
#     corner_list.append(cR1)
#     cRS = Corner('RS', [hR, hS])
#     corner_list.append(cRS)
#     cS1 = Corner('S1', [hS])
#     corner_list.append(cS1)
#     cS2 = Corner('S2', [hS])
#     corner_list.append(cS2)

# # cA1.adjacent_corners = [cA2, cAD]

# # # for i in hexagon_list:
# # #     print(i.index)

#     ### CREATE HEXAGONS ###

#     hA = Hexagon('A', 5, 'rock')
#     hexagon_list.append(hA)
#     hB = Hexagon('B', 2, 'wood')
#     hexagon_list.append(hB)
#     hC = Hexagon('C', 6, 'wood')
#     hexagon_list.append(hC)
#     hD = Hexagon('D', 10, 'wool')
#     hexagon_list.append(hD)
#     hE = Hexagon('E', 9, 'brick')
#     hexagon_list.append(hE)
#     hF = Hexagon('F', 4, 'hay')
#     hexagon_list.append(hF)
#     hG = Hexagon('G', 3, 'brick')
#     hexagon_list.append(hG)
#     hH = Hexagon('H', 8, 'hay')
#     hexagon_list.append(hH)
#     hI = Hexagon('I', 11, 'brick')
#     hexagon_list.append(hI)
#     hJ = Hexagon('J', 0, '-')
#     hexagon_list.append(hJ)
#     hK = Hexagon('K', 5, 'wool')
#     hexagon_list.append(hK)
#     hL = Hexagon('L', 8, 'wool')
#     hexagon_list.append(hL)
#     hM = Hexagon('M', 4, 'wood')
#     hexagon_list.append(hM)
#     hN = Hexagon('N', 3, 'rock')
#     hexagon_list.append(hN)
#     hO = Hexagon('O', 6, 'wood')
#     hexagon_list.append(hO)
#     hP = Hexagon('P', 10, 'rock')
#     hexagon_list.append(hP)
#     hQ = Hexagon('Q', 11, 'hay')
#     hexagon_list.append(hQ)
#     hR = Hexagon('R', 12, 'wool')
#     hexagon_list.append(hR)
#     hS = Hexagon('S', 9, 'hay')
#     hexagon_list.append(hS)

#     ### CREATE CORNERS ###

#     cA1 = Corner('A1', [hA])
#     corner_list.append(cA1)
#     cA2 = Corner('A2', [hA])
#     corner_list.append(cA2)
#     cAB = Corner('AB', [hA, hB])
#     corner_list.append(cAB)
#     cB1 = Corner('B1', [hB])
#     corner_list.append(cB1)
#     cBC = Corner('BC', [hB, hC])
#     corner_list.append(cBC)
#     cC1 = Corner('C1', [hC])
#     corner_list.append(cC1)
#     cC2 = Corner('C2', [hC])
#     corner_list.append(cC2)

#     cD1 = Corner('D1', [hD])
#     corner_list.append(cD1)
#     cAD = Corner('AD', [hD, hA])
#     corner_list.append(cAD)
#     cADE = Corner('ADE', [hA, hD, hE])
#     corner_list.append(cADE)
#     cABE = Corner('ABE', [hA, hB, hE])
#     corner_list.append(cABE)
#     cBEF = Corner('BEF', [hB, hE, hF])
#     corner_list.append(cBEF)
#     cBCF = Corner('BCF', [hC, hB, hF])
#     corner_list.append(cBCF)
#     cCFG = Corner('CFG', [hC, hG, hF])
#     corner_list.append(cCFG)
#     cCG = Corner('CG', [hC, hG])
#     corner_list.append(cCG)
#     cG1 = Corner('G1', [hG])
#     corner_list.append(cG1)

#     cH1 = Corner('cH1', [hH])
#     corner_list.append(cH1)
#     cHD = Corner('HD', [hH, hD])
#     corner_list.append(cHD)
#     cDHI = Corner('DHI', [hD, hH, hI])
#     corner_list.append(cDHI)
#     cDEI = Corner('DEI', [hD, hE, hI])
#     corner_list.append(cDEI)
#     cEIJ = Corner('EIJ', [hE, hI, hJ])
#     corner_list.append(cEIJ)
#     cEFJ = Corner('EFJ', [hE, hJ, hF])
#     corner_list.append(cEFJ)
#     cFJK = Corner('FJK', [hJ, hK, hF])
#     corner_list.append(cFJK)
#     cFGK = Corner('FGK', [hK, hG, hF])
#     corner_list.append(cFGK)
#     cGKL = Corner('GKL', [hL, hG, hK])
#     corner_list.append(cGKL)
#     cGL = Corner('GL', [hL, hG])
#     corner_list.append(cGL)
#     cL1 = Corner('L1', [hL])
#     corner_list.append(cL1)

#     cH2 = Corner('H2', [hH])
#     corner_list.append(cH2)
#     cHM = Corner('HM', [hH, hM])
#     corner_list.append(cHM)
#     cHIM = Corner('HIM', [hH, hI, hM])
#     corner_list.append(cHIM)
#     cIMN = Corner('IMN', [hI, hM, hN])
#     corner_list.append(cIMN)
#     cIJN = Corner('IJN', [hI, hJ, hN])
#     corner_list.append(cIJN)
#     cJNO = Corner('JNO', [hJ, hN, hO])
#     corner_list.append(cJNO)
#     cJKO = Corner('JKO', [hJ, hK, hO])
#     corner_list.append(cJKO)
#     cKOP = Corner('KOP', [hK, hO, hP])
#     corner_list.append(cKOP)
#     cKLP = Corner('KLP', [hK, hL, hP])
#     corner_list.append(cKLP)
#     cLF = Corner('LF', [hL, hF])
#     corner_list.append(cLF)
#     cL2 = Corner('L2', [hL])
#     corner_list.append(cL2)

#     cM1 = Corner('M1', [hM])
#     corner_list.append(cM1)
#     cMQ = Corner('MQ', [hM, hQ])
#     corner_list.append(cMQ)
#     cMNQ = Corner('MNQ', [hM, hN, hQ])
#     corner_list.append(cMNQ)
#     cNQR = Corner('NQR', [hN, hQ, hR])
#     corner_list.append(cNQR)
#     cNOR = Corner('NOR', [hN, hO, hR])
#     corner_list.append(cNOR)
#     cORS = Corner('ORS', [hO, hR, hS])
#     corner_list.append(cORS)
#     cOPS = Corner('OPS', [hP, hO, hS])
#     corner_list.append(cOPS)
#     cPS = Corner('PS', [hP, hS])
#     corner_list.append(cPS)
#     cP1 = Corner('P1', [hP])
#     corner_list.append(cP1)

#     cQ1 = Corner('Q1', [hQ])
#     corner_list.append(cQ1)
#     cQ2 = Corner('Q2', [hQ])
#     corner_list.append(cQ2)
#     cQR = Corner('QR', [hQ, hR])
#     corner_list.append(cQR)
#     cR1 = Corner('R1', [hR])
#     corner_list.append(cR1)
#     cRS = Corner('RS', [hR, hS])
#     corner_list.append(cRS)
#     cS1 = Corner('S1', [hS])
#     corner_list.append(cS1)
#     cS2 = Corner('S2', [hS])
#     corner_list.append(cS2)

# cA1.adjacent_corners = [cA2, cAD]

# # for i in hexagon_list:
# #     print(i.index)