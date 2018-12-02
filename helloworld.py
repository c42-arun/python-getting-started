print("Hello World!")

student_names = ["Jon", "Jim", "Jack"]

for name in student_names:
    print(f"Student name is {name}")

x = 0
for index in range(10):
    x += 10
    print("The value of X is {0}".format(x))


for index in range(5, 100, 10):
    print("The value of index is {0}".format(index)) 

y = 0
while True:
    if y == 7:
        break
    print(y)
    y+=1

