from cvs import reader
with open('rezultati.csv', 'r',encoding="utf=8") as read-obj:
    rezultati =[tuple(line.strip().split(',')) for line in file]
print("studenti koji su polozili")
for ime, prezime, bodovi in rezultati:
    if int(bodovi) > 49:
        print(ime, prezime)
rezultati.sort(key=lambda x: x[1])
ocjene = {"nedovoljan": 0, "dovoljan": 0, "dobar": 0, "vrlodobar": 0, "izvrstan": 0}
for _, _, bodovi in rezultati:
    bodovi = int(bodovi)
    if bodovi < 50:
        ocjene["nedovoljan"] += 1
    elif 50 <= bodovi < 65:
        ocjene["dovoljan"] += 1
    elif 65 <= bodovi < 80:
        ocjene["dobar"] += 1
    elif 80 <= bodovi < 90:
        ocjene["vrlodobar"] += 1
    else:
        ocjene["izvrstan"] += 1
print("\nBroj ostvarenih ocjena po bodovanju")
for ocjena, broj in ocjene.items():
    print(ocjena + ":", broj)
