import numpy as np
from collections import Counter

input_data_path = 'inputs/01.txt'

def part_one():
    data = np.loadtxt(input_data_path, dtype=int)

    left_list = data[:, 0]
    right_list = data[:, 1]

    left_sorted = np.sort(left_list)
    right_sorted = np.sort(right_list)

    distances = np.abs(left_sorted - right_sorted)
    total_distance = np.sum(distances)
    print(f"Total distance is: {total_distance}")


def part_two():
    data = np.loadtxt(input_data_path, dtype=int)

    left_list = data[:, 0]
    right_list = data[:, 1]

    right_counts = Counter(right_list)

    similarity_score = sum(num * right_counts[num] for num in left_list)
    print(f"Similarity score is: {similarity_score}")

if __name__ == '__main__':
    part_one()
    part_two()