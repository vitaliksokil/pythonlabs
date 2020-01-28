def read_large_file(file_handler):
    sum_of_bytes = 0
    for line in file_handler:
        splited_data = line.split('"')
        sum_of_bytes += int(splited_data[2].strip().split(' ')[1])
        yield sum_of_bytes


with open('2017_05_07_nginx.txt') as file_handler:
    for block in read_large_file(file_handler):
        print(block)

