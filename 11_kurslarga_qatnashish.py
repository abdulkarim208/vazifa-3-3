matematika = {"Ali", "Vali", "Madina", "Jasur", "Aziza"}
ingliz = {"Madina", "Jasur", "Sardor", "Aziza", "Malika"}

ikkala = matematika & ingliz
bitta = matematika ^ ingliz

print("Ikkala kursda:", ", ".join(ikkala))
print("Faqat bitta kursda:", ", ".join(bitta))