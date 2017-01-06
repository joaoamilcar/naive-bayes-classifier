import csv


def parse_to_array(filename):
    dataset = []

    with open(filename, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            dataset.append(row)

        return dataset