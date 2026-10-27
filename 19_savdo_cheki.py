savat = {"non": 4000, "sut": 12000, "tuxum": 18000, "yog'": 25000}

jami = 0

for mahsulot in savat:
    jami += savat[mahsulot]

print("Dastlabki summa:", jami, "so'm")

savat["shakar"] = 14000
jami += savat["shakar"]

print("Shakardan keyin:", jami, "so'm")