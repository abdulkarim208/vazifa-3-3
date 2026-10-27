boshlangich_pul = int(input("Boshlang'ich pul: "))
haftalik_qoshimcha = int(input("Haftalik qo'shimcha: "))

jamgarma = boshlangich_pul
hafta = 0

while jamgarma <= 500000:
    jamgarma += haftalik_qoshimcha
    hafta += 1

print(f"Kerakli hafta: {hafta}")