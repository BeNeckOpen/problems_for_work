def file_pars():
    all_sum = 0
    i = 1
    f = open('names.txt', 'r')
    line = f.readline()
    word = line.split('","')
    word[0] = word[0][1:]
    word[len(word) - 1] = word[len(word) - 1][:-1]
    word.sort()
    for one_word in word:
        for letter in one_word:
            sum = ord(letter) - 64
        all_sum = i * sum + all_sum
        i = i + 1
    print(all_sum)


file_pars()
