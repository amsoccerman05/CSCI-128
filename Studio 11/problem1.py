import csv

def is_num_repeated(num, numbers):
    return numbers.count(num) == num

with open('numbers.csv', 'r') as input_file, open('results.csv', 'w', newline='') as output_file:
    csv_reader = csv.reader(input_file)
    csv_writer = csv.writer(output_file)

    num = int(next(csv_reader)[0])

    for row in csv_reader:
        numbers = list(map(int, row))
        result = is_num_repeated(num, numbers)
        csv_writer.writerow([str(result).lower()])

# passed