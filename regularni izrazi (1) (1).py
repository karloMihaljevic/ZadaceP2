'''
Regularni izrazi se koriste za pretragu teksta, uređivanje,
obradu, leksičku analizu...

Neke funkcije regularnih izraza su : "findall", "search", "split", itd...

Potrebno je jednom učitati naredbu "import",
nakon koje slijedi naziv modula (re).

Nakon toga moguće je u programu pozivati funkcije i metode iz učitanog modula.

Razlikujemo više skupina posebnih znakova
te njihove različite funkcije.
'''

#Primjer koristi regularnog izraza:

import re

pattern = '^a...s$'
test_string = 'abyss'
rezultat = re.match(pattern, test_string)

if rezultat:
  print("Podudaraju se.")
else:
  print("Ne podudaraju se.")


'''
U ovom primjeru smo koristili re.match() funkciju
da pronadjemo dio u stringu.

Znak ^ traži dio na kojem tekst počinje,
dok znak $ traži dio gdje tekst završava.

Metoda vraća podudarni dio stringa ako postoji,
a ako ne postoji onda pretraga nije uspjela.
'''
