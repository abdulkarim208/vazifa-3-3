shaharlar = {
    "Toshkent": 3000000,
    "Farg'ona": 300000,
    "Samarqand": 600000
}

eng_kop = 0
eng_kop_shahar = ""
print("500 000 dan ko'p:")

for shahar in shaharlar:
    aholi = shaharlar[shahar]

    if aholi > 500000:
        print(shahar)

    if aholi > eng_kop:
        eng_kop = aholi
        eng_kop_shahar = shahar

print("Eng ko'p aholi:", eng_kop_shahar)