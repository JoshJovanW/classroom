from students import Student
from score import Score
class Classroom:
    def __init__(self):
        self.students = []
     
    def add_students(self):
        names = ["kyoto", "dale", "logy", "carb", "bobby", "tilly", "petey", "natsumi", "tim", "sherly"]
        for name in names:
            name = Student(f"{name}", f"std-{names.index(name) + 1}", names.index(name) + 1)
            self.students.append(name)

    
    def get_ranking(self):
        ranking = []
        
        for students in self.students:
            if len(students.scores.test) != 0 or len(students.scores.quiz) != 0 or students.scores.finals != 0:
                students.scores.find_average()
            ranking.append(students)

        
        for index, students in enumerate(ranking):
            for idx, student in enumerate(ranking):
                if student.scores.average > ranking[index].scores.average:
                    person = student
                    ranking[idx] = ranking[index]
                    ranking[index] = person

        highest_3 = [ranking[-1], ranking[-2], ranking[-3]]

        return highest_3

    def verify_to_end_semester(self):
        verification = {}
        insufficient_tests = []
        no_finals = []
        imbalance = []

        for students in self.students:
            if len(students.scores.test) < 3: 
                insufficient_tests.append([students, f"needs to add { 3 - len(students.scores.test)} test scores"])
        
            if students.scores.finals == 0:
                no_finals.append([students, "have not been inputted the final's score"])

            number_of_tests = 0
            number_of_quiz = 0
    
            if len(students.scores.test) > number_of_tests:
                number_of_tests = len(students.scores.test)

            if len(students.scores.quiz) > number_of_quiz:
                number_of_quiz = len(students.scores.quiz)
        
            if len(students.scores.test) < number_of_tests:
                imbalance.append([students, f"needs {number_of_tests - len(students.scores.test)} more test score"])

            if len(students.scores.quiz) < number_of_quiz:
                imbalance.append([students, f"needs {number_of_quiz - len(students.scores.quiz)} more quiz score"])
                
        verification["insufficient_tests"] = insufficient_tests
        verification["no_finals"] = no_finals
        verification["imbalance"] = imbalance
        
        return verification
    def verify_input(self):
        record = {}

        bulk_input = input("what are the scores of the students?\n")
                
        result = [x.strip() for x in bulk_input.split(',')]
                
        assessment_scores = [element.split(":") for element in result]
                
        student_id = [student.id for student in self.students]
                
        fails = []
        sucesses = []
        reached_requirements_test = []
        reached_requirements_finals = []

        for student in self.students:
            for index, value in enumerate(assessment_scores):
                if student.id == assessment_scores[index][0]:
                    if int(assessment_scores[index][1]) < 0 or int(assessment_scores[index][1]) > 100 or len(student.scores.test) == 6 or student.scores.finals != 0:
                        fails.append(assessment_scores[index])
                    else:
                        sucesses.append(assessment_scores[index])
                               
        for index, value in enumerate(assessment_scores):        
            if assessment_scores[index][0] not in student_id:
                fails.append(assessment_scores[index])

        for student in self.students:
            if len(student.scores.test) == 6:
                reached_requirements_test.append(student)

        for student in self.students:    
            if student.scores.finals != 0:
                reached_requirements_finals.append(student)

        record["sucesses"] = sucesses
        record["fails"] = fails
        record["reached_tests"] = reached_requirements_test
        record["reached_finals"] = reached_requirements_finals

        return record
                

    

   

            






    





