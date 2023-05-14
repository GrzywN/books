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

ile_na_brzegu = 0
for szachownica in szachownice:
    for i in range(8):
        for j in range(8):
            if szachownica[i][j] == 'H' and (i == 0 or j == 0 or i == 7 or j == 7):
                ile_na_brzegu += 1

print(ile_na_brzegu)
