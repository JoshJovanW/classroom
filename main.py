from classroom import Classroom
from students import Student
from score import Score

def main():
    exit = False
    classroom = Classroom()
    classroom.add_students()
     
    print("Welcome to the School Grading system\n\n")
    while exit == False:
        print("Menu: ")
        print("add.scores    -   insert scores for students")
        print("get.ranking   -   get the top 3 students")
        print("end.semester  -   end the semester")

        action = input("What do you want to do? \n")

        if action == "add.scores":
            print("The system works in bulk input.\nThe format of the scores is 'std-1:80' use a comma to seperate students.")

            type_of_score = input("Which score do you want to add? Type 'Test', 'Quiz', or 'finals'.\n").lower()

            if type_of_score == "test":
                records = classroom.verify_input()

                for student in classroom.students: 
                    for index, value in enumerate(records["sucesses"]):
                        if student.id == records["sucesses"][[index][0]]:
                            student.scores.add_test_score(int(records["sucesses"][index][1]))

                if len(records["fails"]) > 0:
                    print(f'succesfully inputted {len(records["sucesses"])} scores.\n')
                    print(f'you failed to input these id scores {len(records["fails"])}')
                    continue

                print("You succesfully inputted every score you inputted.")
                
            elif type_of_score == "quiz":
                records = classroom.verify_input()

                for student in classroom.students: 
                    for index, value in enumerate(records["sucesses"]):
                        if student.id == records["sucesses"][index][0]:
                            student.scores.add_quiz_score(int(records["sucesses"][index][1]))
               
                 
                if len(records["fails"]) > 0:
                    print(f'succesfully inputted {len(records["sucesses"])} scores.\n')
                    print(f'you failed to input these id scores {len(records["fails"])}')
                    continue

                print("You succesfully inputted every score you inputted.")

            
            elif type_of_score == "finals":
                records = classroom.verify_input()

                for student in classroom.students: 
                    for index, value in enumerate(records["sucesses"]):
                        if student.id == records["sucesses"][index][0]:
                            student.scores.set_finals_score(int(records["sucesses"][index][1]))
                
                if len(records["fails"]) > 0:
                    print(f'succesfully inputted {len(records["sucesses"])} scores.\n')
                    print(f'you failed to input these id scores {len(records["fails"])}')
                    continue

                print("You succesfully inputted every score you inputted.")
        elif action == "get.ranking":
            highest_3 = classroom.get_ranking()

            print(f"The first rank is {highest_3[0].name}\n")
            print(f"The second rank is {highest_3[1].name}\n")
            print(f"The third rank is {highest_3[2].name}\n")
                
        elif action == "end.semester":
            verify = classroom.verify_to_end_semester()

            if verify == False:
                print("The requirements for the semester hasn't been reached. Cant end semester.\n")

            elif verify == True:
                print("The semester has been ended. Thank you for using this program.")
                exit = True
        
        else:
            print("That is not a valid action")

main()
