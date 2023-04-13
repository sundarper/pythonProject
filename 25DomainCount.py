import os

with open('./resources/domain_count.txt', 'r') as user_file:
    txt_lines = user_file.readlines()

    print(txt_lines)
    print(type(txt_lines))