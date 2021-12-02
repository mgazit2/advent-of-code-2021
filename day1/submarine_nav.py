# Solution for Advent of Code, day 2
def navigate():
    depth = 0
    aim = 0
    horizontal = 0
    file = open('input', 'r')
    directions = file.readlines()
    file.close()
    directions = [list(map(str, x.split(' '))) for x in directions]
    for pair in directions:
        pair[1] = pair[1].replace('\n', '')
        if pair[0] == 'up':
            aim -= int(pair[1])
        elif pair[0] == 'down':
            aim += int(pair[1])
        elif pair[0] == 'forward':
            horizontal += int(pair[1])
            depth += int(pair[1]) * aim
    print('The final coordinates are: ', horizontal, depth)
    print('And their product is: ', horizontal * depth)


if __name__ == '__main__':
    navigate()
    