harorat = (18, 20, 17, 23, 25, 21, 19)

natija = []

for i in harorat:
    if i > 20:
        natija.append(i)

print("Haroratlar:", *natija, sep=" ")
print("Kunlar soni:", len(natija))