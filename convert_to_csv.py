import os
import csv

dataset_dir = 'initial_dataset'
result_file = 'dataset/dataset.csv'
categories = [
    'business',
    'entertainment',
    'politics',
    'sport',
    'tech'
]


def convert():
    with open(result_file, 'w') as output_file:
        csv_writer = csv.DictWriter(output_file, fieldnames=['text', 'class'])
        csv_writer.writeheader()
        for category in categories:
            handle_category(category, csv_writer)


def handle_category(category, writer):
    category_dir = dataset_dir + "/" + category
    files = os.listdir(category_dir)
    for file_name in files:
        with open(category_dir + '/' + file_name, 'r') as file:
            print("reading file: " + file.name)
            contents = file.read()
            writer.writerow({'text': contents, 'class': category})


if __name__ == '__main__':
    convert()
    print("done")
