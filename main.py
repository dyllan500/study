import random

qNa = {"Turn Ketone to alkene": "THF=PPH3", "Turn Ketone to alcohol": "Na+, BH4-, CH3OH",
       "Turn alkyne to Ketone": "Cat. Hg+2, Cat. H3O+, H2O & BH3 or Cy2BH, KOH, H2O2",
       "Turn alcohol to ketone": "PCC or Jones", "Remove OCH3 & CH3 from O": "Cat. H3O+, H2O",
       "Adding carbon group to Aldhydre": "BrMgR, H2O", "ketone": "1700", "ester": "1700, 1200",
       "alkene": "1600, 3000-3100", "ether": "1100", "halide bond": "600-800", "N": "3000-4000",
       "alkyne": "2100-2250, 3300", "alcohol": "3000-3600", "aldhyde": "1700",
       "NH": "3400", "NH2": "3200-3400", "carboxylic acid": "2500-3000", "methyl":".9",
	   "methylene":"1.3", "methine":"1.5-2", "allyic":"1.8", "carbonyl":"2-2.3", "benzlic":"2.3",
       "alkynyl":"2.5", "nitrogen":"2-3",
	   "halogen":"2-4", "ether H":"2.8", "vinylic":"5-5.3", "aromatic":"7.3", "aldhyde H":"9.7", "alcohol H":".5-5",
	   "phenol":"4-7", "carboxylic acid H":"10-13", "amine":".5-5", "aniline":"3-5", "amide":"5-9"}

qs = []
wrong = []
for i in qNa:
    qs.append(i)
qss = qs
ans = input("Enter: ")
if ans == "f":
    aw = 1
else:
    aw = 2
while True:
    num = len(qs)
    x = 0
    score = 0
    for i in qss:
        print(qNa[i])
    random.shuffle(qs)
    while x < num:

        print("")
        if aw == 1:
            print(qNa[qs[x]])
        else:
            print(qs[x])
        an = input("Enter: ")
        if an == "h":
            for i in qss:
                print(qNa[i])
        else:
            if aw == 1:
                if an in qs[x].lower():
                    print("Correct")
                    print(qs[x] + " " + qNa[qs[x]])
                    score += 1
                    x += 1
                else:
                    print("Wrong")
                    print(qs[x] + " " + qNa[qs[x]])
                    wrong.append(qs[x])
                    x += 1
            else:
                if an in qNa[qs[x]].lower():
                    print("Correct")
                    print(qs[x] + " " + qNa[qs[x]])
                    score += 1
                    x += 1
                else:
                    print("Wrong")
                    print(qs[x] + " " + qNa[qs[x]])
                    wrong.append(qs[x])
                    x += 1
    print("")
    print(score/num)
    print("")
    for i in wrong:
        print(i)
    print("")
    print("play again?")
    print("")
    a = input("Enter: ")
    if a.lower() == "y" or "yes":
        print("")
    else:
        break

