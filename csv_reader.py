import csv


class Csv:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def read(self):
        with open(self.file_path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)

            for line in csv_reader:
                print(line)

    def write(self, line):
        with open(self.file_path, 'a', newline="\n", encoding='utf-8') as new_file:
            csv_writer = csv.writer(new_file, delimiter=',')
            csv_writer.writerow(line)
