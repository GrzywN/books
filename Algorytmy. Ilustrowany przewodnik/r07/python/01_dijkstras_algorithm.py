# graf
graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {}

# tablica koszt�w
infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

# tablica rodzic�w
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

processed = []

def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    # przegl�da ka�dy w�ze� po kolei
    for node in costs:
        cost = costs[node]
        # Je�li jest to najni�szy z dotychczasowych koszt�w i nie zosta� jeszcze przetworzony...
        if cost < lowest_cost and node not in processed:
            # ...ustaw go jako nowy najta�szy w�ze�.
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

# Znajduje najta�szy w�ze�, kt�ry jeszcze nie zosta� przetworzony.
node = find_lowest_cost_node(costs)
# Je�li przetworzono wszystkie w�z�y, p�tla ko�czy dzia�anie.
while node is not None:
    cost = costs[node]
    # Przegl�da wszystkich s�siad�w danego w�z�a.
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        # Je�li dotarcie do tego s�siada jest ta�sze drog� przez ten w�ze�...
        if costs[n] > new_cost:
            # ...zaktualizuj koszt tego w�z�a.
            costs[n] = new_cost
            # W�ze� ten staje si� nowym rodzicem tego s�siada.
            parents[n] = node
    # Oznaczenie w�z�a jako przetworzonego.
    processed.append(node)
    # Znajduje nast�pny w�ze� do przetworzenia i wraca na pocz�tek p�tli.
    node = find_lowest_cost_node(costs)

print "Koszt od pocz�tku do ka�dego w�z�a:"
print costs

