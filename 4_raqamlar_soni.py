son = int(input())

raqamlar_soni = 0

while son > 0:
    son = son // 10
    raqamlar_soni += 1
    
print(f"Raqamlar soni: {raqamlar_soni}")