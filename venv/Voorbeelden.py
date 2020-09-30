# lijst = [["auto", 4, "onzin"],["fiets", 2, "onzin"],["driewieler", 3,"onzin"]]
# #print (lijst)
#
# for i in range(len(lijst)):
#
#     print((lijst[i][0])+" "+str((lijst[i][1])))
#
# # print("auto" + str(4))

ref = "CHHCQWYHSJ"
seq = "HHCCWSFHSJSEYTRIK"

score = 0

if len(ref) != len(seq):
    verschil = len(ref) - len(seq)
    # print (verschil)
    if verschil <0:
        score += verschil
    else:
        score -= verschil

# print(ref[0])

if len(ref)<len(seq):
    for i in range (len(ref)):
        if ref[i] == seq[i]:
            score +=1
        else:
            score -=1
else:
    for i in range (len(seq)):
        if ref[i] == seq[i]:
            score +=1
        else:
            score -=1

print(score)
