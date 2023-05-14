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

pola_atakowane = [
    [1, 3],
    [1, 5],
    [1, 7],
    [2, 4],
    [2, 5],
    [2, 6],
    [3, 1],
    [3, 2],
    [3, 3],
    [3, 4],
    [3, 5],
    [3, 6],
    [3, 7],
    [3, 8],
    [3, 9],
    [4, 4],
    [4, 5],
    [4, 6],
    [5, 3],
    [5, 5],
    [5, 7],
    [6, 2],
    [6, 5],
    [6, 8],
    [7, 1],
    [7, 5],
    [8, 5]
]

for szachownica in szachownice:
    for i in range(8):
        for j in range(8):
            if szachownica[i][j] == 'H':
                for pole in pola_atakowane:
                    if [i + 1, j + 1] == pole:
                        ile_takich_szachownic += 1

print(ile_takich_szachownic)
