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
                        if student.id == records["sucesses"][index][0]:
                            student.scores.add_test_score(int(records["sucesses"][index][1]))

                if len(records["fails"]) > 0:
                    print(f'succesfully inputted {len(records["sucesses"])} scores.\n')
                    print(f'you failed to input these id scores {records["fails"]}')
                    continue

                print("You succesfully inputted every score you inputted.\n")

            elif type_of_score == "quiz":
                records = classroom.verify_input()

                for student in classroom.students: 
                    for index, value in enumerate(records["sucesses"]):
                        if student.id == records["sucesses"][index][0]:
                            student.scores.add_quiz_score(int(records["sucesses"][index][1]))
               
                 
                if len(records["fails"]) > 0:
                    print(f'succesfully inputted {len(records["sucesses"])} scores.\n')
                    print(f'you failed to input these id scores {records["fails"]}')
                    continue

                print("You succesfully inputted every score you inputted.\n")

            
            elif type_of_score == "finals":
                records = classroom.verify_input()

                for student in classroom.students: 
                    for index, value in enumerate(records["sucesses"]):
                        if student.id == records["sucesses"][index][0]:
                            student.scores.set_finals_score(int(records["sucesses"][index][1]))
                
                if len(records["fails"]) > 0:
                    print(f'succesfully inputted {len(records["sucesses"])} scores.\n')
                    print(f'you failed to input these id scores {records["fails"]}')
                    continue

                print("You succesfully inputted every score you inputted.\n")
        elif action == "get.ranking":
            highest_3 = classroom.get_ranking()

            print(f"The first rank is {highest_3[0].name} with score {highest_3[0].scores.average}\n")
            print(f"The second rank is {highest_3[1].name} with score {highest_3[1].scores.average}\n")
            print(f"The third rank is {highest_3[2].name} with score {highest_3[2].scores.average}\n")
                
        elif action == "end.semester":
            verify = classroom.verify_to_end_semester()
            
            if len(verify["insufficient_tests"]) == 0  and len(verify["overinput_tests"]) == 0 and len(verify["no_finals"]) == 0:
                print("successfully ended the semester.")
                break
                exit = True
            
            print("can't end semester because: \n")

            print("needs Tests: \n")

            for failures in verify["insufficient_tests"]:
                print(failures[0].id, failures[1])
            
            print("\n")

            print("over inputted Tests: \n")
            
            for failures in verify["overinput_tests"]:
                print(failures[0].id, failures[1])

            print("\n")

            print("needs_finals: \n")

            for failures in verify["no_finals"]:
                print(failures[0].id, failures[1])

        else:
            print("\nThat is not a valid action")

main()
