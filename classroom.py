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
            students.scores.find_average()
            ranking.append(students)

        for index, scores in enumerate(ranking):
            for idx, score in enumerate(ranking):
                if scores.scores.average > ranking[index].scores.average:
                    score_string = score
                    ranking[idx] = ranking[index]
                    ranking[index] = score_string
        
        highest_3 = [ranking[-1], ranking[-2], ranking[-3]]

        return highest_3

    def verify_to_end_semester(self):
        verified = False
        for students in self.students:
            if len(students.scores.test) >= 3 and len(students.scores.test) <= 6 and students.scores.finals != None and len(students.scores.quiz) != 0:
                verified = True
            else:
                verified = False
                break

            
        return verified
 
    def verify_input(self):
        record = {}

        bulk_input = input("what are the scores of the students?\n")
                
        result = [x.strip() for x in bulk_input.split(',')]
                
        assessment_scores = [element.split(":") for element in result]
                
        student_id = [student.id for student in self.students]
                
        fails = []
        sucesses = []

        for student in self.students:
            for index, value in enumerate(assessment_scores):
                if student.id == assessment_scores[index][0]:
                    if int(assessment_scores[index][1]) < 0 or int(assessment_scores[index][1]) > 100:
                        fails.append(assessment_scores[index][0])
                    else:
                        sucesses.append(int(assessment_scores[index][1]))
                               
        for index, value in enumerate(assessment_scores):        
            if assessment_scores[index][0] not in student_id:
                fails.append(assessment_scores[index][0])

        record["sucesses"] = sucesses
        record["fails"] = fails

        return record
                

    

   

            






    



