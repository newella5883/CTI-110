# Austin Newell

# 3/19/2024

# P2HW2

# Assignment assess student understanding of Lists

grade=[]

grade.append(float(input("Enter grade for Module 1: ")))
grade.append(float(input("Enter grade for Module 2: ")))
grade.append(float(input("Enter grade for Module 3: ")))
grade.append(float(input("Enter grade for Module 4: ")))
grade.append(float(input("Enter grade for Module 5: ")))
grade.append(float(input("Enter grade for Module 6: ")))
print()

print("------------Results------------")
print(f"{'Lowest Grade:':<18}{min(grade):.2f}")
print(f"{'Highest Grade:':<18}{max(grade):.2f}")
print(f"{'Sum of Grades:':<18}{sum(grade):.2f}")
print(f"{'Average:':<18}{sum(grade) / len(grade):.2f}")
print("---------------------------------------------")
