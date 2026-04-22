import random_numbers() from sorting.py

class StudentsGrades:
    def __init__(self, scores):
        self.scores = scores

    def get_by_index(self, index):
        return self.scores[index]

    def count(self):
        return len(self.scores)

    def get_grade(self, index):
        pocet_bodu = self.get_by_index(index)
        if 90 <= pocet_bodu <= 100:
            return "A"
        elif 80 <= pocet_bodu <= 89:
            return "B"
        elif 70 <= pocet_bodu <= 79:
            return "C"
        elif 60 <= pocet_bodu <= 69:
            return "D"
        elif 50 <= pocet_bodu <= 59:
            return "E"
        elif pocet_bodu <= 49:
            return "F"

    def find(self, hledany_pocet_bodu):

        novy = []
        seznam_bodu = self.scores

        for index, hodnota  in enumerate(seznam_bodu):
            if hodnota == hledany_pocet_bodu:
                novy.append(index)

        return novy


    def get_sorted(self):

        scores = list(self.scores)

        velikost = len(scores)

        for e in range(velikost):

            swap = False

            p = 0

            for j in range(velikost - 1):
                prvni_index = p
                druhy_index = p + 1

                if scores[prvni_index] > scores[druhy_index]:
                    scores[prvni_index], scores[druhy_index] = scores[druhy_index], scores[prvni_index]

                    swap = True

                p += 1

            if swap == False:
                return scores

            velikost -= 1

        return scores

    def main(self):
        results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])
        print(f"počet studentů: {results.count()}")
        for x, body in enumerate(results):
            print(f"Student {x}: {body} points – {results.get_grade(body)}")
            if body == 100:
                print(f"plný počet(index): {x}")

        print(results.get_sorted())




if __name__ == "__main__":
    results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])

    print(results.count())  # 9
    print(results.get_by_index(2))  # 91
    print(results.scores)  # [85, 42, 91, 67, 50, 73, 100, 38, 58]

    print(results.get_grade(2))  # A (91 bodů)
    print(results.get_grade(6))  # A (100 bodů)
    print(results.get_grade(7))  # F (38 bodů)

    print(results.find(100))  # [6]
    print(results.find(50))  # [4]
    print(results.find(77))  # []

    print(results.get_sorted())  # [38, 42, 50, 58, 67, 73, 85, 91, 100]
    print(results.scores)  # [85, 42, 91, 67, 50, 73, 100, 38, 58]  ← beze změny


