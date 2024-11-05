import random

cuvinte = ["python", "programare", "calculator", "date", "algoritm"]
cuvant_de_ghicit = random.choice(cuvinte)
progres = ["_" for _ in cuvant_de_ghicit]

incercari_ramase = 6
litere_incercate = []

print("Bine ai venit la jocul Spânzurătoarea!")
print("Cuvântul de ghicit este:", " ".join(progres))

while "_" in progres and incercari_ramase > 0:
    litera = input("Introdu o literă: ").lower()

    if len(litera) != 1 or not litera.isalpha():
        print("Te rog să introduci o singură literă validă.")
        continue

    if litera in litere_incercate:
        print("Ai încercat deja această literă. Te rog să încerci alta.")
        continue

    litere_incercate.append(litera)

    if litera in cuvant_de_ghicit:
        for index, char in enumerate(cuvant_de_ghicit):
            if char == litera:
                progres[index] = litera
        print("Bine făcut! Litera se află în cuvânt.")
    else:
        incercari_ramase -= 1
        print("Îmi pare rău, litera nu se află în cuvânt. Încercări rămase:", incercari_ramase)

    print("Progresul curent:", " ".join(progres))
    print("Încercări rămase:", incercari_ramase)

if "_" not in progres:
    print("Felicitări! Ai ghicit cuvântul:", cuvant_de_ghicit)
else:
    print("Ai pierdut! Cuvântul era:", cuvant_de_ghicit)