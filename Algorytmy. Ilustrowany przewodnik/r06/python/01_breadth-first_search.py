from collections import deque

def person_is_seller(name):
      return name[-1] == 'm'

graph = {}
graph["ty"] = ["alicja", "bartek", "cecylia"]
graph["bartek"] = ["janusz", "patrycja"]
graph["alicja"] = ["patrycja"]
graph["cecylia"] = ["tamara", "jarek"]
graph["janusz"] = []
graph["patrycja"] = []
graph["tamara"] = []
graph["jarek"] = []

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    # Przy u¿yciu tej tablicy kontrolujemy, które osoby ju¿ sprawdziliœmy.
    searched = []
    while search_queue:
        person = search_queue.popleft()
        # Sprawdzamy osobê tylko wtedy, gdy wczeœniej jej nie sprawdzaliœmy.
        if not person in searched:
            if person_is_seller(person):
                print person + " sprzedaje mango!"
                return True
            else:
                search_queue += graph[person]
                # Oznacza osobê jako sprawdzon¹.
                searched.append(person)
    return False

search("ty")
