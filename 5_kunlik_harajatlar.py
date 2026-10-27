jami = 0
soni = 0

while True:
    xarajat = int(input())
    
    if xarajat == 0:
        break
        
    jami += xarajat
    soni += 1

if soni > 0:
    ortacha = jami / soni
else:
    ortacha = 0

print(f"Jami: {jami}")
print(f"Kiritilgan xarajatlar soni: {soni}")
print(f"Ortacha: {ortacha: .2f}")