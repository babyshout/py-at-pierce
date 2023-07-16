rowString = ''         # create an empty string
for row in range(10) :
  rowString = str(row) + ": "
  for col in range(10,20) :
    rowString += str(col) + " "
  print(rowString)
  rowString = ''        # reset the the row
