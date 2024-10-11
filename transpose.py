def transpose(matrix):
    return [list(row) for row in zip(*matrix)]

# Example usage:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Transposed matrix:")
for row in transpose(matrix):
    print(row)
# Output: [1, 4, 7], [2, 5, 8], [3, 6, 9]
