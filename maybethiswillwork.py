if __name__ == '__main__':
    mode = input('[i] Select a Module : {1} Paste | {2} Load File : ')
    if mode == '1':
        print('[i] IO Enabled')
        pasta = input('Paste your text : ')
        string = pasta
        string = string.split(';')
        done = sorted(string)
        for i in done:
            print(i + '\n')
    if mode == '2':
        file = input('Type the name of your file  [DO NOT PUT THE FILES EXTENTION] : ')
        list = open(file + '.txt', 'r').readlines()
        list = [line.replace('\n', '') for line in list]
        x = 0
        for line in list:
            x = x + 1
        print('[i] %s Lines Loaded' % x)
        comb = line.split(';')
        combs = sorted(comb)
        print(combs)
        with open(file + '_sorted.txt', 'a') as savedfile:
            for i in combs:
                savedfile.write(i + '\n')
