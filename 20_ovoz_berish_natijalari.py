ovozlar = {
    "Ali": "Python",
    "Vali": "JavaScript",
    "Madina": "Python",
    "Jasur": "C++",
    "Aziza": "Python",
    "Sardor": "JavaScript"
}

hisob = {}

for til in ovozlar.values():
    if til in hisob:
        hisob[til] += 1
    else:
        hisob[til] = 1

eng_kop = 0
golib = ""

for til in hisob:
    print(til + ":", hisob[til], "ta ovoz")

    if hisob[til] > eng_kop:
        eng_kop = hisob[til]
        golib = til

print("G'olib:", golib)