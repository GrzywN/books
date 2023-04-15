if word_a[i] == word_b[j]:
  # litery pasuj¹
  cell[i][j] = cell[i-1][j-1] + 1
else:
  # litery nie pasuj¹
  cell[i][j] = max(cell[i-1][j], cell[i][j-1])
