
print("Er is een vacature ruimtevuilnisman. Die moet al het ruimtepuin dat rondom de aarde zweeft op gaan ruimen.")
print("We gaan je paar vragen stellen, dan we gaan kijken als je gekwalificeerd bent om bij ons te werken.")
print("Here komen de vragen.")

name    = input("Vraag 1: Wat is je name? : ")
age     = input("Vraag 2: Hoe oud  ben jij? : ")
tetefon = input("Vraag 3: Wat is je telefoon nummer? : ")
Email   = input("Vraag 4: Wat is je E-mail? : ")
s       = input("Vraag 5: wat is je geslacht? man/vrouw : ")
if s =="man":
    vraag10 = input("Vraag 6: heeft een baard langer dan 10 cm? ja/nee : ")
elif s == "vrouw":
    vraag11 = input("Vraag 6: heeft u rood krulhaar langer dan 20 cm? ja/nee : ")
print("")
vraag1 = input("""Vraag 7: 
A : Heb jij meer dan 4 jaar praktijkervaring met dieren-dressuur?
B : Heb jij meer dan 5 jaar ervaring met jongleren?
C : Heb jij meer dan 3 jaar praktijkervaring met acrobatiek?
D : Ik heb niets dat in het bovengenoemde. """)
if vraag1 == "A" or vraag1 == "B" or vraag1 == "C":
    vraag2 = input("Ben je In bezit van een MBO-4 Diploma ? ja/nee : ")
    vraag3 = input("heb jij een geldig Vrachtwagen rijbewijs? ja/nee : ")
    vraag4 = input("heeft u een lange ervaring (lange) meer dan 4 jaar ? ja/nee : ")
    vraag5 = input("Heb je Certificaat “Overleven met gevaarlijk personeel?ja/nee : ")
    vraag6 = input("Hoe lang ben je in cm? : ")
    vraag7 = input("Hoe zwaar ben je in kg? : ")

    if vraag2 == "ja" and vraag3 =="ja" or vraag4 == "ja" or vraag5 == "nee" and vraag6 >=150 and vraag7 <=90:
        print("jij voeldoet aan de eisen, we nemen zo snel mogelijk contact met je op.")

    elif vraag2 == "nee" and vraag3 =="ja" or vraag3 == "nee"  and vraag4 == "ja" or vraag4 =="nee" and vraag5 == "ja" and vraag6 <=150 and vraag7 >=90:
        print("Sorry jij voeldoet heelaas niet aan onze stricte eisen, dus je kan bij ons heelaas niet werken.")
else:
    print("Sorry je can niet door gaan.")