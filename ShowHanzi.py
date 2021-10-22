def contain_zh(s):
    for c in s:
        if '\u4e00' <= c <= '\u9fa5':
            return True
    return False


if __name__ == '__main__':
    path = 'a.txt'
    with open(path) as file:
        for line in file.readlines():
            if contain_zh(line):
                print(line)
