szachownice = []

with open('szachownice.txt', 'r', encoding="UTF-8") as f:
    for line in f:
        line = line.strip()

        szachownice.append(
            [
                list(line[0:8]),
                list(line[8:16]),
                list(line[16:24]),
                list(line[24:32]),
                list(line[32:40]),
                list(line[40:48]),
                list(line[48:56]),
                list(line[56:64]),
            ]
        )

ile_takich_szachownic = 0
for szachownica in szachownice:
    for i in range(8):
        for j in range(8):
            if szachownica[i][j] == 'H':
                rzad = i + 1
                kolumna = j + 1

                po_prostych = 15

                ile_pol_na_lewo = kolumna - 1
                ile_pol_na_prawo = 8 - kolumna
                ile_pol_na_gorze = rzad - 1
                ile_pol_na_dole = 8 - rzad

                gorne_przekatne = min(ile_pol_na_gorze, ile_pol_na_lewo) + min(ile_pol_na_gorze, ile_pol_na_prawo)
                dolne_przekatne = min(ile_pol_na_dole, ile_pol_na_lewo) + min(ile_pol_na_dole, ile_pol_na_prawo)

                wszystkich_atakowanych_pol = po_prostych + gorne_przekatne + dolne_przekatne

                # print(rzad, kolumna, wszystkich_atakowanych_pol)

                if wszystkich_atakowanych_pol >= 23:
                    ile_takich_szachownic += 1

print(ile_takich_szachownic)
