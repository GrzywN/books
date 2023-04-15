def binary_search(list, item):
  # Za pomoc¹ low i high kontrolujemy, która czêœæ listy jest przeszukiwana.
  low = 0
  high = len(list) - 1

  # Dopóki obszar poszukiwañ nie zosta³ zawê¿ony do jednego elementu...
  while low <= high:
    # ...wybieramy œrodkowy element.
    mid = (low + high) // 2
    guess = list[mid]
    # Znaleziono element.
    if guess == item:
      return mid
    # Strzelono za du¿¹ liczbê.
    if guess > item:
      high = mid - 1
    # Strzelono za ma³¹ liczbê.
    else:
      low = mid + 1

  # Element nie istnieje.
  return None

my_list = [1, 3, 5, 7, 9]
print binary_search(my_list, 3) # => 1

# Wartoœæ None w Pythonie oznacza nic, czyli wskazuje, ¿e elementu nie znaleziono.
print binary_search(my_list, -1) # => None
