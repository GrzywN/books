# Znajduje najmniejsz� warto�� w tablicy
def findSmallest(arr):
  # Przechowuje najmniejsz� warto��.
  smallest = arr[0]
  # Przechowuje indeks najmniejszej warto�ci.
  smallest_index = 0
  for i in range(1, len(arr)):
    if arr[i] < smallest:
      smallest = arr[i]
      smallest_index = i
  return smallest_index

# sortuje tablic�
def selectionSort(arr):
  newArr = []
  for i in range(len(arr)):
      # Znajduje najmniejszy element w tablicy i dodaje go do nowej tablicy.
      smallest = findSmallest(arr)
      newArr.append(arr.pop(smallest))
  return newArr

print selectionSort([5, 3, 6, 2, 10])
