myPiece = list(map(int, input().split()))
chessPiece = [1, 1, 2, 2, 2, 8]

for i in range (6):
    print(chessPiece[i]-myPiece[i], end=" ")