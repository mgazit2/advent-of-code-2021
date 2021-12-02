def count_lines():
    increases = 0
    subs = []
    threes = []
    file = open('input', 'r')
    numbers = file.readlines()
    curr = 0
    for i in range(0, len(numbers)):
        sublist = numbers[i:i+3]
        subs.append(sublist)
    for sub in subs:
        sub = sum(int(sub) for sub in sub)
        threes.append(sub)
    print(threes)
    for number in threes:  # I'm lazy, so I didn't add CLI Args; change `threes` to `numbers` for part 1 solution
        if curr == 0:
            curr = int(number)
        if int(number) > curr:
            increases += 1
        curr = int(number)
    print(increases)


if __name__ == '__main__':
    count_lines()
