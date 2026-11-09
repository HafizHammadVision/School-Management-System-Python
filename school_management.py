#School Management System
class Student:
    def __init__(self,student_id,fullName,age,Class,contact_No):
        self.student_id=student_id
        self.fullName=fullName
        self.age=age
        self.Class=Class
        self.contact=contact_No

    def displayInfo(self):
        print("Student_ID :",self.student_id)
        print("Student_FullName :",self.fullName)
        print("Student_Age :",self.age)
        print("Class :",self.Class)
        print("Contact No :",self.contact)
    
class Student_Management:
    def __init__(self,students):
        self.students=students
        
    def add_student(self):
      student_id = input("Enter Student ID : ").strip()

      for student in self.students:
          if student.student_id == student_id:
           print("Student ID already exists")
           return
        
      name=input("Enter Student FullName :")
      try:
         age=int(input("Enter Student Age :"))
      except ValueError:
          print("Please enter a valid integer")
          return 
      Class=input("Class :")
      contact=input("Contact No :")

      new_Student=Student(student_id,name,age,Class,contact) 
      self.students.append(new_Student)
      print("Student Added SuccessFully !")  

            
    def update_student(self):
     student_id=input("Enter Student ID :").strip()
     found=False
     for student in self.students:
        if student_id == student.student_id:
           print("Current Information :")
           student.displayInfo()
           found=True
           print("UPDATE MENU")
           print("1.Name")
           print("2.Age")
           print("3.Class")
           print("4.Contact")
           print("5.All Details")
           print("6.Exit")
           choice=input("What do you want to Update (1-6) ?")
           if choice == '1':
              name=input("Enter Updated Name :")
              student.fullName = name
              print("Name Updated SuccessFully")
              break

           elif choice == '2':
             try:
              age=int(input("Enter Updated Age :"))
             except ValueError:
               print("Please enter a valid integer")
               return 
             student.age=age
             print("Age Updated SuccessFully")
             break

           elif choice == '3':
             Class=input("Enter Updated Class :")
             student.Class=Class
             print("Class Updated SuccessFully")
             break
             
           elif choice == '4':
             contact=input("Enter Updated Contact :")
             student.contact=contact
             print("Contact Updated SuccessFully")
             break

           elif choice == '5':
             name=input("Name :")
             try:
              age=int(input(" Age :"))
             except ValueError:
               print("Please enter a valid integer") 
               return
             Class=input("Class :")
             contact=input("Contact No :")
             student.fullName=name
             student.age=age
             student.Class=Class
             student.contact=contact
             print("Student Updated SuccessFully")
             break

           elif choice == '6':
              break
           
           else:
              print("Incorrect Command ! Try Again")
  
     if not found:
         print("Student was not Found")

    def search_student(self):
     student_id=input("Enter Student ID :").strip()
     found=False
     for student in self.students:
      if student_id == student.student_id:
        print("Student found SuccessFully")
        student.displayInfo()
        found=True
        break
     if not found:
        print("Student was not Found")

    def remove_student(self):
     student_id=input("Enter Student ID :").strip()
     found=False
     for student in self.students:
      if student_id == student.student_id:
        self.students.remove(student)
        print("Student Removed SuccessFully")
        found=True
        break
     if not found:
        print("Student was not Found")

    def view_all_students(self):
     if not self.students :
       print("No Students Available")
     else: 
       for student in self.students: 
        student.displayInfo()


class Marks_Management():
    def __init__(self,students):
        self.students=students
        self.marks_records={}   

    def add_marks(self):
     student_id=input("Enter Student ID :").strip()
     found=False
     for student in self.students:
        if student.student_id == student_id:
         if student_id in self.marks_records:
          print("Marks already exist for this student")
          return
         print("Enter Student Marks")
         try:
          eng=int(input("Add English Marks :"))
         except ValueError:
          print("Please enter a valid integer")
          return
         if eng < 0 or eng > 100:
          print("Marks must be between 0 and 100")
          return
         try: 
          math=int(input("Add Math Marks :"))
         except ValueError:
          print("Please enter a valid integer")
          return
         if math < 0 or math > 100:
          print("Marks must be between 0 and 100")
          return 

         try:
          bio=int(input("Add Biology Marks :"))
         except ValueError:
          print("Please enter a valid integer")
          return
         if bio < 0 or bio > 100:
          print("Marks must be between 0 and 100")
          return

         try:     
          islam=int(input("Add Islamiyat Marks :"))
         except ValueError:
          print("Please enter a valid integer")
          return
         if islam < 0 or islam > 100:
          print("Marks must be between 0 and 100")
          return 
  
         self.marks_records[student_id]={ 
            "English":eng,
            "Math":math,
            "Biology":bio,
            "Islamiyat":islam
         } 

         print("Marks Added SuccessFully")
         found=True
         break
         
     if not found:
        print("Student was not Found")

    def update_marks(self):
     student_id=input("Enter Student ID :").strip()
     found=False
     for student in self.students:
        if student.student_id == student_id:
         if student_id not in self.marks_records:
          print("No Marks Record Found")
          return    
         print("Current Marks :",self.marks_records[student_id])
         found=True
         print("UPDATE MENU")
         print("1.English")
         print("2.Math")
         print("3.Biology")
         print("4.Islamiyat")
         print("5.All Subject Marks")
         choice=input("What do you want to Update (1-5) ?")
         if choice == '1':
            try:
             eng=int(input("Enter Updated Marks :"))
            except ValueError:
              print("Please enter a valid integer")
              return
            
            if eng < 0 or eng > 100:
              print("Marks must be between 0 and 100")
              return
            
            self.marks_records[student_id]["English"]=eng
            print("English Marks Updated SuccessFully")
            break
           
         elif choice == '2':
           try:
            math=int(input("Enter Updated Marks :"))
           except ValueError:
            print("Please enter a valid integer")
            return
           
           if math < 0 or math > 100:
            print("Marks must be between 0 and 100")
            return
           
           self.marks_records[student_id]["Math"]=math
           print("Math Marks Updated SuccessFully")
           break
         
         elif choice == '3':
           try:
            bio=int(input("Enter Updated Marks :"))
           except ValueError:
            print("Please enter a valid integer")
            return
           
           if bio < 0 or bio > 100:
            print("Marks must be between 0 and 100")
            return
            
           self.marks_records[student_id]["Biology"]=bio
           print("Biology Marks Updated SuccessFully")
           break
                      
         elif choice == '4':
           try:
            islam=int(input("Enter Updated Marks :"))
           except ValueError:
            print("Please enter a valid integer")
            return
           
           if islam < 0 or islam > 100:
            print("Marks must be between 0 and 100")
            return
           
           self.marks_records[student_id]["Islamiyat"]=islam
           print("Islamiyat Marks Updated SuccessFully")
           break
 
         elif choice == '5': 
           try:   
            eng=int(input("Enter English Updated Marks :"))
           except ValueError: 
            print("Please enter a valid integer")
            return
           
           if eng < 0 or eng > 100:
             print("Marks must be between 0 and 100")
             return
            
           try: 
            math=int(input("Enter Math Updated Marks :"))
           except ValueError:
             print("Please enter a valid integer")
             return
           
           if math < 0 or math > 100:
              print("Marks must be between 0 and 100")
              return
            
           try: 
            bio=int(input("Enter Biology Updated Marks :"))
           except ValueError: 
            print("Please enter a valid integer")
            return
           
           if bio < 0 or bio > 100:
            print("Marks must be between 0 and 100")
            return
             
           try:
            islam=int(input("Enter Islamiyat Updated Marks :"))
           except ValueError:
             print("Please enter a valid integer")
             return
           
           if islam < 0 or islam > 100:
            print("Marks must be between 0 and 100")
            return 
            
           self.marks_records[student_id]={"English":eng,"Math":math,"Biology":bio,"Islamiyat":islam}
           print("Marks Updated SuccessFully")

         else:
           print("Incorrect Command ! Try Again")

     if not found:
         print ("Student was not Found")

    def view_marks(self):
     student_id = input("Enter Student ID: ").strip()

     if student_id in self.marks_records:
       marks = self.marks_records[student_id]
       print("English :", marks["English"])
       print("Math :", marks["Math"])
       print("Biology :", marks["Biology"])
       print("Islamiyat :", marks["Islamiyat"])

     else:
      print("No Marks Record Found")

    def calculate_totalMarks(self):
        student_id = input("Enter Student ID: ").strip()

        if student_id in self.marks_records:

            marks = self.marks_records[student_id]

            total = (
                marks["English"]
                + marks["Math"]
                + marks["Biology"]
                + marks["Islamiyat"]
            )

            print("Total Marks :", total)

        else:
            print("No Marks Record Found")


    def calculate_averageMarks(self):
        student_id = input("Enter Student ID: ").strip()

        if student_id in self.marks_records:

            marks = self.marks_records[student_id]

            average = (
                marks["English"]
                + marks["Math"]
                + marks["Biology"]
                + marks["Islamiyat"]
            ) / 4

            print("Average :", average)

        else:
            print("No Marks Record Found")

    def generate_grades(self):
        student_id = input("Enter Student ID: ").strip()

        if student_id in self.marks_records:

            marks = self.marks_records[student_id]

            average = (
                marks["English"]
                + marks["Math"]
                + marks["Biology"]
                + marks["Islamiyat"]
            ) / 4

            if average >= 90:
                print("Grade: A+")

            elif average >= 80:
               print("Grade: A")

            elif average >= 70:
                print("Grade: B")

            elif average >= 60:
                print("Grade: C")

            elif average >= 50:
                print("Grade: D")

            else:
                print("Grade: Fail")

        else:
            print("No Marks Record Found")

    
class Reports:
    def __init__(self,students,marks_record):
       self.students=students
       self.marks_record=marks_record

    def student_report_cards(self):
     student_id = input("Enter Student ID: ").strip()
     found=False
     for student in self.students:
      if student.student_id == student_id and student_id in self.marks_record:
        found=True
        student.displayInfo()
        marks = self.marks_record[student_id]
        print("English :", marks["English"])
        print("Math :", marks["Math"])
        print("Biology :", marks["Biology"])
        print("Islamiyat :", marks["Islamiyat"])

        total = (
         marks["English"]
         + marks["Math"]
         + marks["Biology"]
         + marks["Islamiyat"]
         )
        
        print("Total Marks :", total)

        average = (
          marks["English"]
          + marks["Math"]
          + marks["Biology"]
          + marks["Islamiyat"]
          ) / 4
        print("Average :", average)


        if average >= 90:
         print("Grade: A+")

        elif average >= 80:
         print("Grade: A")

        elif average >= 70:
         print("Grade: B")
        
        elif average >= 60:
         print("Grade: C")
        
        elif average >= 50:
         print("Grade: D")
        
        else:
         print("Grade: Fail")
        break
     if not found:
        print("Student was not found")
      

    def top_performing_students(self):
     top_student = None
     highest_average = 0

     for student in self.students:

        if student.student_id in self.marks_record:

            marks = self.marks_record[student.student_id]

            average = (
                marks["English"]
                + marks["Math"]
                + marks["Biology"]
                + marks["Islamiyat"]
            ) / 4

            if average > highest_average:

                highest_average = average
                top_student = student

     if top_student:

        print("\nTop Performing Student")
        top_student.displayInfo()
        print("Average :", highest_average)

     else:
        print("No Marks Record Found")

    def failed_student_list(self):
     found = False

     for student in self.students:

        if student.student_id in self.marks_record:

            marks = self.marks_record[student.student_id]

            average = (
                marks["English"]
                + marks["Math"]
                + marks["Biology"]
                + marks["Islamiyat"]
            ) / 4

            if average < 50:

                print("\nFailed Student")
                student.displayInfo()
                print("Average :", average)

                found = True

     if not found:
        print("No Failed Students Found")


class Teacher:
    def __init__(self,teacher_id,name,subject,contact):
        self.teacher_id=teacher_id
        self.name=name
        self.subject=subject
        self.contact=contact

    def displayInfo(self):
     print("Teacher_ID :",self.teacher_id)
     print("Teacher_Name :",self.name)
     print("Subject :",self.subject)
     print("Contact No :",self.contact)
    
class Teacher_Management:
    def __init__(self,teachers):
        self.teachers=teachers

    def add_teacher(self):
      teacher_id = input("Enter Teacher ID : ").strip()

      for teacher in self.teachers:
       if teacher.teacher_id == teacher_id:
        print("Teacher ID already exists")
        return
      name=input("Enter Teacher Name :")
      subject=input("Subject :")
      contact=input("Contact No :")
      
      new_Teacher=Teacher(teacher_id,name,subject,contact)
      self.teachers.append(new_Teacher)
      print("Teacher Added SuccessFully")

    def view_teachers(self):
      if not self.teachers:
       print("No Teachers Available") 
      else:
        for teacher in self.teachers:
         teacher.displayInfo()

    def search_teacher(self):
     teacher_id=input("Enter Teacher ID :").strip()
     found=False
     for teacher in self.teachers:
       if teacher_id == teacher.teacher_id:
        print("Teacher found SuccessFully")
        teacher.displayInfo()
        found=True
        break
     if not found:
        print("Teacher was not Found")

    def update_teacher(self):
     teacher_id=input("Enter Teacher ID :").strip()
     found=False
     for teacher in self.teachers:
      if teacher_id == teacher.teacher_id:
        print("Current Information :")
        teacher.displayInfo()
        found=True
        print("UPDATE MENU")
        print("1.Name")
        print("2.Subject")
        print("3.Contact")
        print("4.All Details")        
        choice=input("What do you want to Update (1-4) ?")
        if choice == '1':
          name=input("Enter Updated Name :")
          teacher.name = name
          print("Name Updated SuccessFully")
          break
     
        elif choice == '2':
          subject=input("Enter Updated Subject :")
          teacher.subject=subject
          print("Subject Updated SuccessFully")
          break

        elif choice == '3':
         contact=input("Enter Updated Contact :")
         teacher.contact=contact
         print("Contact Updated SuccessFully")
         break
     
        elif choice == '4':
         name=input("Name :")
         subject=input(" Subject :")
         contact=input("Contact No :")
         teacher.name=name
         teacher.subject=subject
         teacher.contact=contact
         print("Teacher All Details Updated SuccessFully")
         break
                
        else:
         print("Incorrect Command ! Try Again")

     if not found:
       print("Teacher was not Found")

    def remove_teacher(self):
     teacher_id=input("Enter Teacher ID :").strip()
     found=False
     for teacher in self.teachers:
      if teacher_id == teacher.teacher_id:
       self.teachers.remove(teacher)
       print("Teacher Removed SuccessFully")
       found=True
       break
     if not found:
        print("Teacher was not Found")       


class File_Managemet:
    def __init__(self,students,teachers,marks_record):
       self.students=students
       self.teachers=teachers
       self.marks_records=marks_record

    def create_file(self):
      open ("students.txt","a").close()
      open ("teachers.txt","a").close()
      open ("marks.txt","a").close()

      print("Files Created Successfully") 
     
    def save_records(self):
     with open("students.txt", "w") as s:

      for student in self.students:
       s.write(
        f"{student.student_id},"
        f"{student.fullName},"
        f"{student.age},"
        f"{student.Class},"
        f"{student.contact}\n")

     print("Students Saved Successfully")

     with open("teachers.txt", "w") as t:
      for teacher in self.teachers:
        t.write(
            f"{teacher.teacher_id},"
            f"{teacher.name},"
            f"{teacher.subject},"
            f"{teacher.contact}\n"
        )
     print("Teachers Saved Successfully")

     with open("marks.txt", "w") as m:

      for student_id, marks in self.marks_records.items():

        m.write(
            f"{student_id},"
            f"{marks['English']},"
            f"{marks['Math']},"
            f"{marks['Biology']},"
            f"{marks['Islamiyat']}\n"
        )
     print("Marks Saved Successfully")  

        
    def load_records(self):
        try:
         with open ("students.txt","r")as s:
            data=s.read()
            print(data)
        except FileNotFoundError:
          print("File doesn't exist")

        try:  
         with open ("teachers.txt","r")as t:
          data=t.read()
          print(data)  
        except FileNotFoundError:
          print("File doesn't exist")

        try:  
         with open ("marks.txt","r")as m:
          data=m.read()
          print(data)
        except FileNotFoundError:
          print("File doesn't exist")  


class Menu:
 def __init__(self,student_manager,teacher_manager,marks_manager,reports,file_manager):
      self.student_manager=student_manager
      self.teacher_manager=teacher_manager
      self.marks_manager=marks_manager
      self.reports=reports
      self.file_manager=file_manager

 def main_Menu(self):
    while True:
      print("========School Management System=========")
      print("1.Student Management")
      print("2.Teacher Management")
      print("3.Marks Management")
      print("4.Reports")
      print("5.Save Records")
      print("6.Load Records")
      print("7.Exit")

      choice=input("Select an Option (1-7) : ")
      if choice == '1' :
         self.student_Menu()
       
      elif choice == '2':
          self.teacher_Menu()
       
      elif choice == '3':
         self.Marks_Menu() 
       
      elif choice == '4' :
          self.Reports_Menu()

      elif choice == '5' :
          self.file_manager.save_records()

      elif choice == '6':
          self.file_manager.load_records() 

      elif choice == '7' :
         print("Thanks for Using School System")
         break

      else:
        print("Incorrect Command ! Try Again")

 def student_Menu(self):
        print("========Student Management=========")
        print("1.Add Student")
        print("2.Update Student")
        print("3.Search Student")
        print("4.Remove Student")
        print("5.View All Students")
        print("6.Back")

        choice=input("Select an Option (1-6) : ")
        if choice == '1' :
         self.student_manager.add_student()
    
        elif choice == '2':
         self.student_manager.update_student()
       
        elif choice == '3':
         self.student_manager.search_student() 

       
        elif choice == '4' :
          self.student_manager.remove_student()

        elif choice == '5' :
          self.student_manager.view_all_students()

        elif choice == '6' :
         return

        else:
         print("Incorrect Command ! Try Again")

 def teacher_Menu(self):
      print("========Teacher Management=========")
      print("1.Add Teacher")
      print("2.Update Teacher")
      print("3.Search Teacher")
      print("4.Remove Teacher")
      print("5.View Teachers")
      print("6.Back")

      choice=input("Select an Option (1-6) : ")
      if choice == '1' :
         self.teacher_manager.add_teacher()
          
      elif choice == '2':
        self.teacher_manager.update_teacher()
             
      elif choice == '3':
        self.teacher_manager.search_teacher() 
      
      elif choice == '4' :
        self.teacher_manager.remove_teacher()
      
      elif choice == '5' :
        self.teacher_manager.view_teachers()
      
      elif choice == '6' :
        return
      
      else:
        print("Incorrect Command ! Try Again")

 def Marks_Menu(self ):
      print("========Marks Management=========")
      print("1.Add Marks")
      print("2.Update Marks")
      print("3.View Marks")
      print("4.Calculate Total")
      print("5.Calcualate Average")
      print("6.Generate Grade")
      print("7.Back")  

      choice=input("Select an Option (1-7) : ")
      if choice == '1' :
         self.marks_manager.add_marks()
          
      elif choice == '2':
         self.marks_manager.update_marks()
             
      elif choice == '3':
        self.marks_manager.view_marks() 
      
      elif choice == '4' :
        self.marks_manager.calculate_totalMarks()
      
      elif choice == '5' :
        self.marks_manager.calculate_averageMarks()

      elif choice == '6' :
        self.marks_manager.generate_grades()

      elif choice == '7' :
        return
      
      else:
        print("Incorrect Command ! Try Again")


 def Reports_Menu(self):
       print("========Reports=========")
       print("1.Student Report Card")
       print("2.Top Performing Student")
       print("3.Failed Student List")
       print("4.Back")

       choice=input("Select an Option (1-4) : ")
       if choice == '1' :
         self.reports.student_report_cards()
                 
       elif choice == '2':
         self.reports.top_performing_students()
                    
       elif choice == '3':
         self.reports.failed_student_list() 

       elif choice == '4' :
         return
              
       else:
        print("Incorrect Command ! Try Again") 

students = []
teachers = []
student_manager = Student_Management(students)
teacher_manager = Teacher_Management(teachers)
marks_manager = Marks_Management(students)
reports = Reports(students,marks_manager.marks_records)
file_manager = File_Managemet(students,teachers,marks_manager.marks_records)        

menu = Menu(student_manager,teacher_manager,marks_manager,reports,file_manager)
file_manager.create_file()
menu.main_Menu()        