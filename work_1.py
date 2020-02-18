def file_pars():
    sum_local = 0
    all_sum = 0
    f = open('names.txt', 'r')
    line = f.readline()
    line = line[1:-1]
    word = line.split('","')
    word.sort()
    for i in range(len(word)):
        for letter in word[i]:
            sum_local += ord(letter) - ord('A') + 1
        all_sum += i * sum_local
        sum_local = 0
    print(all_sum)


file_pars()
