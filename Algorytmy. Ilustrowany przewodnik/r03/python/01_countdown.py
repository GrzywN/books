def countdown(i):
  print i
  # przypadek bazowy
  if i <= 0:
    return
  # przypadek rekurencyjny
  else:
    countdown(i-1)

countdown(5)
