def quicksort(array):
  if len(array) < 2:
    # przypadek bazowy, tablice puste i z jednym elementem s¹ ju¿ posortowane
    return array
  else:
    # przypadek rekurencyjny
    pivot = array[0]
    # podtablica zawieraj¹ca wszystkie elementy mniejsze od œrodkowego
    less = [i for i in array[1:] if i <= pivot]
    # podtablica zawieraj¹ca wszystkie elementy wiêksze od œrodkowego
    greater = [i for i in array[1:] if i > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)

print quicksort([10, 5, 2, 3])