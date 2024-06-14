def ispisi_naopako(string):
    if len(string) == 0:
        return
    else:
        print(string[-1], end="")
        ispisi_naopako(string[:-1])

unos = input("Unesite string: ")
ispisi_naopako(unos)
