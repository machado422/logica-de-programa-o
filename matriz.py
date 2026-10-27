
matriz = [
    [4, 8, 2],
    [1, 6, 9],
    [3, 7, 5]
]

print("Matriz 3x3:")
for l in range(3):
    for c in range(3):
        print(matriz[l][c], end=" ")
    print()  # Quebra de linha ao terminar cada linha

print("\nElemento da Linha 0, Coluna 1:", matriz[0][1])
print("Elemento da Linha 2, Coluna 2:", matriz[2][2])

soma_diagonal = 0

for l in range(3):
    for c in range(3):
        if l == c:
            soma_diagonal += matriz[l][c]
print("\nSoma da diagonal principal:", soma_diagonal)
