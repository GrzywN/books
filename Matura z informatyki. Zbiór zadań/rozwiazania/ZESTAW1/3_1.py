def czy_trojkat(a: int, b: int, c: int):
    return a + b > c and a + c > b and b + c > a


boki_trojkatow = []

with open('odcinki.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        line = line.strip()

        boki_trojkata = line.split(' ')
        boki_trojkatow.append(list(map(int, boki_trojkata)))

ile_trojkatow = 0
for boki_trojkata in boki_trojkatow:
    a, b, c = boki_trojkata

    if czy_trojkat(a, b, c):
        ile_trojkatow += 1

print(ile_trojkatow)
