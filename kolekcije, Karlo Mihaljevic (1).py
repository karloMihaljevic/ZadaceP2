import random
 
imena=['Richard', 'Kevin', 'Edward', 'Debbie', 'Adam', 'Norma', 'Christopher', 'Karen', 'Tami', 'Michael', 'John', 'Roseanna', 'Gerald', 'George', 'Vesta', 'Julie', 'Raymond', 'Janice', 'Susan', 'Kerry', 'Lorenzo', 'Holly', 'Dan', 'Sherri', 'William', 'Karey', 'Marion', 'Melissa', 'Vincent', 'Ruby']

prezimena=['Arnold', 'Simmons', 'Velasco', 'Canada', 'Gibbs', 'Thompson', 'Rendall', 'Harris', 'Hendon', 'Lyles', 'Perez', 'Cleary', 'Hoyman', 'Hall', 'Baker', 'Fichter', 'Colantuono', 'Moose', 'Howard', 'Davis', 'Nutt', 'Cornett', 'Smith', 'Lemus', 'Beltran', 'Ho', 'Cook', 'Samuels', 'Rodriguez', 'Cano']

radnici=[]

for _ in range(15):
    ime= random.choice(imena)
    prezime = random.choice(prezimena)
    satnica =round(random.uniform(4, 6), 2)
    tjedni_sati =random.randint(20, 30)
    radnik={"ime": ime, "prezime": prezime, "satnica": satnica, "tjedni_sati": tjedni_sati}
    radnici.append(radnik)

isplate = []
ukupna_isplata = 0

for radnik in radnici:
    isplata = round(radnik["satnica"] * radnik["tjedni_sati"], 2)
    isplate.append((radnik["ime"],radnik["prezime"],isplata))
    ukupna_isplata += isplata

prosjecna_isplata =ukupna_isplata / len(radnici)

print("-----------------------------------------------")

print("Isplate radnicima:")

print("-----------------------------------------------")

for ime, prezime, isplata in isplate:
    print(f"{ime} {prezime}: {isplata}")
    
print("-----------------------------------------------")

print("\nUkupna isplata za tjedan:",ukupna_isplata)

print("-----------------------------------------------")

print("prosječna isplata za tjedan:",prosjecna_isplata)

print("-----------------------------------------------")

print("\nRadnici s isplatom iznad prosječne:")

print("-----------------------------------------------")

for ime, prezime, isplata in isplate:
    if isplata > prosjecna_isplata:
        print(f"{ime} {prezime}")
