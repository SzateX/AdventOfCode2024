def is_safe(data):
    if data[0] < data[1]:
        return all(1 <= data[i + 1] - data[i] <= 3 for i in range(len(data) - 1))
    elif data[0] > data[1]:
        return all(1 <= data[i] - data[i + 1] <= 3 for i in range(len(data) - 1))
    return False

def is_safe_with_dampener(data):
    # I know this is a brute force solution, but have no time to think of a better one
    # It should be done only with a single pass
    if is_safe(data):
        return True

    for i in range(len(data)):
        new_data = data[:i] + data[i + 1:]
        if is_safe(new_data):
            return True

    return False


def part_one():
    safe_reports = 0
    with open('inputs/02.txt') as f:
        for line in f:
            data = list(map(int, line.strip().split(' ')))
            if is_safe(data):
                safe_reports += 1

    print(f"Safe reports: {safe_reports}")


def part_two():
    safe_reports = 0
    with open('inputs/02.txt') as f:
        for line in f:
            data = list(map(int, line.strip().split(' ')))
            if is_safe_with_dampener(data):
                safe_reports += 1

    print(f"Safe reports with dampener: {safe_reports}")


if __name__ == '__main__':
    part_one()
    part_two()