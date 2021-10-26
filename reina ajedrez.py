col = int(input())
row = int(input())
colN = int(input())
rowN = int(input())

if col == colN or row == rowN or abs(col - colN) == abs(row - rowN):
  print ("YES")
else:
  print ("NO")

#   Imagine a square chessboard. 

# The queen (or queen) can move vertically, horizontally and diagonally any number of cells. 

# Based on the coordinates of the two squares, determine whether the queen can move from the first to the second in one move. If it can, print YES. Otherwise, print NO. The program gets 4 whole numbers from 1 to 8. The first and the second one give the column and the row for the first square, the third and the fourth for the second square.   