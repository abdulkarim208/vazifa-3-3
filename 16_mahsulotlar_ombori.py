ombor = {"olma": 12, "banan": 8, "anor": 15, "uzum": 6}

eng_kop = 0
eng_kam = 100000
kop_nomi = ""
kam_nomi = ""
jami = 0

for nom in ombor:
    son = ombor[nom]
    jami += son

    if son > eng_kop:
        eng_kop = son
        kop_nomi = nom

    if son < eng_kam:
        eng_kam = son
        kam_nomi = nom

print("Eng ko'p:", kop_nomi, "(", eng_kop,"ta)")
print("Eng kam:", kam_nomi, "(", eng_kam,"ta)")
print("Jami mahsulot:", jami,"ta")