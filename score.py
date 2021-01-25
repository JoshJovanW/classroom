class Score:
    def __init__(self):
        self.test = []
        self.quiz = []
        self.finals = None
        self.average = None

    def add_test_score(self, score):
        if score > 0 and score <= 100:
            self.test.append(score)
        

    def add_quiz_score(self, score):
        if score > 0 and score <= 100:
            self.quiz.append(score)

    def set_finals_score(self, score):
        if score > 0 and score <= 100:
            self.finals = score

    def find_average(self):
        average_of_test = sum(self.test)/len(self.test)
        average_of_quiz = sum(self.quiz)/len(self.quiz)
        total_average_score = (average_of_quiz * 0.1) + (average_of_test * 0.5) + (self.finals * 0.4)
        self.average = total_average_score
