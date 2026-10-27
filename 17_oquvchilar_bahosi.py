baholar = {"Ali": 85, "Vali": 72, "Madina": 96, "Jasur": 68}

jami = 0
soni = 0

print("Yuqori ball olganlar:")

for ism, ball in baholar.items():
    jami += ball
    soni += 1

    if ball >= 90:
        print(ism, "-", ball)

ortacha = jami / soni

print("O'rtacha ball:", ortacha)