def part_one():
    with open('inputs/04.txt') as f:
        matrix = f.readlines()

    number_of_xmas = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 'X':
                if j >= 3:
                    if matrix[i][j - 1] == 'M' and matrix[i][j - 2] == 'A' and matrix[i][j - 3] == 'S':
                        number_of_xmas += 1
                if j < len(matrix[i]) - 3:
                    if matrix[i][j + 1] == 'M' and matrix[i][j + 2] == 'A' and matrix[i][j + 3] == 'S':
                        number_of_xmas += 1
                if i >= 3:
                    if matrix[i - 1][j] == 'M' and matrix[i - 2][j] == 'A' and matrix[i - 3][j] == 'S':
                        number_of_xmas += 1
                if i < len(matrix) - 3:
                    if matrix[i + 1][j] == 'M' and matrix[i + 2][j] == 'A' and matrix[i + 3][j] == 'S':
                        number_of_xmas += 1
                if i >= 3 and j >= 3:
                    if matrix[i - 1][j - 1] == 'M' and matrix[i - 2][j - 2] == 'A' and matrix[i - 3][j - 3] == 'S':
                        number_of_xmas += 1
                if i < len(matrix) - 3 and j < len(matrix[i]) - 3:
                    if matrix[i + 1][j + 1] == 'M' and matrix[i + 2][j + 2] == 'A' and matrix[i + 3][j + 3] == 'S':
                        number_of_xmas += 1
                if i >= 3 and j < len(matrix[i]) - 3:
                    if matrix[i - 1][j + 1] == 'M' and matrix[i - 2][j + 2] == 'A' and matrix[i - 3][j + 3] == 'S':
                        number_of_xmas += 1
                if i < len(matrix) - 3 and j >= 3:
                    if matrix[i + 1][j - 1] == 'M' and matrix[i + 2][j - 2] == 'A' and matrix[i + 3][j - 3] == 'S':
                        number_of_xmas += 1

    print(f"Number of XMAS: {number_of_xmas}")

def part_two():
    with open('inputs/04.txt') as f:
        matrix = [line.strip() for line in f]

    number_of_crossed_mas = 0

    for i in range(1, len(matrix) - 1):
        for j in range(1, len(matrix[0]) - 1):
            if matrix[i][j] == 'A':
                if (matrix[i - 1][j - 1] == 'M' and matrix[i + 1][j + 1] == 'S') or (matrix[i - 1][j - 1] == 'S' and matrix[i + 1][j + 1] == 'M'):
                    if (matrix[i - 1][j + 1] == 'M' and matrix[i + 1][j - 1] == 'S') or (matrix[i - 1][j + 1] == 'S' and matrix[i + 1][j - 1] == 'M'):
                        number_of_crossed_mas += 1

    print(f"Number of crossed MAS: {number_of_crossed_mas}")

if __name__ == '__main__':
    part_one()
    part_two()