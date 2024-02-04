# Tuples are immutable array-like structures
point = (5,2)
x = point[0]
y = point[1]

def calculate_square_properties(side_lenght):
  area = side_lenght ** 2
  perimeter = 4 * side_lenght
  return (area, perimeter)

result = calculate_square_properties(5)
print("area: ", result[0])
print("perimeter: ", result[1])