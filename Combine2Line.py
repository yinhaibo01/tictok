import re

if __name__ == '__main__':
    file_path = 'a.txt'

    re_2_line = re.compile('^[a-zA-Z0-9_\s\-.\'\"?,!]+\n$')
    re_line_number = re.compile('^\d+$')

    with open(file_path, 'r') as file:
        content_list = file.readlines()

    length = len(content_list)
    for i in range(length - 1, 0, -1):
        if re_line_number.search(content_list[i]) or re_line_number.search(content_list[i-1]):
            continue
        if re_2_line.search(content_list[i - 1]) and re_2_line.search(content_list[i]):
            content_list[i - 1] = content_list[i - 1][:-1] + ' ' + content_list[i]
            content_list.pop(i)

    with open(file_path, 'w') as file:
        file.truncate(0)
        file.writelines(content_list)
