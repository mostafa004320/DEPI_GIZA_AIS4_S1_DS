class student:


     _id_counter =1
     def __init__(self, name,):
          self.student_id = student._id_counter
          student._id_counter +=1
          self.name = name
          self.grades = {}
          self.enrolled_courses = []

     def __str__(self):
         return f"Student ID: {self.student_id}, Name: {self.name}, Grades: {self.grades}"
     

     def __repr__(self):
         return f"Student ID: {self.student_id}, Name: {self.name}, Grades: {self.grades}"
     def add_grade(self, course_id : int, grade: int):

          self.grades[course_id] = grade
     def enroll_in_course(self, course_id: int):     
         self.enrolled_courses.append(course_id)