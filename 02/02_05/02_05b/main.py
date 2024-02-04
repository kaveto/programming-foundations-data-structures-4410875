seating_chart = [
    ["Sarah", "CLaire", "Ben", "Taylor", "Eva"],
    ["Frankie", "George", "Lindsey", "Izzy", "Jack"],
    ["Katherine", "Lauren", "Mary", "Nathan", "Olive"],
    ["Chad", "April", "Matt", "Thomas", "Penny"]
]
#get the value "lauren". from the most to least
#print(seating_chart[2][1]) 

#recorriendo una matriz
for i,row in enumerate(seating_chart):
  for j, student_name in enumerate(row):
    print(f"student {student_name} is in {i+1}, seat{j+1}")