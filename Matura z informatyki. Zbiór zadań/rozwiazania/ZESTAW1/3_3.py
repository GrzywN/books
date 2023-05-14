from math import sqrt

def czy_trojkat(a: int, b: int, c: int):
    return a + b > c and a + c > b and b + c > a


boki_trojkatow = []

with open('odcinki.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        line = line.strip()

        boki_trojkata = line.split(' ')
        boki_trojkatow.append(list(map(int, boki_trojkata)))

obecna_linia = 0
max_pole = 0
pole_i_linia = dict()
for boki_trojkata in boki_trojkatow:
    a, b, c = boki_trojkata

    if czy_trojkat(a, b, c):
        p = 0.5 * (a + b + c)
        pole = sqrt(p * (p - a) * (p - b) * (p - c))

        pole_i_linia[obecna_linia] = pole

        if pole >= max_pole:
            max_pole = pole

    obecna_linia += 1

for k, v in pole_i_linia.items():
    print(f'Linia: {k}', end=' | ')
    print(f'Pole: {v}')
