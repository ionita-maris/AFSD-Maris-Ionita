meniu = ['papanasi'] * 10 + ['ceafa'] * 3 + ['guias'] * 6
preturi = [["papanasi", 7], ["ceafa", 10], ["guias", 5]]
studenti = ["Liviu", "Ion", "George", "Ana", "Florica"]
comenzi = ["guias", "ceafa", "ceafa", "papanasi", "ceafa"]
tavi = ["tava"] * 7
istoric_comenzi = []

print("Servirea comenzilor:")
for student in studenti:
    if comenzi and tavi:
        comanda_curenta = comenzi.pop(0)
        tava_curenta = tavi.pop()

        print(f"{student} a comandat {comanda_curenta}.")
        istoric_comenzi.append(comanda_curenta)
    else:
        print(f"{student} nu a fost servit deoarece nu mai sunt comenzi sau tăvi disponibile.")

print("\nInventar după procesarea comenzilor:")
comenzi_count = {produs: 0 for produs in ['papanasi', 'ceafa', 'guias']}
for comanda in istoric_comenzi:
    comenzi_count[comanda] += 1

print(f"S-au comandat {comenzi_count['guias']} guias, {comenzi_count['ceafa']} ceafa, {comenzi_count['papanasi']} papanasi.")
print(f"Mai sunt {len(tavi)} tavi.")
print(f"Mai este ceafa: {'ceafa' in meniu and meniu.count('ceafa') > 0}.")
print(f"Mai sunt papanasi: {'papanasi' in meniu and meniu.count('papanasi') > 0}.")
print(f"Mai sunt guias: {'guias' in meniu and meniu.count('guias') > 0}.")

total = 0
for comanda in istoric_comenzi:
    for produs in preturi:
        if produs[0] == comanda:
            total += produs[1]

print(f"\nCantina a încasat: {total} lei.")
produse_sub_7 = [produs for produs in preturi if produs[1] <= 7]
print(f"Produse care costă cel mult 7 lei: {produse_sub_7}.")