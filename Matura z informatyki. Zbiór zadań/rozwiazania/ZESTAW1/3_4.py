def czy_trojkat(a: int, b: int, c: int):
    return a + b > c and a + c > b and b + c > a


boki_trojkatow = []

with open('odcinki.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        line = line.strip()

        boki_trojkata = line.split(' ')
        boki_trojkatow.append(list(map(int, boki_trojkata)))

obecna_linia = 0
max_obwod = 0
obwody = dict()

for boki_trojkata in boki_trojkatow:
    a, b, c = boki_trojkata

    if czy_trojkat(a, b, c):
        obwod = a + b + c

        obwody[obecna_linia] = obwod

        if obwod >= max_obwod:
            max_obwod = obwod

    obecna_linia += 1

ile_trojkatow_z_takim_obwodem = list(obwody.values()).count(max_obwod)
print(f'Największy obwód: {max_obwod}')
print(f'Ile trójkątów o takim obwodzie: {ile_trojkatow_z_takim_obwodem}')
