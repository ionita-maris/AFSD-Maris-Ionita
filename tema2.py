articol="”A fi polițist înseamnă a avea o meserie vocațională, deopotrivă interesantă, palpitantă, dinamică, cu intervenții ce implică cunoștințe temeinice și curaj, riscuri dar și satisfacții. Pasiunea și implicarea, corelate cu spiritul de echipă și corectitudinea, sunt calități imperios necesare profilului unui polițist. Toate aceste aspecte, dar și informații despre cum pot deveni polițiști, urmând cursurile unei forme de învățământ din sistemul de apărare, ordine publică şi siguranţă naţională, le-au aflat astăzi, 22 octombrie, elevi din clasele a XI-a și a XII-a din cadrul Colegiului Național „Mihai Eminescu” Baia Mare. Subiectele au fost dezbătute într-o manieră destinsă, elevilor fiindu-le prezentate tehnica și dotările diverselor structuri din cadrul Inspectoratului de Poliție Județean Maramureș”, a informat IPJ Maramureș."

lungime = len(articol)
parte1 = articol[:lungime // 2]
parte2 = articol[lungime // 2:]
parte1 = parte1.strip().upper()
parte2 = parte2[::-1]
parte2 = parte2.capitalize()
import string
parte2 = parte2.translate(str.maketrans(" "," ", string.punctuation ))
rezultat = parte1 + " " + parte2
print(rezultat)
