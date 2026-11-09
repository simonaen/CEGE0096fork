import csv
from triangleclassifier import TriangleClassifier

if __name__ == "__main__":
    tc = TriangleClassifier()

    with open('./input.csv', newline="") as f:
        for row in csv.reader(f):
            if row:
                tc.classify([float(x) for x in row])

    print(tc)