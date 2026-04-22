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


if __name__ == "__main__":
    results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])

    print(results.count())  # 9
    print(results.get_by_index(2))  # 91
    print(results.scores)  # [85, 42, 91, 67, 50, 73, 100, 38, 58]

    print(results.get_grade(2))  # A (91 bodů)
    print(results.get_grade(6))  # A (100 bodů)
    print(results.get_grade(7))  # F (38 bodů)