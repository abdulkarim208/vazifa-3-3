A = (3, 7)
B = (8, 2)

sumA = sum(A)
sumB = sum(B)

print(f"A yigindisi: {sumA}")
print(f"B yigindisi: {sumB}")

if sumA > sumB:
    print("A yigindisi katta")
elif sumB > sumA:
    print("B yigindisi katta")
else:
    print("yigindilar teng")