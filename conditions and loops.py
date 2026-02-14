name = input("Enter Student Name: ")
regno = input("Enter Register Number: ")

n = int(input("Enter number of subjects: "))

total = 0
result = "Pass"

for i in range(1, n + 1):
    mark = int(input(f"Enter mark for subject {i}: "))

    if mark < 35:
        result = "Fail"

    total += mark

average = total / n

if result == "Fail":
    grade = "No Grade"
elif average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 60:
    grade = "C"
else:
    grade = "D"

print("\n------ STUDENT MARK STATEMENT ------")
print("Name        :", name)
print("Register No :", regno)
print("Total Marks :", total)
print("Average     :", average)
print("Result      :", result)
print("Grade       :", grade)
