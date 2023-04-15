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

# tablica kosztów
infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

# tablica rodziców
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

processed = []

def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    # przegl¹da ka¿dy wêze³ po kolei
    for node in costs:
        cost = costs[node]
        # Jeœli jest to najni¿szy z dotychczasowych kosztów i nie zosta³ jeszcze przetworzony...
        if cost < lowest_cost and node not in processed:
            # ...ustaw go jako nowy najtañszy wêze³.
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

# Znajduje najtañszy wêze³, który jeszcze nie zosta³ przetworzony.
node = find_lowest_cost_node(costs)
# Jeœli przetworzono wszystkie wêz³y, pêtla koñczy dzia³anie.
while node is not None:
    cost = costs[node]
    # Przegl¹da wszystkich s¹siadów danego wêz³a.
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        # Jeœli dotarcie do tego s¹siada jest tañsze drog¹ przez ten wêze³...
        if costs[n] > new_cost:
            # ...zaktualizuj koszt tego wêz³a.
            costs[n] = new_cost
            # Wêze³ ten staje siê nowym rodzicem tego s¹siada.
            parents[n] = node
    # Oznaczenie wêz³a jako przetworzonego.
    processed.append(node)
    # Znajduje nastêpny wêze³ do przetworzenia i wraca na pocz¹tek pêtli.
    node = find_lowest_cost_node(costs)

print "Koszt od pocz¹tku do ka¿dego wêz³a:"
print costs

