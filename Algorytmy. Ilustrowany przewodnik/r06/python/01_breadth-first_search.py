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
    # Przy u�yciu tej tablicy kontrolujemy, kt�re osoby ju� sprawdzili�my.
    searched = []
    while search_queue:
        person = search_queue.popleft()
        # Sprawdzamy osob� tylko wtedy, gdy wcze�niej jej nie sprawdzali�my.
        if not person in searched:
            if person_is_seller(person):
                print person + " sprzedaje mango!"
                return True
            else:
                search_queue += graph[person]
                # Oznacza osob� jako sprawdzon�.
                searched.append(person)
    return False

search("ty")
