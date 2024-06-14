import re
#Provjera e-maila
email_regex = r'^[a-zA-Z]+\.[a-zA-Z]+@fpmoz\.sum\.ba$'

#Provjera eduId-a
eduId_regex = r'^[a-zA-Z][a-zA-Z]+@sum\.ba$'

# Unos e-maila i eduId-a
email=input("Unesite e-mail: ")
eduId=input("Unesite eduId: ")

# Provjera unosa
if re.match(email_regex, email):
    print("e-mail je ispravan!")
else:
    print("e-mail nije ispravan!")

if re.match(eduId_regex, eduId):
    print("eduId je ispravan!")
else:
    print("eduId nije ispravan!")
