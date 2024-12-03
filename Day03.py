import re

def part_one():
    mul_regex = re.compile(r'(mul\(\d{1,3},\d{1,3}\))')
    result = 0
    with open('inputs/03.txt') as f:
        for line in f:
            mul_matches = mul_regex.findall(line)
            for match in mul_matches:
                nums = list(map(int, match[4:-1].split(',')))
                result += nums[0] * nums[1]

    print(f"Result is: {result}")


def part_two():
    program_regex = re.compile(r'((don\'t\(\))|(do\(\))|(mul\(\d{1,3},\d{1,3}\)))')
    result = 0
    multiply = True
    with open('inputs/03.txt') as f:
        for line in f:
            program_matches = program_regex.findall(line)
            for match in program_matches:
                if match[0] == "don't()":
                    multiply = False
                elif match[0] == "do()":
                    multiply = True
                elif multiply:
                    nums = list(map(int, match[0][4:-1].split(',')))
                    result += nums[0] * nums[1]

    print(f"Result is: {result}")



if __name__ == '__main__':
    part_one()
    part_two()