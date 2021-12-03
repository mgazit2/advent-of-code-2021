def power_consumption():
    gamma = []
    epsilon = []
    count_one = 0
    count_zero = 0
    with open('input', 'r') as f:
        data = f.readlines()
        f.close()
    for i in range(len(data[0]) - 1):
        for line in data:
            if line[i] and line[i] == '0':
                count_zero += 1
            elif line[i] and line[i] == '1':
                count_one += 1
        if count_zero > count_one:
            gamma.append(0)
            epsilon.append(1)
            count_zero = 0
            count_one = 0
        else:
            gamma.append(1)
            epsilon.append(0)
            count_zero = 0
            count_one = 0
    print(gamma, epsilon)
    gamma_decimal = 0
    epsilon_decimal = 0
    for i in range(len(gamma)):
        gamma_decimal += gamma[i] * 2 ** (len(gamma) - i - 1)
    for i in range(len(epsilon)):
        epsilon_decimal += epsilon[i] * 2 ** (len(epsilon) - i - 1)
    print(gamma_decimal * epsilon_decimal)


if __name__ == '__main__':
    power_consumption()
