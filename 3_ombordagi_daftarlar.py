ombor = 12

while ombor > 0:
    sotildi = int(input("Sotildi: "))

    if sotildi > ombor:
        print("Omborda buncha daftar yo'q!")
    elif sotildi < 0:
        print("Noto'g'ri son!")
    else:
        ombor = ombor - sotildi
        print("Qoldi:", ombor)

print("Ombor bosh")