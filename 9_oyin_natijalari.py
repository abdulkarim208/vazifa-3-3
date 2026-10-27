natijalar = (12, 18, 15)

jami = 0
eng_katta = natijalar[0]
urinish = 1

for i in range(len(natijalar)):
    jami += natijalar[i]

    if natijalar[i] > eng_katta:
        eng_katta = natijalar[i]
        urinish = i + 1

print("Jami ball:", jami)
print("Eng yaxshi urinish:", urinish)
print("Eng yaxshi natija:", eng_katta)