student_heights=input("input a list of students heights:  ").split()
for n in range (0,len(student_heights)):
    student_heights[n]=int(student_heights[n])
print(student_heights)
i=0
m=0
for x in  student_heights:
    m+=x  #sum of heights
    i+=1 #number of students
average=m/i
print(f"average is {average}")