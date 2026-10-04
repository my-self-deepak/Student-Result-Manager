import json

class Student_Result_Manager:

    def __init__(self):

        try: 
            with open("Student_Record.json" , "r") as file:
                self.student = json.load(file)

        except FileNotFoundError:
            self.student = {}


    def save_data(self):
        with open("Student_Record.json" , "w") as file:
            json.dump(self.student, file)



    def delete_student(self):
        name = input("the student's name to delete : ")

        if name in self.student:
            del self.student[name]
            print('Student deleteded successfully✅')
            self.save_data()

        else:
            print('\n ❌️ Student not Found!!!')
        


    def add_student(self):
        
        try:
            name = input('Enter Student name : ')
            if name in self.student:
                print("Name is already exists")
            else:
                marks = int(input('Enter Student marks : '))
                if marks < 0 or marks > 100:
                    print("\nPlease enter the marks between 0 to 100")
                    print("Try Again----")
                else:
                    self.student[name] = marks
                    self.save_data()
                    print("\nData save successfully ✅")

        except ValueError:
            print('\n❌️ Add Marks in number !!!!')

            
    def view_student(self):

        if not self.student:
            print("No Data found ❌️ ")

        else:
            print('\n')
            for name, marks in self.student.items():
                print(name, ":", marks)

    def check_result(self):

        name = input("enter the name to result : ")

        if name in self.student:

            marks = self.student[name]
            if marks >= 40:
                print(f'Student is 🥳 pass with {marks} marks')

            else:
                print(f"Student is 😔 Fail with {marks} marks")

        else: 
            print(" ❌️ No Student found")

     
    def menu(self):

        while True:
            print('\n----Student Result Manager----\n')
            print('1️⃣ : To Enter To Student ➡️ ')
            print('2️⃣ : Enter TO view student👀')
            print('3️⃣ : Enter To check Student marks ➡️')
            print('4️⃣ : Enter To Delete Student 🚮')
            print('5️⃣ : Enter To Exit ➜] \n')
            try:
                choice = int(input("Please enter Your choice : "))
            
                if choice == 1:
                    self.add_student()

                elif choice == 2:
                    self.view_student()

                elif choice == 3:
                    self.check_result()

                elif choice == 4:
                    self.delete_student()

                elif choice == 5:
                    print('Exiting......')
                    break

                else:
                    print('please enter valid choice ❌️ ')

            except ValueError:
                print("please enter the choice ❌️ ")


admin = Student_Result_Manager()
admin.menu()