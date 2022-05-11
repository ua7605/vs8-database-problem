from csv_reader import Csv

if __name__ == '__main__':
    csv = Csv("database.csv")
    line = ["Feature", "Point", 51.24100592861111, 4.419389888888889, 0.14, 332.417, 1652104106.4142032]
    csv.write(line=line)
    csv.read()
