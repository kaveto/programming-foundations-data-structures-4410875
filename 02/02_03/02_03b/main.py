''' 
Problem Statement: Compute the average number of pets each student 
has in a given class. 
'''

student_pet_count_list = [0, 1, 0, 2, 1, 1, 4, 0, 0, 0, 3, 2, 1, 3, 0, 2, 2, 4]

ITEM_AT_INDEX_THREE = student_pet_count_list[3] #counting from start to back
ITEM_THREE_FROM_BACK = student_pet_count_list[-3] #counting from back to start
NUM_OF_STUDENTS = len(student_pet_count_list)
print(NUM_OF_STUDENTS)

sum = 0
for i in student_pet_count_list:
  sum = sum + i
print(sum)
# average = sum / number of items
average = sum/NUM_OF_STUDENTS
print(average)
